
# filename : Pelanggan.py
from db import DBConnection as mydb
class Pelanggan:
    def __init__(self):
        self.__ID=None
        self.__NAMA_USER=None
        self.__JENIS_KELAMIN=None
        self.__EMAIL=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def ID(self):
        return self.__ID
    @property
    def NAMA_USER(self):
        return self.__NAMA_USER
        
    @NAMA_USER.setter
    def NAMA_USER(self, value):
        self.__NAMA_USER = value
    @property
    def JENIS_KELAMIN(self):
        return self.__JENIS_KELAMIN
        
    @JENIS_KELAMIN.setter
    def JENIS_KELAMIN(self, value):
        self.__JENIS_KELAMIN = value
    @property
    def EMAIL(self):
        return self.__EMAIL
        
    @EMAIL.setter
    def EMAIL(self, value):
        self.__EMAIL = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__NAMA_USER,self.__JENIS_KELAMIN,self.__EMAIL)
        sql="INSERT INTO Pelanggan (NAMA_USER,JENIS_KELAMIN,EMAIL) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__NAMA_USER,self.__JENIS_KELAMIN,self.__EMAIL, id)
        sql="UPDATE pelanggan SET NAMA_USER = %s,JENIS_KELAMIN = %s,EMAIL = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_USER(self, NAMA_USER):
        self.conn = mydb()
        val = (self.__JENIS_KELAMIN,self.__EMAIL, NAMA_USER)
        sql="UPDATE pelanggan SET JENIS_KELAMIN = %s,EMAIL = %s WHERE NAMA_USER=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pelanggan WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_USER(self, NAMA_USER):
        self.conn = mydb()
        sql="DELETE FROM pelanggan WHERE NAMA_USER='" + str(NAMA_USER) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pelanggan WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__ID = self.result[0]
        self.__NAMA_USER = self.result[1]
        self.__JENIS_KELAMIN = self.result[2]
        self.__EMAIL = self.result[3]
        self.conn.disconnect
        return self.result
    def getByNAMA_USER(self, NAMA_USER):
        a=str(NAMA_USER)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pelanggan WHERE NAMA_USER='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__ID = self.result[0]
           self.__NAMA_USER = self.result[1]
           self.__JENIS_KELAMIN = self.result[2]
           self.__EMAIL = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__ID = ''
           self.__NAMA_USER = ''
           self.__JENIS_KELAMIN = ''
           self.__EMAIL = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pelanggan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,JENIS_KELAMIN FROM pelanggan"
        self.result = self.conn.findAll(sql)
        return self.result 