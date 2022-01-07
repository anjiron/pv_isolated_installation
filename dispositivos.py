
class SetDispositivos():
    def __init__(self):
        # Estos datos de entra en el futuro vendrán desde web 
        self.datos = {}


    def dispositivos(self):
        self.datos = {
                    'luminarias': {'numero': 16, 'potencia': 10, 'horas': 6},
                    'ordenadores': {'numero': 2, 'potencia': 100, 'horas': 2},
                    'frigorifico': {'numero': 2, 'potencia': 700, 'horas': 12},
                    'ventilador': {'numero': 2, 'potencia': 80, 'horas': 4},
                    'lavadora': {'numero': 1, 'potencia': 800, 'horas': 1},
                    'television': {'numero': 2, 'potencia': 100, 'horas': 4},
                    'bomba_presion': {'numero': 1, 'potencia': 130, 'horas': 1}
                    }
        return self.datos

