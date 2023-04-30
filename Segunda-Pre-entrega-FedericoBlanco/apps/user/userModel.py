class userModel:
    def __init__(self, dni: str, name: str, last_name: str, email: str, password: str, subscribed: bool = False) -> None:
        self.dni = dni
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.subscribed = subscribed

    def __str__(self):
        return f'\n********************\nUser -->\n   DNI: {self.dni}\n   Name: {self.name} {self.last_name}\n   Email: {self.email}\n   Password: {self.password}\n   Subrscribed: {self.subscribed}\n********************\n'
    
