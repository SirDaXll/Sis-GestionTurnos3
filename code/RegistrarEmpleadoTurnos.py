import csv
from PyQt6.QtWidgets import QWidget, QApplication,QDateTimeEdit, QComboBox, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QMessageBox, QLineEdit, QHBoxLayout
from PyQt6.QtCore import QDateTime
from Empleado import Empleado
from Turno import Turno
lista_turnos = []
Lista_empleados=[]
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Nombre Empresa")

        # self.boton_registrar = QPushButton("Registrar Empleado")
        # self.boton_registrar.clicked.connect(lambda: self.funcion_auxiliar(1))

        self.boton_crear = QPushButton("Crear Turno")
        self.boton_crear.clicked.connect(lambda: self.funcion_auxiliar(2))

        self.boton_modificar = QPushButton("Modificar Turno")
        self.boton_modificar.clicked.connect(lambda: self.funcion_auxiliar(3))

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interfaz Principal"))
        # layout.addWidget(self.boton_registrar)
        layout.addWidget(self.boton_crear)
        layout.addWidget(self.boton_modificar)

        central_widget = QDialog()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def funcion_auxiliar(self,id):
        # if id == 1:
        #     ventana_registro = VentanaRegistro()
        #     ventana_registro.exec()
        if id == 2:
            ventana_turno = VentanaTurnos()
            ventana_turno.exec()
        elif id == 3:
            ventana_modificar = VentanaModificar()
            ventana_modificar.exec()


class VentanaRegistro(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Registro De Empleados (Nombre Empresa)")

        self.etiqueta_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()
        self.etiqueta_rol=QLabel("Rol")
        self.combo_box=QComboBox()
        self.combo_box.addItem("Gerente")
        self.combo_box.addItem("Jefe de turno")
        self.combo_box.addItem("Recepcionista")
        self.combo_box.addItem("Botones")        
        self.combo_box.addItem("Guardia de seguridad")
        self.combo_box.addItem("Mucama")
        self.combo_box.addItem("Cocinero")        
        self.combo_box.addItem("Bartender")
        self.combo_box.addItem("Camarero")

        self.etiqueta_usuario = QLabel("Usuario")
        self.campo_usuario = QLineEdit()
        self.etiqueta_contrasena = QLabel("Contraseña:")
        self.campo_contrasena = QLineEdit()
        self.campo_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.etiqueta_contrasena_confirmar = QLabel("Confirmar Contraseña:")
        self.campo_contrasena_confirmar=QLineEdit()
        self.campo_contrasena_confirmar.setEchoMode(QLineEdit.EchoMode.Password)
        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(self.etiqueta_rol)
        layout.addWidget(self.combo_box)
        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.campo_usuario)
        layout.addWidget(self.etiqueta_contrasena)
        layout.addWidget(self.campo_contrasena)
        layout.addWidget(self.etiqueta_contrasena_confirmar)
        layout.addWidget(self.campo_contrasena_confirmar)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_datos(self):                    # funcion de guardar datos 
               
        nombre = self.campo_nombre.text().strip()
        usuario = self.campo_usuario.text().strip()
        contrasena = self.campo_contrasena.text().strip()
        contrasena_confirmar=self.campo_contrasena_confirmar.text().strip()
        rol=self.combo_box.currentText()
        if not nombre or not usuario or not contrasena:
            QMessageBox.information(self, "Empleados (Nombre Empresa)", "debe rellenar todos los campos.")
        elif contrasena!= contrasena_confirmar:
            QMessageBox.information(self,"Empleados (Nombre Empresa)","contraseñas diferentes")
        else:
           with open("dataset/empleados.csv","a",newline="") as archivo_csv:
            archivo_csv.write(nombre + ",")
            archivo_csv.write(rol + ",")
            archivo_csv.write(usuario + ",")
            archivo_csv.write(contrasena + "\n")
            QMessageBox.information(self, "Empleados (Nombre Empresa)", "Empleado registrado exitosamente.")
            Lista_empleados.append(str(nombre + " " + usuario))
            self.campo_nombre.clear()
            self.campo_usuario.clear()
            self.campo_contrasena.clear()
            self.campo_contrasena_confirmar.clear()
            self.close()
            archivo_csv.close()

class VentanaTurnos(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Turnos Nombre Empresa")

        self.etiqueta_fecha_hora = QLabel("Fecha")
        self.campo_fecha_hora = QDateTimeEdit()
        self.etiqueta_empleado = QLabel("Empleado")
        self.campo_empleado = QComboBox()

        # Configuración
        # Despliega calendario
        self.campo_fecha_hora.setCalendarPopup(True)
        # Solo se pueden ingresar turnos nuevos de la fecha actual en adelante
        self.campo_fecha_hora.setMinimumDateTime(QDateTime.currentDateTime())

        self.cargar_empleados_csv()

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_fecha_hora)
        layout.addWidget(self.campo_fecha_hora)
        layout.addWidget(self.etiqueta_empleado)
        layout.addWidget(self.campo_empleado)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def cargar_empleados_csv(self):
        with open("dataset/empleados.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            for row in reader:
                empleado = row[0]
                self.campo_empleado.addItem(empleado)

    def guardar_datos(self):
        fecha = self.campo_fecha_hora.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        empleado = self.campo_empleado.currentText()

        turno = [empleado, fecha]
        self.guardar_turno_csv(turno)

        QMessageBox.information(self, "Turnos Nombre Empresa", "Turno creado exitosamente.")
        self.close()

    def guardar_turno_csv(self, turno):
        with open("dataset/turnos.csv", "a", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(turno)

        # Actualizar la lista de turnos
        lista_turnos.append(str(turno))

class VentanaModificar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar turnos")
        #Elementos
        etiqueta_turno = QLabel("Turno")
        self.turnos = QComboBox()
        self.boton_aceptar = QPushButton("Aceptar")
        #Config
        self.turnos.addItems(lista_turnos)
        self.boton_aceptar.clicked.connect(lambda: self.desplegar(1))

        #Contenedores
        campos = QHBoxLayout()
        campos.addWidget(etiqueta_turno)
        campos.addWidget(self.turnos)
        
        campos_widget = QWidget()
        campos_widget.setLayout(campos)

        contenedor = QVBoxLayout()
        contenedor.addWidget(campos_widget)
        contenedor.addWidget(self.boton_aceptar)

        self.setLayout(contenedor)
    
    def desplegar(self,id):
        if id == 1:
            ventana_modificando = VentanaModificando()
            ventana_modificando.exec()

class VentanaModificando(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modificando turno")

        self.etiqueta_fecha_hora = QLabel("Fecha")
        self.campo_fecha_hora = QDateTimeEdit()
        self.campo_empleado = QComboBox()
        
        #Config
        #Despliega calendario
        self.campo_fecha_hora.setCalendarPopup(True)
        #Solo se pueden ingresar turnos nuevos de la fecha actual en adelante
        self.campo_fecha_hora.setMinimumDateTime(QDateTime.currentDateTime())
        self.campo_empleado.addItems(Lista_empleados)

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_fecha_hora)
        layout.addWidget(self.campo_fecha_hora)
        layout.addWidget(self.etiqueta_empleado)
        layout.addWidget(self.campo_empleado)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_datos(self):
        fecha = self.campo_fecha_hora.text()
        print(fecha)

        QMessageBox.information(self, "Turnos nombre empresa", "Turno creado exitosamente.")
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec()
