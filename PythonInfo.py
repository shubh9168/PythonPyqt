import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QWidget, QDesktopWidget
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
import fitz  # PyMuPDF
from PyQt5 import QtCore, QtGui, QtWidgets


class C2W_PythonInfo(object):
    def infoPage(self, parent):
        self.c2w_dialog = QtWidgets.QDialog(parent)
        self.c2w_ui = Ui_C2W_PythonInfoDialog()
        self.c2w_ui.setupUi(self.c2w_dialog)
        self.c2w_dialog.show()


class PDFViewer(QtWidgets.QWidget):
    def __init__(self, pdf_path):
        super().__init__()
        self.init_ui(pdf_path)

    def init_ui(self, pdf_path):
        layout = QtWidgets.QVBoxLayout(self)
        self.c2w_pdf_view = QtWidgets.QGraphicsView(self)
        layout.addWidget(self.c2w_pdf_view)
        self.c2w_pdf_scene = QtWidgets.QGraphicsScene(self)
        self.c2w_pdf_view.setScene(self.c2w_pdf_scene)
        self.c2w_load_pdf(pdf_path)

    def c2w_load_pdf(self, pdf_path):
        pdf_document = fitz.open(pdf_path)
        y_position = 0
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)

            image = page.get_pixmap()
            pil_image = Image.frombytes(
                "RGB", (image.width, image.height), image.samples)
            qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height,
                            QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            image_item = QGraphicsPixmapItem(pixmap)
            image_item.setPos(0, y_position)
            y_position += image_item.pixmap().height()
            self.c2w_pdf_scene.addItem(image_item)
        pdf_document.close()


class Ui_C2W_PythonInfoDialog(object):
    def c2w_openLink(self, event):
        print("hello")
        QtGui.QDesktopServices.openUrl(
            QtCore.QUrl("https://www.core2web.in/"))

    def setupUi(self, Widget):
        desktop = QDesktopWidget()
        primary_screen = desktop.screenGeometry(desktop.primaryScreen())
        monitor_width = primary_screen.width()
        monitor_height = primary_screen.height()
        Widget.setObjectName("Widget")
        Widget.resize(monitor_width, monitor_height)
        self.c2w_widget = QtWidgets.QWidget(Widget)
        self.c2w_widget.setGeometry(QtCore.QRect(0, 0, monitor_width, 50))
        self.c2w_widget.setStyleSheet("background:#0E1D35;")
        self.c2w_widget.setObjectName("widget")
        self.c2w_imageLabel1 = QtWidgets.QLabel(self.c2w_widget)
        self.c2w_imageLabel1.setGeometry(QtCore.QRect(15, 0, 200, 50))
        self.c2w_imageLabel1.setObjectName("imageLabel")
        pixmap1 = QtGui.QPixmap('./assets/images/Group 943logo.png')

        self.c2w_imageLabel1.setPixmap(pixmap1)
        self.c2w_imageLabel1.mouseDoubleClickEvent = self.c2w_openLink

        self.c2w_frame = QtWidgets.QFrame(Widget)
        self.c2w_frame.setGeometry(
            QtCore.QRect(0, 50, monitor_width, monitor_height-50))
        self.c2w_frame.setStyleSheet(
            "background:#2B3D5B;\nfont-style: poppins")
        self.c2w_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.c2w_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.c2w_frame.setObjectName("frame")
        self.c2w_tabWidget = QtWidgets.QTabWidget(self.c2w_frame)
        self.c2w_tabWidget.setGeometry(
            QtCore.QRect(0, 0, monitor_width, monitor_height-50))
        self.c2w_tabWidget.setObjectName("tabWidget")
        self.c2w_tab = QtWidgets.QWidget()
        self.c2w_tab.setObjectName("tab")
        self.c2w_tabWidget.addTab(self.c2w_tab, "")
        self.c2w_tab_2 = QtWidgets.QWidget()
        self.c2w_tab_2.setObjectName("tab_2")
        self.c2w_tabWidget.addTab(self.c2w_tab_2, "")

        self.c2w_tab_3 = QtWidgets.QWidget()
        self.c2w_tab_3.setObjectName("tab_3")
        self.c2w_tabWidget.addTab(self.c2w_tab_3, "")

        self.c2w_tab_4 = QtWidgets.QWidget()
        self.c2w_tab_4.setObjectName("tab_4")
        self.c2w_tabWidget.addTab(self.c2w_tab_4, "")
        self.c2w_tabStyle = """height:200px;width:50px;background-color:red;"""
        self.c2w_tab.setStyleSheet("background-color: #C3C3C3;")
        self.c2w_tab_2.setStyleSheet("background-color: #C3C3C3;")
        self.c2w_tab_3.setStyleSheet("background-color: #C3C3C3;")

        self.c2w_pdf_viewer = PDFViewer('./assets/pdf/python Intro.pdf')
        layout = QtWidgets.QVBoxLayout(self.c2w_tab)
        layout.addWidget(self.c2w_pdf_viewer)

        self.c2w_pdf_viewer = PDFViewer('./assets/pdf/python History.pdf')
        layout = QtWidgets.QVBoxLayout(self.c2w_tab_2)
        layout.addWidget(self.c2w_pdf_viewer)
        self.c2w_pdf_viewer = PDFViewer('./assets/pdf/python index.pdf')
        layout = QtWidgets.QVBoxLayout(self.c2w_tab_3)
        layout.addWidget(self.c2w_pdf_viewer)
        self.retranslateUi(Widget)
        self.c2w_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Python Library"))
        self.c2w_tabWidget.setTabText(self.c2w_tabWidget.indexOf(
            self.c2w_tab), _translate("Widget", "Introduction"))
        self.c2w_tabWidget.setTabText(self.c2w_tabWidget.indexOf(
            self.c2w_tab_2), _translate("Widget", "History"))
        self.c2w_tabWidget.setTabText(self.c2w_tabWidget.indexOf(
            self.c2w_tab_3), _translate("Widget", "Index"))
        self.c2w_tabWidget.setTabText(self.c2w_tabWidget.indexOf(
            self.c2w_tab_4), _translate("Widget", "Practice"))


