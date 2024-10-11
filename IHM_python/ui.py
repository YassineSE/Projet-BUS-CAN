from PyQt5 import QtWidgets
import sys

class IHM(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configuration de la fenêtre principale
        self.setWindowTitle('Interfaçage IHM')
        self.setGeometry(100, 100, 600, 400)

        # Ajout de Widgets pour afficher les données
        self.pressure_label = QtWidgets.QLabel('Pression: ', self)
        self.luminosity_label = QtWidgets.QLabel('Luminosité: ', self)
        self.distance_label = QtWidgets.QLabel('Distance: ', self)
        self.wind_speed_label = QtWidgets.QLabel('Vitesse du vent: ', self)

        # Mise en page
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pressure_label)
        layout.addWidget(self.luminosity_label)
        layout.addWidget(self.distance_label)
        layout.addWidget(self.wind_speed_label)
        self.setLayout(layout)

        self.show()

def main():
    # Lancement de l'application
    app = QtWidgets.QApplication(sys.argv)
    ihm = IHM()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
