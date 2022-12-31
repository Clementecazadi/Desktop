# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(600, 700)
        MainWindow2.setMinimumSize(QtCore.QSize(600, 700))
        MainWindow2.setMaximumSize(QtCore.QSize(600, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icon3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow2.setWindowIcon(icon)
        MainWindow2.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.516773, y1:0.21, x2:0.504773, y2:1, stop:0 rgba(69, 84, 79, 255), stop:0.982955 rgba(20, 237, 190, 255))")
        centralwidget = QtWidgets.QWidget(MainWindow2)
        centralwidget.setObjectName("centralwidget")
        centralwidget.setMinimumSize(QtCore.QSize(600, 700))
        centralwidget.setMaximumSize(QtCore.QSize(600, 700))
        self.verticalLayout = QtWidgets.QVBoxLayout(centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main2 = QtWidgets.QFrame(centralwidget)
        self.frame_main2.setStyleSheet("background-color: rgb(69, 84, 79, 189);\n"
"border-radius: 60px")
        self.frame_main2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main2.setObjectName("frame_main2")
        self.frame_logo = QtWidgets.QFrame(self.frame_main2)
        self.frame_logo.setGeometry(QtCore.QRect(210, 20, 171, 161))
        self.frame_logo.setStyleSheet("QFrame{\n"
"background-image: url(:/image/canc.png);\n"
"background-repeat: None;\n"
"background-position: center;\n"
"border-radius:1px;\n"
"background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"QFrame:hover{\n"
"background-image: url(:/image/ox2.png);\n"
"}")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.label_texto = QtWidgets.QLabel(self.frame_main2)
        self.label_texto.setGeometry(QtCore.QRect(0, 190, 581, 471))
        self.label_texto.setStyleSheet("padding: 10px;\n"
"background-color: rgb(255, 255, 255, 0);")
        self.label_texto.setObjectName("label_texto")
        self.label_texto.setOpenExternalLinks(True)
        self.verticalLayout.addWidget(self.frame_main2)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "About"))
        self.label_texto.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#fc9202;\">Licença</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Este é um software livre e open-souce, você não precisa pagar </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">nada para o obter.</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Você tem permissão para:</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">- Res-distribuir este software</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">- Estudar e modificar o seu </span><a href=\"https://github.com/Clemente-CANC/Jogo_da_velha.git\"><span style=\" font-size:12pt; text-decoration: underline; color:#fc9202;\">código-fonte</span></a><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\"> dando </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">créditos a CANC ou CANC-Design.</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#fc9202;\">Sobre a CANC</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Olá, meu nome é Clemente Alberto N. Cazadi, a CANC é uma </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">startup Angolana criada por mim que é especializada</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">na criação de software de gestão para escola, </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">salão de beleza, restaurante, lojas ...</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#e7e7e7;\">Para mais informações visite a nossa pagina Facebook:</span></p><p align=\"center\"><a href=\"https://www.facebook.com/CANC-design-103879817903979/\"><span style=\" font-size:14pt; text-decoration: underline; color:#fc9202;\">https://www.facebook.com/CANC-design</span></a></p><p align=\"center\"><br/></p></body></html>"))
import rec


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QWidget()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
