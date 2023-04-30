
from db.database import Database
from apps.appMenu import appMenu

def main():
    try:
        Database().upload_db()
        appMenu()
    except Exception as e:
        print(f"\nHubo un error en la funcion main()", type(e).__name__)
    finally:
        print("\nFIN DEL PROGRAMA!!!")

main()