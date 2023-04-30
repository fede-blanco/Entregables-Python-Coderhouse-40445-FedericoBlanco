from .user import user


def login(user_login = None):
    if user_login:
        return user_login
    else:
        print("\n ***  ***  ***  LOGIN TO PROCEED  ***  ***  ***")
        searched_dni = input("\nIngrese DNI del usuario a loguear: ")
        searched_user = user.show_user(searched_dni)
        if searched_user:
            searched_password = input("\nIngrse la contraseña del usuario: ")
            if searched_password != searched_user.password:
                print("\n--> contraseña incorrecta")
                return False
        else:
            print("Usuario inexistente")
            return False
        
        print("\nLogin Exitoso!!\n")
        user_logged = f"{searched_user.name} {searched_user.last_name}"
        # print(f"{user_logged}")
        return user_logged