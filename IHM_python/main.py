from PyQt5 import QtCore, QtWidgets
import sys
from can_interface import CANInterface
from ui import IHM

class MainApp:
    def __init__(self):
        self.can_interface = CANInterface()
        self.ihm = IHM()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(10)  # Mettre à jour toutes les 10 msecondes

    def update_data(self):
        # Mise à jour des données affichées
        msg = self.can_interface.receive_message()
        
        if msg:
            # Vérifie que msg.data a au moins 4 éléments
            
                # Si le message vient de l'ID 0x55 pour la vitesse du vent
                if msg.id == 0x55:  # ID pour la vitesse du vent
                    print(msg)
                    self.ihm.wind_speed_label.setText(f'Vitesse du vent: {msg.data[0]}')  # Supposons que la vitesse est dans le premier élément
               
                else:
                    # Afficher un message d'erreur ou une valeur par défaut
                    self.ihm.pressure_label.setText('Pression: N/A')
                    self.ihm.luminosity_label.setText('Luminosité: N/A')
                    self.ihm.distance_label.setText('Distance: N/A')
                    self.ihm.wind_speed_label.setText('Vitesse du vent: N/A')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
