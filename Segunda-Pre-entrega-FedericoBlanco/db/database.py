from .fileManager import FileManager
from apps.user.userModel import userModel
from apps.user.userController import userController

class Database:
    
    def __init__(self) -> None:
        self.file_manager = FileManager()

    def upload_db(self):
        try:   
          # print(" COMIENZA upload_db() -- 12 database.py")
          data = self.file_manager.read_file()
          # print("upload_db() -- 14 database.py")
          if data:
            if data.get('users'):
                for user_data in data['users']:
                    user = userModel(**user_data)
                    userController().upload_user(user)
            # print("upload_db() -- 20 database.py")
        except Exception as e:
          print(f"\nHubo un error en la funcion upload_db()", type(e).__name__)

  
    def save_in_db(self) -> None:
        # print("19 -- database.py")
        data = {}
        if userController.user_list:
            # print("22 -- database.py")
            data["users"] = []
            for user in userController.user_list:
                data["users"].append(user.__dict__)
                # print("DATA guardada en lista --> 24 database.py")
                # print(data["users"])
        self.file_manager.save_file(data)