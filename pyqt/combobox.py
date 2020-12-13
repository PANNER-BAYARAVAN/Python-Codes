import sys
from PyQt5.QtWidgets import *
 
a = QApplication([])
w = QWidget()
w.resize(320, 100)
w.setWindowTitle("Sample ComboBox!")
 
combo = QComboBox(w)
combo.addItem("Python")
combo.addItem("Perl")
combo.addItem("Java")
combo.addItem("C++")
combo.move(20,20)

button = QPushButton(w)
def on_button_clicked():
    alert = QMessageBox()
    #alert.setText('You clicked the button!')
    alert.setText(combo.currentText())
    alert.exec_()


button.setText("Submit")
button.clicked.connect(on_button_clicked)
button.move(20,60)

#button.show()

 
w.show()
sys.exit(a.exec_())
