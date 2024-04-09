from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,  QVBoxLayout, QLabel, QPushButton, QListWidget, QFileDialog
import os
from PIL import Image
from PyQt5.QtGui import QPixmap
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.image_path = None
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        self.image_path = os.path.join(dir, filename)
        self.image = Image.open(self.image_path)
    def showImage(self, path):
        img_lbl.hide()
        pixmapimage = QPixmap(path)
        w, h = img_lbl.width(), img_lbl.height()
        pixmapimage = pixmapimage.scaled(w, h)
        img_lbl.setPixmap(pixmapimage)
        img_lbl.show()
    def saveImage(self):
        '''сохраняеет копию файла'''
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)




#Создание приложени
app = QApplication([])
win = QWidget()
win.resize(1000,780)
win.setWindowTitle('Easy Editor')

#Создаиние виджетов
dir_btn = QPushButton('Папка')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркало')
rez_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч/Б')
#-----------------------
img_lbl = QLabel('Картинка')
img_list = QListWidget()

#Зоздание линий
btns_line = QHBoxLayout()
main_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

btns_line.addWidget(left_btn)
btns_line.addWidget(bw_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(mirror_btn)
btns_line.addWidget(rez_btn)

v_line1.addWidget(dir_btn)
v_line1.addWidget(img_list)

v_line2.addWidget(img_lbl)
v_line2.addLayout(btns_line)

main_line.addLayout(v_line1, 20)
main_line.addLayout(v_line2, 80)

win.setLayout(main_line)
#Логика
workdir = ''
workImage = ImageProcessor()
def filter(files, ext):
    result = []
    for filename in files:
        for e in ext:
            if filename.endswith(e):
                result.append(filename)
    return result
def openFolder():
    global workdir
    ext =  ['.jpg','.png','jpeg','.bmp','gif']
    workdir = QFileDialog.getExistingDirectory()
    files_names = os.listdir(workdir)
    filenames = filter(files_names, ext)
    img_list.clear()
    img_list.addItems(filenames)

def showImage():
    filename = img_list.currentItem().text()
    workImage.loadImage(workdir, filename)
    workImage.showImage(workImage.image_path)




#конекты
dir_btn.clicked.connect(openFolder)
img_list.itemClicked.connect(showImage)
bw_btn.clicked.connect(workImage.do_bw)

#Запуск приложения
win.show()
app.exec_()






#Создание приложени
app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('Easy Editor')

#Создаиние виджетов
dir_btn = QPushButton('Папка')
left_btn = QPushButton('Лево')
right_btn = QPushButton('Право')
mirror_btn = QPushButton('Зеркало')
rez_btn = QPushButton('Резкость')
bw_btn = QPushButton('Ч/Б')
#-----------------------
img_lbl = QLabel('Картинка')
img_list = QListWidget()

#Зоздание линий
btns_line = QHBoxLayout()
main_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()

btns_line.addWidget(left_btn)
btns_line.addWidget(bw_btn)
btns_line.addWidget(right_btn)
btns_line.addWidget(mirror_btn)
btns_line.addWidget(rez_btn)

v_line1.addWidget(dir_btn)
v_line1.addWidget(img_list)

v_line2.addWidget(img_lbl)
v_line2.addLayout(btns_line)

main_line.addLayout(v_line1, 20)
main_line.addLayout(v_line2, 80)

win.setLayout(main_line)
#Логика
workdir = ''
workImage = ImageProcessor()
def filter(files, ext):
    result = []
    for filename in files:
        for e in ext:
            if filename.endswith(e):
                result.append(filename)
    return result
def openFolder():
    global workdir
    ext =  ['.jpg','.png','jpeg','.bmp','gif']
    workdir = QFileDialog.getExistingDirectory()
    files_names = os.listdir(workdir)
    filenames = filter(files_names, ext)
    img_list.clear()
    img_list.addItems(filenames)

def showImage():
    filename = img_list.currentItem().text()
    workImage.loadImage(workdir, filename)
    workImage.showImage(workImage.image_path)




#конекты
dir_btn.clicked.connect(openFolder)
img_list.itemClicked.connect(showImage)

#Запуск приложения
win.show()
app.exec_()
