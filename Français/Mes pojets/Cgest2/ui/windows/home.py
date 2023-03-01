from ui.all_import_gui import *
from PySide6.QtCore import Qt
from ui.custome.Label import AdvencedLabel, get_font


# Criando widgets para o bloco de pratos em alta.
class Block_dish_in_high(QFrame):
    def __init__(self, dish_name:str = 'Desconhecido', orders:int = 0, dish_price:int = 0, tax:int = 0):
        super(Block_dish_in_high, self).__init__()
        self.setStyleSheet('background-color: qlineargradient'
        '(spread:pad, x1:0.519, y1:0, x2:0.5, y2:0.835, stop:0 rgba(128, 71, 213, 255), stop:1 '
        'rgba(43, 19, 77, 255));')
        # Criando elementos do bloco.
        self.dish_name = QLabel(dish_name)
        self.dish_name.setStyleSheet('background-color: #00000000; color: #ffffff')
        font = get_font('JosefinSans-SemiBold.ttf', font_size=18)
        font.setItalic(True)
        self.dish_name.setFont(font)
        self.dish_name.setWordWrap(True)
        self.order = AdvencedLabel(f'Commands: {orders}', font_size=14)
        self.order.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.price_of_dish = AdvencedLabel(f'Prix: {dish_price} kzs', font_size=14)
        self.price_of_dish.setStyleSheet('background-color: #00000000; color: #ffffff')
        # Elementos da taxa de conversão.
        self.tax_label = AdvencedLabel('Tax:', font_size=14)
        self.tax_label.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.tax_progress = QProgressBar()
        self.tax_progress.setMaximum(100)
        self.tax_progress.setMinimum(0)
        self.tax_progress.setValue(tax)
        self.tax_progress.setTextVisible(False)
        self.tax_progress.setMaximumHeight(5)
        self.tax_progress.setStyleSheet('''
                QProgressBar::chunk {
                    background-color: #fedb04;
	                border-radius: 2px
                };
                border-radius: 2px;
        ''')
        self.tax_percent_label = AdvencedLabel(f'{tax}%', font_size= 14)
        self.tax_percent_label.setStyleSheet('background-color: #00000000; color: #ffffff')
        # Criando layout para os elementos TAX
        self.tax_layout = QHBoxLayout()
        self.tax_layout.setContentsMargins(0, 0, 0, 0)
        self.tax_layout.setSpacing(10)
        # Adicionando elementos TAX
        self.tax_layout.addWidget(self.tax_label)
        self.tax_layout.addWidget(self.tax_progress)
        self.tax_layout.addWidget(self.tax_percent_label)
        # Criando layout para todos elementos que não sejam o titulo do prato.
        self.elements = QVBoxLayout()
        self.elements.setContentsMargins(0, 0, 0, 0)
        self.elements.setSpacing(5)
        # Adicionando elementos no layout.
        self.elements.addWidget(self.order)
        self.elements.addWidget(self.price_of_dish)
        self.elements.addLayout(self.tax_layout)
        # Criando layout para o bloco inteiro
        self.block_layout = QVBoxLayout(self)
        
        if len(dish_name) > 30:
            self.block_layout.setSpacing(0)
            self.block_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.block_layout.setSpacing(10)
            self.block_layout.setContentsMargins(10, 20, 10, 10)
        # Adicionando elementos ao layout
        self.block_layout.addWidget(self.dish_name)
        self.block_layout.addLayout(self.elements)

        
class Block_dish_manager(QWidget):
    def __init__(self):
        super(Block_dish_manager, self).__init__()
        self.ui_layers = QListWidget()
        self.ui_layers.setViewMode(QListWidget.ListMode)
        self.ui_layers.setSpacing(5)
        self.ui_layers.setMovement(QListWidget.Static)
        self.ui_layers.setWordWrap(True)
        self.ui_layers.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.ui_layers.setStyleSheet(""
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(85, 170, 255);\n"
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
            " }\n")
        self.ui_layers.setSelectionMode(QListWidget.NoSelection)
        # Criando o layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.ui_layers)

    def add_new_layers(self):
        dados = (['Carne de pato assado com batatas fritas.', 89, 3500, 82], 
                 ['Feigoada de borco', 79, 3900, 75],
                 ['Sopa de futos do mar', 70, 2000, 66])
        for x in range(3):
            widget = Block_dish_in_high(dados[x][0], dados[x][1], dados[x][2], dados[x][3])
            item = QListWidgetItem()
            self.ui_layers.insertItem(self.ui_layers.count(), item)
            self.ui_layers.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())


# Criando o bloco pedidos activos        
class Block_order_active(QFrame):
    def __init__(self, dish_name:str = 'Desconhecido', table_num:int = 0, enter_order:str = '23'):
        super(Block_order_active, self).__init__()
        # Definindo a core de fundo do widget
        self.setStyleSheet('background-color: qlineargradient'
        '(spread:pad, x1:0.519, y1:0, x2:0.5, y2:0.835, stop:0 rgba(128, 71, 213, 255), stop:1 '
        'rgba(43, 19, 77, 255));')
        # Criando elementos do bloco.
        self.dish_name_order = QLabel(dish_name)
        self.dish_name_order.setStyleSheet('background-color: #00000000; color: #ffffff')
        font = get_font('JosefinSans-SemiBold.ttf', font_size=18)
        font.setItalic(True)
        self.dish_name_order.setFont(font)
        self.dish_name_order.setWordWrap(True)
        self.table = AdvencedLabel(f'Messa: {table_num}', font_size=14)
        self.table.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.enter_order = AdvencedLabel(f'Entrada: {enter_order}', font_size=14)
        self.enter_order.setStyleSheet('background-color: #00000000; color: #ffffff')
        
        # Criando layout para todos elementos que não sejam o titulo do prato.
        self.elements = QVBoxLayout()
        self.elements.setContentsMargins(0, 0, 0, 0)
        self.elements.setSpacing(5)
        # Adicionando elementos no layout.
        self.elements.addWidget(self.table)
        self.elements.addWidget(self.enter_order)
         # Criando layout para o bloco inteiro
        self.block_layout = QVBoxLayout(self)
        
        if len(dish_name) > 30:
            self.block_layout.setSpacing(0)
            self.block_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.block_layout.setSpacing(10)
            self.block_layout.setContentsMargins(10, 20, 10, 10)
        # Adicionando elementos ao layout
        self.block_layout.addWidget(self.dish_name_order)
        self.block_layout.addLayout(self.elements)

        
class Block_order_manager(QWidget):
    def __init__(self):
        super(Block_order_manager, self).__init__()
        self.ui_layers = QListWidget()
        self.ui_layers.setViewMode(QListWidget.ListMode)
        self.ui_layers.setSpacing(5)
        self.ui_layers.setMovement(QListWidget.Static)
        self.ui_layers.setWordWrap(True)
        self.ui_layers.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.ui_layers.setStyleSheet(""
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(85, 170, 255);\n"
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
            " }\n")
        self.ui_layers.setSelectionMode(QListWidget.NoSelection)
        # Criando o layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.ui_layers)

    def add_new_layers(self):
        dados = (['Feigoada de borco', 7,'12h: 45min: 23sec'],
                 ['Carne de pato assado com batatas fritas.', 9, '12h: 56min: 21sec'], 
                 ['Sopa de futos do mar', 2, '13h: 20min: 15sec'])
        for x in range(3):
            widget = Block_order_active(dados[x][0], dados[x][1], dados[x][2])
            item = QListWidgetItem()
            self.ui_layers.insertItem(self.ui_layers.count(), item)
            self.ui_layers.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())

# Criando o bloco stock em baixo.
class Block_low_stock(QFrame):
    def __init__(self, product_name:str = 'Desconhecido', stock:float = 0, weight_total:float = 0):
        super(Block_low_stock, self).__init__()
        self.setStyleSheet('background-color: qlineargradient'
        '(spread:pad, x1:0.519, y1:0, x2:0.5, y2:0.835, stop:0 rgba(128, 71, 213, 255), stop:1 '
        'rgba(43, 19, 77, 255));')
        # Criando elementos do bloco...
        self.product_name = QLabel(product_name)
        self.product_name.setAlignment(Qt.AlignHCenter)
        self.product_name.setStyleSheet('background-color: #00000000; color: #ffffff')
        font = get_font('berkshire.ttf', font_size=24)
        font.setItalic(True)
        self.product_name.setFont(font)
        self.product_name.setWordWrap(True)
        self.stock = AdvencedLabel(f'Peso total: {stock} de {weight_total}Kg', font_size=14)
        self.stock.setStyleSheet('background-color: #00000000; color: #ffffff')
        percent =int((stock * 100) / weight_total)
        self.percent_label_1 = AdvencedLabel('Percentagem:', font_size=14)
        self.percent_label_1.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.percent_progress = QProgressBar()
        self.percent_progress.setMaximum(100)
        self.percent_progress.setMinimum(0)
        self.percent_progress.setValue(percent)
        self.percent_progress.setTextVisible(False)
        self.percent_progress.setMaximumHeight(5)
        self.percent_progress.setStyleSheet('''
                QProgressBar::chunk {
                    background-color: #fedb04;
	                border-radius: 2px
                };
                border-radius: 2px;
        ''')
        self.percent_label_2 = AdvencedLabel(f'{percent}%', font_size= 14)
        self.percent_label_2.setStyleSheet('background-color: #00000000; color: #ffffff')

        # Criando layout para os elementos de percentagem
        self.percent_layout = QHBoxLayout()
        self.percent_layout.setContentsMargins(0, 0, 0, 0)
        self.percent_layout.setSpacing(10)
        # Adicionando elementos TAX
        self.percent_layout.addWidget(self.percent_label_1)
        self.percent_layout.addWidget(self.percent_progress)
        self.percent_layout.addWidget(self.percent_label_2)
        # Criando layout para todos elementos que não sejam o titulo do produto
        self.elements = QVBoxLayout()
        self.elements.setContentsMargins(0, 0, 0, 0)
        self.elements.setSpacing(5)
        # Adicionando elementos no layout.
        self.elements.addWidget(self.stock)
        self.elements.addLayout(self.percent_layout)
        # Criando layout para o bloco inteiro
        self.block_layout = QVBoxLayout(self)
        self.block_layout.setSpacing(10)
        self.block_layout.setContentsMargins(10, 10, 10, 10)
        # Trecho de codigo em suspenção
        """"
        if len(product_name) > 10:
            self.block_layout.setSpacing(10)
            self.block_layout.setContentsMargins(10, 10, 10, 10)
        else:
            self.block_layout.setSpacing(10)
            self.block_layout.setContentsMargins(10, 20, 10, 10)
        """
        # Adicionando elementos ao layout
        self.block_layout.addWidget(self.product_name)
        self.block_layout.addLayout(self.elements)


class Block_stock_manager(QWidget):
    def __init__(self):
        super(Block_stock_manager, self).__init__()
        self.ui_layers = QListWidget()
        self.ui_layers.setViewMode(QListWidget.ListMode)
        self.ui_layers.setSpacing(5)
        self.ui_layers.setMovement(QListWidget.Static)
        self.ui_layers.setWordWrap(True)
        self.ui_layers.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.ui_layers.setStyleSheet(""
            " QScrollBar:vertical {\n"
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 14px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(85, 170, 255);\n"
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
            " }\n")
        self.ui_layers.setSelectionMode(QListWidget.NoSelection)
        # Criando o layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.ui_layers)

    def add_new_layers(self):
        dados = (['Arroz', 6, 25],
                 ['Carne de pato', 2, 10], 
                 ['Batatas', 5.8, 24], ['Pimenta', 2, 4],
                 ['Alho', 1.2, 5], ['Cebola', 1, 5], )
        for x in range(6):
            widget = Block_low_stock(dados[x][0], dados[x][1], dados[x][2])
            item = QListWidgetItem()
            self.ui_layers.insertItem(self.ui_layers.count(), item)
            self.ui_layers.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())

class Page_home(QWidget):
    def __init__(self):
        super(Page_home, self).__init__()
        # Criando elementos para a home.
        self.home_page_name_restaurante = AdvencedLabel('Restaurante Baia Verde', 'berkshire.ttf', 50)
        self.home_page_name_restaurante.setAlignment(Qt.AlignHCenter)
        self.home_page_name_restaurante.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.main_frame = QFrame()
        # Criando bloco onde serão mostradas os pratos em em alta dentro mainframe.
        self.pratos_em_alta_frame = QFrame()
        self.pratos_em_alta_frame.setStyleSheet('''background-color: #080808;
        border-radius: 10px
        ''')
        self.pratos_em_alta_title = AdvencedLabel('Pratos em alta', 'berkshire.ttf', 35)
        self.pratos_em_alta_title.setStyleSheet('color: #ffea65')
        self.pratos_em_alta_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pratos_em_alta_title.setAlignment(Qt.AlignHCenter)
        self.pratos_em_alta_blocos = Block_dish_manager()
        self.pratos_em_alta_blocos.add_new_layers()
        # Criando um layout para pratos_em_alta_frame
        self.pratos_em_alta_layout = QVBoxLayout(self.pratos_em_alta_frame)
        self.pratos_em_alta_layout.setContentsMargins(0, 5, 0, 5)
        self.pratos_em_alta_layout.setSpacing(0)
        # adicionando elementos ao pratos_em_alta_layout
        self.pratos_em_alta_layout.addWidget(self.pratos_em_alta_title)
        self.pratos_em_alta_layout.addWidget(self.pratos_em_alta_blocos)

        # Criando bloco onde serão mostradas os pedidos ativos dentro mainframe.
        self.pedidos_ativos_frame = QFrame()
        self.pedidos_ativos_frame.setStyleSheet('''background-color: #080808;
        border-radius: 10px
        ''')
        self.pedidos_ativos_title = AdvencedLabel('Pedidos ativos', 'berkshire.ttf', 35)
        self.pedidos_ativos_title.setStyleSheet('color: #ffea65')
        self.pedidos_ativos_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.pedidos_ativos_title.setAlignment(Qt.AlignHCenter)
        self.pedidos_ativos_blocos = Block_order_manager()
        self.pedidos_ativos_blocos.add_new_layers()
        # Criando um layout para pedidos_ativos_frame
        self.pedidos_ativos_layout = QVBoxLayout(self.pedidos_ativos_frame)
        self.pedidos_ativos_layout.setSpacing(0)
        self.pedidos_ativos_layout.setContentsMargins(0, 5, 0, 5)
        # Adicionaodo elementos a pedidos_ativos_layout
        self.pedidos_ativos_layout.addWidget(self.pedidos_ativos_title)
        self.pedidos_ativos_layout.addWidget(self.pedidos_ativos_blocos)

        # Criando bloco onde serão mostradas o Estoque em baixa dentro mainframe.
        self.estoque_em_baixa_frame = QFrame()
        self.estoque_em_baixa_frame.setStyleSheet('''background-color: #080808;
        border-radius: 10px
        ''')
        self.estoque_em_baixa_title = AdvencedLabel('Estoque em baixa', 'berkshire.ttf', 35)
        self.estoque_em_baixa_title.setStyleSheet('color: #ffea65')
        self.estoque_em_baixa_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.estoque_em_baixa_title.setAlignment(Qt.AlignHCenter)
        self.estoque_em_baixa_blocos = Block_stock_manager()
        self.estoque_em_baixa_blocos.add_new_layers()
        # Criando um layout para estoque_em_baixa_frame
        self.estoque_em_baixa_layout = QVBoxLayout(self.estoque_em_baixa_frame)
        self.estoque_em_baixa_layout.setSpacing(0)
        self.estoque_em_baixa_layout.setContentsMargins(0, 5, 0, 5)
        # Adicionaodo elementos a pedidos_ativos_layout
        self.estoque_em_baixa_layout.addWidget(self.estoque_em_baixa_title)
        self.estoque_em_baixa_layout.addWidget(self.estoque_em_baixa_blocos)

        # Criando layout para main_frame.
        self.main_frame_layout = QHBoxLayout(self.main_frame)
        self.main_frame_layout.setSpacing(15)
        self.main_frame_layout.setContentsMargins(0, 10, 0, 0)
        # Adicionado elementos ao main_frame_layout
        self.main_frame_layout.addWidget(self.pratos_em_alta_frame)
        self.main_frame_layout.addWidget(self.pedidos_ativos_frame)
        self.main_frame_layout.addWidget(self.estoque_em_baixa_frame)
        # Criando um layout para class Home_Page.
        self.home_page_layout = QVBoxLayout(self)
        self.home_page_layout.setContentsMargins(15, 15, 15, 15)
        self.home_page_layout.setSpacing(15)
        # Adicionando elementos no layout.
        self.home_page_layout.addWidget(self.home_page_name_restaurante)
        self.home_page_layout.addWidget(self.main_frame)
