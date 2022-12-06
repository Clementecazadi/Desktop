from PySide6.QtWidgets import QWidget, QStackedWidget, QFrame, QVBoxLayout, QSizePolicy
from PySide6.QtCore import Qt
from ui.windows.home import Page_home
from ui.windows.caixa import caixa_page


class Pages(QStackedWidget):
    def __init__(self):
        super(Pages, self).__init__()
        self.setStyleSheet("background-color: #13252c")

        # Criando a pagina principal.
        self.home_page = Page_home()
        
        # Criando o pagina do Caixa.
        self.caixa_page = caixa_page()

        # Adicionando a pagina a StackedWidget
        self.addWidget(self.home_page)
        self.addWidget(self.caixa_page)
