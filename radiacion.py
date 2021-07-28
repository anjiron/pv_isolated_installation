
import pandas

class GetRadiacion():
    def __init__(self):
        self.latitud = 38.27
        self.longitud = -3.05

    def obtener_radiacion_min(self):

        url = 'http://www.adrase.com/adrasemaps/php/monthly_popup.php?lat=' + str(self.latitud) + '&lon=' + str(self.longitud) + '&var_tipe=0'
        
        try:
            df_tabla_resultados = pandas.read_html(url)  
        except: print("EL VALOR DE LATITUD O LONGITUD INTRODUCIDO ESTÁ FUERA DE RANGO\n VALORES VÁLIDOS: ESPAÑA\n")

        print(df_tabla_resultados[0])
        valores_minimos = df_tabla_resultados[0].min(numeric_only=True, axis=1)
        rad_media_min = valores_minimos.iloc[2]
        
        return rad_media_min


# print(GetRadiacion().obtener_radiacion_min())