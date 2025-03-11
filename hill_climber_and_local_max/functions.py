import math
import os

from matplotlib import pyplot as plt


class OptimizationFunction:
    def __init__(self, name, function, bounds):
        self.name = name
        self.function = function
        self.bounds = bounds

    def evaluate(self, v):
        return self.function(v)


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


functions = [
    OptimizationFunction("Sphere", sphere_function, (-5.12, 5.12)),
    OptimizationFunction("Dixon-Price", dixon_price_function, (-10, 10)),
    OptimizationFunction("Michaelowicz", michaelowicz_function, (0, math.pi)),
    OptimizationFunction("Styblinski-Tang", styblinski_tang_function, (-5, 5)),
    OptimizationFunction("Rastrigin", rastrigin_function, (-5.12, 5.12))
]


def plot_function(func_name, best_point, best_value, best_values_history):
    plt.figure(figsize=(10, 5))
    plt.plot(best_values_history)
    plt.title(f"{func_name}\nBest value: {best_value:.2f}\nBest point: {best_point}")
    plt.xlabel("Iteration")
    plt.ylabel("Function value")
    plt.tight_layout()
    plt.show()
