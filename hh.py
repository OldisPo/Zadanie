import random
import matplotlib.pyplot as plt
import tkinter as tk  # Na tvorbu GUI
from PIL import Image, ImageTk  # Na načítanie a zobrazenie obrázka

# Funkcia na vykreslenie grafu
def plot_graph():
    try:
        # Získanie hodnoty násobenia z input boxu
        multiplier = float(multiplier_entry.get())
    except ValueError:
        # Ak vstup nie je číslo, použije sa predvolená hodnota 2
        multiplier = 2
    
    # 1. Generovanie 40 náhodných záporných čísel
    negatives = [random.randint(-100, -1) for _ in range(40)]
    
    # 2. Zoradenie čísel od najmenšieho po najväčšie
    sorted_negatives = sorted(negatives)
    
    # 3. Násobenie čísel a odstránenie záporného znamienka
    positive_values = [abs(num * multiplier) for num in sorted_negatives]
    
    # 4. Vykreslenie grafu
    plt.figure(figsize=(10, 5))
    plt.plot(positive_values, marker='o', linestyle='-', color='blue', label='Kladné hodnoty')
    plt.title(f'Graf kladných hodnôt (Násobenie: {multiplier}x)')
    plt.xlabel('Index')
    plt.ylabel('Hodnota')
    plt.legend()
    plt.grid()
    plt.show()

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Programovacie techniky")
root.geometry("600x400")  # Zvýšená šírka pre obrázok

# Zobrazenie mena, priezviska a zadania
predmet_label = tk.Label(root, text="Programovacie techniky", font=("Arial", 12))
menoPriezvisko_label = tk.Label(root, text="Šimon Oľha", font=("Arial", 12))
task_label = tk.Label(root, text="Úloha 17", font=("Arial", 12))

# Vstupné pole na zadanie násobiteľa
multiplier_label = tk.Label(root, text="Zadajte násobiteľ:", font=("Arial", 12))
multiplier_entry = tk.Entry(root, font=("Arial", 12))
multiplier_entry.insert(0, "2")  # Predvolená hodnota 2

# Tlačidlo na vykreslenie grafu
plot_button = tk.Button(root, text="Vykresliť graf", command=plot_graph, font=("Arial", 14))

# Načítanie obrázka
try:
    img = Image.open("tuke.jpg")  # Názov vášho obrázka
    img = img.resize((100, 100))  # Zmena veľkosti obrázka
    img_tk = ImageTk.PhotoImage(img)
    
    # Label pre obrázok v pravom hornom rohu
    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk  # Uloženie referencie na obrázok
    img_label.place(x=480, y=10)  # Umiestnenie do pravého horného rohu
except Exception as e:
    print(f"Chyba pri načítaní obrázka: {e}")

# Rozloženie prvkov
predmet_label.pack(pady=10)
menoPriezvisko_label.pack(pady=10)
task_label.pack(pady=10)
multiplier_label.pack(pady=5)
multiplier_entry.pack(pady=5)
plot_button.pack(pady=20)

# Spustenie GUI
root.mainloop()
