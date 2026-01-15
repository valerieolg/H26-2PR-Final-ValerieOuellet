import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFrame, QLineEdit, QLabel

liste = []
def charger():
    f = open("resultats.txt", "r")
    for l in liste:
        l.setText(f.readline())
    f.close()
def sauver():
    f = open("resultats.txt", "w")
    for l in liste:
        f.write(l.text()+"\n")
    f.close()

def window():
    app = QApplication(sys.argv)
    win = QWidget()


if __name__ == '__main__':
    window()