
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user = 'root',
            passwd = '1234',
            db = 'monitoreo_trabajo'
            )
        self.cursor = self.connection.cursor()
        print('Conexion exitosa')
       

    