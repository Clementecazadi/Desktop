from ui.all_import_gui import *

class AdvencedLine_edit(QLineEdit):
    def __init__( self, txt: str = '', font_family: str = 'JosefinSans-SemiBold.ttf', 
                font_size: int = 0, color: str = '#f2f2f2', border_radius:int = 10, border_color:str = '#',
                link: bool = False):
        super(AdvencedLine_edit, self).__init__()
        self.setPlaceholderText(txt)
        self.setFont(get_font(font_family, font_size))
        self.setMinimumHeight(50)
        self.setFocus(Qt.NoFocusReason)
        self.setStyleSheet(f"""

            QLineEdit{{
                color: #444444;
                background-color: #f2f2f2;
                padding: 10px;
                border: 3px solid #00d4aa;
                border-radius: {border_radius};
            }}
        
        
        """)
