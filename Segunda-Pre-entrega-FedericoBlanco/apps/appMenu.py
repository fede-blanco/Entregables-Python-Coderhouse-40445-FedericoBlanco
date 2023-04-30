from .user.userMenu import userMenu

def appMenu():
    try:
        print("\n*****  *****  *****  MENU PRINCIPAL  *****  *****  *****\n")

        select_menu = input(f"--> Inserte '1' para MENU DE USUARIOS\n--> Inserte '2' para MENU DE PRODUCTOS\n--> Inserte 'enter' para SALIR DE LA APLICACION\n")

        user_login = False

        if select_menu == "1":
            userMenu.user_menu(user_login)
            appMenu()
        elif select_menu == "2":
            print("PRODUCTS MENU selected")
            appMenu()
        elif select_menu not in ("1", "2"):
            print("Saliendo de la aplicacion...")
        return
    except Exception as e:
        print(f"\nHubo un error en la funcion AppMenu()", type(e).__name__)