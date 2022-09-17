from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect
from PySide6.QtCore import Property
from PySide6.QtGui import QFontDatabase, QFont
from os.path import abspath
from os import getcwd


def get_font(path:str = '', font_size:int = 0):
    # buscar a fonte pela raiz. 
    font_path = abspath(getcwd())
    font_path += f'/ui/fonts/{path}' 
    #----------------------
    # carregando a fonte.
    font_load = QFontDatabase.addApplicationFont(font_path)
    family_font = QFontDatabase.applicationFontFamilies(font_load)
    fontcustome = QFont(family_font[1], font_size)
    return fontcustome


class AdvencedLabel(QLabel):
    def __init__(self, txt:str = '', path:str = 'josefin.ttf', font_size:int = 0, color:str = '#ffffff', link:bool = False):
        super(AdvencedLabel, self).__init__()
        self._opacity:float = 34
        self.setFont(get_font(path, font_size))
        self.setText(txt)
        self.setStyleSheet(f'color: {color}; font: 500')
        if link:
            self.setOpenExternalLinks(True)
    @Property(float)
    def opacity(self):
        return self._opacity 
    
    @ opacity.setter
    def setOpacity(self, value:float):
        self._opacity = QGraphicsOpacityEffect().opacity(value)
        self.setGraphicsEffect(self._opacity)