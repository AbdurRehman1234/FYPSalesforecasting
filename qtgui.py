import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
from PyQt5 import QtCore
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'TimeSeries analysis'
        self.left = 50
        self.top = 50
        self.width = 700
        self.height = 600
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('pound.png'))
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.home()
        self.gui = FilePicker()
        self.gui.show()
        
        self.show()
    def home(self):
        btn = QPushButton("Quit", self)
        btn.setToolTip('Press this button to quit')
        btn.resize(100,50)
        btn.move(300,500)
        self.show()
class FilePicker(QtGui.QWidget):
	def __init__(self,parent):
		QtGui.QMainWindow.__init__(self)
		self.setWindowTitle('FilePicker')
		self.verticalbox = QtGui.QVBoxLayout()
		self.setLayout(self.verticalbox)
		#Creating a label which displays the path to chosen file
		self.lbl = QtGui.QLabel('No file selected')
		self.verticalbox.addWidget(self.lbl)

		#creating push button labeled as choose csv

		btn = QtGui.QpuchButton('Choose file' , self)
		self.vbox.addWidget(btn)

		#connecting button to file handler 
		self.connect(btn, QtCore.SIGNAL('clicked()'), self.get_fname)

	def get_fname(self):
	
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Select file')

        if fname == True:
        		self.lbl.setText(fname)
        else:
            	self.lbl.setText('No file selected')

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Upload You CSV")
        self.tabs.addTab(self.tab2,"Settings")
        self.tabs.addTab(self.tab3,"Output")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Upload CSV")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())