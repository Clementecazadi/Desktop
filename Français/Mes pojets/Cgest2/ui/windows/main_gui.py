from ui.all_import_gui import *
from ui.windows.Pages import Pages


# 1. Criando a classe da janela a ser exibida.
class Ui_iterface(object):
    def UI_setup(self, window_app: QMainWindow):
        if not window_app.objectName():
            window_app.setObjectName('MainWindows')
        window_app.resize(1280, 720)
        window_app.setMinimumSize(1280, 700)
        # Adicionando um icone a janela.
        icon = QPixmap(path_local('logov1.png'))
        icon = icon.scaled(45, 45, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        window_app.setWindowIcon(icon)
        # 2. Crianda e configurando MainFrame que a o frame principal. 
        self.Mainframe = QFrame(window_app)
        window_app.setCentralWidget(self.Mainframe)
        # 3. Criando um layout para mainframe
        self.Mainframe_layout = QHBoxLayout(self.Mainframe)
        self.Mainframe_layout.setContentsMargins(0, 0, 0, 0)
        self.Mainframe_layout.setSpacing(0)
        # 4. Criando seções de conteúdo no mainframe.
        self.left_button_frame = QFrame()
        self.left_button_frame.setMaximumWidth(50)
        self.left_button_frame.setMinimumWidth(50)
        self.left_button_frame.setStyleSheet("background-color: #397e72")
        # 4.1 criando um layout para left_button
        self.left_button_frame_layout = QVBoxLayout(self.left_button_frame)
        self.left_button_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.left_button_frame_layout.setSpacing(0)
        # 4.1 Criando elementos para layout de left button
        self.menu_burger = Button_custome_1('Ocultar Menu', icon_path='menu_burger.svg')
        self.left_button_home = Button_custome_1('Página Principal', icon_path='home.svg', is_active=True)
        self.left_button_caixa = Button_custome_1('Caixa', icon_path='caixa.svg')
        self.left_button_mesa = Button_custome_1('Mesas', icon_path='dining_table.svg')
        self.left_button_pratos = Button_custome_1('Produtos', icon_path='dish.svg')
        self.left_button_stoque = Button_custome_1('Stoque', icon_path='stock.svg')
        self.left_button_statistica = Button_custome_1('Statisticas', icon_path='statistic.svg')
        self.left_button_user = Button_custome_1('Usuários', icon_path='people.svg')
        self.left_button_settings = Button_custome_1('Configurações', icon_path='settings.svg')
        self.left_button_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.left_button_frame_ene = QFrame()
        self.left_button_frame_ene.setMinimumHeight(30)
        self.left_button_frame_ene.setStyleSheet("""
            background-color: #004455
        """)

        self.left_button_frame_layout.addWidget(self.menu_burger)
        self.left_button_frame_layout.addWidget(self.left_button_home)
        self.left_button_frame_layout.addWidget(self.left_button_caixa)
        self.left_button_frame_layout.addWidget(self.left_button_mesa)
        self.left_button_frame_layout.addWidget(self.left_button_pratos)
        self.left_button_frame_layout.addWidget(self.left_button_stoque)
        self.left_button_frame_layout.addWidget(self.left_button_statistica)
        self.left_button_frame_layout.addItem(self.left_button_spacer)
        self.left_button_frame_layout.addWidget(self.left_button_user)
        self.left_button_frame_layout.addWidget(self.left_button_settings)
        self.left_button_frame_layout.addWidget(self.left_button_frame_ene)
        self.right_contente_frame = QFrame()
        # 4.2 Criando um layout.
        self.right_contente_frame_layout = QVBoxLayout(self.right_contente_frame)
        self.right_contente_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.right_contente_frame_layout.setSpacing(0)
        # 4.2 Criando elementos no right contente frame.
        # 5 criando o layout top_user_login
        self.top_user_login = QFrame()
        self.top_user_login.setStyleSheet("background-color: #004455")
        # self.top_user_login.setMinimumHeight(100)
        self.top_user_login.setMaximumHeight(100)
        # 5.1 criando um layout para top_user_login
        self.top_user_login_layout = QHBoxLayout(self.top_user_login)
        self.top_user_login_layout.setContentsMargins(15, 10, 15, 10)
        self.top_user_login_layout.setSpacing(0)
        # 5.2 criando elementos para top_user_login.
        self.top_user_frame_info = QFrame()
        self.top_user_frame_info.setMinimumHeight(80)
        # 5.2.1 criando layout para frame_info
        self.top_user_frame_info_layout = QHBoxLayout(self.top_user_frame_info)
        self.top_user_frame_info_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_frame_info_layout.setSpacing(0)
        # 5.2.1.1 Criando elementos para frame_info
        self.top_user_frame_info_image = QFrame()
        # 5.2.1.1.1 carregando a imagen do usuário
        self.top_user_frame_info_foto_profil = QLabel(self.top_user_frame_info_image)
        self.top_user_frame_info_foto_profil.setPixmap(mask_image('clemente.jpg', 80))
        self.top_user_frame_info_foto_profil.show()
        self.top_user_frame_info_foto_profil.setMinimumWidth(90)
        self.top_user_frame_info_image.setMinimumWidth(90)
        self.top_user_frame_info_lables = QFrame()
        # 5.2.1.1.2 Criando um layout para info_labels
        self.top_user_frame_info_lables_layout = QVBoxLayout(self.top_user_frame_info_lables)
        self.top_user_frame_info_lables_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_frame_info_lables_layout.setSpacing(0)
        # 5.2.1.1.2.1 Criando elementos para info_lables_layout
        self.top_user_frame_info_lables_spacer = QSpacerItem(2, 10, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.top_user_frame_info_lable_name = AdvencedLabel('Clemente cazadi', font_size=20)
        self.top_user_frame_info_lable_name.setMinimumHeight(40)
        self.top_user_frame_info_lable_profil = AdvencedLabel('Administrador', font_size=16, color='#afafe9')
        # 5.2.1.1.2 Adicionando elementos no layout info_lables_layout
        self.top_user_frame_info_lables_layout.addItem(self.top_user_frame_info_lables_spacer)
        self.top_user_frame_info_lables_layout.addWidget(self.top_user_frame_info_lable_name)
        self.top_user_frame_info_lables_layout.addWidget(self.top_user_frame_info_lable_profil)
        # 5.2.1 Adicionando elementos no layout frame_info
        self.top_user_frame_info_layout.addWidget(self.top_user_frame_info_image)
        self.top_user_frame_info_layout.addWidget(self.top_user_frame_info_lables)
        self.top_user_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.top_user_rigth_frame = QFrame()
        self.top_user_rigth_frame.setMinimumHeight(80)
        # 5.2.2 Criando um layout para rigth frame.
        self.top_user_rigth_frame_layout = QVBoxLayout(self.top_user_rigth_frame)
        self.top_user_rigth_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_rigth_frame_layout.setSpacing(0)
        # 5.2.2.1 Criando elementos para  rigth frame.
        self.top_user_rigth_frame_simple_view_frame = QFrame()
        # Criando um layout para simple view frame
        self.top_user_rigth_frame_simple_view_layout = QHBoxLayout(self.top_user_rigth_frame_simple_view_frame)
        self.top_user_rigth_frame_simple_view_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_rigth_frame_simple_view_layout.setSpacing(5)
        self.top_user_rigth_frame_simple_view_spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.top_user_rigth_frame_simple_view_name_user = AdvencedLabel('Clemente Cazadi', font_size=14)
        self.top_user_rigth_frame_simple_view_name_user.setHidden(True)
        self.top_user_rigth_frame_simple_view_button = Button_custome_1('', icon_path='hide_user_info.svg', ste=False,
                                                                      height=30, minimum_width=30)
        self.top_user_rigth_frame_simple_view_button.setStyleSheet("""
         QPushButton{
            background-color: #004455;
            border-radius: 14px;
        }

        QPushButton:hover{
            background-color: #a76cff;
        }
        QPushButton:pressed{
            background-color: #6c3cb4;
        }""")
        self.top_user_rigth_frame_simple_view_button.setMaximumSize(30, 30)
        self.top_user_rigth_frame_simple_view_layout.addItem(self.top_user_rigth_frame_simple_view_spacer)
        self.top_user_rigth_frame_simple_view_layout.addWidget(self.top_user_rigth_frame_simple_view_name_user)
        self.top_user_rigth_frame_simple_view_layout.addWidget(self.top_user_rigth_frame_simple_view_button)

        self.top_user_rigth_frame_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.top_user_rigth_exit_frame = QFrame()
        self.top_user_rigth_exit_frame_layout = QHBoxLayout(self.top_user_rigth_exit_frame)
        self.top_user_rigth_exit_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.top_user_rigth_exit_frame_layout.setSpacing(0)
        self.top_user_rigth_exit_spacer = QSpacerItem(10, 10, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.top_user_pushbutton = QPushButton()
        self.top_user_pushbutton.setMinimumSize(100, 30)
        self.top_user_pushbutton.setMaximumSize(100, 30)

        self.top_user_pushbutton.setText('Terminar')
        self.top_user_pushbutton.setFont(get_font('JosefinSans-SemiBold.ttf', 14))
        self.top_user_pushbutton.setStyleSheet("""QPushButton{
            color: #ffffff;
            background-color: #9955ff;
            border-radius: 5px;
        }

        QPushButton:hover{
            background-color: #a76cff;
        }
        QPushButton:pressed{
            background-color: #6c3cb4;
        }""")
        self.top_user_rigth_exit_frame_layout.addItem(self.top_user_rigth_exit_spacer)
        self.top_user_rigth_exit_frame_layout.addWidget(self.top_user_pushbutton)
        # 5.2.2 Adicionando elementos no layout rigth_frame:
        self.top_user_rigth_frame_layout.addWidget(self.top_user_rigth_frame_simple_view_frame)
        self.top_user_rigth_frame_layout.addItem(self.top_user_rigth_frame_spacer)
        self.top_user_rigth_frame_layout.addWidget(self.top_user_rigth_exit_frame)
        # 5.1 Adicionado elementos no layout top_user_login.
        self.top_user_login_layout.addWidget(self.top_user_frame_info)
        self.top_user_login_layout.addItem(self.top_user_spacer)
        self.top_user_login_layout.addWidget(self.top_user_rigth_frame)
        # 6 Criando as areas de trabalho.
        self.main_cotente = Pages()
        # Criando o credit bar
        self.credit_bar = QFrame()
        self.credit_bar.setStyleSheet("background-color: #004455")
        self.credit_bar.setMinimumHeight(30)
        # 7 criando um layout para creditbar.
        self.credit_bar_layout = QHBoxLayout(self.credit_bar)
        self.credit_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.credit_bar_layout.setSpacing(0)
        # 7.1 Criando elementos para o creditbar.
        self.left_spacer1_credit = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.left_spacer2_credit = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.credit_bar_label = AdvencedLabel("Create by: Clemente Alberto N. Cazadi", 'JosefinSans-SemiBold.ttf', 12,
                                              '#ffffff')
        # 7 Adicionado os elementos no layout.
        self.credit_bar_layout.addItem(self.left_spacer1_credit)
        self.credit_bar_layout.addWidget(self.credit_bar_label)
        self.credit_bar_layout.addItem(self.left_spacer2_credit)
        # 4.2 adicionar layout.
        self.right_contente_frame_layout.addWidget(self.top_user_login)
        self.right_contente_frame_layout.addWidget(self.main_cotente)
        self.right_contente_frame_layout.addWidget(self.credit_bar)
        # 3. Adicionando ao layout do frame. 
        self.Mainframe_layout.addWidget(self.left_button_frame)
        self.Mainframe_layout.addWidget(self.right_contente_frame)
