from ui.all_import_gui import *

def mask_image(img:str = '', size:int = 64):
    # buscar a imagem pela raiz. 
    image_path = abspath(getcwd())
    image_path += f'/ui/images/{img}' 
    # lendo a imagem sob-forma binaria.
    image_bi = open(image_path, 'rb').read()
    # Caregendo a imagem e convertendo em 32-bit ARGB (adicionando canal alpha)
    image = QImage.fromData(image_bi, 'jpg')
    image.convertToFormat(QImage.Format_ARGB32)
    # recortar imagem para quadrado.
    imgsize = min(image.width(), image.height())
    rect = QRect((image.width() - imgsize) / 2, (image.height() - imgsize) / 2,imgsize,imgsize,)
    image = image.copy(rect)
    # Criando a imagem de saida com o mesmo tamanho e com canal alpha e feito 
    # completamete transparencia.
    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)

    brush = QBrush(image)
    painter = QPainter(out_img)
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.drawEllipse(0, 0, imgsize, imgsize)
    painter.end()

    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size * pr
    pm = pm.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    return pm
