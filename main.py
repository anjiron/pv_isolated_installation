
import dispositivos
import potencial_total
import energia_total
import radiacion

class PvInsolated():
    def __init__(self):
        self.radiacion = radiacion.GetRadiacion()
        self.dispositivos = dispositivos.SetDispositivos()
        datos_dic = self.dispositivos.dispositivos()
        self.potencia_t = potencial_total.GetPotenciaTotal(datos_dic)
        self.energia_t = energia_total.GetEnergiaTotal(datos_dic)
        
        print (datos_dic)
        print ("Potencia total: ", self.potencia_t.potencia_total())
        print ("Energía total: ", self.energia_t.energia_total())
    
    
    # def rendimiento_instalacion(self):
    #     n = 0.75
    #     energia = self.energia_total() / n
    #     return print(energia)



PvInsolated()