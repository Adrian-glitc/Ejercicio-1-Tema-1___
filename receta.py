class Receta:
    def __init__(self, texto_corrupto):
        self.texto_corrupto = texto_corrupto
        self.texto_invertido = ""
        self.nombre_receta = ""
        self.calorias = ""
        
    def procesar_texto(self):
            # Invertir la cadena
            self.texto_invertido = self.texto_corrupto[::-1]

            # Separar el texto en partes
            partes = self.texto_invertido.split(" ")

            # Extraer el nombre de la receta y las calorías
            self.nombre_receta = " ".join(partes[3:])  # Unir las palabras que forman el nombre de la receta
            self.calorias = partes[1]  # Obtener el número de calorías
        
    def obtener_resultado(self):
            # Formatear el texto
        return f"La receta de {self.nombre_receta} contiene {self.calorias} calorías."