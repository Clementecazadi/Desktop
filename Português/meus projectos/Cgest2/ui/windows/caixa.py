from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidget, QListWidgetItem, QScrollBar, QStackedWidget, QTreeWidget, QTreeWidgetItem,\
    QHeaderView
from PySide6.QtCore import Qt
from ui.custome.button import Button_custome_2
from ui.custome.Label import get_font, AdvencedLabel

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
        self.right_widget.setStyleSheet('background-color: #0c0c0c')
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

        self.product_list = QTreeWidget()
        self.header = QHeaderView(Qt.Horizontal)
        self.header.setFont(get_font('JosefinSans-SemiBold.ttf', 18))
        #self.header.setSectionsMovable(False)
        self.header.setSectionResizeMode(QHeaderView.Stretch)
        self.product_list.setHeader(self.header)
        self.product_list.setHeaderLabels(['Codigo', 'Nome do Prod.', 'Quantia', 'Preço'])
        self.product_list.setStyleSheet(""
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: #9955ff;\n"
            "    min-height: 25px;\n"
            "	border-radius: 7px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 7px;\n"
            "    border-bottom-right-radius: 7px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63"
                                    ", 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 7px;\n"
            "    border-top-right-radius: 7px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
        "QTreeWidget {	\n"
        "   color: #ffffff;"
        "   text-align: center;"
        "	background-color: #0c0c0c;\n"
        "	border-radius: 5px;\n"
        "}\n"
        "QTreeWidget::item{\n"
        "   height:35px;"
        "	padding-left: 5px;\n"
        #"	padding-right: 5px;\n"
        "}\n"
        "QTreeWidget::item:selected{\n"
        "	background-color: #9955ff;}\n"
        "QHeaderView::section{\n"
        "	Background-color: #35c2a6;\n"
        #"	width: 50px;\n"
        #"	border: 7px solid rgb(44, 49, 60);\n"
        "	border-style: none;\n"
        "}\n"
        ""
        "QTableWidget::horizontalHeader {	\n"
        "	background-color: rgb(81, 255, 0);\n"
        "}\n"
        "QHeaderView::section:horizontal\n"
        "{\n"
        "   border: 1px solid rgb(32, 34, 42);\n"
        "	background-color: #35c2a6;\n"
        "   width: 10px;\n"
        "   height: 30px;"
        "   color: #ffffff;"
        "	padding: 10px;\n"
        "}\n")
        self.product_list.setFont(get_font('JosefinSans-SemiBold.ttf', 14))
        listas = [['01911', 'Carne de porco', '2', '3600 Kzs'], 
        ['45432', 'Sandwiche de frango', '1', '2200 Kzs'], ['34213', 'Feigoado de borco', '2', '3450 Kzs']]
        for x in range(3):
            item = QTreeWidgetItem(self.product_list, listas[x])
            for x in range(4):
                item.setTextAlignment(x, Qt.AlignCenter)
                item.setToolTip(1, item.text(1))

        self.purchase_details_main_layout = QHBoxLayout()
        self.purchase_details_main_layout.setContentsMargins(0, 0, 0, 0)
        self.purchase_details_main_layout.setSpacing(0)

        self.purchase_details_layout_1 = QVBoxLayout()
        self.purchase_details_layout_1.setContentsMargins(0, 0, 0, 0)
        self.purchase_details_layout_1.setSpacing(10)
        self.dining_table_lable = AdvencedLabel('Mesa: 6', font_size=16)
        self.total_price_lable = AdvencedLabel('Preço total: 9250 Kzs', font_size=16)
        self.tax_lable = AdvencedLabel('Iva: 14%', font_size=16)
        self.purchase_details_layout_1.addWidget(self.dining_table_lable)
        self.purchase_details_layout_1.addWidget(self.total_price_lable)
        self.purchase_details_layout_1.addWidget(self.tax_lable)

        self.purchase_details_layout_2 = QVBoxLayout()
        self.purchase_details_layout_2.setContentsMargins(0, 0, 0, 0)
        self.purchase_details_layout_2.setSpacing(10)
        self.final_price = AdvencedLabel('Preço Final: 10345 Kzs', font_size=16)
        self.cliente_money_lable = AdvencedLabel('Dinheiro: 11000 Kzs', font_size=16)
        self.customer_change_lable = AdvencedLabel('Troco do cliente: 655 Kzs', font_size=16)
        self.purchase_details_layout_2.addWidget(self.final_price)
        self.purchase_details_layout_2.addWidget(self.cliente_money_lable)
        self.purchase_details_layout_2.addWidget(self.customer_change_lable)


        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_1)
        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_2)
        # Adicionado Elmenetos ao layout left_layout 
        self.left_layout.addLayout(self.left_button_layout)
        self.left_layout.addWidget(self.product_list)
        self.left_layout.addLayout(self.purchase_details_main_layout)