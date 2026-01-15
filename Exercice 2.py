import sys

from PyQt6.QtWidgets import *

liste = []
def charger():
    f = open("resultats.txt", "r")
    for l in liste:
        l.setText(f.readline())
    f.close()
def sauvegarder():
    f = open("resultats.txt", "w")
    for l in liste:
        f.write(l.text()+"\n")
    f.close()

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(50, 50, 500, 400)
    win.setWindowTitle("Comment doubler un nombre sans utiliser sa tête")

    l1 = Qlabel("Entrer la valeur de N :")
    n = QLineEdit()

    l2 = QLabel("Voici le double de N :")
    double = QLineEdit()

    frame = QFrame(win)
    frame.setGeometry(10, 10, 300, 200)

    grid = QGridLayout()
    frame.setLayout(grid)

    grid.addWidget(QPushButton("Charger", frame))

    win.show()
    sys.exit(app.exec())

def b1_clicked():
    print(n * 2)


def b2_clicked():
    print("Sauvegarde réussie!")

def b3_clicked():
    print("Résultat chargé!")


if __name__ == '__main__':
    window()