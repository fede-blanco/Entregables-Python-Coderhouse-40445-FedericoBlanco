import json
from pathlib import Path


class FileManager:
    def __init__(self) -> None:
        #Se pone .parent.parent para que el archivo se cree en la carpeta raiz
        BASE_DIR = Path(__file__).resolve().parent.parent
        self.file_path = BASE_DIR / "database.json"

    def read_file(self) -> dict | None:
        if self.file_path.exists():
            try:
                with open(self.file_path, encoding="UTF-8") as file:
                  data = json.load(file)
                  return data
            except json.JSONDecodeError:
                print("El archivo existe pero tiene errores")
                return
        else:
            print("El archivo de la base de datos no existe.")
            print("Se crea el archivo", self.file_path)
            data = {}
            data['users']: list = []
            with open(self.file_path, "w",encoding="UTF-8") as file:
               json.dump(data,file,indent=4,ensure_ascii=False) 


    def save_file(self, data) -> None:
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4,ensure_ascii=False)
