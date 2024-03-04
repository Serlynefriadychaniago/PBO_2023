import bcrypt
# filename : Users.py
from db import DBConnection as mydb
class Users:
    def __init__(self):
        self.__ID=None
        self.__EMAIL=None
        self.__nama=None
        self.__password=None
        self.__level=None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None    
    
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def ID(self):
        return self.__ID
    @property
    def EMAIL(self):
        return self.__EMAIL
        
    @EMAIL.setter
    def EMAIL(self, value):
        self.__EMAIL = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def password(self):
        return self.__password
        
    @password.setter
    def password(self, value):
        self.__password = value
    @property
    def level(self):
        return self.__level
        
    @level.setter
    def level(self, value):
        self.__level = value
    def cekUsername(self, EMAIL):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE EMAIL='" + EMAIL + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__ID = self.result[0]
           self.__EMAIL = self.result[1]
           self.__nama = self.result[2]
           self.__password = self.result[3]
           self.__level = self.result[4]
           self.affected = self.conn.cursor.rowcount
           self.__uservalid = True
        else:
           self.__ID = ''
           self.__EMAIL = ''
           self.__nama = ''
           self.__password = ''
           self.__level = ''
           self.affected = 0
           self.__uservalid = False
        return self.__uservalid
    def cekPassword(self, password):
        hashedpass=self.__password.encode('utf-8')
        c = password.encode('utf-8')
        d = bcrypt.checkpw(c, hashedpass)
        if(d):
            self.__passwordvalid=True
        else:
            self.__passwordvalid=False
        return self.__passwordvalid
    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if(a==True):
            b = self.cekPassword(password)
            if(b==True):
                self.__loginvalid=True
            else:
                self.__loginvalid=False
        else:
            self.__loginvalid=False
        
        val = []
        val = [self.__level, self.__loginvalid]
        return val
    def simpan(self):
        self.conn = mydb()
        val = (self.__EMAIL,self.__nama,self.__password,self.__level)
        sql="INSERT INTO Users (EMAIL,nama,password,level) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__EMAIL,self.__nama,self.__password,self.__level, id)
        sql="UPDATE users SET EMAIL = %s,nama = %s,password = %s,level = %s WHERE ID=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByEMAIL(self, EMAIL):
        self.conn = mydb()
        val = (self.__nama,self.__password,self.__level, EMAIL)
        sql="UPDATE users SET nama = %s,password = %s,level = %s WHERE EMAIL=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM users WHERE ID='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByEMAIL(self, EMAIL):
        self.conn = mydb()
        sql="DELETE FROM users WHERE EMAIL='" + str(EMAIL) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM users WHERE ID='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__ID = self.result[0]
        self.__EMAIL = self.result[1]
        self.__nama = self.result[2]
        self.__password = self.result[3]
        self.__level = self.result[4]
        self.conn.disconnect
        return self.result
    def getByEMAIL(self, EMAIL):
        a=str(EMAIL)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM users WHERE EMAIL='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__ID = self.result[0]
           self.__EMAIL = self.result[1]
           self.__nama = self.result[2]
           self.__password = self.result[3]
           self.__level = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__ID = ''
           self.__EMAIL = ''
           self.__nama = ''
           self.__password = ''
           self.__level = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM users"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,nama FROM users"
        self.result = self.conn.findAll(sql)
        return self.result  