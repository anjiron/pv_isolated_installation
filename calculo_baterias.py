
import energia_total

class SetBaterias():
    def __init__(self, energia_total):

        self.energia_total = energia_total
        self.prof_des_diaria = 0.15
        self.prof_des_semanal = 0.60
        self.tension_instalacion = 24

    def capacidad_bat_prof_diaria(self):
        energia_diaria_necesaria = self.energia_total / self.prof_des_diaria
        capac_diaria = energia_diaria_necesaria / self.tension_instalacion
        return capac_diaria

    def capacidad_bat_prof_semanal(self):
        energia_semanal_necesaria = (self.energia_total * 7) / self.prof_des_semanal
        capac_semanal = energia_semanal_necesaria / self.tension_instalacion

        return capac_semanal


#SetBaterias(3534).capacidad_bat_prof_diaria()
#SetBaterias(3534).capacidad_bat_prof_semanal()