class Cansat:
    def __init__(self, pais, equipo):
        if isinstance(pais, str) and isinstance(equipo,str):
            self.pais = pais
            self.equipo = equipo
        else:
            raise ValueError("Pais y equipo tienen que ser Strings!")
        
    def datos(self):
        print(f"Este cansat es de: {self.pais}\ny del equipo: {self.equipo}")
        
    def camara(self):
        imagen=input("¿Que ves?: ")
        print(f"El cansat esta viendo: {imagen}")
