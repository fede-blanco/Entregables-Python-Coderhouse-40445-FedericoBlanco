from db.database import Database
from .user import user
from .login import login


class userMenu:

    # def __init__(self) -> None:
    #     self.db = Database()

    @staticmethod
    def user_menu(user_login):
        # print(user_login)
        try:
            print("\n***** ***** *****   MENU DE USUARIO   ***** ***** *****\n")

            options = input(f"--> Inserte '1' para REGISTRAR USUARIO\n--> Inserte '2' para MODIFICAR USUARIO\n--> Inserte '3' para ELIMINAR USUARIO\n--> Inserte '4' para LISTAR USUARIOS\n--> Inserte 'enter' para regresar al MENU PRINCIPAL\n")

            if options == '1':
                user.create()
                # print("TERMINO CREATE, AHORA A GUARDAR -- 18 -- userMenu.py")
                Database().save_in_db()

            elif options == '2':
                user_login = login(user_login)
                # print(f" linea 24 -- userMenu.py --> {user_login}")
                if user_login == False:
                    print("Loguin Incorrecto")
                    return userMenu.user_menu(user_login)
                user.update(user_login)
                Database().save_in_db()
                # print(f" linea 30 -- userMenu.py --> {user_login}")
                return userMenu.user_menu(user_login)
            
            elif options == '3':
                user_login = login(user_login)
                if user_login == False:
                    print("Loguin Incorrecto")
                    return userMenu.user_menu(user_login)
                user.delete(user_login)
                Database().save_in_db()
                return userMenu.user_menu(user_login)
            
            elif options == '4':
                user.list_users()
                return userMenu.user_menu(user_login)

            elif options not in ("1", "2", "3", "4"):
                print("\nSALIENDO DEL MENU DE USUARIOS\n")

        except Exception as e:
            print(f"\nHubo un error en la funcion user_menu()", type(e).
            __name__)
        