from ui.all_import_gui import *

def get_font(path: str = '', font_size: int = 0):
    # buscar a fonte pela raiz. 
    font_path = abspath(getcwd())
    font_path += f'/ui/fonts/{path}'
    # ----------------------
    # carregando a fonte.
    font_load = QFontDatabase.addApplicationFont(font_path)
    family_font = QFontDatabase.applicationFontFamilies(font_load)
    fontcustome = QFont(family_font[0], font_size)
    return fontcustome


class AdvencedLabel(QLabel):

    def __init__(self, txt: str = '', path: str = 'JosefinSans-SemiBold.ttf', font_size: int = 0, color: str = '#ffffff',
                 link: bool = False):
        super(AdvencedLabel, self).__init__()
        self.setFont(get_font(path, font_size))
        self.setText(txt)
        self.setAlignment(Qt.AlignVCenter)
        self.setStyleSheet(f'color: {color};')
        if link:
            self.setOpenExternalLinks(True)
