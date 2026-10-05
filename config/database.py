import sqlite3
from sqlite3 import Connection, Cursor


class database:
    """
    Clase que gestiona la conexion a la base de datos implementando
    el patron singleton para evitar multiples instancias innecesarias.
    """
    _instance = None
    _db_path = "clinica.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(database, cls).__new__(cls)
        return cls._instance


    def get_connection(self)-> connection:
        """
        Retorna una conexion ala base dedatos sqlite.
        """
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row #Permite acceder a las columnas por nombre
        return conn



    def init_db(self) -> None:
        """
        inicializa la base de datos creando las tablas necesarias si noexisten
        """
        conn = self.get_connection()
        try:
            cursor: Cursor = conn.cursor()

            #tabla departamento

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento  (
                id_departamento integer primary key autoincrement,
                nombre TEXT NOT NULL,
                piso integer not null
                )
            """)
            #tabla paciente
            cursor.execute("""
               CREATE TABLE IF NOT EXISTS paciente (
               rut text primary key,
               nombre text not null,
               edad integer not null,
               prevision text not null,
               id_departamento integer,
               foreign key(id_departamento) references departamento(id_departamento) on delete set null
               )
            """)


            conn.commit()
        except sqlite3.Error as e:
            print(f"error al inicializar la base de datos: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    db = database()
    db.init_db()
    print("Base de datos inicializada correctamente")