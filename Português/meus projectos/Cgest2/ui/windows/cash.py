from ui.all_import_gui import *
from ui.custome.button import Button_custome_2, Button_custome_3
from ui.custome.Label import get_font, AdvencedLabel

class cash_page(QWidget):
    def __init__(self):
        super(cash_page, self).__init__()
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
        self.product = Button_custome_2(icon_path='product.svg')
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
        #self.purchase_details_main_layout.
        self.purchase_details_layout_1 = QVBoxLayout()
        self.purchase_details_layout_1.setContentsMargins(0, 0, 0, 0)
        self.purchase_details_layout_1.setSpacing(10)
        self.service_id = AdvencedLabel('ID do servico: 0125', font_size=16)
        self.dining_table_lable = AdvencedLabel('Mesa: 6', font_size=16)
        self.final_price = AdvencedLabel('Preço Final: 10345 Kzs', font_size=16)

        self.purchase_details_layout_1.addWidget(self.service_id)
        self.purchase_details_layout_1.addWidget(self.dining_table_lable)
        self.purchase_details_layout_1.addWidget(self.final_price)
        #------
        self.purchase_details_layout_2 = QVBoxLayout()
        self.purchase_details_layout_2.setContentsMargins(0, 0, 0, 0)
        self.purchase_details_layout_2.setSpacing(10)
        
        self.cliente_money_lable = AdvencedLabel('Dinheiro: 11000 Kzs', font_size=16)
        self.customer_change_lable = AdvencedLabel('Troco do cliente: 655 Kzs', font_size=16)
        self.customer_stat_lable = AdvencedLabel('', font_size=16)

        self.purchase_details_layout_2.addWidget(self.cliente_money_lable)
        self.purchase_details_layout_2.addWidget(self.customer_change_lable)
        self.purchase_details_layout_2.addWidget(self.customer_stat_lable)

        # Adicionado os detalhes para o layout.
        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_1)
        self.purchase_details_main_layout.addLayout(self.purchase_details_layout_2)
        # Adicionado Elmenetos ao layout left_layout 
        self.left_layout.addLayout(self.left_button_layout)
        self.left_layout.addWidget(self.product_list)
        self.left_layout.addLayout(self.purchase_details_main_layout)

        # Criando paginas para right_widget.

        # Pagina zero quando nehuma opção for selecionada.
        self.informative_page = QWidget()
        self.informative_page.setStyleSheet('background: #6c3cb4;')
        # Adicionando uma imagem com QPixmap.
        self.cash_image = QPixmap(path_local('cozinhera.png'))
        self.cash_image = self.cash_image.scaled(330, 450, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.cash_image_label = QLabel()
        self.cash_image_label.setPixmap(self.cash_image)

        self.informative_label = AdvencedLabel("Escolha uma opção", path="berkshire.ttf", 
                                            font_size=28)
        self.informative_label.setAlignment(Qt.AlignCenter)
        self.informative_spacer1 = QSpacerItem(5, 5, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.informative_spacer2 = QSpacerItem(5, 5, QSizePolicy.Fixed, QSizePolicy.Expanding)


        self.informative_page_layout = QVBoxLayout(self.informative_page)
        self.informative_page_layout.setSpacing(15)
        self.informative_page_layout.addItem(self.informative_spacer1)
        self.informative_page_layout.addWidget(self.cash_image_label)
        self.informative_page_layout.addWidget(self.informative_label)
        self.informative_page_layout.addItem(self.informative_spacer2)


        # Pagina para adicionar coisas (produtos e mesas).
        self.add_things = QWidget()
        # Criando um layout para add_thinks.
        self.add_things_layout = QVBoxLayout(self.add_things)
        self.add_things_layout.setContentsMargins(25, 15, 25, 15)
        self.add_things_layout.setSpacing(20)
        # Criando elementos para add_things
        self.add_title = AdvencedLabel("Adicionar produtos", path="berkshire.ttf", 
                                        font_size=28, color='#fee546')
        self.add_title.setAlignment(Qt.AlignCenter) 
        # -------
        self.add_text_show = QLabel('56330')
        self.add_text_show.setAlignment(Qt.AlignRight)
        self.add_text_show.setFont(get_font('JosefinSans-SemiBold.ttf', 40))
        self.add_text_show.setStyleSheet("""
                color: #89b489;
                border-bottom: 4px solid #fee546;
        """)
        self.add_buttons_layout = QGridLayout()
        self.add_buttons_layout.setObjectName(u"gridLayout")
        self.add_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.add_buttons_layout.setSpacing(10)
        # Criando os botões para buttons_layout
        self.add_button_1 = Button_custome_3('1', shortcut='1')
        self.add_button_2 = Button_custome_3('2', shortcut='2')
        self.add_button_3 = Button_custome_3('3', shortcut='3')
        self.add_button_4 = Button_custome_3('4', shortcut='4')
        self.add_button_5 = Button_custome_3('5', shortcut='5')
        self.add_button_6 = Button_custome_3('6', shortcut='6')
        self.add_button_7 = Button_custome_3('7', shortcut='7')
        self.add_button_8 = Button_custome_3('8', shortcut='8')
        self.add_button_9 = Button_custome_3('9', shortcut='9')
        self.add_button_0 = Button_custome_3('0', shortcut='0')
        self.add_button_backspace = Button_custome_2(height= 90, width= 90, icon_path="backspace.svg",
            btn_color= 'qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.5, y2:1,' 
                        'stop:0 rgba(153, 85, 255, 255), stop:1 rgba(34, 0, 85, 255))',
            btn_hover='qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.5, y2:1,'
                        'stop:0 rgba(169, 113, 255, 255), stop:1 rgba(58, 0, 144, 255))',
            btn_pressed= 'qlineargradient(spread:pad, x1:0.496, y1:0.00568182, x2:0.524, y2:1,'
                        'stop:0 rgba(254, 229, 70, 255), stop:1 rgba(140, 123, 3, 255));')
        self.add_button_backspace.setShortcut('backspace')
        self.add_button_enter = Button_custome_2(height= 90, width= 90, icon_path="enter.svg",
            btn_color= 'qlineargradient(spread:pad, x1:0.505, y1:0, x2:0.5, y2:1,' 
                        'stop:0 rgba(153, 85, 255, 255), stop:1 rgba(34, 0, 85, 255))',
            btn_hover='qlineargradient(spread:pad, x1:0.495, y1:0, x2:0.5, y2:1,'
                        'stop:0 rgba(169, 113, 255, 255), stop:1 rgba(58, 0, 144, 255))',
            btn_pressed= 'qlineargradient(spread:pad, x1:0.496, y1:0.00568182, x2:0.524, y2:1,'
                        'stop:0 rgba(254, 229, 70, 255), stop:1 rgba(140, 123, 3, 255));')
        self.add_button_enter.setShortcut('return')
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
        self.add_buttons_layout.addWidget(self.add_button_backspace, 3, 1, 1, 1)
        self.add_buttons_layout.addWidget(self.add_button_enter, 3, 2, 1, 1)
        # Criando um  item de spacer.
        self.add_spacer = QSpacerItem(5, 1, QSizePolicy.Fixed, QSizePolicy.Expanding)
        # Adicionando elementos ao layout add_things.
        self.add_things_layout.addWidget(self.add_title)
        self.add_things_layout.addWidget(self.add_text_show)
        self.add_things_layout.addLayout(self.add_buttons_layout)
        self.add_things_layout.addItem(self.add_spacer)


        # Criando outra pagina para right_widget, uma lista de espera.
        self.wait_list = QWidget()
        self.wait_qtree = QTreeWidget()
        self.header2 = QHeaderView(Qt.Horizontal)
        self.header2.setFont(get_font('JosefinSans-SemiBold.ttf', 18))
        self.header2.setSectionResizeMode(QHeaderView.Stretch)
        self.wait_qtree.setHeader(self.header2)
        self.wait_qtree.setStyleSheet(
            "QTreeWidget {	\n"
        "   color: #ffffff;"
        "   text-align: center;"
        "	background-color: #0c0c0c;\n"
        "	border-radius: 5px;\n"
        "}\n"
        "QTreeWidget::item{\n"
        "   height:35px;"
        "	padding-left: 5px;\n"
        "}\n"
        "QTreeWidget::item:selected{\n"
        "	background-color: #35c2a6;}\n"
        "QTableWidget::horizontalHeader {	\n"
        "	background-color: rgb(81, 255, 0);\n"
        "}\n"
        "QHeaderView::section:horizontal\n"
        "{\n"
        "   border: 1px solid rgb(32, 34, 42);\n"
        "	background-color: #9955ff;\n"
        "   width: 10px;\n"
        "   height: 30px;"
        "   color: #ffffff;"
        "	padding: 10px;\n"
        "}")
        self.wait_qtree.setHeaderLabels(('ID', 'Data'))
        self.wait_qtree.setFont(get_font('JosefinSans-SemiBold.ttf', 14))
        listas = [['00011', '12:50:45'], 
        ['- 00012 -', '13:00:20'], ['00013', '13:30:50']]
        for x in range(3):
            item = QTreeWidgetItem(self.wait_qtree, listas[x])
            for x in range(4):
                item.setTextAlignment(x, Qt.AlignCenter)

        self.wait_button_recharge = Button_custome_2(icon_path='recharge.svg')
        self.wait_button_delete = Button_custome_2(icon_path='cancel.svg')
        # Criando um layout para mostrar botões.
        self.wait_buttons_layout = QHBoxLayout()
        self.wait_buttons_layout.setContentsMargins(10, 10, 10, 15)
        # Adicionando botões para o layout.
        self.wait_buttons_layout.addWidget(self.wait_button_recharge)
        self.wait_buttons_layout.addWidget(self.wait_button_delete)  
        # Criando um layout para wait_list.
        self.wait_list_layout = QVBoxLayout(self.wait_list)
        # Adicionando elementos para wait_list_layout.
        self.wait_list_layout.addWidget(self.wait_qtree)
        self.wait_list_layout.addLayout(self.wait_buttons_layout)

        # Criando outra pagina para right_widget, uma pagina para faturar a compra.
        self.facture_page = QWidget()
        # Criando elementos para pagina de faturação.
        self.facture_title = AdvencedLabel("Faturar a compra", path="berkshire.ttf", 
                                            font_size=28, color='#fee546')
        self.facture_title.setAlignment(Qt.AlignCenter)
        self.fact_details_label = AdvencedLabel("Detalhes da Compra", font_size=18)
        self.fact_details_label.setAlignment(Qt.AlignCenter)
        self.fact_final_price = AdvencedLabel("Preço final: 10345 Kzs", font_size=14)
        # Criando um layout para detalhes da compra.
        self.fact_details_layout = QVBoxLayout()
        self.fact_details_layout.addWidget(self.fact_details_label)
        self.fact_details_layout.addWidget(self.fact_final_price)

        self.fact_pay_methods_label = AdvencedLabel('Métodos de Pagamentos', font_size=18)
        self.fact_pay_methods_label.setAlignment(Qt.AlignCenter)
        self.fact_pay_methods_button1 = Button_custome_2(icon_path='money.svg')
        self.fact_pay_methods_button2 = Button_custome_2(icon_path= 'credit card.svg')
        # Criando um layout para botões de pagamentos.
        self.fact_pay_buttons_layout = QHBoxLayout()
        self.fact_pay_buttons_layout.addWidget(self.fact_pay_methods_button1)
        self.fact_pay_buttons_layout.addWidget(self.fact_pay_methods_button2)
        # Criando um layout para métodos de pagamentos.
        self.fact_pay_methods_layout = QVBoxLayout()
        self.fact_pay_methods_layout.addWidget(self.fact_pay_methods_label)
        self.fact_pay_methods_layout.addLayout(self.fact_pay_buttons_layout)
        
        self.finish_facture = Button_custome_3('Finalizar', 60, 250, shortcut='return', font_size=28)
        self.finish_facture_layoout = QHBoxLayout()
        self.finish_facture_layoout.addWidget(self.finish_facture)
        self.fact_spacer = QSpacerItem(5, 5, QSizePolicy.Fixed, QSizePolicy.Expanding)

        # Criando e adicionando elementos para facture_layout.
        self.facture_layout = QVBoxLayout(self.facture_page)
        self.facture_layout.setContentsMargins(15, 15, 15, 15)
        self.facture_layout.setSpacing(35)
        self.facture_layout.addWidget(self.facture_title)
        self.facture_layout.addLayout(self.fact_details_layout)
        self.facture_layout.addLayout(self.fact_pay_methods_layout)
        self.facture_layout.addItem(self.fact_spacer)
        self.facture_layout.addLayout(self.finish_facture_layoout)

        # Adicionado elementos a QStrackeWidget right_widget.
        self.right_widget.addWidget(self.informative_page)
        self.right_widget.addWidget(self.add_things)
        self.right_widget.addWidget(self.wait_list)
        self.right_widget.addWidget(self.facture_page)

        self.cancel_bill.clicked.connect(lambda:self.mode(0))
        self.finish_facture.clicked.connect(lambda:self.mode(0))
        self.dining_table.clicked.connect(lambda:self.mode(1))
        self.product.clicked.connect(lambda:self.mode(2))
        self.product_number.clicked.connect(lambda:self.mode(3))
        self.bill_wait_list.clicked.connect(lambda:self.mode(4))
        self.facture.clicked.connect(lambda:self.mode(5))
        self.fact_pay_methods_button1.clicked.connect(lambda:self.pay_methods_func(1))
        self.fact_pay_methods_button2.clicked.connect(lambda:self.pay_methods_func(2))
        
        
        
    # Criando funções personalizadas
        
    def mode(self, button_id:int = 0):
        # Recetando todos os botões.
        self.dining_table.set_active(False)
        self.product.set_active(False)
        self.product_number.set_active(False)
        self.delete_product.set_active(False)
        self.bill_wait.set_active(False)
        self.bill_wait_list.set_active(False)
        self.facture.set_active(False)
        
        if button_id == 0:
            self.right_widget.setCurrentIndex(0)
            self.fact_pay_methods_button1.set_active(False)
            self.fact_pay_methods_button2.set_active(False)

        elif button_id == 1:
            self.dining_table.set_active(True)
            self.right_widget.setCurrentIndex(1)
            self.add_title.setText('Indique a mesa')

        elif button_id == 2:
            self.product.set_active(True)
            self.right_widget.setCurrentIndex(1)
            self.add_title.setText('Adicione produtos')

        elif button_id == 3:
            self.product_number.set_active(True)
            self.right_widget.setCurrentIndex(1)
            self.add_title.setText('Indique a quantia')

        elif button_id == 4:
            self.bill_wait_list.set_active(True)
            self.right_widget.setCurrentIndex(2)
            
        elif button_id == 5:
            self.facture.set_active(True)
            self.right_widget.setCurrentIndex(3)

    def pay_methods_func(self, button_id):
        self.fact_pay_methods_button1.set_active(False)
        self.fact_pay_methods_button2.set_active(False)


        if button_id == 1:
            self.fact_pay_methods_button1.set_active(True)
            self.right_widget.setCurrentIndex(1)
            self.add_title.setText('Dinhero do cliente')

        elif button_id == 2:
            self.fact_pay_methods_button2.set_active(True)

