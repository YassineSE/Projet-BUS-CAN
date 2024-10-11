import can
from dataclasses import dataclass
from typing import List

# Définition de la structure du message CAN
@dataclass
class CAN_Message:
    id: int                # Identifiant 29 bits
    data: List[int]       # Champ de données (jusqu'à 8 octets)
    length: int           # Longueur du champ de données en octets
    format: int           # 0 - IDENTIFIANT STANDARD, 1 - IDENTIFIANT ÉTENDU
    type: int             # 0 - CADRE DE DONNÉES, 1 - CADRE À DISTANCE

class CANInterface:
    def __init__(self, channel='can0'):
        # Initialisation de la connexion CAN
        self.bus = can.interface.Bus(channel=channel, bustype='socketcan')

    def send_message(self, can_message: CAN_Message):
        # Envoi d'un message CAN
        msg = can.Message(
            arbitration_id=can_message.id,
            data=can_message.data[:can_message.length],  # Envoyer uniquement la longueur valide
            is_extended_id=can_message.format == 1  # Élargi si le format est 1
        )
        self.bus.send(msg)

    def receive_message(self) -> CAN_Message:
        # Réception d'un message CAN
        msg = self.bus.recv()
        if msg:
            can_message = self.decode_message(msg)
            return can_message
        return None

    def decode_message(self, msg) -> CAN_Message:
        # Décodage d'un message CAN reçu
        can_message = CAN_Message(
            id=msg.arbitration_id,
            data=list(msg.data),
            length=len(msg.data),
            format=1 if msg.is_extended_id else 0,
            type=0  # Supposer que c'est un CADRE DE DONNÉES pour simplifier
        )
        return can_message
