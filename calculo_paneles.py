
class SetPaneles():
    def __init__(self, energia_total, rad_media_min):
        self.energia_total = energia_total
        self.rad_media_min = rad_media_min
        self.p_pico_panel = 400
        numero_paneles = self.calculo_paneles()


    def calculo_paneles(self):
        paneles = self.energia_total / ( self.p_pico_panel * self.rad_media_min * 0.9)
        return print(paneles)


SetPaneles(3534, 2)
