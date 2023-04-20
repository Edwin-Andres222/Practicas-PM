from logger_base import log

class Persona:
    def __init__(self, idpersona = None, nombre=None, email=None, edad=None) -> None:
        self._idpersona = idpersona
        self._nombre = nombre
        self._edad = edad
        self._email = email
    
    def __str__(self) -> str:
        
        return f"""
        Id Persona: {self._idpersona}, Nombre: {self._nombre}, Email: {self._email}, Edad: {str(self._edad)}
        """
    
    @property
    def idPersona(self):
        return self._idpersona
    @idPersona.setter
    def idPersona(self, idpersona):
        self._idpersona = idpersona

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def Nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def Edad(self, edad):
        self._edad = edad

    @property
    def Email(self):
        return self._email
    @Email.setter
    def Email(self, email):
        self._email = email


if __name__ == "__main__":
    persona1 = Persona(1,"Edwin", "Edwin@gmail.com", 22)
    log.debug(persona1)