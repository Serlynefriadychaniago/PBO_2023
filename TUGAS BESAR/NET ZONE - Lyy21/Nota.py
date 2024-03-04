
# filename : Nota.py
from db import DBConnection as mydb
class Nota:
    def __init__(self):
        self.__ID=None
        self.__NAMA_USER=None
        self.__ID_KOMPUTER=None
        self.__TANGGAL=None
        self.__JAM_MULAI=None
        self.__JAM_SELESAI=None
        self.__LAMA_WAKTU=None
        self.__TARIF_PER_JAM=None
        self.__TOTAL_BAYAR=None
        self.__STATUS_BAYAR=None
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
    def ID_KOMPUTER(self):
        return self.__ID_KOMPUTER
        
    @ID_KOMPUTER.setter
    def ID_KOMPUTER(self, value):
        self.__ID_KOMPUTER = value
    @property
    def TANGGAL(self):
        return self.__TANGGAL
        
    @TANGGAL.setter
    def TANGGAL(self, value):
        self.__TANGGAL = value
    @property
    def JAM_MULAI(self):
        return self.__JAM_MULAI
        
    @JAM_MULAI.setter
    def JAM_MULAI(self, value):
        self.__JAM_MULAI = value
    @property
    def JAM_SELESAI(self):
        return self.__JAM_SELESAI
        
    @JAM_SELESAI.setter
    def JAM_SELESAI(self, value):
        self.__JAM_SELESAI = value
    @property
    def LAMA_WAKTU(self):
        return self.__LAMA_WAKTU
        
    @LAMA_WAKTU.setter
    def LAMA_WAKTU(self, value):
        self.__LAMA_WAKTU = value
    @property
    def TARIF_PER_JAM(self):
        return self.__TARIF_PER_JAM
        
    @TARIF_PER_JAM.setter
    def TARIF_PER_JAM(self, value):
        self.__TARIF_PER_JAM = value
    @property
    def TOTAL_BAYAR(self):
        return self.__TOTAL_BAYAR
        
    @TOTAL_BAYAR.setter
    def TOTAL_BAYAR(self, value):
        self.__TOTAL_BAYAR = value
    @property
    def STATUS_BAYAR(self):
        return self.__STATUS_BAYAR
        
    @STATUS_BAYAR.setter
    def STATUS_BAYAR(self, value):
        self.__STATUS_BAYAR = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__NAMA_USER,self.__ID_KOMPUTER,self.__TANGGAL,self.__JAM_MULAI,self.__JAM_SELESAI,self.__LAMA_WAKTU,self.__TARIF_PER_JAM,self.__TOTAL_BAYAR,self.__STATUS_BAYAR)
        sql="INSERT INTO Nota (NAMA_USER,ID_KOMPUTER,TANGGAL,JAM_MULAI,JAM_SELESAI,LAMA_WAKTU,TARIF_PER_JAM,TOTAL_BAYAR,STATUS_BAYAR) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__NAMA_USER,self.__ID_KOMPUTER,self.__TANGGAL,self.__JAM_MULAI,self.__JAM_SELESAI,self.__LAMA_WAKTU,self.__TARIF_PER_JAM,self.__TOTAL_BAYAR,self.__STATUS_BAYAR, id)
        sql="UPDATE nota SET NAMA_USER = %s,ID_KOMPUTER = %s,TANGGAL = %s,JAM_MULAI = %s,JAM_SELESAI = %s,LAMA_WAKTU = %s,TARIF_PER_JAM = %s,TOTAL_BAYAR = %s,STATUS_BAYAR = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA_USER(self, NAMA_USER):
        self.conn = mydb()
        val = (self.__ID_KOMPUTER,self.__TANGGAL,self.__JAM_MULAI,self.__JAM_SELESAI,self.__LAMA_WAKTU,self.__TARIF_PER_JAM,self.__TOTAL_BAYAR,self.__STATUS_BAYAR, NAMA_USER)
        sql="UPDATE nota SET ID_KOMPUTER = %s,TANGGAL = %s,JAM_MULAI = %s,JAM_SELESAI = %s,LAMA_WAKTU = %s,TARIF_PER_JAM = %s,TOTAL_BAYAR = %s,STATUS_BAYAR = %s WHERE NAMA_USER=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM nota WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA_USER(self, NAMA_USER):
        self.conn = mydb()
        sql="DELETE FROM nota WHERE NAMA_USER='" + str(NAMA_USER) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM nota WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__ID = self.result[0]
        self.__NAMA_USER = self.result[1]
        self.__ID_KOMPUTER = self.result[2]
        self.__TANGGAL = self.result[3]
        self.__JAM_MULAI = self.result[4]
        self.__JAM_SELESAI = self.result[5]
        self.__LAMA_WAKTU = self.result[6]
        self.__TARIF_PER_JAM = self.result[7]
        self.__TOTAL_BAYAR = self.result[8]
        self.__STATUS_BAYAR = self.result[9]
        self.conn.disconnect
        return self.result
    def getByNAMA_USER(self, NAMA_USER):
        a=str(NAMA_USER)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM nota WHERE NAMA_USER='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__ID = self.result[0]
           self.__NAMA_USER = self.result[1]
           self.__ID_KOMPUTER = self.result[2]
           self.__TANGGAL = self.result[3]
           self.__JAM_MULAI = self.result[4]
           self.__JAM_SELESAI = self.result[5]
           self.__LAMA_WAKTU = self.result[6]
           self.__TARIF_PER_JAM = self.result[7]
           self.__TOTAL_BAYAR = self.result[8]
           self.__STATUS_BAYAR = self.result[9]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__ID = ''
           self.__NAMA_USER = ''
           self.__ID_KOMPUTER = ''
           self.__TANGGAL = ''
           self.__JAM_MULAI = ''
           self.__JAM_SELESAI = ''
           self.__LAMA_WAKTU = ''
           self.__TARIF_PER_JAM = ''
           self.__TOTAL_BAYAR = ''
           self.__STATUS_BAYAR = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM nota"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,ID_KOMPUTER FROM nota"
        self.result = self.conn.findAll(sql)
        return self.result 