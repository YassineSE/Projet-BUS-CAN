import tkinter as tk
from tkinter import StringVar, ttk
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

        temperature_var.set(temperature)
        pressure_var.set(pressure)
        humidity_var.set(humidity)
        distance_var.set(distance)

        time.sleep(1)

def collect_data_3():
    while True:
        # Simuler la collecte des degrés d'orientation

        phi = random.randint(0,360)
        theta = random.randint(0,360)
        psi = random.randint(0,360) 
        phi_var.set(phi)
        theta_var.set(theta)
        psi_var.set(psi)

        time.sleep(1)  # Attendre 3 secondes avant la prochaine collecte

# Fonction pour démarrer les threads
def start_threads():
    threading.Thread(target=collect_data_1, daemon=True).start()
    threading.Thread(target=collect_data_2, daemon=True).start()
    threading.Thread(target=collect_data_3, daemon=True).start()

# Créer la fenêtre principale
root = tk.Tk()
root.title("IHM de collecte de données")

# Variables pour mettre à jour les labels
# Partie 1
wind_speed_var = StringVar()

# Partie 2
temperature_var = StringVar()
pressure_var = StringVar()
humidity_var = StringVar()
distance_var = StringVar()

# Partie 3
phi_var = StringVar()
theta_var = StringVar()
psi_var = StringVar()

data_var = StringVar()
orientation_var = StringVar()




################ PARTIE 1 ###########################
# Création des sections
"""
frame1 = tk.Frame(root)
frame1.pack(pady=10)
label1 = tk.Label(frame1, textvariable=wind_speed_var, font=("Helvetica", 14))
label1.pack()
"""

# Partie 1: Affichage de la vitesse du vent et activation du mode manuel
frame1 = ttk.LabelFrame(root, text="Partie 1: Vitesse du Vent", padding=(10, 5))
frame1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Label et bouton pour la vitesse du vent
vitesse_label = ttk.Label(frame1, textvariable=wind_speed_var, font=("Helvetica", 14))
vitesse_label.grid(row=0, column=0, padx=10, pady=5)

# Bouton pour activer le mode manuel
mode_manuel_btn = ttk.Button(frame1, text="Activer mode manuel") #, command=activer_mode_manuel)
mode_manuel_btn.grid(row=1, column=0, padx=10, pady=5)





######################## PARTIE 2 #####################################

# Partie 2: Récupération de l'humidité, pression, température et distance, et bouton switch luminosité

frame2 = ttk.LabelFrame(root, text="Partie 2: Conditions ambiantes", padding=(10, 5))
frame2.grid(row=1, column=0, padx=10, pady=5, sticky="ew")



humidity_text_label = ttk.Label(frame2, text="Humidité: ", font=("Helvetica", 14))
humidity_text_label.grid(row=0, column=0, padx=10, pady=5)
humidity_label = ttk.Label(frame2, textvariable=humidity_var , font=("Helvetica", 14))
humidity_label.grid(row=0, column=3, padx=10, pady=5)


pressure_text_label = ttk.Label(frame2, text="Pression: ", font=("Helvetica", 14))
pressure_text_label.grid(row=1, column=0, padx=10, pady=5)
pressure_label = ttk.Label(frame2, textvariable=pressure_var , font=("Helvetica", 14))
pressure_label.grid(row=1, column=3, padx=10, pady=5)


temperature_text_label = ttk.Label(frame2, text="Température: ", font=("Helvetica", 14))
temperature_text_label.grid(row=2, column=0, padx=10, pady=5)
temperature_label = ttk.Label(frame2, textvariable=pressure_var , font=("Helvetica", 14))
temperature_label.grid(row=2, column=3, padx=10, pady=5)

distance_text_label = ttk.Label(frame2, text="Distance: ", font=("Helvetica", 14))
distance_text_label.grid(row=3, column=0, padx=10, pady=5)
distance_label = ttk.Label(frame2, textvariable=distance_var , font=("Helvetica", 14))
distance_label.grid(row=3, column=3, padx=10, pady=5)

# Bouton pour switcher la luminosité
luminosity_btn = ttk.Button(frame2, text="Switch luminosité") #, command=switch_luminosité)
luminosity_btn.grid(row=4, column=2, padx=10, pady=5)



######################### PARTIE 3 ############################

# Partie 3: Récupération des degrés d'orientation de l'accéléromètre et bouton pour 3D view
frame3 = ttk.LabelFrame(root, text="Partie 3: Orientation Accéléromètre", padding=(10, 5))
frame3.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

phi_text_label = ttk.Label(frame3, text="Phi: ", font=("Helvetica", 14))
phi_text_label.grid(row=5, column=0, padx=10, pady=5)
phi_label = ttk.Label(frame3, textvariable=phi_var, font=("Helvetica", 14))
phi_label.grid(row=5, column=3, padx=10, pady=5)

theta_text_label = ttk.Label(frame3, text="Theta: ", font=("Helvetica", 14))
theta_text_label.grid(row=6, column=0, padx=10, pady=5)
theta_label = ttk.Label(frame3, textvariable=phi_var, font=("Helvetica", 14))
theta_label.grid(row=6, column=3, padx=10, pady=5)


psi_text_label = ttk.Label(frame3, text="Psi: ", font=("Helvetica", 14))
psi_text_label.grid(row=7, column=0, padx=10, pady=5)
psi_label = ttk.Label(frame3, textvariable=phi_var, font=("Helvetica", 14))
psi_label.grid(row=7, column=3, padx=10, pady=5)

# Bouton pour ouvrir une vue 3D
view_3d_btn = ttk.Button(frame3, text="Ouvrir vue 3D") #, command=ouvrir_3D_view)
view_3d_btn.grid(row=8, column=2, padx=10, pady=5)



"""


frame2 = tk.Frame(root)
frame2.pack(pady=10)
label2 = tk.Label(frame2, textvariable=data_var, font=("Helvetica", 14))
label2.pack()

frame3 = tk.Frame(root)
frame3.pack(pady=10)
label3 = tk.Label(frame3, textvariable=orientation_var, font=("Helvetica", 14))
label3.pack()


"""



# Démarrer les threads directement sans bouton
start_threads()

# Démarrer l'interface graphique
root.mainloop()
