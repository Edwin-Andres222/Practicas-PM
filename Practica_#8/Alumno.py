# -Definir una clase usuario que contenga como atributos:
# Usuario, Contraseña, Rol, Nombre, CURP, Ciudad
class Alumno:
    def __init__(self) -> None:
        self._usuario='';
        self._password='';
        self._rol='';
        self._nombre='';
        self._curp='';
        self._ciudad='';
    @property
    #Lectura
    def Usuario(self):
        return self._usuario
    #Escritura
    @Usuario.setter
    def Usuario(self,a):
        self._usuario=a
    
    @property 
    #Lectura
    def Password(self):
        return self._password
    #Escritura
    @Password.setter
    def Password(self,a):
        self._password=a
    
    @property
    #Lectura
    def Rol(self):
        return self._rol
    #Escritura
    @Rol.setter
    def Rol(self,a):
        self._rol=a

    @property
    #Lectura
    def Nombre(self):
        return self._nombre
    #Escritura
    @Nombre.setter
    def Nombre(self,a):
        self._nombre=a

    @property
    #Lectura
    def Curp(self):
        return self._curp
    #Escritura
    @Curp.setter
    def Curp(self,a):
        self._curp=a

    @property
    #Lectura
    def Ciudad(self):
        return self._ciudad
    #Escritura
    @Ciudad.setter
    def Ciudad(self,a):
        self._ciudad=a

    #Metodos
    def AltaAlumno(self,u,p,r,n,curp,c):
        self.Usuario = u
        self.Password = p
        self.Rol = r
        self.Nombre = n
        self.Curp=curp
        self.Ciudad=c
        return "REGISTRADO CON EXITO"    
    
    
    
