class Triangle:
    def __init__(self, nombre, symbol='*'):
        self.nombre = nombre
        self.symbol = symbol

    def lignes(self):
        lignes = []
        for i in range(self.nombre):
            espaces = " " * (self.nombre - 1)
            nbetoiles = self.symbol * (i + 1)
            lignes.append(espaces + nbetoiles)
        return lignes


class Affichage:
    def __init__(self, triangle):
        self.triangle = triangle

    def afficher(self):
        lignes = self.triangle.lignes()
        for ligne in lignes:
            print(ligne + " " + ligne.strip())


n = int(input("Saisissez un nombre entier : "))

triangle = Triangle(n)
affichage = Affichage(triangle)
affichage.afficher()