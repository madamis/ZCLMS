import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, uic, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QDialog

UIClass, QtBaseClass = uic.loadUiType("developer/ZOMBA_CITY_dev.ui")

class MyApp(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('developer in details')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_pushButton_clicked_2)
        self.pushButton_6.clicked.connect(self.on_pushButton_clicked_6)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.textEdit.setText('______Detailed Information_____\n \n Name: Lawrence Reneck \n \n '
                              'Address:PO BOx 1050 Zomba \n \n Date Aplied : 12th April 2018 \n \n Date Approved: 24th'
                              'January 2019 \n \n Scrutiny Fee: K24000.00 \n \n Balance: K7000.00 ' +self.label_3.text())

    def on_pushButton_clicked_2(self):
        self.textEdit.setText('______Detailed Information_____\n \n Name: Oscar Nguluwe \n \n '
                              'Address:PO BOx 1050 Zomba \n \n Date Aplied : 12th April 2018 \n \n Date Approved: 24th'
                              'January 2019 \n \n Scrutiny Fee: K24000.00 \n \n Balance: K7000.00 ' + self.label_4.text())

    def on_pushButton_clicked_3(self):
        self.textEdit.setText('______Detailed Information_____\n \n Name: Davis Banda \n \n '
                              'Address:PO BOx 1050 Zomba \n \n Date Aplied : 12th April 2018 \n \n Date Approved: 24th'
                              'January 2019 \n \n Scrutiny Fee: K24000.00 \n \n Balance: K7000.00 ' + self.label_5.text())
    def on_pushButton_clicked_6(self):
        self.textEdit.setText('\n \n\n \n\n \n\n \n\n \n \n \n\n \n\n \n >>>The new developer has been added')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
