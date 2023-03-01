from ui.all_import_gui import *
from ui.windows.home import Page_home
from ui.windows.cash import cash_page


class Pages(QStackedWidget):
    def __init__(self):
        super(Pages, self).__init__()
        self.setStyleSheet("background-color: #13252c")

        # Criando a pagina principal.
        self.home_page = Page_home()
        
        # Criando o pagina do Caixa.
        self.cash_page = cash_page()

        # Adicionando a pagina a StackedWidget
        self.addWidget(self.home_page)
        self.addWidget(self.cash_page)
