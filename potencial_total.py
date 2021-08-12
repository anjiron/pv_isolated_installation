
class GetPotenciaTotal():
    def __init__(self, datos):
        self.p_total = 0
        self.datos = datos

    def potencia_total(self):
        for i in self.datos.values():
            self.p_total = self.p_total + i['potencia']   
        return self.p_total