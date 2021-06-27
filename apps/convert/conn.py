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

    def conversion(self, dataset):
        command = f"""
        SELECT (rate * {dataset[0]}), end FROM CONVERSIONS
        WHERE start = '{dataset[1]}';
        """
        return self.execute(command)[0]
