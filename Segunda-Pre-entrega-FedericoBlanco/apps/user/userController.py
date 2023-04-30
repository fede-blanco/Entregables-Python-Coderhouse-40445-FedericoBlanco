from .userModel import userModel

class userController:
    
    user_list: list[userModel] = []

    def __init__(self):
        self.model = userModel

    def __repr__(self) -> str:
        return f'\n********************\nUser -->\n   DNI: {self.dni} ---   Name: {self.name} {self.last_name} ---  Email: {self.email} ---   Subrscribed: {self.subscribed}\n********************'

    @staticmethod
    def register_user(dni:str, name:str, last_name:str, email:str, password:str):
        new_user = userModel(dni, name, last_name, email, password)
        userController.user_list.append(new_user)

        print(new_user)
        # print("Append exitoso -- 19 userController.py")
        # print("---> Usuario registrado satisfactoriamente\n")

    @staticmethod
    def upload_user(user: userModel):
        userController.user_list.append(user)

    @staticmethod
    def update_user(searched_dni: str, name:str, last_name:str, email:str, password:str, subscribed:bool):
        for user in userController.user_list:
            if user.dni == searched_dni:
                user.name = name
                user.last_name = last_name
                user.email = email
                user.password= password
                user.subscribed = subscribed
                # print("---> Usuario modificado satisfactoriamente\n")
                return
        return print(f"El usuario con el DNI {searched_dni} no se puede modificar - no existe en nuestra base de datos\n")

    @staticmethod
    def delete_user(searched_dni: str):
        for user in userController.user_list:
            if user.dni == searched_dni:
                userController.user_list.remove(user)
                # print(f"---> Usuario con dni {searched_dni} eliminado satisfactoriamente")
                return
        return print(f"El usuario con el DNI {searched_dni} no existe en la base de datos\n")
                             
    @staticmethod
    def read_user(searched_dni: str):
        for user in userController.user_list:
            if user.dni == searched_dni:
                # print(user)
                return user
        return print(f"El usuario con el DNI {searched_dni} no existe en la base de datos\n")
    
    @staticmethod
    def show_user_list():
        if userController.user_list:
            print("\n**********  LISTA DE USUARIOS  **************")
            for user in userController.user_list:
                print(f'User -->\n   DNI: {user.dni}  ---   Name: {user.name} {user.last_name}  ---  Email: {user.email}  ---   Password: {user.password}  ---  Subrscribed: {user.subscribed}')
            print("********************************************\n")
        else:
            False

