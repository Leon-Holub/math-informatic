import numpy as np
import random
import matplotlib.pyplot as plt
from typing import List, Tuple
import pandas as pd
import os
import time

Item = Tuple[int, int, int, int]  # (class, id, volume, value)

def generate_items(class_count: int, items_in_class: int)  -> List[Item]:
    items = []
    for cls in range(1, class_count + 1):
        for item_id in range(1, items_in_class + 1):
            volume = random.randint(1, 50)
            value = random.randint(1, 50)
            items.append((cls, item_id, volume, value))
    return items

def group_items_by_class(items: List[Item], num_classes: int) -> List[List[Item]]:
    classes = [[] for _ in range(num_classes)]
    for item in items:
        classes[item[0] - 1].append(item)
    return classes

def find_best_combination(classes: List[List[Item]], capacity: int) -> Tuple[List[Item], int]:
    best_combination = []
    highest_value = 0

    def backtrack(index: int, current_combination: List[Item], current_volume: int, current_value: int):
        nonlocal best_combination, highest_value

        if current_volume > capacity:
            return
        if index == len(classes):
            if current_value > highest_value:
                highest_value = current_value
                best_combination = current_combination[:]
            return

        for item in classes[index]:
            backtrack(
                index + 1,
                current_combination + [item],
                current_volume + item[2],
                current_value + item[3]
            )

    backtrack(0, [], 0, 0)
    return best_combination, highest_value

class KnapsackProblem:
    def __init__(self, classes: List[List[Item]], capacity: int):
        self.classes = classes
        self.capacity = capacity
        self.num_classes = len(classes)

    def evaluate(self, solution: List[int]) -> int:
        total_volume = 0
        total_value = 0
        for class_index, item_index in enumerate(solution):
            item = self.classes[class_index][item_index]
            total_volume += item[2]
            total_value += item[3]

        if total_volume > self.capacity:
            return -1  # penalizace
        return total_value

    def random_solution(self) -> List[int]:
        return [random.randint(0, len(cls) - 1) for cls in self.classes]

    def neighbor(self, solution: List[int], prob=0.2) -> List[int]:
        neighbor = solution[:]
        for i in range(len(neighbor)):
            if random.random() < prob:
                options = list(range(len(self.classes[i])))
                options.remove(neighbor[i])
                neighbor[i] = random.choice(options)
        return neighbor

def simulated_annealing(problem: KnapsackProblem, evaluations=1000, T0=100, Tf=0.01, prob=0.2):
    current_solution = problem.random_solution()
    current_value = problem.evaluate(current_solution)
    best_solution = current_solution[:]
    best_value = current_value

    history = [current_value]
    evaluations_used = 1
    evaluated = set()
    evaluated.add(tuple(current_solution))

    while evaluations_used < evaluations:
        T = T0 - (T0 - Tf) * (evaluations_used / evaluations)
        neighbor = problem.neighbor(current_solution, prob)
        key = tuple(neighbor)
        if key in evaluated:
            continue  # přeskočíme duplicitní řešení
        evaluated.add(key)
        neighbor_value = problem.evaluate(neighbor)
        evaluations_used += 1

        delta = neighbor_value - current_value

        if delta > 0 or random.random() < np.exp(delta / T):
            current_solution = neighbor
            current_value = neighbor_value
            if neighbor_value > best_value:
                best_solution = neighbor
                best_value = neighbor_value

        history.append(best_value)

    return best_solution, best_value, history

def plot_graph(history, brute_value):
    os.makedirs("charts", exist_ok=True)
    fig_graph, ax_graph = plt.subplots(figsize=(10, 5))
    ax_graph.plot(history, label="SA", color='black')
    ax_graph.hlines(brute_value, xmin=0, xmax=len(history), colors='red', label="Brute Force")
    ax_graph.set_xlabel("Počet ohodnocení")
    ax_graph.set_ylabel("Kvalita")
    ax_graph.set_title("Konvergenční graf")
    ax_graph.legend()
    ax_graph.grid(True)
    plt.tight_layout()
    plt.savefig("charts/convergence_graph.png")
    plt.close()

def compare_with_brute_force(classes: List[List[Item]], capacity: int):
    problem = KnapsackProblem(classes, capacity)
    start_time = time.time()
    sa_solution, sa_value, history = simulated_annealing(problem, evaluations=10000)
    sa_duration = time.time() - start_time

    start_time = time.time()
    brute_items, brute_value = find_best_combination(classes, capacity)
    brute_duration = time.time() - start_time

    brute_volume = sum([i[2] for i in brute_items])
    sa_items = [classes[i][idx] for i, idx in enumerate(sa_solution)]
    sa_volume = sum([i[2] for i in sa_items])

    print("\n=== BRUTE FORCE ===")
    df_brute = pd.DataFrame(brute_items, columns=["Třída", "Id", "Objem", "Cena"])
    print(df_brute)
    print("Suma objem:", brute_volume, "Suma cena:", brute_value, f"čas: {brute_duration:.4f}s")

    print("\n=== SIMULATED ANNEALING ===")
    df_sa = pd.DataFrame(sa_items, columns=["Třída", "Id", "Objem", "Cena"])
    print(df_sa)
    print("Suma objem:", sa_volume, "Suma cena:", sa_value, f"čas: {sa_duration:.4f}s")

    if brute_value > 0:
        percentual = (sa_value / brute_value) * 100
        print(f"\nSA dosáhlo {percentual:.2f}% optimální hodnoty")
    else:
        print("\nNelze spočítat procentuální rozdíl – hodnota brute force je 0")

    plot_graph(history, brute_value)

if __name__ == "__main__":
    class_count = 20
    items_in_class = 3
    max_weight = 20 * class_count

    items = generate_items(class_count, items_in_class)
    classes = group_items_by_class(items, class_count)

    compare_with_brute_force(classes, max_weight)
