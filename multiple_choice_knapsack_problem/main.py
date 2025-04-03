from typing import Tuple, List
import random
import pandas as pd
import time

Item = Tuple[int, int, int, int]

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

if __name__ == "__main__":
    class_count = 24
    items_in_class = 3

    max_weight = 20 * class_count

    items = generate_items(class_count, items_in_class)
    classes = group_items_by_class(items, class_count)

    print(f"Maximalni vaha: {max_weight}")
    print(f"Pocet trid: {class_count}")
    print(f"Pocet predmetu v tride: {items_in_class}")
    print("\nPredmety:")
    column_names = ["Třída", "Id", "Objem", "Cena"]
    df_items = pd.DataFrame(items, columns=column_names)
    print(df_items)

    start_time = time.time()
    best_combination, best_value = find_best_combination(classes, max_weight)
    end_time = time.time()

    df_items = pd.DataFrame(best_combination, columns=column_names)
    print("\nNejlepsi kombinace:")
    print(df_items)
    print(f"Nejvyssi hodnota: {best_value}")
    print(f"Vypocet trval {end_time - start_time} sekund")







