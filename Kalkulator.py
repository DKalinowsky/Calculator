from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import sys
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):

        #nazwa aplikacji
        self.setWindowTitle("Kalkulator")

        #dodanie etykiet do programu
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik:", self)
        etykieta4 = QLabel("Liczba 1:", self)
        etykieta5 = QLabel("Liczba 2:", self)

        #dodanie pól do etykiet, w które user będzie wpisywał liczby, pola edycji
        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        jedenbt = QPushButton("1", self)
        dwabt = QPushButton("2", self)
        trzybt = QPushButton("3", self)
        czterybt = QPushButton("4", self)
        piecbt = QPushButton("5", self)
        szescbt = QPushButton("6", self)
        siedembt = QPushButton("7", self)
        osiembt = QPushButton("8", self)
        dziewiecbt = QPushButton("9", self)
        zerobt = QPushButton("0", self)

        djedenbt = QPushButton("1", self)
        ddwabt = QPushButton("2", self)
        dtrzybt = QPushButton("3", self)
        dczterybt = QPushButton("4", self)
        dpiecbt = QPushButton("5", self)
        dszescbt = QPushButton("6", self)
        dsiedembt = QPushButton("7", self)
        dosiembt = QPushButton("8", self)
        ddziewiecbt = QPushButton("9", self)
        dzerobt = QPushButton("0", self)

        ukladW = QHBoxLayout()
        ukladW.addWidget(jedenbt)
        ukladW.addWidget(dwabt)
        ukladW.addWidget(trzybt)
        ukladW.addWidget(czterybt)
        ukladW.addWidget(piecbt)
        ukladW.addWidget(szescbt)
        ukladW.addWidget(siedembt)
        ukladW.addWidget(osiembt)
        ukladW.addWidget(dziewiecbt)
        ukladW.addWidget(zerobt)

        ukladV = QHBoxLayout()
        ukladV.addWidget(djedenbt)
        ukladV.addWidget(ddwabt)
        ukladV.addWidget(dtrzybt)
        ukladV.addWidget(dczterybt)
        ukladV.addWidget(dpiecbt)
        ukladV.addWidget(dszescbt)
        ukladV.addWidget(dsiedembt)
        ukladV.addWidget(dosiembt)
        ukladV.addWidget(ddziewiecbt)
        ukladV.addWidget(dzerobt)

        #rozmieszczenie etykiet w aplikacji(dodajemy kolejne widgety wraz z numerem wiersza i kolumny)
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)
        ukladT.addWidget(etykieta4, 3, 0)
        ukladT.addWidget(etykieta5, 4, 0)

        #rozmieszczenie w aplikacji pól edycji
        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        #dodanie przycisków
        dodajBtn = QPushButton("Dodaj", self)
        odejmijBtn = QPushButton("Odejmij", self)
        podzielBtn = QPushButton("Pomnóż", self)
        pomnozBtn = QPushButton("Podziel", self)

        #przypisanie działań do przycisków
        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(podzielBtn)
        ukladH.addWidget(pomnozBtn)

        #rozmieszczenie przycisków i przypisanych do nich działań w aplikacji
        ukladT.addLayout(ukladH, 2, 1, 1, 3)
        ukladT.addLayout(ukladW, 3, 1, 1, 3)
        ukladT.addLayout(ukladV, 4, 1, 1, 3)

        #połączenie guzików z działaniem
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        pomnozBtn.clicked.connect(self.dzialanie)
        podzielBtn.clicked.connect(self.dzialanie)

        #połaczenie guzików z działaniem v2
        jedenbt.clicked.connect(self.dzialanie1)
        dwabt.clicked.connect(self.dzialanie1)
        trzybt.clicked.connect(self.dzialanie1)
        czterybt.clicked.connect(self.dzialanie1)
        piecbt.clicked.connect(self.dzialanie1)
        szescbt.clicked.connect(self.dzialanie1)
        siedembt.clicked.connect(self.dzialanie1)
        osiembt.clicked.connect(self.dzialanie1)
        dziewiecbt.clicked.connect(self.dzialanie1)
        zerobt.clicked.connect(self.dzialanie1)

        djedenbt.clicked.connect(self.dzialanie2)
        ddwabt.clicked.connect(self.dzialanie2)
        dtrzybt.clicked.connect(self.dzialanie2)
        dczterybt.clicked.connect(self.dzialanie2)
        dpiecbt.clicked.connect(self.dzialanie2)
        dszescbt.clicked.connect(self.dzialanie2)
        dsiedembt.clicked.connect(self.dzialanie2)
        dosiembt.clicked.connect(self.dzialanie2)
        ddziewiecbt.clicked.connect(self.dzialanie2)
        dzerobt.clicked.connect(self.dzialanie2)

        #dodanie układu etykiet i widgetow do aplikacji
        self.setLayout(ukladT)

        #rozmiar aplikacji
        self.resize(500, 100)
        self.show()

        #dodanie działań

    def dzialanie1(self):
        wybor = self.sender()

        if wybor.text() == "1":
            self.liczba1Edt.setText(str(1))
        if wybor.text() == "2":
            self.liczba1Edt.setText(str(2))
        if wybor.text() == "3":
            self.liczba1Edt.setText(str(3))
        if wybor.text() == "4":
            self.liczba1Edt.setText(str(4))
        if wybor.text() == "5":
            self.liczba1Edt.setText(str(5))
        if wybor.text() == "6":
            self.liczba1Edt.setText(str(6))
        if wybor.text() == "7":
            self.liczba1Edt.setText(str(7))
        if wybor.text() == "8":
            self.liczba1Edt.setText(str(8))
        if wybor.text() == "9":
            self.liczba1Edt.setText(str(9))
        if wybor.text() == "0":
            self.liczba1Edt.setText(str(0))

    def dzialanie2(self):
        wybor = self.sender()

        if wybor.text() == "1":
            self.liczba2Edt.setText(str(1))
        if wybor.text() == "2":
            self.liczba2Edt.setText(str(2))
        if wybor.text() == "3":
            self.liczba2Edt.setText(str(3))
        if wybor.text() == "4":
            self.liczba2Edt.setText(str(4))
        if wybor.text() == "5":
            self.liczba2Edt.setText(str(5))
        if wybor.text() == "6":
            self.liczba2Edt.setText(str(6))
        if wybor.text() == "7":
            self.liczba2Edt.setText(str(7))
        if wybor.text() == "8":
            self.liczba2Edt.setText(str(8))
        if wybor.text() == "9":
            self.liczba2Edt.setText(str(9))
        if wybor.text() == "0":
            self.liczba2Edt.setText(str(0))

    def dzialanie(self):
        wybor = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""
            if wybor.text() == "Dodaj":
                wynik = liczba1 + liczba2
                self.wynikEdt.setText(str(wynik))
            if wybor.text() == "Odejmij":
                wynik = liczba1 - liczba2
                self.wynikEdt.setText(str(wynik))
            if wybor.text() == "Pomnóż":
                wynik = liczba1 * liczba2
                self.wynikEdt.setText(str(wynik))
            if wybor.text() == "Podziel":
                if liczba1 == 0:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Nie można dzielić przez 0")
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()

                if liczba2 == 0:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Nie można dzielić przez 0")
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()

                wynik = liczba1 / liczba2
                self.wynikEdt.setText(str(wynik))
        except:
            pass

app = QApplication(sys.argv)
ex = App()
app.exec_()
