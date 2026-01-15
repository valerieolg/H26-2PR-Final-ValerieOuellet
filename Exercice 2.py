# Importer les modules nécessaires :
# - os pour récupérer le nom de l'utilisateur
# - sys pour le fonctionnement d'une application (ouvrir et ffermer l'app)
# - PyQt6 Qwidgets pour créer l'interface de l'application (le GUi). Je les importe tous mais ceux utilisés seront QApplication, QLabel, QWidget

import os
import sys
from PyQt6.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setGeometry(50, 50, 350, 200)
    win.setWindowTitle("Comment doubler un nombre sans utiliser sa tête")

    frame = QFrame(win)
    frame.setGeometry(10, 10, 300, 200)

    grid = QGridLayout()
    frame.setLayout(grid)

    ######################################################################
    # Je crée mes Labels et mes lineEdits
    ######################################################################
    qlabel1 = QLabel(win)
    qlabel1.setText("Entrer la valeur de N :")
    grid.addWidget(qlabel1,0,0)

    qLine1 = QLineEdit(win)
    qLine1.setGeometry(50, 100, 200, 50)
    grid.addWidget(qLine1, 0, 1)
    liste.append(qLine1)

    qlabel2 = QLabel(win)
    qlabel2.setText("Voici le double :")
    grid.addWidget(qlabel2,1,0)

    qLine2 = QLineEdit(win)
    qLine2.setGeometry(50, 100, 200, 50)
    grid.addWidget(qLine2, 1, 1)
    liste.append(qLine1)

    ######################################################

    b1 = grid.addWidget(QPushButton("Valider l'opération", frame))
    b2 = grid.addWidget(QPushButton("Sauvegarder", frame))
    b3 = grid.addWidget(QPushButton("Charger", frame))

    win.show()
    sys.exit(app.exec())

    ######################################################
    # Création des boutons
    ######################################################

def b1_clicked():
    print(n * 2)


def b2_clicked():
    print("Sauvegarde réussie!")

def b3_clicked():
    print("Résultat chargé!")


###########################################
liste = []
def charger():
    user = os.getlogin()
    f = open("C:users/" + user + "/resultats.txt", "r")
    f.readline()
    f.close()
def sauvegarder():
    f = open("resultats.txt", "w")
    for l in liste:
        f.write(l.text()+"\n")
    f.close()



if __name__ == '__main__':
    window()