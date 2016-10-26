
from PyQt4.QtGui import QMainWindow, QWidget, QLabel,QGridLayout,QPushButton
class CallWindow(QWidget):
    # **************************************************
    #Constructor de la clase
    #**************************************************

    def __init__(self,server):
        super(CallWindow, self).__init__()
        self.server = server
        self.initUI()

    def initUI(self):
        finish_button = QPushButton('Finalizar llamada')
        finish_button.clicked.connect(lambda: self.finish_call())
        grid = QGridLayout()


        grid.addWidget(finish_button)
        self.setLayout(grid)
        self.setGeometry(350, 350, 500, 500)
        self.setWindowTitle('Llamada')
        self.show()

    def finish_call(self):
        self.close()
    """Evento llamado cuando se cierra la ventana
       Detendremos la llamada para el servidor de xmlrpc
    """
    def closeEvent(self, event):
        self.server.finish_call()
        event.accept()

class DummyClass(QWidget):
        def __init__(self):
            super(DummyClass, self).__init__()
