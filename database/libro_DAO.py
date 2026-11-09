from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""


class LibroDAO:
    def __init__(self):
        pass

    def get_tutti_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor()
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
        cursor.execute(query)

        result = []
        for row in cursor:
            result.append(row[0])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []

        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT DISTINCT l.* 
            FROM libro l
            LEFT JOIN possesso p ON l.id = p.id_libro
            WHERE (%s IS NULL OR p.id_biblioteca = %s)
              AND (%s IS NULL OR l.genere = %s)
        """
        cursor.execute(query, (id_biblioteca, id_biblioteca, genere, genere))

        result = []
        for row in cursor:
            result.append(Libro(**row))

        cursor.close()
        cnx.close()
        return result