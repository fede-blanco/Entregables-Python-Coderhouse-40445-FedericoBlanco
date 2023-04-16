from pathlib import Path
import json

#Obtenemos la ruta de la carpeta padre del archivo donde estamos
BASE_DIR = Path(__file__).resolve().parent

# Se crea una variable con la ruta hacia el archivo .json
nombre_archivo_json = "dataUsuarios_primeraPreEntrega.json"
ruta_json = BASE_DIR / nombre_archivo_json

def inicializar_persistencia(ruta_json):
  if ruta_json.exists():
    with open(ruta_json, encoding="UTF-8") as archivo:
        #se carga lo que haya en el archivo en la variable data
        data = json.load(archivo)
        print(data)
        return data
  else:
    # Se crea un diccionario que sera el objeto con el contenido del json
    data = {}
    # Se crea la lista con la clave "usuarios" dentro del objeto data
    data['usuarios']: list[dict] = []
    print(data)
    return data
data = inicializar_persistencia(ruta_json)

def registrar_usuario(data):
    try:
        entrada_nombre: str
        entrada_contraseña: str
        entrada_nombre= input("\nIngrese su nombre de usuario: ")
        entrada_contraseña = input("\nIngrese su contraseña: ")
        usuario = { "nombre_usuario": entrada_nombre, "contraseña" : entrada_contraseña}
        data['usuarios'].append(usuario)

        # Asentamos la lista de usuarios registrados en nuestro archivo .json para darle persistencia al programa
        #Con "as" le asignamos un nombre de variable
        with open(ruta_json,"w",encoding="UTF-8") as archivo_json:
            json.dump(data,archivo_json,indent=4,ensure_ascii=False)

        return print(f"\nusuario registrado: {usuario}"), menu(data)
    
    except Exception as e:
        print(f"\nHubo un error en la funcion registrar_ursuario", type(e).__name__)


def registrar_primer_usuario(data):
  try:
    
    inicio = input("\nIndique si quiere registrar un nuevo usuario (s/n): ")
    if inicio.lower() == "s":
      return registrar_usuario(data)
    elif inicio.lower() == "n":
      return print("\nAdios, vuelve pronto!!"), menu(data)
    else:
      print("No se ingreso una respuesta valida --> 's' o 'n'")
      return registrar_primer_usuario(data)
  except Exception as e:
    print(f"\nHubo un error en la funcion registrar_primer_ursuario", type(e).__name__)


def registrar_otro_usuario(data):
  try:
    inicio = input("\nIndique si quiere registrar otro usuario (s/n): ")
    if inicio.lower() == "s":
      registrar_usuario(data)
      registrar_otro_usuario(data)
    elif inicio.lower() == "n":
      return print("\nAdios, vuelve pronto!!"), menu(data)
    else:
      print("\nNo se ingreso una respuesta valida --> 's' o 'n'")
      return registrar_otro_usuario(data)
  except Exception as e:
    print(f"\nHubo un error en la funcion registrar_otro_ursuario", type(e).__name__)


def mostrar_usuarios(data):
  try:
    return print(f"\n{data}")
  except Exception as e:
    print(f"Hubo un error en la funcion mostrar_ursuario", type(e).__name__)

def login_usuarios(data):
    try:
        usuarios = data['usuarios']
        
        if len(usuarios) > 0:
            usuario_ingresado_login: str
            contraseña_ingresada_login: str
            usuario_ingresado_login = input(f"\nIngrese Nombre de usuario para login: ")
            contraseña_ingresada_login = input(f"\nIngrese contraseña para login: ")
            usuario_logueado = None
            for usuario in usuarios:
                if usuario['nombre_usuario'] == usuario_ingresado_login and usuario['contraseña'] == contraseña_ingresada_login:
                      usuario_logueado = usuario
                      return print(f"\nLogin exitoso!! Bienvenido {usuario_logueado['nombre_usuario']} !!"), usuario_logueado, menu(data)
                else:
                   pass
            if not usuario_logueado:
                return print(f"\nEl usuario o la contraseña no coinciden con alguno de nuestra base de datos"), menu(data)
            
        else:
            return print("\nNo hay usuarios registrados en la base de datos aun")
      
    except Exception as e:
      print(f"Hubo un error en la funcion login_usuarios", type(e).__name__)
       

def menu(data):
  try:
      registrar_o_login = input(f"\n--> Para registrar un usuario inserte el numero '1'\n--> Para realizar un login inserte el numero '2'\n--> Para salir inserte el numero '3'\n ")
      if registrar_o_login == "1":
          registrar_primer_usuario(data)
          mostrar_usuarios(data)
      elif registrar_o_login == "2":
          login_usuarios(data)
      elif registrar_o_login == "3":
          return print(f"\nAdios!!!")
      elif registrar_o_login not in ("1", "2", "3"):
         print("\nIngresaste un dato invalido, prueba nuevamente: \n")
         return menu(data)
  except Exception as e:
      print(f"\nHubo un error en la funcion menu()", type(e).__name__)
   


def main(data):
  try:
     menu(data)
  except Exception as e:
      print(f"\nHubo un error en la funcion main", type(e).__name__)
  finally:
     print("\nFIN DEL PROGRAMA!!!")


main(data)