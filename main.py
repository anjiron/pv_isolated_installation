
class PvInsolated():
    def __init__(self):
        self.dispositivos()
        self.add_calculo_energia()
        self.potencia_total()
        self.energia_total()
        return
    
    def dispositivos(self):
        self.datos = {
                    'luminarias': {'numero': 16, 'potencia': 10, 'horas': 6},
                    'ordenadores': {'numero': 2, 'potencia': 70, 'horas': 2},
                    'frigorifico': {'numero': 3, 'potencia': 700, 'horas': 12},
                    'television': {'numero': 2, 'potencia': 100, 'horas': 4}
                    }
        return 
    
    def add_calculo_energia(self):
        for i in self.datos.values():
            e_diaria = i['numero'] * i['potencia'] + i['horas']
            i.update({'energia': e_diaria})
        return
    
    def potencia_total(self):
        p_total = 0
        for i in self.datos.values():
            p_total = p_total + i['potencia']   
        return print(p_total)
              

    def energia_total(self):
        e_total = 0
        for i in self.datos.values():
            e_total = e_total + i['energia']   
        return print(e_total)



PvInsolated()