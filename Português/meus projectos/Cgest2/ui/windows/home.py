from PySide6.QtWidgets import QWidget, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, \
    QProgressBar, QListWidget, QListWidgetItem, QScrollBar
from PySide6.QtCore import Qt
from ui.custome.Label import AdvencedLabel, get_font


# Criando widgets para o bloco de pratos em alta.
class Block_dish_in_high(QFrame):
    def __init__(self):
        super(Block_dish_in_high, self).__init__()
        self.setStyleSheet('background-color: qlineargradient'
        '(spread:pad, x1:0.519, y1:0, x2:0.5, y2:0.835, stop:0 rgba(128, 71, 213, 255), stop:1 '
        'rgba(43, 19, 77, 255));')
        # Criando elementos do bloco.
        self.dish_name = QLabel('Carne de pato assado com batatas fritas.')
        self.dish_name.setStyleSheet('background-color: #00000000; color: #ffffff')
        font = get_font('JosefinSans-SemiBold.ttf', font_size=18)
        font.setItalic(True)
        self.dish_name.setFont(font)
        self.dish_name.setWordWrap(True)
        self.commands = AdvencedLabel('Pedidos: 89', font_size=14)
        self.commands.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.price_of_dish = AdvencedLabel('Preso: 3500 kz', font_size=14)
        self.price_of_dish.setStyleSheet('background-color: #00000000; color: #ffffff')
        # Elementos da taxa de conversão.
        self.tax_label = AdvencedLabel('Taxa:', font_size=14)
        self.tax_label.setStyleSheet('background-color: #00000000; color: #ffffff')
        self.tax_progress = QProgressBar()
        self.tax_progress.setMaximum(100)
        self.tax_progress.setMinimum(0)
        self.tax_progress.setValue(82)
        self.tax_progress.setTextVisible(False)
        self.tax_progress.setMaximumHeight(5)
        self.tax_progress.setStyleSheet('''
                QProgressBar::chunk {
                    background-color: #fedb04;
	                border-radius: 2px
                };
                border-radius: 2px;
        ''')
        self.tax_percent_label = AdvencedLabel('82%', font_size= 14)
        self.tax_percent_label.setStyleSheet('background-color: #00000000; color: #ffffff')
        # Criando layout para os elementos TAX
        self.tax_layout = QHBoxLayout()
        self.tax_layout.setContentsMargins(0, 0, 0, 0)
        self.tax_layout.setSpacing(10)
        # Adicionando elementos TAX
        self.tax_layout.addWidget(self.tax_label)
        self.tax_layout.addWidget(self.tax_progress)
        self.tax_layout.addWidget(self.tax_percent_label)
        # Criando layout para todos elementos que não o titulo do prato.
        self.elements = QVBoxLayout()
        self.elements.setContentsMargins(0, 0, 0, 0)
        self.elements.setSpacing(5)
        # Adicionando elementos no layout.
        self.elements.addWidget(self.commands)
        self.elements.addWidget(self.price_of_dish)
        self.elements.addLayout(self.tax_layout)
        # Criando layout para o bloco inteiro
        self.block_layout = QVBoxLayout(self)
        self.block_layout.setContentsMargins(10, 10, 10, 10)
        self.block_layout.setSpacing(5)
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
        scrobar = QScrollBar()
        scrobar.set
        #self.ui_layers.setVerticalScrollBar()
        self.ui_layers.setSelectionMode(QListWidget.NoSelection)
        # Criando o layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.ui_layers)

    def add_new_layers(self):
        for x in range(3):
            widget = Block_dish_in_high()
            item = QListWidgetItem()
            self.ui_layers.insertItem(self.ui_layers.count(), item)
            self.ui_layers.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())

#class 

class Page_home(QWidget):
    def __init__(self):
        super(Page_home, self).__init__()
        # Criando elementos para a home.
        self.home_page_name_restaurante = AdvencedLabel('Restaurente Baia Verde', 'berkshire.ttf', 50)
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
        self.pedidos_ativos_blocos = QFrame()
        # Criando um layout para pedidos_ativos_frame
        self.pedidos_ativos_layout = QVBoxLayout(self.pedidos_ativos_frame)
        self.pedidos_ativos_layout.setSpacing(0)
        self.pedidos_ativos_layout.setContentsMargins(0, 5, 0, 0)
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
        self.estoque_em_baixa_blocos = QFrame()
        # Criando um layout para estoque_em_baixa_frame
        self.estoque_em_baixa_layout = QVBoxLayout(self.estoque_em_baixa_frame)
        self.estoque_em_baixa_layout.setSpacing(0)
        self.estoque_em_baixa_layout.setContentsMargins(0, 5, 0, 0)
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
