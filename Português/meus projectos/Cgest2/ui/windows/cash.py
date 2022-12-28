from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidget, QListWidgetItem, QScrollBar, QStackedWidget, QTreeWidget, QTreeWidgetItem,\
    QHeaderView, QGridLayout, QPushButton
from PySide6.QtCore import Qt
from ui.custome.button import Button_custome_2, Button_custome_3
from ui.custome.Label import get_font, AdvencedLabel

class caixa_page(QWidget):
    def __init__(self):
        super(caixa_page, self).__init__()
        # Criando o layout principal.
        self.main_layout = QHBoxLayout(self)
        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(15)
        # Criando o layouts secundarios.
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
        # Criando uma lisa de produtos para left_layout.
        self.product_list = QTreeWidget()
        self.header = QHeaderView(Qt.Horizontal)
        self.header.setFont(get_font('JosefinSans-SemiBold.ttf', 18))
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

        # Criando as lable para mostras detalhes da venda.
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

        # Adicionado os detalhes para o layout.
        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_1)
        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_2)
        # Adicionado Elmenetos ao layout left_layout 
        self.left_layout.addLayout(self.left_button_layout)
        self.left_layout.addWidget(self.product_list)
        self.left_layout.addLayout(self.purchase_details_main_layout)

        # Criando elementos para right_widget.

        # Janela para adicionar produtos e mesas.
        self.add_thinks = QWidget()

        # Criando um layout para add_thinks.
        self.add_things_layout = QVBoxLayout(self.add_thinks)
        self.add_things_layout.setContentsMargins(25, 10, 25, 15)
        self.add_things_layout.setSpacing(5)

        # Criando elementos para add_things
        self.add_title = AdvencedLabel("Adicionar produtos", path="berkshire.ttf", 
                                        font_size=24, color='#fedb04')
        self.add_title.setAlignment(Qt.AlignCenter) 
        # -------
        self.add_text_show = QLabel('!23')
        self.add_text_show.setAlignment(Qt.AlignRight)
        self.add_text_show.setFont(get_font('JosefinSans-SemiBold.ttf', 48))
        self.add_buttons_layout = QGridLayout()
        self.add_buttons_layout.setObjectName(u"gridLayout")
        self.add_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.add_buttons_layout.setSpacing(10)

        # Criando os botões para buttons_layout
        self.add_button_1 = Button_custome_3()
        self.add_button_2 = Button_custome_3('2')
        self.add_button_3 = Button_custome_3('3')
        self.add_button_4 = Button_custome_3('4')
        self.add_button_5 = Button_custome_3('5')
        self.add_button_6 = Button_custome_3('6')
        self.add_button_7 = Button_custome_3('7')
        self.add_button_8 = Button_custome_3('8')
        self.add_button_9 = Button_custome_3('9')
        self.add_button_0 = Button_custome_3('0')
        self.add_button_action = QPushButton()
        self.add_button_action.setText('Adiconar')
        self.add_button_action.setFont(get_font('JosefinSans-SemiBold.ttf', 26))
        self.add_button_action.setMinimumHeight(90)
        self.add_button_action.setStyleSheet("""
                QPushButton{
                    color: #ffffff;
                    background-color: qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.5, y2:1, 
                    stop:0 rgba(153, 85, 255, 255), stop:1 rgba(34, 0, 85, 255));
                    border-radius: 5px;
                    border: none;
                }
                QPushButton:hover{
                    background-color: qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.5, y2:1, 
                    stop:0 rgba(169, 113, 255, 255), stop:1 rgba(58, 0, 144, 255));
                }
                QPushButton:pressed{
                    background-color: qlineargradient(spread:pad, x1:0.496, y1:0.00568182, x2:0.524, y2:1, 
                    stop:0 rgba(254, 229, 70, 255), stop:1 rgba(140, 123, 3, 255));
                }
        """)


        self.add_buttons_layout.addWidget(self.add_button_1, 0, 0, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_2, 0, 1, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_3, 0, 2, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_4, 1, 0, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_5, 1, 1, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_6, 1, 2, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_7, 2, 0, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_8, 2, 1, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_9, 2, 2, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_0, 3, 0, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_action, 3, 1, 1, 2)

        
        self.add_things_layout.addWidget(self.add_title)
        self.add_things_layout.addWidget(self.add_text_show)
        self.add_things_layout.addLayout(self.add_buttons_layout)

        self.right_widget.addWidget(self.add_thinks)
        