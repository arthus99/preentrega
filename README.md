# preentrega
Primera preentrega de Coder

## Documentación del Sistema de Gestión de Usuarios

### Descripción

Este es un sistema simple de gestión de usuarios en Python. Permite agregar, mostrar, borrar usuarios, y gestionar usuarios mediante un archivo JSON para persistencia de datos. 

### Clases

#### `Accion` (Enum)

Esta enumeración define las posibles acciones que el usuario puede realizar desde el menú principal.

- `Agrega_Usuario` (1): Agregar un nuevo usuario.
- `Muestra_Usuarios` (2): Mostrar todos los usuarios.
- `Login` (3): Iniciar sesión.
- `Guarda_en_Archivo` (4): Guardar los usuarios en un archivo.
- `Leer_de_Archivo` (5): Leer los usuarios desde un archivo.
- `Salir` (100): Salir del programa.

#### `TipoPantalla` (Enum)

Esta enumeración define los tipos de pantallas que se pueden mostrar.

- `DatosUsuario` (1): Pantalla para ingresar datos del usuario (usuario y contraseña).
- `Main` (2): Pantalla principal del menú.

#### `Mnu`

Clase con métodos estáticos para manejar la interfaz de usuario.

##### Métodos

- `limpiar_pantalla()`
  - **Descripción**: Limpia la pantalla de la consola según el sistema operativo.
  
- `imprime_strings(*msgs)`
  - **Descripción**: Imprime una o más cadenas de texto en la consola.

- `imprime_pantalla(tipo: TipoPantalla) -> dict`
  - **Descripción**: Muestra la pantalla correspondiente al tipo de pantalla proporcionado y devuelve un diccionario con los datos ingresados.
  - **Parámetro**:
    - `tipo`: Tipo de pantalla a mostrar (debe ser una instancia de `TipoPantalla`).
  - **Retorno**: Un diccionario con los datos ingresados o una acción seleccionada.

#### `CtrlUsr`

Clase que maneja la lógica de usuarios, incluyendo la gestión y persistencia de datos.

##### Atributos

- `Usrs` (dict): Diccionario que almacena los usuarios y sus contraseñas.
- `_stop` (bool): Bandera para controlar la entrada del usuario.
- `_CurrentUser` (str): Usuario actualmente activo.
- `_CurrentPws` (str): Contraseña actualmente activa.
- `_file_path` (str): Ruta del archivo donde se guardan los usuarios.

##### Métodos

- `__init__(self, Usrs: dict)`
  - **Descripción**: Inicializa la clase con un diccionario de usuarios y lee los datos desde el archivo.

- `Valida_Usuario(usr: str, pws: str) -> bool`
  - **Descripción**: Valida si el usuario y la contraseña son correctos.
  - **Parámetros**:
    - `usr`: Nombre de usuario.
    - `pws`: Contraseña.
  - **Retorno**: `True` si el usuario y la contraseña son válidos, de lo contrario `False`.

- `Obten_Datos_Usuario()`
  - **Descripción**: Obtiene los datos del usuario (usuario y contraseña) desde la entrada del usuario.

- `Agregar_a_lista()`
  - **Descripción**: Agrega el usuario actual a la lista de usuarios si no existe ya.

- `Borra_Usuario()`
  - **Descripción**: Borra el usuario actual de la lista de usuarios.

- `Muestra_Usuarios()`
  - **Descripción**: Muestra todos los usuarios almacenados en el diccionario.

- `Guarda_en_Archivo()`
  - **Descripción**: Guarda el diccionario de usuarios en un archivo JSON.

- `Lee_de_Archivo()`
  - **Descripción**: Lee el diccionario de usuarios desde un archivo JSON.

### Uso

1. **Inicialización**
   - Se inicializa el sistema con un diccionario vacío `myUsrs` y se crea una instancia de `CtrlUsr`.

2. **Interacción del Usuario**
   - El programa muestra un menú principal y permite al usuario seleccionar una acción.
   - Dependiendo de la acción seleccionada, se puede agregar un usuario, mostrar usuarios, iniciar sesión, guardar en archivo, leer de archivo o salir del programa.

3. **Persistencia**
   - Los usuarios se almacenan en un archivo `usuarios.json` para su persistencia entre ejecuciones del programa.

## Ejemplo de Uso

Al ejecutar el programa, el usuario verá el menú principal. Puede seleccionar una opción ingresando el número correspondiente. Por ejemplo, para agregar un usuario, el usuario seleccionaría la opción 1, luego ingresaría el nombre de usuario y la contraseña cuando se le solicite.

```bash
################# Menú #################
Escriba la acción a realizar (número) ó 'S' para Salir
	1. Agregar Usuario
	2. Mostrar Usuarios
	3. Login
	4. Guardar Usuarios a Archivo
	5. Leer Usuarios desde Archivo

Acción: 1
Usuario: joe
Contraseña: pa$$w0rd

Usuario: joe se ha agregado.

################# Menú #################
Escriba la acción a realizar (número) ó 'S' para Salir
	1. Agregar Usuario
	2. Mostrar Usuarios
	3. Login
	4. Guardar Usuarios a Archivo
	5. Leer Usuarios desde Archivo

Acción: 2
Usuario: joe, Contraseña: pa$$w0rd
Usuario: arthus, Contraseña: yeah!!
