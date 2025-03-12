import functions
import numpy as np

from functions import plot_function

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

    plot_file_url = plot_function(f"{optFunction.name} - Local search", best_point, best_value, best_values_history, iterations, dimensions, std, neighbors)
    return best_point, best_value, plot_file_url

def hill_climber(optFunction, start_point, iterations=20, dimensions=2, neighbors=3, std=3):
    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_values_history = [current_value]

    for _ in range(iterations):
        candidates = generate_valid_candidates(current_point, lower_bound, upper_bound, std, dimensions, neighbors)

        candidate_values = np.array([optFunction.evaluate(candidate) for candidate in candidates])

        best_index = np.argmin(candidate_values)
        best_point = candidates[best_index]
        best_value = candidate_values[best_index]

        if best_value < current_value:
            current_point = best_point
            current_value = best_value

        best_values_history.append(best_value)

    plot_file_url = plot_function(f"{optFunction.name} - Hill climber", best_point, best_value, best_values_history, iterations, dimensions, std, neighbors)
    return best_point, best_value, plot_file_url

def start_functions(opt_function=None, do_hill_climber=True, do_local_search=True, iterations=20, dimensions=2, neighbors=3, std=3):
    if opt_function:
        functions_to_run = [opt_function]
    else:
        functions_to_run = functions.functions

    for function in functions_to_run:
        start_point = np.random.uniform(function.bounds[0], function.bounds[1], dimensions)
        print(f"\nStart point for {function.name}: {start_point}")
        if do_local_search:
            local_search(function, start_point, iterations, dimensions, neighbors, std)

        if do_hill_climber:
            hill_climber(function, start_point,iterations, dimensions, neighbors, std)


def start_functions_experiments():
    dimensions_to_try = [2, 5, 10]
    iterations_to_try = [20, 50, 100]
    neighbors_to_try = [3, 5, 10]
    std_to_try = [1, 3, 5]

    for function in functions.functions:
        for dimensions in dimensions_to_try:
            start_point = np.random.uniform(function.bounds[0], function.bounds[1], dimensions)
            for iterations in iterations_to_try:
                for neighbors in neighbors_to_try:
                    for std in std_to_try:
                        local_search(function, start_point, iterations, dimensions, neighbors, std)
                        hill_climber(function, start_point, iterations, dimensions, neighbors, std)


if __name__ == "__main__":
    start_functions()
