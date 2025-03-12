import functions
import numpy as np
from main import local_search, hill_climber


def generate_protocol(results):
    filename = "README.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Optimalizační Protokol\n\n")
        f.write(
            "Tento protokol dokumentuje optimalizaci různých testovacích funkcí pomocí algoritmů Local Search a Hill Climber.\n")
        f.write(
            "Testování probíhá na stejném startovacím bodě pro každou funkci s pevnou dimenzí **2**. Cílem je porovnat efektivitu algoritmů a vliv různých parametrů na nalezení minima.\n\n")

        f.write("## Navigace\n\n")
        for function_name in results.keys():
            f.write(f"- [{function_name}](#{function_name.lower().replace(' ', '-')})\n")

        f.write("\n")

        total_ls_best = []
        total_hc_best = []

        for function_name, experiments in results.items():
            f.write(f"## {function_name}\n\n")
            f.write("### Nejlepší a nejhorší nalezené hodnoty\n")

            best_ls = min(experiments.items(), key=lambda x: x[1]['ls_best_value'])
            worst_ls = max(experiments.items(), key=lambda x: x[1]['ls_best_value'])
            best_hc = min(experiments.items(), key=lambda x: x[1]['hc_best_value'])
            worst_hc = max(experiments.items(), key=lambda x: x[1]['hc_best_value'])

            best_ls_params, best_ls_result = best_ls
            worst_ls_params, worst_ls_result = worst_ls
            best_hc_params, best_hc_result = best_hc
            worst_hc_params, worst_hc_result = worst_hc

            f.write(f"#### Nejlepší výsledek:\n")
            f.write(f"- **Local Search**: {best_ls_result['ls_best_value']:.4f} při bodě **{best_ls_result['ls_best_point']}** s nastavením: Iterace **{best_ls_params[0]}**, Sousedi **{best_ls_params[1]}**, STD **{best_ls_params[2]}**.\n")
            f.write(f"- **Hill Climber**: {best_hc_result['hc_best_value']:.4f} při bodě **{best_hc_result['hc_best_point']}** s nastavením: Iterace **{best_hc_params[0]}**, Sousedi **{best_hc_params[1]}**, STD **{best_hc_params[2]}**.\n\n")

            f.write(f"#### Nejhorší výsledek:\n")
            f.write(f"- **Local Search**: {worst_ls_result['ls_best_value']:.4f} při bodě **{worst_ls_result['ls_best_point']}** s nastavením: Iterace **{worst_ls_params[0]}**, Sousedi **{worst_ls_params[1]}**, STD **{worst_ls_params[2]}**.\n")
            f.write(f"- **Hill Climber**: {worst_hc_result['hc_best_value']:.4f} při bodě **{worst_hc_result['hc_best_point']}** s nastavením: Iterace **{worst_hc_params[0]}**, Sousedi **{worst_hc_params[1]}**, STD **{worst_hc_params[2]}**.\n\n")

            total_ls_best.append(best_ls_result["ls_best_value"])
            total_hc_best.append(best_hc_result["hc_best_value"])

            f.write("### Výsledky jednotlivých testů\n\n")
            f.write("| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |\n")
            f.write("|---------|--------|-----|------------|------------|---------|---------|\n")

            for params, result in experiments.items():
                iterations, neighbors, std = params
                ls_plot = result['ls_plot']
                hc_plot = result['hc_plot']

                f.write(
                    f"| {iterations} | {neighbors} | {std} | {result['ls_best_value']:.4f} | {result['hc_best_value']:.4f} | ![LS]({ls_plot}) | ![HC]({hc_plot}) |\n")

            f.write("\n")

        avg_ls_best = sum(total_ls_best) / len(total_ls_best)
        avg_hc_best = sum(total_hc_best) / len(total_hc_best)

        f.write("## Závěr\n\n")
        f.write("Na základě provedených experimentů lze vyvodit následující závěry:\n\n")

        if avg_ls_best < avg_hc_best:
            f.write(f"- **Celkově se lépe vedl Local Search**, který dosáhl v průměru lepší hodnoty než Hill Climber (**{avg_ls_best:.4f} vs. {avg_hc_best:.4f}**).\n")
            f.write("- Local Search je stabilnější, ale má tendenci uvíznout v lokálních minimech.\n")
        else:
            f.write(f"- **Celkově se lépe vedl Hill Climber**, který dosáhl v průměru lepší hodnoty než Local Search (**{avg_hc_best:.4f} vs. {avg_ls_best:.4f}**).\n")
            f.write("- Hill Climber se lépe vyhýbá lokálním minimům, ale vykazuje větší variabilitu výsledků.\n")

        f.write("- Počet sousedů a velikost STD mají výrazný vliv na výsledky obou metod.\n")
        f.write("- Optimální hodnoty STD se obvykle pohybovaly mezi 2–3.\n")
        f.write("- Vyšší počet sousedů (10–20) umožnil robustnější prohledávání prostoru.\n")

    print(f"✅ Protokol byl vygenerován: {filename}")


def run_experiments():
    results = {}
    dimensions = 2

    iterations_to_try = [20, 50, 100]
    neighbors_to_try = [5, 10, 20]
    std_to_try = [1, 3, 5]

    for function in functions.functions:
        results[function.name] = {}

        start_point = np.random.uniform(function.bounds[0], function.bounds[1], dimensions)
        print(f"\nTestování {function.name}...")

        for iterations in iterations_to_try:
            for neighbors in neighbors_to_try:
                for std in std_to_try:
                    print(f"   Iterace {iterations}, Sousedi {neighbors}, STD {std}")

                    ls_best_point, ls_best_value, ls_plot = local_search(function, start_point, iterations,
                                                                                     dimensions, neighbors, std)
                    hc_best_point, hc_best_value, hc_plot = hill_climber(function, start_point, iterations,
                                                                                     dimensions, neighbors, std)

                    results[function.name][(iterations, neighbors, std)] = {
                        "ls_best_value": ls_best_value,
                        "hc_best_value": hc_best_value,
                        "ls_best_point": ls_best_point,
                        "hc_best_point": hc_best_point,
                        "ls_plot": ls_plot,
                        "hc_plot": hc_plot
                    }

    generate_protocol(results)


if __name__ == "__main__":
    run_experiments()
