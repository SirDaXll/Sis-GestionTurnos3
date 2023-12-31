import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QListWidget,QHBoxLayout,QDialog,QGridLayout,QMessageBox
from PyQt6.QtCore import Qt
class ModificarContraseña(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Contraseña")

    #ventanas
        #ventana principal
        ventanaGrande=QVBoxLayout()# integra logo  y subventana
        subVentana=QHBoxLayout()#integra lista a la derecha y ventana derecha
        ventanaderecha=QVBoxLayout()#incluye dos botones derechos
        listita=["Dante","Camilo","Diego","Massimo","Tomas"]
        self.lista=QListWidget()#lista
        self.lista.addItems(listita)
        
        #logo
        logo=QLabel(self)
        imagen = QPixmap(r"asset/logo.png")       
        logo.setPixmap(imagen)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #botones
        mc=QPushButton("Modificar Contraseña")
        volver=QPushButton("Volver")
        volver.clicked.connect(self.cerrar)#creo que se puede achicar la funcion
        mc.clicked.connect(self.modificar_contrasena)
        mc.clicked.connect(self.get_items)


        #asignar widgets
        ventanaderecha.addWidget(mc)
        ventanaderecha.addWidget(volver)
        subVentana.addWidget(self.lista)
        
        ventanaGrande.addWidget(logo)
        

        #asignar ventanas
        ventana=QWidget()
        subVentana.addLayout(ventanaderecha)
        ventanaGrande.addLayout(subVentana)
        ventana.setLayout(ventanaGrande)
        self.setCentralWidget(ventana)
        


    def modificar_contrasena(self):
        modificar = Modificar()
        modificar.exec()
    def cerrar(self):
        self.close()
    def get_items(self):
        items=self.lista.selectedItems()
        for item in items:
            return item.text()
class Modificar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cambio de Contraseña")

        #ventana
        ventanita=QVBoxLayout()

        #grid
        datos=QGridLayout()
        
        #informacion de pantalla
        #self.titulo=QLabel("Cambiar contraseña de usuario")#aqui va el nombre de la persona tambien 
        self.contrasena=QLabel("Contraseña:")
        self.confirmar_contrasena=QLabel("Confirmar contraseña:")
        #datoas a ingresar
        self.modificar_contrasena=QLineEdit("")
        self.modificar_contrasena.setEchoMode(QLineEdit.EchoMode.Password)#primera contraseña
        self.modificar_confirmar=QLineEdit("")
        self.modificar_confirmar.setEchoMode(QLineEdit.EchoMode.Password)#segunda contraseña
        #boton
        cambiar=QPushButton("Cambiar")
        cambiar.clicked.connect(self.igualdad)
        #asignar las al grid
        datos.addWidget(self.contrasena,0,0)
        datos.addWidget(self.confirmar_contrasena,1,0)
        datos.addWidget(self.modificar_contrasena,0,1)
        datos.addWidget(self.modificar_confirmar,1,1)
        
        #ventanita.addWidget(self.titulo)
        ventanita.addLayout(datos)
        ventanita.addWidget(cambiar)

        self.setLayout(ventanita)

    def igualdad(self):
        a=self.modificar_contrasena.text()
        b=self.modificar_confirmar.text()
        c=a.replace(" ","")
        if a==b:
            if c!="":         
                QMessageBox.information(self, "Modificar contraseña (empleado)", "Contraseña cambiada.")
                self.close()
            else:
               QMessageBox.information(self, "Modificar contraseña (empleado)", "Contraseña vacía.")

        else:
            QMessageBox.information(self, "Modificar contraseña (empleado)", "Contraseñas diferentes.")
       
#se puede arreglar el mesnaje al colocar una contraseña y otra vacia para que diga que haya una vacia

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=ModificarContraseña()
    ventana.show()
    sys.exit(app.exec())