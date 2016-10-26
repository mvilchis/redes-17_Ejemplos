from PyQt4.QtCore import SIGNAL, QObject,QThread, Qt


class SignalManager(QThread):
    def __init__(self,GUI):
        QThread.__init__(self)
        #Ligamos la signal de add_message_signal a la interfaz grafica
        QObject.connect(self, SIGNAL('text_signal'),GUI.insert_text_window, Qt.QueuedConnection)

    def add_message_signal(self,message):
        self.emit(SIGNAL('text_signal'),message )
