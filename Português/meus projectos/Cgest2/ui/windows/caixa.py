from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidget, QListWidgetItem, QScrollBar, QStackedWidget, QTreeWidget, QTreeWidgetItem,\
    QHeaderView
from PySide6.QtCore import Qt
from ui.custome.button import Button_custome_2

class caixa_page(QWidget):
    def __init__(self):
        super(caixa_page, self).__init__()
        # Criando o layout principal.
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
        # Criando o layout secundario.
        self.left_layout = QVBoxLayout()
        # Criando a parte direito do layout para adicionar produtos e quantias.
        self.right_widget = QStackedWidget()
        self.right_widget.setStyleSheet('background-color: #000000')
        self.right_widget.setMaximumWidth(350)
    
        # Adicionando o left_layout e right ao menu principal.
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addWidget(self.right_widget)

        # Criando elemento para left_layout.
        self.dining_table = Button_custome_2(icon_path='dining_table2.svg')
        self.product = Button_custome_2(icon_path='product.svg', is_active=True)
        self.product_number = Button_custome_2(icon_path='product number.svg')
        self.delete_product = Button_custome_2(icon_path='delete product.svg')
        self.bill_wait = Button_custome_2(icon_path='bill_waiting.svg')
        self.bill_wait_list = Button_custome_2(icon_path='list_bill.svg')
        self.facture = Button_custome_2(icon_path='facture.svg')
        self.cancel_bill = Button_custome_2(icon_path='cancel.svg', icon_color='#ff8080')
        self.product_list = QTreeWidget()
        self.header = QHeaderView(Qt.Horizontal)
        self.header.setDefaultSectionSize(200)
        self.header.sectionR
        self.header.setSectionsMovable(False)
        self.product_list.setHeader(self.header)
        self.product_list.setHeaderLabels(['Codigo', 'Nome do Prod.', 'Quantia', 'Preço'])
        self.product_list.setStyleSheet(""
        "QTreeWidget {	\n"
        "	background-color: #0c0c0c;\n"
        "	border-radius: 5px;\n"
        "}\n"
        "QTableWidget::item{\n"
        "	border-color: rgb(44, 49, 60);\n"
        "	padding-left: 5px;\n"
        "	padding-right: 5px;\n"
        "	gridline-color: rgb(44, 49, 60);\n"
        "}\n"
        "QTableWidget::item:selected{\n"
        "	background-color: rgb(85, 170, 255);}\n"
        "QHeaderView::section{\n"
        "	Background-color: #35c2a6;\n"
        "	width: 50px;\n"
        "	border: 1px solid rgb(44, 49, 60);\n"
        "	border-style: none;\n"
        "    border-bottom: 1px solid rgb(44, 49, 60);\n"
        "    border-right: 1px solid rgb(44, 49, 60);\n"
        "}\n"
        ""
        "QTableWidget::horizontalHeader {	\n"
        "	background-color: rgb(81, 255, 0);\n"
        "}\n"
        "QHeaderView::section:horizontal\n"
        "{\n"
        "    border: 1px solid rgb(32, 34, 42);\n"
        "	background-color: #35c2a6;\n"
        "   width: 10px;\n"
        "   height: 30px;"
        "   color: #ffffff;"
        "	padding: 10px;\n"
        "}\n"
        "QHeaderView::section:vertical\n"
        "{\n"
        "    border: 1px solid rgb(44, 49, 60);\n"
        "}\n")

        # Criando um layout para botões.
        self.left_button_layout = QHBoxLayout()
        self.left_button_layout.setContentsMargins(0, 0, 0, 0)
        self.left_button_layout.setSpacing(10)

        # Adicionando os botões para o layout
        self.left_button_layout.addWidget(self.dining_table)
        self.left_button_layout.addWidget(self.product)
        self.left_button_layout.addWidget(self.product_number)
        self.left_button_layout.addWidget(self.delete_product)
        self.left_button_layout.addWidget(self.bill_wait)
        self.left_button_layout.addWidget(self.bill_wait_list)
        self.left_button_layout.addWidget(self.facture)
        self.left_button_layout.addWidget(self.cancel_bill)
        


        


        
        self.left_layout.addLayout(self.left_button_layout)
        self.left_layout.addWidget(self.product_list)
        



        
        
        