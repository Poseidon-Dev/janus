import sqlite3
from core import config

class ConversionConn:

    def __init__(self):
        self.conn = sqlite3.connect(config.DB_LOCATION)
        self.cur = self.conn.cursor()

    def execute(self, command):
        self.cur.execute(command)
        result = self.cur.fetchall()
        self.conn.close()
        return result

    def all(self):
        command = 'SELECT * FROM CONVERSIONS'
        return self.execute(command)

    def keys(self):
        command = 'SELECT DESCRIPTION FROM CONVERSION_NAMES'
        return self.execute(command)

    def conversion(self, dataset):
        command = f"""
        SELECT c.rate, c.end FROM CONVERSIONS as c
        JOIN conversion_names as cn
        ON cn.ref = c.start
        WHERE cn.description = '{dataset[1]}';
        """
        return self.execute(command)[0]
