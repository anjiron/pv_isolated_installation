
import dispositivos
import potencial_total
import energia_total
import radiacion
import calculo_paneles
import calculo_baterias

class PvInsolated():
    def __init__(self):
        self.radiacion = radiacion.GetRadiacion()
        radiacion_min = self.radiacion.obtener_radiacion_min()
        self.dispositivos = dispositivos.SetDispositivos()
        datos_dic = self.dispositivos.dispositivos()
        self.potencia_t = potencial_total.GetPotenciaTotal(datos_dic)
        self.energia_t = energia_total.GetEnergiaTotal(datos_dic)
        energia_t = self.energia_t.energia_total()
        self.calculo_paneles = calculo_paneles.SetPaneles(energia_t, radiacion_min)
        paneles = self.calculo_paneles.calculo_paneles()
        self.calculo_baterias = calculo_baterias.SetBaterias(energia_t)
        cap_baterias_diaria = self.calculo_baterias.capacidad_bat_prof_diaria()
        cap_baterias_tres_dias = self.calculo_baterias.capacidad_bat_prof_tres_dias()

        print (datos_dic)
        print ("Potencia total: ", self.potencia_t.potencia_total)
        print ("Energía total: ", energia_t)
        print ("Radiacion minima: ", radiacion_min)
        print ("Paneles a instalar: ", paneles)
        print ("Capacidad baterias a instalar (Diaria): ", cap_baterias_diaria)
        print ("Capacidad baterias a instalar (Tres_Dias): ", cap_baterias_tres_dias)
    # def rendimiento_instalacion(self):
    #     n = 0.75
    #     energia = self.energia_total() / n
    #     return print(energia)



PvInsolated()