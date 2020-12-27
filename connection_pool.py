import mysql.connector
from sheets import tupla_leoni, tupla_lontra, tupla_retriever, tupla_castoro

connection = mysql.connector.connect(host="localhost", database="photoX",
                                     user="root", password="TaekwondoGym_99")

print(tupla_leoni)
print(tupla_lontra)
print(tupla_retriever)
print(tupla_castoro)

cursor = connection.cursor(prepared=True)

sql = """ UPDATE categoria set cane=%s, auto=%s, quadro=%s, soleggiato=%s, 
            gatto=%s, moto=%s, scultura=%s, coperto=%s WHERE nome=%s """

cursor.execute(sql, tupla_leoni)
cursor.execute(sql, tupla_lontra)
cursor.execute(sql, tupla_retriever)
cursor.execute(sql, tupla_castoro)
connection.commit()
