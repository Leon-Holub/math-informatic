import functions
import numpy as np

from functions import plot_function

# Parametry  zadání
iterations = 20  # Počet iterací
dimensions = 2  # Počet dimenzí
neighbors = 3  # Počet generovaných sousedů
std = 3  # Standardní odchylka generování sousedů


def generate_valid_candidates(current_point, lower_bound, upper_bound):
    candidates = []
    for _ in range(neighbors):
        while True:
            new_candidate = current_point + np.random.normal(0, std, dimensions)
            if np.all((new_candidate >= lower_bound) & (new_candidate <= upper_bound)):
                candidates.append(new_candidate)
                break
    return np.array(candidates)


def local_search(optFunction, start_point):
    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_values_history = [current_value]  # Ukládáme historii nejlepší hodnoty

    for _ in range(iterations):
        candidates = np.vstack([
            current_point,  # Přidáme aktuální bod do výběru
            generate_valid_candidates(current_point, lower_bound, upper_bound)
        ])

        candidate_values = np.array([optFunction.evaluate(candidate) for candidate in candidates])

        best_index = np.argmin(candidate_values)
        best_point = candidates[best_index]
        best_value = candidate_values[best_index]

        if best_value < current_value:
            current_point = best_point
            current_value = best_value

        best_values_history.append(best_value)

    plot_function(f"{optFunction.name} - Local search", best_point, best_value, best_values_history)


def hill_climber(optFunction, start_point):
    lower_bound, upper_bound = optFunction.bounds
    current_point = start_point.copy()
    current_value = optFunction.evaluate(current_point)

    best_values_history = [current_value]

    for _ in range(iterations):
        candidates = generate_valid_candidates(current_point, lower_bound, upper_bound)

        candidate_values = np.array([optFunction.evaluate(candidate) for candidate in candidates])

        best_index = np.argmin(candidate_values)
        best_point = candidates[best_index]
        best_value = candidate_values[best_index]

        if best_value < current_value:
            current_point = best_point
            current_value = best_value

        best_values_history.append(best_value)

    plot_function(f"{optFunction.name} - Hill climber", best_point, best_value, best_values_history)


def start_functions(opt_function=None, do_hill_climber=True, do_local_search=True):
    if opt_function:
        functions_to_run = [opt_function]
    else:
        functions_to_run = functions.functions

    for function in functions_to_run:
        start_point = np.random.uniform(function.bounds[0], function.bounds[1], dimensions)
        print(f"\nStart point for {function.name}: {start_point}")
        if do_local_search:
            local_search(function, start_point)
        if do_hill_climber:
            hill_climber(function, start_point)



if __name__ == "__main__":
    start_functions()
