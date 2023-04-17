from Bebida import Bebida
from cursorDelPool import CursorDelPool
from logger_base import log
class BebidaDAO:

    _SELECCIONAR = "SELECT * FROM Bebida"
    _INSERAR = "INSERTAR INTO Bebida(Nombre,Precio) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE Bebida SET Nombre=%s, Precio=%s"
    _ELIMINAR = "DELETE FROM Bebida WHERE idBebida=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            bebidas =[]
            for r in registros:
                bebida = Bebida(r[0],r[1],r[2])
                bebidas.append(bebida)
            return bebidas

    @classmethod
    def insertar(cls,bebida):
        with CursorDelPool() as cursor:
            valores = (bebida.Nombre,bebida.Precio)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,bebida):
        with CursorDelPool() as cursor:
            valores = (bebida.Nombre,bebida.Precio,bebida.idBebida)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,bebida):
        with CursorDelPool() as cursor:
            valores = (bebida.idbebida)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    bebida1 = Bebida(nombre="Pepsi",precio=25.50)
    bebidaInsertada = BebidaDAO.actualizar(bebida1)
    log.debug(f"Bebida Insertada{bebidaInsertada}")
    #Actualizar
    bebida1 = Bebida(id_Bebida=1,nombre="Pepsi Cola",precio=20.00)
    bebidaActualizada = BebidaDAO.actualizar(bebida1)
    log.debug(f"Persona actualizada{bebidaActualizada}")
    #eliminar
    bebida1 = Bebida(id_Bebida=1)
    bebidaEliminada = BebidaDAO.eliminar(bebida1)
    log.debug(f"Bebida Eliminada{bebidaEliminada}")