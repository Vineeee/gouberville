import sqlite3
from sqlite3 import Error
import os
import os.path
import ctypes
 
def create_database(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def execute_import(database_name, sql_file):

    """ delete the old tables """
    if os.path.isfile(database_name):
        os.remove(database_name)

    """ create the tables """
    try:
        query = open(sql_file, 'r').read()
        sqlite3.complete_statement(query)
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.executescript(query)
    except Exception as e:
        MessageBoxW = ctypes.windll.user32.MessageBoxW
        errorMessage = database_name + ': ' + str(e)
        MessageBoxW(None, errorMessage, 'Error', 0)
        cursor.close()
        raise
    finally:
        conn.close()

def import_gouberville_paragraphe(file_name, database_name):
    lines = [line.rstrip('\n') for line in open(file_name)]
    
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        for line in lines:
            if line == '':
                continue
            cursor.execute("insert into TEXTE_PARAGRAPHES (paragraphe) values ('" + line.replace("'","''") + "')")
        conn.commit()
        cursor.close()
    except Exception as e:
        #MessageBoxW = ctypes.windll.user32.MessageBoxW
        errorMessage = database_name + ': ' + str(e)
        print(errorMessage)
        cursor.close()
        raise
    finally:
        conn.close()

 
if __name__ == '__main__':
    database_name = "/home/dev/workspaceConda/gouberville/gouberville.db"
    sql_file = "/home/dev/workspaceConda/gouberville/import.sql"
    texte_gouberville = "/home/dev/workspaceConda/gouberville/data/gouberville.txt"
    texte_gouberville2 = "/home/dev/workspaceConda/gouberville/data/gouberville2.txt"
    #create_database(database_name)
    #execute_import(database_name, sql_file)
    #import_gouberville_paragraphe(texte_gouberville, database_name)
    import_gouberville_paragraphe(texte_gouberville2, database_name)
    