from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidget, QListWidgetItem, QScrollBar, QStackedWidget
from PySide6.QtCore import Qt
from ui.custome.button import Button_custome_2

class caixa_page(QWidget):
    def __init__(self):
        super(caixa_page, self).__init__()
        # Criando o layout principal.
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        # Criando o layout secundario.
        self.left_layout = QVBoxLayout()
        # Criando a parte direito do layout.
        self.right_widget = QStackedWidget()
        self.right_widget.setStyleSheet('background-color: #000000')
    
        # Adicionando o left_layout e right ao menu principal.
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addWidget(self.right_widget)

        # Criando elemento para left_layout.
        self.dining_table = Button_custome_2(icon_path='contas em espera.svg')
        # Criando um layout para botões.
        self.left_button_layout = QHBoxLayout()
        self.left_button_layout.addWidget(self.dining_table)

        self.left_layout.addLayout(self.left_button_layout)



        
        
        