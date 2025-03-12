# Horolezecký algoritmus a lokální prohledávání 

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
- **Local Search**: 0.0001 při bodě **[0.00599551 0.00968066]** s nastavením: Iterace **100**, Sousedi **5**, STD **3**.
- **Hill Climber**: 0.0057 při bodě **[-0.07309605 -0.01797293]** s nastavením: Iterace **20**, Sousedi **10**, STD **1**.

#### Nejhorší výsledek:
- **Local Search**: 0.3493 při bodě **[ 0.01458932 -0.5908189 ]** s nastavením: Iterace **20**, Sousedi **5**, STD **3**.
- **Hill Climber**: 4.1263 při bodě **[-1.74142306  1.0458111 ]** s nastavením: Iterace **20**, Sousedi **5**, STD **3**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 0.0593 | 1.6317 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 0.3493 | 4.1263 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 0.2641 | 3.0836 | ![LS](plots/Sphere__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 0.0300 | 0.0057 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 0.1271 | 0.2900 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 0.3028 | 2.8612 | ![LS](plots/Sphere__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 0.0081 | 0.0882 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 0.0301 | 0.2759 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 0.0123 | 2.0951 | ![LS](plots/Sphere__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 0.0132 | 0.4208 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 0.0609 | 2.6381 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 0.2342 | 1.5743 | ![LS](plots/Sphere__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 0.0084 | 0.2173 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 0.0055 | 1.1482 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.0321 | 0.0908 | ![LS](plots/Sphere__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 0.0018 | 0.1499 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 0.0014 | 1.8327 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 0.0030 | 1.2336 | ![LS](plots/Sphere__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.0046 | 0.1067 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 0.0001 | 2.4356 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 0.0109 | 1.4488 | ![LS](plots/Sphere__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 0.0037 | 0.1800 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 0.0063 | 0.1316 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 0.0305 | 0.4782 | ![LS](plots/Sphere__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.0008 | 0.0819 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 0.0109 | 0.4368 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 0.0105 | 1.3951 | ![LS](plots/Sphere__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Sphere__Hill_climber_I100_D2_N20_STD5.png) |

## Dixon-Price

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: 0.0018 při bodě **[0.96743807 0.68545169]** s nastavením: Iterace **50**, Sousedi **20**, STD **1**.
- **Hill Climber**: 0.0010 při bodě **[0.98723849 0.71264259]** s nastavením: Iterace **100**, Sousedi **20**, STD **3**.

#### Nejhorší výsledek:
- **Local Search**: 0.5454 při bodě **[ 0.69217363 -0.10210748]** s nastavením: Iterace **20**, Sousedi **20**, STD **5**.
- **Hill Climber**: 299.8511 při bodě **[0.39119073 2.97461709]** s nastavením: Iterace **20**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 0.0020 | 1.0874 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 0.2728 | 5.5677 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 0.1852 | 299.8511 | ![LS](plots/DixonPrice__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 0.0203 | 0.1441 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 0.0680 | 0.7454 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 0.0977 | 7.9132 | ![LS](plots/DixonPrice__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 0.0046 | 0.1027 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 0.0421 | 0.2666 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 0.5454 | 0.7909 | ![LS](plots/DixonPrice__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 0.0292 | 0.6704 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 0.2890 | 63.6882 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 0.0843 | 1.1258 | ![LS](plots/DixonPrice__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 0.0024 | 0.5577 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 0.1537 | 0.3828 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.1992 | 14.3804 | ![LS](plots/DixonPrice__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 0.0018 | 0.0869 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 0.0020 | 2.3680 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 0.0538 | 13.5762 | ![LS](plots/DixonPrice__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.0190 | 0.8329 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 0.0366 | 2.4068 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 0.1634 | 12.9863 | ![LS](plots/DixonPrice__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 0.0112 | 0.4477 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 0.0053 | 14.7251 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 0.0310 | 0.4417 | ![LS](plots/DixonPrice__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.0025 | 0.1108 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 0.0043 | 0.0010 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 0.0086 | 4.9948 | ![LS](plots/DixonPrice__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/DixonPrice__Hill_climber_I100_D2_N20_STD5.png) |

## Michaelowicz

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: -1.8001 při bodě **[2.19800145 1.56635011]** s nastavením: Iterace **20**, Sousedi **20**, STD **3**.
- **Hill Climber**: -1.3558 při bodě **[1.9998671  1.58933013]** s nastavením: Iterace **50**, Sousedi **5**, STD **5**.

#### Nejhorší výsledek:
- **Local Search**: -1.0014 při bodě **[1.65779641 1.58014727]** s nastavením: Iterace **20**, Sousedi **5**, STD **5**.
- **Hill Climber**: -0.0175 při bodě **[0.94451831 1.85170986]** s nastavením: Iterace **50**, Sousedi **5**, STD **3**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | -1.5400 | -1.1739 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | -1.5032 | -0.1691 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | -1.0014 | -0.0548 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | -1.6135 | -0.9780 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | -1.7095 | -0.1876 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | -1.3554 | -0.5205 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | -1.6618 | -0.8774 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | -1.8001 | -1.0485 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | -1.7667 | -0.9999 | ![LS](plots/Michaelowicz__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | -1.7884 | -0.4902 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | -1.2661 | -0.0175 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | -1.5324 | -1.3558 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | -1.7411 | -0.8063 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | -1.6108 | -0.9483 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | -1.6693 | -0.8469 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | -1.7789 | -1.0000 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | -1.6927 | -0.8007 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | -1.6476 | -0.9770 | ![LS](plots/Michaelowicz__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | -1.6982 | -0.7854 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | -1.4466 | -0.4565 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | -1.6237 | -0.1156 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | -1.7819 | -0.7974 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | -1.6762 | -0.6727 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | -1.6386 | -0.9845 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | -1.7932 | -1.1274 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | -1.7938 | -1.0387 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | -1.7267 | -0.9853 | ![LS](plots/Michaelowicz__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Michaelowicz__Hill_climber_I100_D2_N20_STD5.png) |

## Styblinski-Tang

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: -78.3239 při bodě **[-2.91359255 -2.92318409]** s nastavením: Iterace **100**, Sousedi **20**, STD **1**.
- **Hill Climber**: -78.2842 při bodě **[-2.90366253 -2.95584409]** s nastavením: Iterace **50**, Sousedi **10**, STD **5**.

#### Nejhorší výsledek:
- **Local Search**: -62.4907 při bodě **[ 3.00899019 -3.08395995]** s nastavením: Iterace **20**, Sousedi **10**, STD **3**.
- **Hill Climber**: -34.3021 při bodě **[-3.55531442 -0.58831738]** s nastavením: Iterace **50**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | -77.4847 | -54.7023 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | -77.6432 | -64.4777 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | -62.8518 | -57.6188 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | -64.1302 | -62.5209 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | -62.4907 | -78.0506 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | -77.4084 | -57.5062 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | -78.2710 | -63.4023 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | -77.8979 | -75.3508 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | -77.8258 | -67.9829 | ![LS](plots/StyblinskiTang__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | -64.1046 | -72.8303 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | -76.2956 | -44.2230 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | -77.6399 | -34.3021 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | -78.3188 | -77.5695 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | -78.2592 | -73.3352 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | -77.9119 | -78.2842 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | -78.2976 | -60.6621 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | -77.8779 | -67.9204 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | -78.0885 | -77.3092 | ![LS](plots/StyblinskiTang__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | -64.1306 | -76.5206 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | -77.8807 | -63.3663 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | -77.1127 | -46.8622 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | -64.1582 | -75.5996 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | -78.2870 | -70.2795 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | -77.9158 | -62.2189 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | -78.3239 | -78.1754 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | -78.3144 | -57.9772 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | -78.1005 | -63.3245 | ![LS](plots/StyblinskiTang__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/StyblinskiTang__Hill_climber_I100_D2_N20_STD5.png) |

## Rastrigin

### Nejlepší a nejhorší nalezené hodnoty
#### Nejlepší výsledek:
- **Local Search**: 0.0747 při bodě **[0.00854437 0.01743464]** s nastavením: Iterace **50**, Sousedi **5**, STD **3**.
- **Hill Climber**: 0.5977 při bodě **[-0.02905179 -0.04676051]** s nastavením: Iterace **100**, Sousedi **10**, STD **1**.

#### Nejhorší výsledek:
- **Local Search**: 9.8566 při bodě **[0.83619229 1.94871973]** s nastavením: Iterace **20**, Sousedi **5**, STD **3**.
- **Hill Climber**: 30.7557 při bodě **[ 2.22830561 -0.63207692]** s nastavením: Iterace **100**, Sousedi **5**, STD **5**.

### Výsledky jednotlivých testů

| Iterace | Sousedi | STD | LS Hodnota | HC Hodnota | LS Graf | HC Graf |
|---------|--------|-----|------------|------------|---------|---------|
| 20 | 5 | 1 | 3.9926 | 15.3733 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD1.png) |
| 20 | 5 | 3 | 9.8566 | 4.1658 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD3.png) |
| 20 | 5 | 5 | 3.0941 | 27.4898 | ![LS](plots/Rastrigin__Local_search_I20_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N5_STD5.png) |
| 20 | 10 | 1 | 1.4141 | 6.0832 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD1.png) |
| 20 | 10 | 3 | 4.1994 | 1.1072 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD3.png) |
| 20 | 10 | 5 | 1.8156 | 24.1998 | ![LS](plots/Rastrigin__Local_search_I20_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N10_STD5.png) |
| 20 | 20 | 1 | 1.0359 | 2.0235 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD1.png) |
| 20 | 20 | 3 | 2.4163 | 12.1162 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD3.png) |
| 20 | 20 | 5 | 1.3942 | 11.9827 | ![LS](plots/Rastrigin__Local_search_I20_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I20_D2_N20_STD5.png) |
| 50 | 5 | 1 | 1.5990 | 19.3888 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD1.png) |
| 50 | 5 | 3 | 0.0747 | 11.5590 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD3.png) |
| 50 | 5 | 5 | 4.0147 | 25.4808 | ![LS](plots/Rastrigin__Local_search_I50_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N5_STD5.png) |
| 50 | 10 | 1 | 1.0600 | 7.0181 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD1.png) |
| 50 | 10 | 3 | 1.4650 | 13.7680 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD3.png) |
| 50 | 10 | 5 | 0.5972 | 12.3828 | ![LS](plots/Rastrigin__Local_search_I50_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N10_STD5.png) |
| 50 | 20 | 1 | 0.1305 | 4.5481 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD1.png) |
| 50 | 20 | 3 | 1.0600 | 9.9378 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD3.png) |
| 50 | 20 | 5 | 1.3764 | 16.0192 | ![LS](plots/Rastrigin__Local_search_I50_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I50_D2_N20_STD5.png) |
| 100 | 5 | 1 | 0.5589 | 2.6137 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD1.png) |
| 100 | 5 | 3 | 2.6674 | 28.5195 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD3.png) |
| 100 | 5 | 5 | 2.5347 | 30.7557 | ![LS](plots/Rastrigin__Local_search_I100_D2_N5_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N5_STD5.png) |
| 100 | 10 | 1 | 0.2597 | 0.5977 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD1.png) |
| 100 | 10 | 3 | 1.3574 | 6.0861 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD3.png) |
| 100 | 10 | 5 | 0.5442 | 30.2604 | ![LS](plots/Rastrigin__Local_search_I100_D2_N10_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N10_STD5.png) |
| 100 | 20 | 1 | 0.1542 | 1.6022 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD1.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD1.png) |
| 100 | 20 | 3 | 1.5406 | 3.8935 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD3.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD3.png) |
| 100 | 20 | 5 | 0.2089 | 11.0679 | ![LS](plots/Rastrigin__Local_search_I100_D2_N20_STD5.png) | ![HC](plots/Rastrigin__Hill_climber_I100_D2_N20_STD5.png) |

## Závěr

Na základě provedených experimentů lze vyvodit následující závěry:

- **Local Search byl úspěšnější** ve většině testovaných funkcí (4 vs. 1).
- Local Search dosahoval stabilnějších výsledků, ale měl tendenci uvíznout v lokálních minimech.
- Počet sousedů a velikost STD mají výrazný vliv na výsledky obou metod.
- Optimální hodnoty STD se obvykle pohybovaly mezi 2–3.
- Vyšší počet sousedů (10–20) umožnil robustnější prohledávání prostoru.
