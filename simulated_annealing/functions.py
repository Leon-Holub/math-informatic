import os
import re

import pandas as pd
from matplotlib import pyplot as plt

import optimalization_funtions
import numpy as np


def generate_valid_candidates(current_point, lower_bound, upper_bound, std, dimensions, neighbors):
    candidates = []
    for _ in range(neighbors):
        while True:
            new_candidate = current_point + np.random.normal(0, std, dimensions)
            if np.all((new_candidate >= lower_bound) & (new_candidate <= upper_bound)):
                candidates.append(new_candidate)
                break
    return np.array(candidates)


def local_search(optFunction, start_point, iterations=20, dimensions=2, neighbors=3, std=3):
    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_values_history = [current_value]

    for _ in range(iterations):
        candidates = np.vstack([
            current_point,
            generate_valid_candidates(current_point, lower_bound, upper_bound, std, dimensions, neighbors)
        ])

        candidate_values = np.array([optFunction.evaluate(candidate) for candidate in candidates])

        best_index = np.argmin(candidate_values)
        best_point = candidates[best_index]
        best_value = candidate_values[best_index]

        if best_value < current_value:
            current_point = best_point
            current_value = best_value

        best_values_history.append(best_value)

    return best_point, best_value, best_values_history


def hill_climber(optFunction, start_point, iterations=20, dimensions=2, neighbors=3, std=3):
    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_values_history = [current_value]
    best_value = current_value

    for _ in range(iterations):
        candidates = generate_valid_candidates(current_point, lower_bound, upper_bound, std, dimensions, neighbors)
        candidate_values = np.array([optFunction.evaluate(candidate) for candidate in candidates])
        best_index = np.argmin(candidate_values)
        best_point = candidates[best_index]
        best_candidate_value = candidate_values[best_index]

        if best_candidate_value < current_value:
            current_point = best_point
            current_value = best_candidate_value

        if current_value < best_value:
            best_value = current_value

        best_values_history.append(best_value)

    return current_point, best_value, best_values_history


def simulated_annealing(optFunction, start_point, iterations=100, dimensions=2, neighbors=3, std=3, T0=100, Tf=0.01):
    import numpy as np

    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_point = current_point.copy()
    best_value = current_value

    best_values_history = [current_value]

    for i in range(1, iterations + 1):
        T = T0 - (T0 - Tf) * (i / iterations)

        candidates = generate_valid_candidates(
            current_point, lower_bound, upper_bound, std, dimensions, neighbors
        )

        for candidate in candidates:
            candidate_value = optFunction.evaluate(candidate)
            delta = candidate_value - current_value

            if delta < 0 or np.random.rand() < np.exp(-delta / T):
                current_point = candidate
                current_value = candidate_value

                if current_value < best_value:
                    best_point = current_point.copy()
                    best_value = current_value

        best_values_history.append(best_value)

    return best_point, best_value, best_values_history


def run_algorithm_multiple_times(algorithm_func, opt_function, dimensions, population, iterations, runs, std, **kwargs):
    results = []
    histories = []

    for _ in range(runs):
        start = np.random.uniform(opt_function.bounds[0], opt_function.bounds[1], dimensions)
        result = algorithm_func(opt_function, start, iterations, dimensions, population, std, **kwargs)
        _, best_value, history = result
        results.append(best_value)
        histories.append(history)

    return results, histories


def calc_stats(name, results):
    return {
        "Algorithm": name,
        "Min": np.min(results),
        "Max": np.max(results),
        "Mean": np.mean(results),
        "Median": np.median(results),
        "STD": np.std(results)
    }


def generate_filename(func_name, iterations, dimensions, neighbors, std):
    clean_func_name = re.sub(r"[^a-zA-Z0-9_]", "", func_name.replace(" ", "_"))
    return f"{clean_func_name}_I{iterations}_D{dimensions}_N{neighbors}_STD{std}.png"


def plot_convergence(histories_dict, fileName, title="Convergence"):
    plt.figure(figsize=(10, 6))
    for label, histories in histories_dict.items():
        mean_hist = np.mean(histories, axis=0)
        plt.plot(mean_hist, label=label)
    all_values = [val for history in histories_dict.values() for run in history for val in run]
    if all(v > 0 for v in all_values):
        plt.yscale("log")
    else:
        plt.yscale("linear")
    plt.xlabel("iteration")
    plt.ylabel("f(x)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    os.makedirs("charts", exist_ok=True)
    plt.savefig(os.path.join("charts", fileName))
    plt.close()


def plot_table_from_dataframe(df, fileName, title="Statistika algoritmů"):
    df = df.round(5)
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.axis('off')
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     loc='center',
                     cellLoc='center')
    table.scale(1, 2)
    plt.title(title)
    plt.tight_layout()
    os.makedirs("tables", exist_ok=True)
    plt.savefig(os.path.join("tables", fileName))
    plt.close()


def compare_algorithms(opt_func, dimensions=5, population=10, runs=30, std=1, T0=100, Tf=0.01):
    max_fes = 10000 * dimensions
    iterations = max_fes // population

    results = {}
    histories = {}

    results["LS"], histories["LS"] = run_algorithm_multiple_times(local_search, opt_func, dimensions, population,
                                                                  iterations, runs, std)
    results["HC"], histories["HC"] = run_algorithm_multiple_times(hill_climber, opt_func, dimensions, population,
                                                                  iterations, runs, std)
    results["SA"], histories["SA"] = run_algorithm_multiple_times(simulated_annealing, opt_func, dimensions, population,
                                                                  iterations, runs, std, T0=T0, Tf=Tf)

    stats = [calc_stats(name, values) for name, values in results.items()]
    df_stats = pd.DataFrame(stats)
    file_name = generate_filename(opt_func.name, iterations, dimensions, population, std)
    return df_stats, histories, file_name


if __name__ == "__main__":
    df, histories, file_name = compare_algorithms(functions.sphere_function)
    print(df.to_string(index=False))
    plot_convergence(histories, file_name, title="SphereF")
    plot_table_from_dataframe(df, file_name, title="Statistika algoritmů - Shere Function")