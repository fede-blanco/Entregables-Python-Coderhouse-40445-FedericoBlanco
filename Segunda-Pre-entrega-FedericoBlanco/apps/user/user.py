from .userController import userController

class user:
    

    # def __init__(self) -> None:
    #     self.controller = userController()

    @staticmethod
    def create():
      dni = input("Introduzca DNI: ")
      searched_dni = userController.read_user(dni)
      if  searched_dni:
        return print(f"El usuario con el dni {searched_dni} ya existe en nuestra base de datos")
      name = input("Introduzca nombre de usuario: ")
      last_name = input("Introduzca apellido de usuario: ")
      email = input("Introduzca email: ")
      password = input("Introduzca su password: ")
      #Lo guardamos en la lista
      userController.register_user(dni,name,last_name,email,password)
      return ("---> Usuario creado exitosamente!!\n")
    
    @staticmethod
    def update(user_login):
       print("\n*************   MODIFICAR USUARIO  **************")
       print(f"Usuario logueado: {user_login}\n")
       dni = input("Introduce el dni del usuario a modificar: ")
       searched_user = userController.read_user(dni)
       if not searched_user:
          return print(f"No se encontro el usuario con dni {dni}")
       else:
          print("Ingrese valor o presione 'enter' para proseguir")
          update_name = input("Introduzca nuevo nombre de usuario: ")
          if update_name:
            new_name = update_name
          else:
             new_name = searched_user.name

          print("Ingrese valor o presione 'enter' para proseguir")
          update_last_name= input("Introduzca nuevo apellido de usuario: ")
          if update_last_name:
            new_last_name = update_last_name
          else:
             new_last_name = searched_user.last_name

          print("Ingrese valor o presione 'enter' para proseguir")
          update_email= input("Introduzca nuevo email de usuario: ")
          if update_email:
            new_email = update_email
          else:
             new_email = searched_user.email

          print("Ingrese valor o presione 'enter' para proseguir")
          update_password= input("Introduzca nuevo password de usuario: ")
          if update_password:
            new_password = update_password
          else:
             new_password = searched_user.password

          new_subscribed = searched_user.subscribed

          userController.update_user(dni,new_name,new_last_name,new_email,new_password, new_subscribed)

          return print(f"--> Usuario con dni {dni} modificado exitosamente!!")

    @staticmethod
    def delete(user_login):
       print("\n*************   ELIMINAR USUARIO  **************")
       print(f"Usuario logueado: {user_login}\n")


       dni = input("Introduce el dni del usuario a eliminar: ")
       searched_user = userController.read_user(dni)
       if not searched_user:
          return print(f"No se encontro el usuario con dni {dni}")
       else:
          userController.delete_user(dni)
          return print(f"\nusuario con dni {dni} eliminado exitosamente!!\n")

    @staticmethod
    def list_users():
       return userController.show_user_list()
    
    @staticmethod
    def show_user(searched_dni):
       return userController.read_user(searched_dni)


