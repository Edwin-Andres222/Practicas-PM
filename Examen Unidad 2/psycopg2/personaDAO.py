from persona import Persona
from cursorDelPool import CursorDelPool
from logger_base import log

class PersonaDAO:

    _SELECCIONAR= "SELECT * FROM persona ORDER BY id"
    _INSERTAR = "INSERT INTO persona(id, nombre, edad, correo) VALUES (%s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre = %s, edad = %s, correo = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.idPersona, persona.Nombre, persona.Edad, persona.Email)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad, persona.Email, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,persona):
        with CursorDelPool as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    persona1 = Persona(5,nombre="Jesus", edad="21",email="jesus@gmail.com")
    personasInsertadas = PersonaDAO.insertar(persona1)
    persona2 = Persona(6,nombre="Edwin", edad="22",email="Edwin@hotmail.com")
    personasInsertadas = PersonaDAO.insertar(persona2)
    log.debug(f"Personas Agregadas: {personasInsertadas}")
    #Leer
    personas = PersonaDAO.seleccionar()
    for p in personas:
        log.debug(p)