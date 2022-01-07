
class SetDispositivos():
    def __init__(self, num_dispositivos):
        # Los datos de entra vienen desde la web, el número de cada dispositivo
        # por ahora la potencia y horas de utilización se quedan fijas.

        self.num_dispositivos = num_dispositivos
        self.datos = {}


    def dispositivos(self):
        self.datos = {
                    'luminarias': {'numero': self.num_dispositivos['luminarias'], 'potencia': 10, 'horas': 6},
                    'ordenadores': {'numero': self.num_dispositivos['ordenadores'], 'potencia': 100, 'horas': 2},
                    'frigorificos': {'numero': self.num_dispositivos['frigorificos'], 'potencia': 700, 'horas': 12},
                    'ventiladores': {'numero': self.num_dispositivos['ventilador'], 'potencia': 80, 'horas': 4},
                    'lavadoras': {'numero': self.num_dispositivos['lavadoras'], 'potencia': 800, 'horas': 1},
                    'televisiones': {'numero': self.num_dispositivos['televisiones'], 'potencia': 100, 'horas': 4},
                    'bomba_presion': {'numero': self.num_dispositivos['bomba_presion'], 'potencia': 130, 'horas': 1}
                    }
        return self.datos

