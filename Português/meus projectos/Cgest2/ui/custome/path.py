from os import getcwd
from os.path import abspath

def path_local(img:str = '', local ="/ui/images/"):
    # buscar a imagem pela raiz. 
    image_path = abspath(getcwd())
    image_path += f'{local}{img}'
    return image_path 