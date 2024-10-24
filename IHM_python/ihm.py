import tkinter as tk
from tkinter import StringVar, ttk
import threading
import random
import time
from communication_handler import *


com = CommunicationHandler()

# Fonctions de collecte de données simulées
def collect_data_1():
    while True:
        # Simuler la collecte de la vitesse du vent
        if not mode_manuel_active:
            com.send_motor_mode(0)
            com.get_wind_speed(enable_print=False)
            
            speed = com.wind_speed
            wind_speed_var.set(f"Vitesse du vent : {speed} km/h")

        elif mode_manuel_active:
            
            com.send_motor_mode(1)
            tmp_speed = motor_speed_entry.get()
            if tmp_speed != "":
                tmp_speed = int(tmp_speed)
                if tmp_speed >= 0 and tmp_speed <256:
                    com.send_motor_speed(int(tmp_speed))
        time.sleep(0.1)

def collect_data_2():
    global mode_luminosity
    while True:

        donnes = com.get_pres_hum_temp_dist_lum_measurements()
        

        if donnes is not None:
            humidity = donnes.get("humidity", None) 
            pressure = donnes.get("pressure", None)  
            temperature = donnes.get("temperature", None)   
            distance = donnes.get("distance", None)

            temperature_var.set(temperature)
            pressure_var.set(pressure)
            humidity_var.set(humidity)
            distance_var.set(distance)
            if mode_luminosity:
                print(f"Luminosity is {mode_luminosity}")
                luminosity = donnes.get("luminosity", None)
                luminosity_var.set(luminosity)

        #time.sleep(0.01)

def collect_data_3():
    while True:
        # Simuler la collecte des degrés d'orientation
        angles = com.get_orientation_measurements()
        if angles is not None:
                    phi = angles.get("phi", None) 
                    theta = angles.get("theta", None)  
                    psi = angles.get("psi", None)   
                                
                    phi_var.set(phi)
                    theta_var.set(theta)
                    psi_var.set(psi)

        
        #time.sleep(0.1)  # Attendre 3 secondes avant la prochaine collecte


# Variable pour garder la trace de l'état du mode manuel
mode_manuel_active = False
mode_luminosity = False
# Fonction pour activer le mode manuel (qui active l'entrée)
def activer_mode_manuel():
    global mode_manuel_active
    
    if not mode_manuel_active:
        motor_speed_entry.config(state="normal")  # Activer l'entrée pour le mode manuel
        mode_manuel_btn.config(text="Passer en mode auto")  # Changer le texte du bouton
        mode_manuel_active = True

    else:
        motor_speed_entry.config(state="disabled")  # Désactiver l'entrée pour le mode auto
        mode_manuel_btn.config(text="Activer mode manuel")  # Revenir au texte initial
        mode_manuel_active = False

def switch_luminosity():
    global mode_luminosity

    if not mode_luminosity:
        luminosity_label.config(state = "normal")
        luminosity_text_label.config(state = "normal")
        mode_luminosity = True
        com.switch_lum_dist()
    else:
        luminosity_label.config(state = "disabled")
        luminosity_text_label.config(state = "disabled")
        mode_luminosity = False
        com.switch_lum_dist()

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
motor_speed_var = StringVar(value="0")  # Vitesse du moteur

# Partie 2
temperature_var = StringVar()
pressure_var = StringVar()
humidity_var = StringVar()
distance_var = StringVar()
luminosity_var = StringVar()

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

# Label pour afficher la vitesse du vent
vitesse_label = ttk.Label(frame1, textvariable=wind_speed_var, font=("Helvetica", 14))
vitesse_label.grid(row=0, column=0, padx=10, pady=5)

# Bouton pour activer le mode manuel
mode_manuel_btn = ttk.Button(frame1, text="Activer mode manuel", command=activer_mode_manuel)
mode_manuel_btn.grid(row=1, column=0, padx=10, pady=5)

# Entrée pour spécifier la vitesse du moteur (désactivée par défaut)
motor_speed_label = ttk.Label(frame1, text="Vitesse du moteur (en tr/min):", font=("Helvetica", 12))
motor_speed_label.grid(row=2, column=0, padx=10, pady=5)

motor_speed_entry = ttk.Entry(frame1, textvariable=motor_speed_var, state="disabled", width=10)
motor_speed_entry.grid(row=3, column=0, padx=10, pady=5)



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
temperature_label = ttk.Label(frame2, textvariable=temperature_var , font=("Helvetica", 14))
temperature_label.grid(row=2, column=3, padx=10, pady=5)

distance_text_label = ttk.Label(frame2, text="Distance: ", font=("Helvetica", 14))
distance_text_label.grid(row=3, column=0, padx=10, pady=5)
distance_label = ttk.Label(frame2, textvariable=distance_var , font=("Helvetica", 14))
distance_label.grid(row=3, column=3, padx=10, pady=5)

luminosity_text_label = ttk.Label(frame2, text="Luminosité: ", font=("Helvetica", 14))
luminosity_text_label.grid(row=4, column=0, padx=10, pady=5)
luminosity_label = ttk.Label(frame2, textvariable=luminosity_var , font=("Helvetica", 14))
luminosity_label.grid(row=4, column=3, padx=10, pady=5)

# Bouton pour switcher la luminosité
luminosity_btn = ttk.Button(frame2, text="Switch luminosité", command=switch_luminosity) #, command=switch_luminosité)
luminosity_btn.grid(row=5, column=2, padx=10, pady=5)



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
theta_label = ttk.Label(frame3, textvariable=theta_var, font=("Helvetica", 14))
theta_label.grid(row=6, column=3, padx=10, pady=5)


psi_text_label = ttk.Label(frame3, text="Psi: ", font=("Helvetica", 14))
psi_text_label.grid(row=7, column=0, padx=10, pady=5)
psi_label = ttk.Label(frame3, textvariable=psi_var, font=("Helvetica", 14))
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
