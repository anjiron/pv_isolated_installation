class GetEnergiaTotal():
    def __init__(self, datos):
        self.datos = datos
        self.e_total = 0
        self.add_calculo_energia()

    def add_calculo_energia(self):
        for i in self.datos.values():
            e_diaria = i['numero'] * i['potencia'] + i['horas']
            i.update({'energia': e_diaria})
        return
    
    def energia_total(self):
        for i in self.datos.values():
            self.e_total = self.e_total + i['energia']   
        return self.e_total