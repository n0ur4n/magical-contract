name="dobby"
email="dobbythefreeelf"
phonenumber=441256

class magical_contact:
    def __init__(self,name,email,phonenumber) -> None:
        self.__name=name
        self.__email=email
        self.__phonenumber=phonenumber

    def get_name(self,name):
        return self.__name

    def get_email(self,email):
        return self.__email
    
    def get_phonenumber(self,phonenumber):
        return self.__phonenumber
    
    def set_email(self,email):
        self.__email=email

    def set_phonenumber(self,phonenumber):
        self.__phonenumber=phonenumber

    def describe(self):
        return f" name : {self.get_name()}, email: {self.get_email()} , phone number: {self.get_phonenumber()}"
dobby=magical_contact("Dobby","dobbythefreeelf@gmail.com","04452688")  