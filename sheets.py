import gspread

from oauth2client.service_account import ServiceAccountCredentials
from functions import user_management, probability_section, users_division
from constants import categorie

############ SETTAGGIO AMBIENTE #############

# adesso dobbiamo creare uno scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
sheet = client.open("SondaggioProgetto").sheet1

############ INIZIO MANIPOLAZIONE DATI ###############

# data è una lista di dizionari dove ogni dizionario è un utente
data = sheet.get_all_records()

# in questo modo abbiamo una lista di chiavi esclusa quella relative alle informazioni cronologiche
keys = list(data[0].keys())[1:]

# categorie psicologiche
categorie_psicologiche = ("Leone", "Lontra", "Golden Retriever", "Castoro")

# alla funzione passiamo come parametro i dati, le categorie, e tutte le chiavi
# keys[1:] sono le chiavi relative alle risposte
# keys[0] sono le domande relative alle foto scelte
users = user_management(data, categorie_psicologiche, keys[4:], keys[0:4])

p = probability_section(users[1], categorie[3], 3)
print(users[1])

print("Probabilità di scegliere " + categorie[3][0] + ": ", p[categorie[3][0]])
print("Probabilità di scegliere" + categorie[3][1] + ": ", p[categorie[3][1]])

users_by_category = users_division(users, categorie_psicologiche)

print(users_by_category["Leone"])
