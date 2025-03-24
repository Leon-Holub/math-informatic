import os
import optimalization_funtions
from simulated_annealing.functions import compare_algorithms, plot_convergence, plot_table_from_dataframe


def generate_protocol(output_file="README.md"):
    functions_to_run = [
        functions.sphere_function,
        functions.rastrigin_function,
        functions.styblinski_tang_function
    ]
    dimensions_list = [5, 10, 20]
    neighbors = 10
    std = 1
    summary_data = []

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Simulované žíhání a porovnání s HC a LC\n\n")

        f.write("## Navigace\n")
        for func in functions_to_run:
            func_anchor = func.name.lower()
            f.write(f"- [{func.name}](#{func_anchor})\n")
            for dim in dimensions_list:
                dim_anchor = f"{func.name.lower()}--dimenze-{dim}"
                f.write(f"  - [Dimenze {dim}](#{dim_anchor})\n")
        f.write("\n---\n")

        for func in functions_to_run:
            f.write(f"\n## {func.name}\n")
            f.write(f"**Boundaries:** {func.bounds}\n")
            print(f"Running {func.name}...")

            for dim in dimensions_list:
                print(f"Dimension {dim}...")
                max_fes = 10000 * dim

                df, histories, file_name = compare_algorithms(
                    opt_func=func,
                    dimensions=dim,
                    population=neighbors,
                    runs=30,
                    std=std,
                    T0=100,
                    Tf=0.01
                )
                df = df.round(5)

                best_row = df.loc[df["Min"].idxmin()]
                worst_row = df.loc[df["Max"].idxmax()]

                f.write(f"\n### {func.name} – Dimenze {dim}\n")
                f.write(f"- 🏆 Nejlepší: algoritmus {best_row['Algorithm']} s hodnotou {best_row['Min']}\n")
                f.write(f"- 💀 Nejhorší: algoritmus {worst_row['Algorithm']} s hodnotou {worst_row['Max']}\n")

                chart_path = os.path.join("charts", file_name)
                table_path = os.path.join("tables", file_name)
                plot_convergence(histories, file_name, title=f"{func.name} - {dim}D")
                plot_table_from_dataframe(df, file_name, title=f"{func.name} - {dim}D")

                f.write(f"\n![Tabulka](./{table_path})\n")
                f.write(f"\n![Graf](./{chart_path})\n")

                for _, row in df.iterrows():
                    summary_data.append({
                        "Function": func.name,
                        "Dimension": dim,
                        "Algorithm": row["Algorithm"],
                        "Mean": row["Mean"]
                    })

        f.write("\n---\n")
        f.write("\n## Závěrečné shrnutí\n")
        summary_df = {}
        for entry in summary_data:
            key = (entry["Function"], entry["Dimension"])
            if key not in summary_df:
                summary_df[key] = []
            summary_df[key].append((entry["Algorithm"], entry["Mean"]))

        for (func_name, dim), entries in summary_df.items():
            best_algo = min(entries, key=lambda x: x[1])
            f.write(f"- Pro funkci **{func_name}**, dimenzi **{dim}** si nejlépe vedl algoritmus **{best_algo[0]}** s průměrnou hodnotou **{best_algo[1]:.5f}**\n")

    print(f"Protokol byl vygenerován do souboru {output_file}")


if __name__ == "__main__":
    generate_protocol()
