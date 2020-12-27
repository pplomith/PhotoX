import numpy as np
import random
from constants import num_answers, num_rows, num_columns, sezioni, sezioni_label


def users_management(data, categories, keys_answers, key_photos):

    users_dataset = []

    for i, d in enumerate(data):

        # questo è l'utente che deve essere inserito
        user = {"Numero campione": i, "Categoria psicologica": ""}

        # grazie a questo ciclo per ogni sezione di foto si crea una tupla contente gli interi
        for s in range(0, 4):
            photos_section = d[key_photos[s]].split(", ")
            for h in range(0, num_answers):
                photos_section[h] = int(photos_section[h])

            user[sezioni[s]] = tuple(photos_section)

        answers = []
        for key in keys_answers:
            answers.append(d[key])

        # trasformiamo la lista di risposte in un numpy array e lo modifichiamo rendendolo
        # una matrice con n_rows = 10  e n_columns = 4
        answers = np.array(answers)
        answers.shape = (num_rows, num_columns)

        # si sommano i valori di ciascuna colonna per vedere i punteggi per ciascuna categoria
        category_marks = answers.sum(axis=0)

        user["Categoria psicologica"] = categories[manage_same_value(category_marks)]
        users_dataset.append(user)

    return users_dataset


# funzione che gestisce il caso in cui ci siano colonne con lo stesso valore
def manage_same_value(category_marks):
    occorrenze_max = category_marks.tolist().count(np.max(category_marks))
    indexes = []

    if occorrenze_max > 1:
        max = np.max(category_marks)
        for i in range(0, category_marks.size):
            if category_marks[i] == max:
                indexes.append(i)

        index = random.choice(indexes)

    else:
        index = np.argmax(category_marks)

    return index


"""
funzione che divide gli utenti per categoria psicologica in modo da rendere più 
semplice svolgere i calcoli. 
funzione che returna un dizionario di liste, dove ogni lista contiene dizionari
le chiavi del dizionario principale sono i nomi delle categorie psicologiche
"""


def users_division(users, cat_ps):
    users_by_category = {cat_ps[0]: [], cat_ps[1]: [], cat_ps[2]: [], cat_ps[3]: []}

    for user in users:
        users_by_category[user["Categoria psicologica"]].append(user)

    return users_by_category


""" 
presi in input tutti gli utenti, la categoria psicologica di interesse 
e le categorie di foto calcola il valore atteso per ciascuna categoria 
di foto, per la categoria psicologica scelta 
"""


def valore_atteso_psyche(users_by_category, cat_psicologica, categorie_photo):
    # una volta calcolata la probabilità per una categoria possiamo calcolare i valori attesi
    dict_psyche = probability_psyche_category(users_by_category, cat_psicologica, categorie_photo)

    print(dict_psyche)
    print(dict_psyche.keys())

    # dict_psyche è un dizionario di liste
    # rimuoviamo i duplicati e poi contiamo quante volte ogni elemento è contenuto lì dentro
    # questa lista contiene i valori attesi per i cani, le auto, i quadri e il cielo soleggiato

    dict_first = {"Cane": [], "Auto": [], "Quadro": [], "Soleggiato": []}
    keys_dict = list(dict_first.keys())

    """
    il dizionario prodotto con questo ciclo contiene le percentuali di scelta per tutti gli utenti di quella
    categoria psicologica per le label di "Cane", "Auto", "Quadro" e "Soleggiato"
    """
    for key in dict_psyche.keys():
        for i in range(0, 4):
            dict_first[keys_dict[i]].append(dict_psyche[key][i][keys_dict[i]])

    print(dict_first)

    """
    ora dobbiamo togliere i duplicati dalla lista per ciascuna categoria di foto. 
    Possiamo scegliere qualiasi tipo di struttura dati. Optiamo per un dizionario 
    di insiemi. La funzione set() toglie automaticamente i duplicati. 
    """
    dict_support = {"Cane": {}, "Auto": {}, "Quadro": {}, "Soleggiato": {}}
    for key in dict_first.keys():
        dict_support[key] = set(dict_first[key])

    print(dict_support)

    """
    adesso creaimo un dizionario che per le categorie di foto "Cane", "Auto", "Quadro", "Soleggiato", 
    scrive quanto è probabile che gli utenti di quella categoria ne abbiana selezionato una certa percentuale 
    di foto. 
    """
    dict_quantity_prob = {"Cane": {}, "Auto": {}, "Quadro": {}, "Soleggiato": {}}
    for key in dict_support.keys():
        for e in list(dict_support[key]):
            dict_quantity_prob[key][e] = dict_first[key].count(e) / len(dict_first[key])

    print(dict_quantity_prob)

    """
    a questo punto non resta altro che andare ad applicare la formula dei valore atteso, per 
    ciascuna categoria di foto "Cane", "Auto", "Quadro", "Soleggiato". 
    E(X) = p(x1) * x1 + ... + p(xn) * xn, che nel caso specifico sarà. Quindi calcoliamo 
    E(Cane), E(Auto), E(Quadro) ed E(Soleggiato). 
    """
    dict_valori_attesi = {"Cane": 0, "Auto": 0, "Quadro": 0, "Soleggiato": 0, "Gatto": 0, "Moto": 0, "Scultura": 0,
                          "Coperto": 0}
    i = 4
    l1 = list(dict_valori_attesi.keys())
    for key in dict_quantity_prob.keys():
        for key1 in dict_quantity_prob[key].keys():
            print(dict_quantity_prob[key][key1], key1)
            dict_valori_attesi[key] += (dict_quantity_prob[key][key1] * key1)
            dict_valori_attesi[key] = round(dict_valori_attesi[key], 1)
            dict_valori_attesi[l1[i]] = round(1 - dict_valori_attesi[key], 1)

        i += 1

    print(dict_valori_attesi)

    return dict_valori_attesi


""" 
presi in input gli utenti classificati in una determinata categoria, la categoria psicologica e le 
categorie di foto la funzione calcola le probabilità per ciascuna sezione per gli utenti di una categoria determinata 
"""

def probability_psyche_category(users_by_category, cat_psicologica, categorie_photo):

    """
    dizionario che indirizza gli utenti per numero campione. Il dizionario per ciascun utente contiene
    una lista che a sua volta contiene le probabilità di scelta per quell'utente, per le diverse categorie
    di foto
    """
    dict_camp = {}
    for user in users_by_category[cat_psicologica]:
        dict_camp[user["Numero campione"]] = []

    """
    lista di probabilità per un utente 
    """
    probability = []
    for user in users_by_category[cat_psicologica]:
        for i in range(0, 4):
            probability.append(probability_section(user, categorie_photo[i], i))

        dict_camp[user["Numero campione"]] = probability
        probability = []

    return dict_camp


""" 
preso in input un utente, le categorie di foto, il numero della sezione di scelta del questionario 
calcola le probabilità per un solo utente, per una categoria per quella sezione sezione 
"""


def probability_section(user, categorie_foto, section_number):
    # lista di foto per la sezione desiderata
    photos = photo_function(user)[section_number]

    # modifichiamo gli indici facendoli partire da 0
    sezione_photos = []
    for i in photos:
        sezione_photos.append(i - 1)

    # memorizzazione delle label corrispondenti alle foto scelte
    sezione_label = []
    for s in sezione_photos:
        sezione_label.append(sezioni_label[section_number][s])
        
    p_campioni_dict = {}
    for i in range(0, 2):
        p_campioni_dict[categorie_foto[i]] = sezione_label.count(categorie_foto[i]) / num_answers

    return p_campioni_dict


"""
dato in input un utente returna una lista di tuple, dove ognu tupla 
è l'elenco di foto che è stato scelto dall'utente
"""


def photo_function(user):
    photo_list_section = []

    for s in sezioni:
        photo_list_section.append(user[s])

    return photo_list_section
