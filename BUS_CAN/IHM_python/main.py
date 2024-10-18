import sys
from can_interface import CANInterface, CAN_Message
import time

ID_1 = 1

class MainApp:
    def __init__(self):
        # Initialisation de l'interface CAN
        self.can_interface= CANInterface(channel='can0')      

    
    def send_vel_motor(self, vel):

        # Préparation du message avec ID = 1 et données = [140]
        message = CAN_Message(
            id=1,               # Identifiant du message
            data=[3,vel],         # Données, ici la valeur 140
            length=2,           # Longueur des données
            format=0,           # Format standard (11 bits)
            type=0              # Cadre de données (Data Frame)
        )
        self.can_interface.send_message(message)

    def get_vel_vent(self):
         # Préparation du message avec ID = 1 et données = [140]
        message = CAN_Message(
            id=1,               # Identifiant du message
            data=[1],         # Données, ici la valeur 140
            length=1,           # Longueur des données
            format=0,           # Format standard (11 bits)
            type=0              # Cadre de données (Data Frame)
        )
        self.can_interface.send_message(message)
        msg = self.can_interface.receive_message()  # Recevoir un message
        if msg:
            # Mettre à jour les labels de l'IHM en fonction de l'ID du message
            if msg.id == 0x55:  # Vitesse du vent
                vitesse_vent = msg.data[0] 
                print('Velocité du vent:' + str(vitesse_vent))


    def send_mode_moteur(self, manuel):

        # Préparation du message avec ID = 1 et données = [140]
        message = CAN_Message(
            id=1,               # Identifiant du message
            data=[2,manuel],    # 1 manuel, 0 auto
            length=2,           # Longueur des données
            format=0,           # Format standard (11 bits)
            type=0              # Cadre de données (Data Frame)
        )
        self.can_interface.send_message(message)


if __name__ == '__main__':
    main_app = MainApp() 
    vel = 50
    print('mode auto')
    time.sleep(5)
    main_app.send_vel_motor(vel)
    main_app.send_mode_moteur(1)
    print('mode manuel')
    time.sleep(5)
    main_app.send_mode_moteur(0)
    print('mode auto')
    while(1):
        main_app.get_vel_vent()
        



    
        




