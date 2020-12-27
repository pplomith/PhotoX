import gspread

from oauth2client.service_account import ServiceAccountCredentials
from constants import categorie
from functions import users_management, probability_section, users_division, valore_atteso_psyche

""" SETTAGGIO AMBIENTE """

# adesso dobbiamo creare uno scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
sheet = client.open("SondaggioProgetto").sheet1

""" INIZIO MANIPOLAZIONE DATI """

# data è una lista di dizionari dove ogni dizionario è un utente
data = sheet.get_all_records()

# in questo modo abbiamo una lista di chiavi esclusa quella relative alle informazioni cronologiche
keys = list(data[0].keys())[1:]

# categorie psicologiche
categorie_psicologiche = ("Leone", "Lontra", "Golden Retriever", "Castoro")

""" 
alla funzione passiamo come parametro i dati, le categorie, e tutte le chiavi
keys[1:] sono le chiavi relative alle risposte
keys[0] sono le domande relative alle foto scelte
"""

users = users_management(data, categorie_psicologiche, keys[4:], keys[0:4])
p = probability_section(users[0], categorie[3], 3)

# print("Probabilità di scegliere " + categorie[3][0] + ": ", p[categorie[3][0]])
# print("Probabilità di scegliere " + categorie[3][1] + ": ", p[categorie[3][1]])

users_by_category = users_division(users, categorie_psicologiche)

""" valori attesi per le diverse categorie """

valori_attesi_leone = valore_atteso_psyche(users_by_category, categorie_psicologiche[0], categorie)
#valori_attesi_lontra = valore_atteso_psyche(users_by_category, categorie_psicologiche[1], categorie)
#valori_attesi_retriever = valore_atteso_psyche(users_by_category, categorie_psicologiche[2], categorie)
#valori_attesi_castoro = valore_atteso_psyche(users_by_category, categorie_psicologiche[3], categorie)

"""
tupla_leoni = (str(valori_attesi_leone["Cane"]), str(valori_attesi_leone["Auto"]),
               str(valori_attesi_leone["Quadro"]), str(valori_attesi_leone["Soleggiato"]),
               str(valori_attesi_leone["Gatto"]), str(valori_attesi_leone["Moto"]),
               str(valori_attesi_leone["Scultura"]), str(valori_attesi_leone["Coperto"]),
               "Leone")

tupla_lontra = (str(valori_attesi_lontra["Cane"]), str(valori_attesi_lontra["Auto"]),
                str(valori_attesi_lontra["Quadro"]), str(valori_attesi_lontra["Soleggiato"]),
                str(valori_attesi_lontra["Gatto"]), str(valori_attesi_lontra["Moto"]),
                str(valori_attesi_lontra["Scultura"]), str(valori_attesi_lontra["Coperto"]),
                "Lontra")

tupla_retriever = (str(valori_attesi_retriever["Cane"]), str(valori_attesi_retriever["Auto"]),
                   str(valori_attesi_retriever["Quadro"]), str(valori_attesi_retriever["Soleggiato"]),
                   str(valori_attesi_retriever["Gatto"]), str(valori_attesi_retriever["Moto"]),
                   str(valori_attesi_retriever["Scultura"]), str(valori_attesi_retriever["Coperto"]),
                   "Golden Retriever")

tupla_castoro = (str(valori_attesi_castoro["Cane"]), str(valori_attesi_castoro["Auto"]),
                 str(valori_attesi_castoro["Quadro"]), str(valori_attesi_castoro["Soleggiato"]),
                 str(valori_attesi_castoro["Gatto"]), str(valori_attesi_castoro["Moto"]),
                 str(valori_attesi_castoro["Scultura"]), str(valori_attesi_castoro["Coperto"]),
                 "Castoro") 
"""