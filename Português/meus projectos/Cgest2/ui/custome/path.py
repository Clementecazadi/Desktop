from ui.all_import_gui import *

def path_local(img:str = '', local ="/ui/images/"):
    # buscar a imagem pela raiz. 
    image_path = abspath(getcwd())
    image_path += f'{local}{img}'
    return image_path 