from Auto import Auto
from cursorDelPool import CursorDelPool
from logger_base import log
class AutoDAO:

    _SELECCIONAR = "SELECT * FROM Auto"
    _INSERAR = "INSERTAR INTO Auto(modelo,precio) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE Auto SET modelo=%s, precio=%s"
    _ELIMINAR = "DELETE FROM Auto WHERE idAuto=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            Autos =[]
            for r in registros:
                auto = Auto(r[0],r[1],r[2])
                Autos.append(auto)
            return Autos

    @classmethod
    def insertar(cls,auto):
        with CursorDelPool() as cursor:
            valores = (auto.modelo,auto.precio)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,auto):
        with CursorDelPool() as cursor:
            valores = (auto.modelo,auto.precio,auto.idAuto)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,auto):
        with CursorDelPool() as cursor:
            valores = (auto.idAuto)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    Auto1 = Auto(modelo="KIA",precio=250000.00)
    AutoInsertada = AutoDAO.actualizar(Auto1)
    log.debug(f"Auto Insertada{AutoInsertada}")
    #Actualizar
    Auto1 = Auto(id_Auto=1,modelo="Kia Rio",precio=150000.00)
    AutoActualizada = AutoDAO.actualizar(Auto1)
    log.debug(f"Persona actualizada{AutoActualizada}")
    #eliminar
    Auto1 = Auto(id_Auto=1)
    AutoEliminada = AutoDAO.eliminar(Auto1)
    log.debug(f"Auto Eliminada{AutoEliminada}")