import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import os


class OptimizationFunction:
    def __init__(self, name, function, bounds):
        self.name = name  # Název funkce
        self.function = function  # Odkaz na výpočetní funkci
        self.bounds = bounds  # Rozsah hodnot

    def evaluate(self, v):
        return self.function(v)


def plotChart(x, y, title, xLabel, yLabel):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()


def sphereFunction(v):
    return sum([x ** 2 for x in v])


def dixonPriceFunction(v):
    return (v[0] - 1) ** 2 + sum([i * (2 * v[i] ** 2 - v[i - 1]) ** 2 for i in range(1, len(v))])


def michaelowiczFunction(v):
    return -sum([math.sin(v[i]) * math.sin((i + 1) * v[i] ** 2 / math.pi) ** 20 for i in range(len(v))])


def styblinskiTangFunction(v):
    return sum([x ** 4 - 16 * x ** 2 + 5 * x for x in v]) / 2


def zakharovFunction(v):
    sum1 = sum(x ** 2 for x in v)
    sum2 = sum(0.5 * (i + 1) * x for i, x in enumerate(v))
    return sum1 + sum2 ** 2 + sum2 ** 4


def showCoveragePlot(values, maxFES, D, func_name, best_value, best_point, bounds, save=True):
    plt.figure(figsize=(10, 5))
    plt.plot(values, label="Nejlepší hodnota", color='orange')
    plt.xlabel("FES")
    plt.ylabel("f(x)")
    plt.title(f"{func_name} v {D}D (maxFES = {maxFES})")
    plt.legend()
    plt.grid()

    # Připravení textu pro zobrazení v grafu
    settings_text = (
        f"Nejlepší řešení: {best_value:.6f}\n"
        f"Bod: {best_point}\n"
        f"Rozsah: {bounds}\n"
        f"Dimenze: {D}\n"
        f"Počet hodnocení: {maxFES}"
    )

    # Vykreslení textu do grafu
    plt.text(0.02 * maxFES, 0.9 * max(values), settings_text, fontsize=10, verticalalignment='top')

    if save:
        os.mkdir("charts") if not os.path.exists("charts") else None
        plt.savefig(f"charts/convergence_{func_name}_{D}D.png")
    else:
        plt.show()


if __name__ == '__main__':
    dimensions = [5, 10, 20]
    maxFES_per_D = 10000
    functions = [
        OptimizationFunction("Sphere", sphereFunction, (-10, 10)),
        OptimizationFunction("Dixon-Price", dixonPriceFunction, (-10, 10)),
        OptimizationFunction("Michaelowicz", michaelowiczFunction, (0, math.pi)),
        OptimizationFunction("Styblinski-Tang", styblinskiTangFunction, (-5, 5)),
        OptimizationFunction("Zakharov", zakharovFunction, (-5, 10))
    ]

    results = []
    convergence_data = {}

    # Algoritmus náhodného prohledávání
    for d in dimensions:
        maxFES = maxFES_per_D * d
        for optFunction in functions:
            best_value = float("inf")
            best_point = None
            values_over_time = []

            for _ in range(maxFES):
                candidate = np.random.uniform(optFunction.bounds[0], optFunction.bounds[1], d)
                value = optFunction.evaluate(candidate)

                if value < best_value:
                    best_value = value
                    best_point = candidate

                values_over_time.append(best_value)

            # Uložení výsledků
            results.append({
                "Funkce": optFunction.name,
                "Dimenze": d,
                "Nejlepší hodnota": best_value,
                "Nejlepší bod": best_point
            })

            # Uložení průběhu konvergence
            convergence_data[(optFunction.name, d, optFunction.bounds)] = (values_over_time, best_value, best_point)

    # Převedení výsledků do DataFrame
    df_results = pd.DataFrame(results)
    print(df_results)

    for (func_name, D, bounds), (values, best_value, best_point) in convergence_data.items():
        showCoveragePlot(values, maxFES_per_D, D, func_name, best_value, best_point, bounds, save=True)

    '''
    vector = np.random.rand(5)
    sphereFunctionX = np.linspace(-5.12, 5.12, 100)
    plotChart(sphereFunctionX, [sphereFunction([x]) for x in sphereFunctionX], 'Sphere Function', 'x', 'f(x)')

    dixonPriceFunctionX = np.linspace(-10, 10, 100)
    plotChart(dixonPriceFunctionX, [dixonPriceFunction([x]) for x in dixonPriceFunctionX], 'Dixon-Price Function', 'x',
              'f(x)')

    michaelowiczFunctionX = np.linspace(0, math.pi, 100)
    plotChart(michaelowiczFunctionX, [michaelowiczFunction([x]) for x in michaelowiczFunctionX],
              'Michaelowicz Function', 'x', 'f(x)')

    styblinskiTangFunctionX = np.linspace(-5, 5, 100)
    plotChart(styblinskiTangFunctionX, [styblinskiTangFunction([x]) for x in styblinskiTangFunctionX],
              'Styblinski-Tang Function', 'x', 'f(x)')

    zakharovFunctionX = np.linspace(-5, 10, 100)
    plotChart(zakharovFunctionX, [zakharovFunction([x]) for x in zakharovFunctionX],
              'Zakharov Function', 'x', 'f(x)')
    '''

    print("Sphere Function")
