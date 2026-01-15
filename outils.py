class Outils:
    def __init__(self):
        self.liste_nombres = []

    def saisir(self):
        print("Saisissez 10 nombres entiers :")
        i = 1
        while i <= 10:
            try:
                n = int(input(f"{i}/10 : ").strip())
            except ValueError:
                print("Entrez un nombre entier.")
            self.liste_nombres.append(n)
            i += 1

    def min(self):
        nombre_min = min(self.liste_nombres)
        print(f"La valeur min est : {nombre_min}")

    def max(self):
        nombre_max = min(self.liste_nombres)
        print(f"La valeur max est : {nombre_max}")

    def somme(self):
        somme = sum(self.liste_nombres)
        print(f"La somme des nombres est : {somme}")

    def moyenne(self):
        moyenne = sum(self.liste_nombres) / len(self.liste_nombres)
        print(f"La moyenne des nombres est : {moyenne}")

if __name__ == "__main__":
    outil = Outils()
    outil.saisir()
    outil.min()
    outil.max()
    outil.somme()
    outil.moyenne()