from ui.all_import_gui import *

class login_gui(QMainWindow):
    def __init__(self):
        super(login_gui, self).__init__()
        self.setFixedSize(900, 600)
        # Adicionando um icone a janela.
        icon = QPixmap(path_local('logov1.png'))
        icon = icon.scaled(45, 45, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setWindowIcon(icon)
        
        # Criando um layout 
        
    