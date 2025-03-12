# Optimalizační Protokol

Tento protokol dokumentuje optimalizaci různých testovacích funkcí pomocí algoritmů Local Search a Hill Climber.
Testování probíhá na stejném startovacím bodě pro každou funkci s pevnou dimenzí **2**. Cílem je porovnat efektivitu algoritmů a vliv různých parametrů na nalezení minima.

## Navigace

- [Sphere](#sphere)
- [Dixon-Price](#dixon-price)
- [Michaelowicz](#michaelowicz)
- [Styblinski-Tang](#styblinski-tang)
- [Rastrigin](#rastrigin)

## Sphere

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: 0.0000 při bodě **[-0.00426142 -0.0004346 ]** s nastavením: Iterace **100**, Sousedi **20**, STD **1**.
- **Hill Climber**: 0.0054 při bodě **[-0.0730295  -0.00410318]** s nastavením: Iterace **100**, Sousedi **20**, STD **1**.

#### Nejhorší výsledek:
- **Local Search**: 0.3373 při bodě **[ 0.11370976 -0.5695711 ]** s nastavením: Iterace **20**, Sousedi **10**, STD **5**.
- **Hill Climber**: 6.7356 při bodě **[-0.58748868  2.52793146]** s nastavením: Iterace **20**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 0.0570 | 1.3022 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 0.0377 | 2.4860 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 0.2971 | 6.7356 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 0.0104 | 0.9621 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 0.0202 | 2.5378 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 0.3373 | 0.0234 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 0.0015 | 0.0550 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 0.0045 | 0.9010 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 0.0098 | 4.1221 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 0.0087 | 0.2344 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 0.0343 | 2.2458 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 0.0407 | 1.0542 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 0.0052 | 0.0655 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 0.0391 | 4.6655 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.1631 | 3.2660 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 0.0042 | 0.1803 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 0.0152 | 0.3140 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 0.0045 | 0.3559 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.0052 | 0.1063 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 0.0021 | 1.0325 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 0.0652 | 3.7228 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 0.0008 | 0.1795 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 0.0036 | 1.8700 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 0.0228 | 4.6003 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.0000 | 0.0054 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 0.0027 | 1.4614 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 0.0045 | 1.9410 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD5.png) |

## Dixon-Price

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: 0.0006 při bodě **[ 0.99133908 -0.71183797]** s nastavením: Iterace **50**, Sousedi **20**, STD **1**.
- **Hill Climber**: 0.0072 při bodě **[0.92255713 0.69163401]** s nastavením: Iterace **100**, Sousedi **20**, STD **3**.

#### Nejhorší výsledek:
- **Local Search**: 0.2716 při bodě **[ 1.48414512 -0.9156855 ]** s nastavením: Iterace **50**, Sousedi **5**, STD **5**.
- **Hill Climber**: 331.9081 při bodě **[ 6.19662628 -3.43933891]** s nastavením: Iterace **100**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 0.0074 | 0.3072 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 0.1835 | 2.9332 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 0.0348 | 269.1522 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 0.0603 | 0.0812 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 0.0273 | 0.1860 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 0.2132 | 3.8380 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 0.0202 | 0.3778 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 0.0627 | 1.8671 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 0.0438 | 0.3902 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 0.0230 | 4.0096 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 0.0461 | 1.4334 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 0.2716 | 14.6732 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 0.0083 | 0.5568 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 0.0250 | 1.9451 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.1873 | 3.3098 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 0.0006 | 0.3748 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 0.0261 | 1.1176 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 0.1270 | 17.6982 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.0010 | 0.2902 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 0.0138 | 2.4810 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 0.0040 | 331.9081 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 0.0021 | 0.7560 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 0.0655 | 0.3891 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 0.0121 | 1.5464 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.0033 | 0.5901 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 0.0401 | 0.0072 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 0.0125 | 13.6464 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD5.png) |

## Michaelowicz

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: -1.7930 při bodě **[2.21053349 1.58428296]** s nastavením: Iterace **50**, Sousedi **20**, STD **1**.
- **Hill Climber**: -1.7999 při bodě **[2.19402687 1.57224726]** s nastavením: Iterace **100**, Sousedi **10**, STD **5**.

#### Nejhorší výsledek:
- **Local Search**: -1.0578 při bodě **[2.10519969 2.69117377]** s nastavením: Iterace **20**, Sousedi **5**, STD **3**.
- **Hill Climber**: -0.0554 při bodě **[0.96033311 1.28392457]** s nastavením: Iterace **50**, Sousedi **5**, STD **1**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | -1.1689 | -0.8171 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | -1.0578 | -0.6569 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | -1.4866 | -1.1914 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | -1.5871 | -1.6115 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | -1.7560 | -0.8953 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | -1.6158 | -1.5957 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | -1.7769 | -0.9889 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | -1.6580 | -0.8560 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | -1.7624 | -1.0563 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | -1.6781 | -0.0554 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | -1.7675 | -0.7741 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | -1.7099 | -0.5582 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | -1.7079 | -0.7788 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | -1.6578 | -1.1840 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | -1.7497 | -0.6848 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | -1.7930 | -0.9894 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | -1.7197 | -1.3043 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | -1.7574 | -1.4759 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | -1.7562 | -0.9917 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | -1.4272 | -0.9858 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | -1.7021 | -0.8361 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | -1.7280 | -0.8301 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | -1.7240 | -0.7982 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | -1.7398 | -1.7999 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | -1.7891 | -1.0919 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | -1.7729 | -1.7876 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | -1.7333 | -0.9278 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD5.png) |

## Styblinski-Tang

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: -78.3069 při bodě **[-2.87962065 -2.9334426 ]** s nastavením: Iterace **50**, Sousedi **10**, STD **3**.
- **Hill Climber**: -76.9750 při bodě **[-2.65004185 -3.04034882]** s nastavením: Iterace **100**, Sousedi **20**, STD **5**.

#### Nejhorší výsledek:
- **Local Search**: -49.7613 při bodě **[2.68991047 2.61238816]** s nastavením: Iterace **50**, Sousedi **5**, STD **1**.
- **Hill Climber**: -30.5086 při bodě **[2.15005793 1.35298787]** s nastavením: Iterace **50**, Sousedi **5**, STD **1**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | -50.0400 | -35.3314 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | -78.2727 | -61.8062 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | -76.8142 | -57.2296 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | -49.9874 | -48.6334 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | -76.1671 | -58.5550 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | -77.7391 | -56.6698 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | -50.0099 | -48.1022 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | -78.1484 | -73.6107 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | -78.0697 | -63.3896 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | -49.7613 | -30.5086 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | -77.6800 | -44.3328 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | -76.8516 | -75.1769 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | -49.9421 | -48.9855 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | -78.3069 | -64.7443 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | -77.6104 | -68.1694 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | -50.0559 | -49.1269 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | -78.1780 | -57.1526 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | -77.9621 | -76.2889 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | -50.0012 | -49.9458 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | -77.9410 | -66.7672 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | -72.5970 | -63.2071 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | -50.0224 | -48.9054 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | -78.0597 | -72.3556 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | -77.9712 | -53.7302 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | -50.0562 | -49.9355 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | -78.2075 | -76.0643 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | -78.2884 | -76.9750 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD5.png) |

## Rastrigin

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: 0.2724 při bodě **[0.0025254  0.03704861]** s nastavením: Iterace **50**, Sousedi **20**, STD **5**.
- **Hill Climber**: 2.3382 při bodě **[0.02529328 1.07388394]** s nastavením: Iterace **100**, Sousedi **20**, STD **1**.

#### Nejhorší výsledek:
- **Local Search**: 5.9143 při bodě **[ 0.85064392 -0.97176801]** s nastavením: Iterace **20**, Sousedi **5**, STD **5**.
- **Hill Climber**: 27.6347 při bodě **[-0.20539425 -1.60832174]** s nastavením: Iterace **20**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 2.6939 | 8.1947 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 2.9670 | 26.0070 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 5.9143 | 27.6347 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 3.3067 | 4.6619 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 1.1164 | 4.1723 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 2.6541 | 13.9815 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 0.5759 | 3.4170 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 1.4992 | 11.2915 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 2.4961 | 18.1318 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 0.6055 | 14.5338 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 1.8648 | 17.0988 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 1.1244 | 15.1923 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 0.5562 | 6.0361 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 1.8855 | 10.6224 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.6285 | 10.3309 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 1.1679 | 4.9898 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 2.5142 | 6.4272 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 0.2724 | 10.1282 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.4940 | 15.5991 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 1.6021 | 13.6450 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 2.5878 | 19.7122 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 1.1713 | 10.8011 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 1.9953 | 9.5745 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 1.7360 | 18.9999 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.3408 | 2.3382 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 1.9247 | 4.4789 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 1.0737 | 11.5834 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD5.png) |

## Závěr

Na základě provedených experimentů lze vyvodit následující závěry:

- **Celkově se lépe vedl Local Search**, který dosáhl v průměru lepší hodnoty než Hill Climber (**-15.9654 vs. -15.2848**).
- Local Search je stabilnější, ale má tendenci uvíznout v lokálních minimech.
- Počet sousedů a velikost STD mají výrazný vliv na výsledky obou metod.
- Optimální hodnoty STD se obvykle pohybovaly mezi 2–3.
- Vyšší počet sousedů (10–20) umožnil robustnější prohledávání prostoru.
