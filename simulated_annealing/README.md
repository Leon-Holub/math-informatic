# Simulované žíhání a porovnání s HC a LC

## Navigace
- [Sphere](#sphere)
  - [Dimenze 5](#sphere--dimenze-5)
  - [Dimenze 10](#sphere--dimenze-10)
  - [Dimenze 20](#sphere--dimenze-20)
- [Rastrigin](#rastrigin)
  - [Dimenze 5](#rastrigin--dimenze-5)
  - [Dimenze 10](#rastrigin--dimenze-10)
  - [Dimenze 20](#rastrigin--dimenze-20)
- [Styblinski-Tang](#styblinski-tang)
  - [Dimenze 5](#styblinski-tang--dimenze-5)
  - [Dimenze 10](#styblinski-tang--dimenze-10)
  - [Dimenze 20](#styblinski-tang--dimenze-20)

---

## Sphere
**Boundaries:** (-5.12, 5.12)

### Sphere – Dimenze 5
- 🏆 Nejlepší: algoritmus LS s hodnotou 0.00332
- 💀 Nejhorší: algoritmus SA s hodnotou 0.27221

![Tabulka](./tables\Sphere_I5000_D5_N10_STD1.png)

![Graf](./charts\Sphere_I5000_D5_N10_STD1.png)

### Sphere – Dimenze 10
- 🏆 Nejlepší: algoritmus HC s hodnotou 0.24033
- 💀 Nejhorší: algoritmus SA s hodnotou 2.44785

![Tabulka](./tables\Sphere_I10000_D10_N10_STD1.png)

![Graf](./charts\Sphere_I10000_D10_N10_STD1.png)

### Sphere – Dimenze 20
- 🏆 Nejlepší: algoritmus HC s hodnotou 2.14009
- 💀 Nejhorší: algoritmus SA s hodnotou 10.33037

![Tabulka](./tables\Sphere_I20000_D20_N10_STD1.png)

![Graf](./charts\Sphere_I20000_D20_N10_STD1.png)

## Rastrigin
**Boundaries:** (-5.12, 5.12)

### Rastrigin – Dimenze 5
- 🏆 Nejlepší: algoritmus HC s hodnotou 0.73266
- 💀 Nejhorší: algoritmus SA s hodnotou 11.9999

![Tabulka](./tables\Rastrigin_I5000_D5_N10_STD1.png)

![Graf](./charts\Rastrigin_I5000_D5_N10_STD1.png)

### Rastrigin – Dimenze 10
- 🏆 Nejlepší: algoritmus HC s hodnotou 19.18697
- 💀 Nejhorší: algoritmus SA s hodnotou 49.49222

![Tabulka](./tables\Rastrigin_I10000_D10_N10_STD1.png)

![Graf](./charts\Rastrigin_I10000_D10_N10_STD1.png)

### Rastrigin – Dimenze 20
- 🏆 Nejlepší: algoritmus LS s hodnotou 93.52824
- 💀 Nejhorší: algoritmus SA s hodnotou 153.25281

![Tabulka](./tables\Rastrigin_I20000_D20_N10_STD1.png)

![Graf](./charts\Rastrigin_I20000_D20_N10_STD1.png)

## Styblinski-Tang
**Boundaries:** (-5, 5)

### Styblinski-Tang – Dimenze 5
- 🏆 Nejlepší: algoritmus HC s hodnotou -195.21574
- 💀 Nejhorší: algoritmus HC s hodnotou -138.20218

![Tabulka](./tables\StyblinskiTang_I5000_D5_N10_STD1.png)

![Graf](./charts\StyblinskiTang_I5000_D5_N10_STD1.png)

### Styblinski-Tang – Dimenze 10
- 🏆 Nejlepší: algoritmus SA s hodnotou -379.86878
- 💀 Nejhorší: algoritmus HC s hodnotou -269.0033

![Tabulka](./tables\StyblinskiTang_I10000_D10_N10_STD1.png)

![Graf](./charts\StyblinskiTang_I10000_D10_N10_STD1.png)

### Styblinski-Tang – Dimenze 20
- 🏆 Nejlepší: algoritmus SA s hodnotou -683.21899
- 💀 Nejhorší: algoritmus LS s hodnotou -537.15597

![Tabulka](./tables\StyblinskiTang_I20000_D20_N10_STD1.png)

![Graf](./charts\StyblinskiTang_I20000_D20_N10_STD1.png)

---

## Závěrečné shrnutí
- Pro funkci **Sphere**, dimenzi **5** si nejlépe vedl algoritmus **LS** s průměrnou hodnotou **0.03412**
- Pro funkci **Sphere**, dimenzi **10** si nejlépe vedl algoritmus **LS** s průměrnou hodnotou **0.53703**
- Pro funkci **Sphere**, dimenzi **20** si nejlépe vedl algoritmus **HC** s průměrnou hodnotou **3.45278**
- Pro funkci **Rastrigin**, dimenzi **5** si nejlépe vedl algoritmus **HC** s průměrnou hodnotou **4.00736**
- Pro funkci **Rastrigin**, dimenzi **10** si nejlépe vedl algoritmus **LS** s průměrnou hodnotou **30.89031**
- Pro funkci **Rastrigin**, dimenzi **20** si nejlépe vedl algoritmus **HC** s průměrnou hodnotou **117.01526**
- Pro funkci **Styblinski-Tang**, dimenzi **5** si nejlépe vedl algoritmus **SA** s průměrnou hodnotou **-193.42713**
- Pro funkci **Styblinski-Tang**, dimenzi **10** si nejlépe vedl algoritmus **SA** s průměrnou hodnotou **-359.90679**
- Pro funkci **Styblinski-Tang**, dimenzi **20** si nejlépe vedl algoritmus **SA** s průměrnou hodnotou **-646.34103**
