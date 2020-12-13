import sys
from PyQt5.QtWidgets import *
 
a = QApplication([])
 
w = QMainWindow()
w.resize(320, 240)
w.setWindowTitle("Sample Caldender!")
 

cal = QCalendarWidget(w)
cal.setGridVisible(True)
cal.move(0, 0)
cal.resize(320,240)
 
w.show()
sys.exit(a.exec_())
