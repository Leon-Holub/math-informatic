# Analýza optimalizačních funkcí pomocí náhodného prohledávání

Tento projekt implementuje optimalizační algoritmus **náhodného prohledávání** pro různé testovací funkce.  
Výsledky jsou vizualizovány pomocí grafů zobrazujících konvergenci algoritmu.

## **Použité optimalizační funkce**

Optimalizujeme následující funkce:

- **Sphere Function**
- **Dixon-Price Function**
- **Michaelowicz Function**
- **Styblinski-Tang Function**
- **Rastrigin Function**

Každá z funkcí je testována ve třech dimenzích: **5D, 10D a 20D**.

## **Struktura kódu**

Hlavní soubor **`main.py`** obsahuje:

- Implementaci optimalizačních funkcí
- Náhodný vyhledávací algoritmus
- Ukládání a vizualizaci výsledků pomocí knihovny `matplotlib`

## **Výstupy**

Každý běh algoritmu generuje konvergenční grafy v adresáři `charts/`, pojmenované podle formátu:

Níže jsou ukázky výsledků pro různé dimenze:

### **Sphere Function**

#### **5D**

![Sphere 5D](charts/convergence_Sphere_5D.png)

#### **10D**

![Sphere 10D](charts/convergence_Sphere_10D.png)

#### **20D**

![Sphere 20D](charts/convergence_Sphere_20D.png)

### **Dixon-Price Function**

#### **5D**

![Dixon-Price 5D](charts/convergence_Dixon-Price_5D.png)

#### **10D**

![Dixon-Price 10D](charts/convergence_Dixon-Price_10D.png)

#### **20D**

![Dixon-Price 20D](charts/convergence_Dixon-Price_20D.png)

---

### **Michaelowicz Function**

#### **5D**

![Michaelowicz 5D](charts/convergence_Michaelowicz_5D.png)

#### **10D**

![Michaelowicz 10D](charts/convergence_Michaelowicz_10D.png)

#### **20D**

![Michaelowicz 20D](charts/convergence_Michaelowicz_20D.png)

---

### **Styblinski-Tang Function**

#### **5D**

![Styblinski-Tang 5D](charts/convergence_Styblinski-Tang_5D.png)

#### **10D**

![Styblinski-Tang 10D](charts/convergence_Styblinski-Tang_10D.png)

#### **20D**

![Styblinski-Tang 20D](charts/convergence_Styblinski-Tang_20D.png)

---

### **Rastrigin Function**

#### **5D**

![Rastrigin 5D](charts/convergence_Rastrigin_5D.png)

#### **10D**

![Rastrigin 10D](charts/convergence_Rastrigin_10D.png)

#### **20D**

![Rastrigin 20D](charts/convergence_Rastrigin_20D.png)
