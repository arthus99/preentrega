from enum import Enum   # Para los Enumeradores
import json             # Para utilizar formato json
import os, platform     # Para limpiar la pantalla

class Accion(Enum):
    Agrega_Usuario = 1
    Muestra_Usuarios = 2
    Login = 3
    Guarda_en_Archivo = 4
    Salir = 100
    Lee_de_Archivo = 5

class TipoPantalla(Enum):
    DatosUsuario = 1
    Main = 2

class Mnu:

    @staticmethod
    def limpiar_pantalla():
        # Limpia la pantalla de la consola.
        sistema = platform.system()   #Determina el so donde se ejecuta el script
        if sistema == 'Windows':
            os.system('cls')  # Comando para limpiar la pantalla en Windows
        elif sistema == 'Linux' or sistema == 'Darwin':
            os.system('clear')  # Comando para limpiar la pantalla en Linux y macOS
        else:
            print("\n" * 100)  # Método general si no se reconoce el sistema operativo

    
    @staticmethod
    def imprime_strings(msgs:tuple):
        for item in msgs:
            print(item)
    @staticmethod
    def imprime_pantalla(tipo: TipoPantalla) -> dict:
        """
        Muestra la pantalla adecuada de acuerdo al "TipoPantalla" y regresa un diccionario 
        con los nombres de los campos como llaves y los valores recolectados.
        """
        respuesta = {}

        if tipo == TipoPantalla.DatosUsuario:
            usr = input("Usuario: ").strip()
            pws = input("Contraseña: ").strip()
            respuesta.update({"usr": usr, "pws": pws})

        elif tipo == TipoPantalla.Main:
            print("################# Menú #################")
            print("Escriba la acción a realizar (número) ó 'S' para Salir")
            print("\t1. Agregar Usuario")
            print("\t2. Mostrar Usuarios")
            print("\t3. Login")
            print("\t4. Guardar Usuarios a Archivo")
            print("\t5. Leer Usuarios desde Archivo")
            print("\n" * 3)
            accion = input("Acción: ").strip()

            if accion.lower() == "s":
                respuesta = {"accion": Accion.Salir}
            elif accion.isdigit():
                accion = int(accion)
                try:
                    respuesta = {"accion": Accion(accion)}
                except ValueError:
                    print("Error: Acción no reconocida\n\n\n")
                    respuesta = None
            else:
                print("Error: Entrada no válida\n\n\n")
                respuesta = None

        else:
            print("Error: Tipo de pantalla no reconocido\n\n\n")
            respuesta = None

        return respuesta if respuesta else {}

class CtrlUsr:

    def __init__(self, Usrs: dict) -> None:
        self.Usrs = Usrs
        self._stop = False
        self._CurrentUser = None
        self._CurrentPws = None
        self._file_path = 'usuarios.json'
        self.Lee_de_Archivo()

    @property
    def CurrentUser(self):
        return self._CurrentUser

    @CurrentUser.setter
    def CurrentUser(self, valor):
        self._CurrentUser = valor

    @property
    def CurrentPws(self):
        return self._CurrentPws

    @CurrentPws.setter
    def CurrentPws(self, valor):
        self._CurrentPws = valor

    def Valida_Usuario(self, usr, pws) -> bool:
        if usr in self.Usrs and self.Usrs[usr] == pws:
            Mnu.imprime_strings(("\n\n¡Usted ha iniciado sesión!\n\n\n",))
            return True
        else:
            Mnu.imprime_strings(("\n\nUsuario o Contraseña incorrecta.\n\n\n",))
            return False

    def Obten_Datos_Usuario(self):
        self._stop = False
        while not self._stop:
            respuesta = Mnu.imprime_pantalla(TipoPantalla.DatosUsuario)
            if respuesta:
                usr = respuesta.get("usr")
                pws = respuesta.get("pws")
                if usr.lower() in ["salir", "s"] or pws.lower() in ["salir", "s"]:
                    self._stop = True
                    self._CurrentUser = None
                    self._CurrentPws = None
                else:
                    self._CurrentUser = usr
                    self._CurrentPws = pws
                    self._stop = True

    def Agregar_a_lista(self):
        if self._CurrentUser and self._CurrentPws:
            if self._CurrentUser not in self.Usrs:
                self.Usrs[self._CurrentUser] = self._CurrentPws
                Mnu.imprime_strings((f"Usuario: {self._CurrentUser} se ha agregado.\n\n\n",))
            else:
                Mnu.imprime_strings((f"Usuario: {self._CurrentUser} ya existe en la BD\n\n\n",))

            self.CurrentUser = None
            self.CurrentPws = None

    def Borra_Usuario(self):
        if self._CurrentUser in self.Usrs:
            del self.Usrs[self._CurrentUser]
            self._CurrentUser = None
            self._CurrentPws = None

    def Muestra_Usuarios(self):
        if self.Usrs:
            # Mostrar los usuarios en formato de diccionario
            for usr, pwd in self.Usrs.items():
                Mnu.imprime_strings((f"Usuario: {usr}, Contraseña: {pwd}",))
            Mnu.imprime_strings(("\n\n",))
        else:
            Mnu.imprime_strings(("No existen Usuarios en la BD.\n\n\n",))

    def Guarda_en_Archivo(self):
        try:
            with open(self._file_path, 'w') as file:
                json.dump(self.Usrs, file, indent=4, ensure_ascii=False)
            Mnu.imprime_strings((f"Datos guardados en {self._file_path}",))
        except IOError as e:
            Mnu.imprime_strings((f"Error al guardar los datos: {e}",))

    def Lee_de_Archivo(self):
        try:
            with open(self._file_path, 'r') as file:
                self.Usrs = json.load(file)
            Mnu.imprime_strings((f"Datos leídos desde {self._file_path}\n\n",))
        except FileNotFoundError:
            Mnu.imprime_strings((
                f"El archivo {self._file_path} no se encontró.",
                f"Ejecute la opción: {Accion.Muestra_Usuarios.value}. {Accion.Muestra_Usuarios.name}",
                f"o {Accion.Agrega_Usuario.value}. {Accion.Agrega_Usuario.name}"
            ))
        except json.JSONDecodeError:
            Mnu.imprime_strings((f"Error al decodificar el archivo {self._file_path}.",))
        except IOError as e:
            Mnu.imprime_strings((f"Error al leer el archivo: {e}",))

# Define el dict myUsrs
myUsrs = {}

# Inicializa la clase con el dic: myUsrs
Control = CtrlUsr(myUsrs)

salir = False
while not salir:
    try:
        respuesta = Mnu.imprime_pantalla(TipoPantalla.Main)
        if respuesta and "accion" in respuesta:
            if respuesta["accion"] == Accion.Agrega_Usuario:
                Control.Obten_Datos_Usuario()
                Control.Agregar_a_lista()
                Mnu.limpiar_pantalla()
            elif respuesta["accion"] == Accion.Guarda_en_Archivo:
                Control.Guarda_en_Archivo()
                Mnu.limpiar_pantalla()
                Mnu.imprime_strings((f"Los datos han sido guardados.\n\n\n",))
            elif respuesta["accion"] == Accion.Login:
                Control.Obten_Datos_Usuario()
                Control.Valida_Usuario(Control.CurrentUser, Control.CurrentPws)
            elif respuesta["accion"] == Accion.Muestra_Usuarios:
                Mnu.limpiar_pantalla()
                Control.Muestra_Usuarios()
            elif respuesta["accion"] == Accion.Lee_de_Archivo:
                Control.Lee_de_Archivo()
                Control.Muestra_Usuarios()
            elif respuesta["accion"] == Accion.Salir:
                salir = True
    except Exception as e:
        import traceback
        error_info = traceback.format_exc()
        Mnu.imprime_strings((f"Ocurrió un error inesperado: {error_info}\n\n\n",))
