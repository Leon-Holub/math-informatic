import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import os


class OptimizationFunction:
    def __init__(self, name, function, bounds):
        self.name = name
        self.function = function
        self.bounds = bounds

    def evaluate(self, v):
        return self.function(v)


def plot_chart(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def sphere_function(v):
    return sum([x ** 2 for x in v])


def dixon_price_function(v):
    return (v[0] - 1) ** 2 + sum([i * (2 * v[i] ** 2 - v[i - 1]) ** 2 for i in range(1, len(v))])


def michaelowicz_function(v):
    return -sum([math.sin(v[i]) * math.sin((i + 1) * v[i] ** 2 / math.pi) ** 20 for i in range(len(v))])


def styblinski_tang_function(v):
    return sum([x ** 4 - 16 * x ** 2 + 5 * x for x in v]) / 2


def rastrigin_function(v):
    return 10 * len(v) + sum([x ** 2 - 10 * math.cos(2 * math.pi * x) for x in v])


def show_coverage_plot(values, max_fes, d, func_name, best_value, best_point, bounds, save=True):
    plt.figure(figsize=(10, 5))
    plt.plot(values, label="Best value", color='orange')
    plt.xlabel("FES")
    plt.ylabel("f(x)")
    plt.title(f"{func_name} in {d}D (maxFES = {max_fes})")
    plt.legend()
    plt.grid()

    settings_text = (
        f"Best solution: {best_value:.6f}\n"
        f"Point: {best_point}\n"
        f"Bounds: {bounds}\n"
        f"Dimensions: {d}\n"
        f"Evaluation count: {max_fes}"
    )

    plt.text(0.02 * max_fes, 0.9 * max(values), settings_text, fontsize=10, verticalalignment='top')

    if save:
        os.mkdir("charts") if not os.path.exists("charts") else None
        plt.savefig(f"charts/convergence_{func_name}_{d}D.png")
    else:
        plt.show()


if __name__ == '__main__':
    dimensions = [5, 10, 20]
    max_fes_per_d = 10000
    functions = [
        OptimizationFunction("Sphere", sphere_function, (-5.12, 5.12)),
        OptimizationFunction("Dixon-Price", dixon_price_function, (-10, 10)),
        OptimizationFunction("Michaelowicz", michaelowicz_function, (0, math.pi)),
        OptimizationFunction("Styblinski-Tang", styblinski_tang_function, (-5, 5)),
        OptimizationFunction("Rastrigin", rastrigin_function, (-5.12, 5.12))
    ]

    results = []
    convergence_data = {}

    for d in dimensions:
        max_fes = max_fes_per_d * d
        for opt_function in functions:
            best_value = float("inf")
            best_point = None
            values_over_time = []

            for _ in range(max_fes):
                candidate = np.random.uniform(opt_function.bounds[0], opt_function.bounds[1], d)
                value = opt_function.evaluate(candidate)

                if value < best_value:
                    best_value = value
                    best_point = candidate

                values_over_time.append(best_value)

            results.append({
                "Function": opt_function.name,
                "Dimensions": d,
                "Best Value": best_value,
                "Best Point": best_point
            })

            convergence_data[(opt_function.name, d, opt_function.bounds)] = (values_over_time, best_value, best_point)

    df_results = pd.DataFrame(results)
    print(df_results)

    for (func_name, d, bounds), (values, best_value, best_point) in convergence_data.items():
        show_coverage_plot(values, max_fes_per_d, d, func_name, best_value, best_point, bounds, save=True)

    print("Sphere Function")
