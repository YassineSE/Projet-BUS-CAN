import tkinter as tk
from tkinter import StringVar
import threading
import random
import time

# Fonctions de collecte de données simulées
def collect_data_1():
    while True:
        # Simuler la collecte de la vitesse du vent
        speed = random.randint(0, 100)  # Remplacez par une collecte réelle
        wind_speed_var.set(f"Vitesse du vent : {speed} km/h")
        time.sleep(1)  # Attendre 1 seconde avant la prochaine collecte

def collect_data_2():
    while True:
        # Simuler la collecte de l'humidité, pression, température et distance
        humidity = random.randint(20, 80)  # Remplacez par une collecte réelle
        pressure = random.randint(900, 1100)  # Remplacez par une collecte réelle
        temperature = random.randint(-10, 40)  # Remplacez par une collecte réelle
        distance = random.randint(0, 100)  # Remplacez par une collecte réelle
        data = f"Humidité : {humidity}%, Pression : {pressure} hPa, Température : {temperature} °C, Distance : {distance} m"
        data_var.set(data)
        time.sleep(2)  # Attendre 2 secondes avant la prochaine collecte

def collect_data_3():
    while True:
        # Simuler la collecte des degrés d'orientation
        orientation = random.randint(0, 360)  # Remplacez par une collecte réelle
        orientation_var.set(f"Orientation : {orientation}°")
        time.sleep(3)  # Attendre 3 secondes avant la prochaine collecte

# Fonction pour démarrer les threads
def start_threads():
    threading.Thread(target=collect_data_1, daemon=True).start()
    threading.Thread(target=collect_data_2, daemon=True).start()
    threading.Thread(target=collect_data_3, daemon=True).start()

# Créer la fenêtre principale
root = tk.Tk()
root.title("IHM de collecte de données")

# Variables pour mettre à jour les labels
wind_speed_var = StringVar()
data_var = StringVar()
orientation_var = StringVar()

# Création des sections
frame1 = tk.Frame(root)
frame1.pack(pady=10)
label1 = tk.Label(frame1, textvariable=wind_speed_var, font=("Helvetica", 14))
label1.pack()

frame2 = tk.Frame(root)
frame2.pack(pady=10)
label2 = tk.Label(frame2, textvariable=data_var, font=("Helvetica", 14))
label2.pack()

frame3 = tk.Frame(root)
frame3.pack(pady=10)
label3 = tk.Label(frame3, textvariable=orientation_var, font=("Helvetica", 14))
label3.pack()

# Démarrer les threads directement sans bouton
start_threads()

# Démarrer l'interface graphique
root.mainloop()
