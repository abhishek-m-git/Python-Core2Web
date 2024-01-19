import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QComboBox
from PyQt5.QtGui import QColor

class ColorChangerApp (QWidget):
    def __init__(self):
        super().__init__()

        self.int_ui()

    def int_ui(self):
        #create QVBOxlayout
        layout = QVBoxLayout()

        #create a qcombobox and add colors to it
        color_combo = QComboBox(self)
        colors = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
        color_combo.addItems(colors)

        #connect the color change signal to slot
        color_combo.currentIndexChanged.connect(self.change_color)

        #add the Qcombobox to layout
        layout.addWidget(color_combo)

        #set the layout for main window
        self.setLayout(layout)

        #set the intial bg color explicitly
        self.change_color(0)

        #set.the window properties
        self.setGeometry(500,300,500,400)
        self.setWindowTitle('Girgit App')

    def change_color(self,index):
        #get the selected color from qbox combo
        color_name = self.sender().currentText() if self.sender() else "Red"

        #get the Qcolor object based on the color names
        color = QColor(color_name)

        #set the bg of thw window
        self.setStyleSheet(f"background-color:{color.name()};")

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = ColorChangerApp()
    ex.show()
    sys.exit(app.exec_())
    