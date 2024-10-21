import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
root = tk.Tk()
root.title("IHM pour Bus CAN")

# Fonction vide pour les boutons (à remplacer par des implémentations réelles plus tard)
def activer_mode_manuel():
    print("Mode manuel activé")

def switch_luminosité():
    print("Luminosité changée")

def ouvrir_3D_view():
    print("Ouverture de la vue 3D")

# Partie 1: Affichage de la vitesse du vent et activation du mode manuel
frame1 = ttk.LabelFrame(root, text="Partie 1: Vitesse du Vent", padding=(10, 5))
frame1.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

# Label et bouton pour la vitesse du vent
vitesse_label = ttk.Label(frame1, text="Vitesse du vent: 0 km/h")
vitesse_label.grid(row=0, column=0, padx=10, pady=5)

# Bouton pour activer le mode manuel
mode_manuel_btn = ttk.Button(frame1, text="Activer mode manuel", command=activer_mode_manuel)
mode_manuel_btn.grid(row=1, column=0, padx=10, pady=5)

# Partie 2: Récupération de l'humidité, pression, température et distance, et bouton switch luminosité
frame2 = ttk.LabelFrame(root, text="Partie 2: Conditions ambiantes", padding=(10, 5))
frame2.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Labels pour afficher les données
humidité_label = ttk.Label(frame2, text="Humidité: --%")
humidité_label.grid(row=0, column=0, padx=10, pady=5)

pression_label = ttk.Label(frame2, text="Pression: -- hPa")
pression_label.grid(row=1, column=0, padx=10, pady=5)

température_label = ttk.Label(frame2, text="Température: --°C")
température_label.grid(row=2, column=0, padx=10, pady=5)

distance_label = ttk.Label(frame2, text="Distance: -- m")
distance_label.grid(row=3, column=0, padx=10, pady=5)

# Bouton pour switcher la luminosité
luminosité_btn = ttk.Button(frame2, text="Switch luminosité", command=switch_luminosité)
luminosité_btn.grid(row=4, column=0, padx=10, pady=5)

# Partie 3: Récupération des degrés d'orientation de l'accéléromètre et bouton pour 3D view
frame3 = ttk.LabelFrame(root, text="Partie 3: Orientation Accéléromètre", padding=(10, 5))
frame3.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

# Label pour l'orientation de l'accéléromètre
orientation_label = ttk.Label(frame3, text="Orientation: --°")
orientation_label.grid(row=0, column=0, padx=10, pady=5)

# Bouton pour ouvrir une vue 3D
view_3d_btn = ttk.Button(frame3, text="Ouvrir vue 3D", command=ouvrir_3D_view)
view_3d_btn.grid(row=1, column=0, padx=10, pady=5)

# Boucle principale de l'interface
root.mainloop()
