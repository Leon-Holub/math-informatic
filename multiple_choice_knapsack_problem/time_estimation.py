import pandas as pd

# Výchozí bod: 20 tříd = 136.47 sekund
base_n = 20
base_time = 136.47

# Vypočteme pro 19 až 24 tříd
rows = []
for n in range(10, 25):
    factor = 3 ** (n - base_n)
    estimated_time = base_time * factor
    rows.append((n, f"{estimated_time:.2f} s"))

# Do tabulky
df_estimates = pd.DataFrame(rows, columns=["Počet tříd", "Odhadovaný čas výpočtu"])
print(df_estimates)
