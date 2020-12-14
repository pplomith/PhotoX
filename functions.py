import numpy as np
from constants import num_answers, num_rows, num_columns, sezioni, sezioni_label


def user_management(data, categories, keys_answers, key_photos):

    i = 0
    users_dataset = []

    for d in data:

        # questo è l'utente che deve essere inserito
        user = {"Numero campione": i, "Categoria psicologica": ""}
        i += 1

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
        category_marks = np.array(category_marks)

        index = np.argmax(category_marks)
        user["Categoria psicologica"] = categories[index]

        users_dataset.append(user)

    return users_dataset


# funzione che divide gli utenti per categoria in modo da rendere più semplice svolgere i calcoli
# funzione che returna un dizionario di liste, dove ogni lista contiene dizionari
# le chiavi del dizionario principale sono i nomi delle categorie psicologiche
def users_division(users, cat_ps):

    users_by_category = {cat_ps[0]: [], cat_ps[1]: [], cat_ps[2]: [], cat_ps[3]: []}

    for user in users:
        users_by_category[user["Categoria psicologica"]].append(user)

    return users_by_category


# funzione che returna una lista di tuple, di foto
def photo_function(user):

    # una lista di tuple, dove ogni tupla è la selezione di foto per quell'utente
    photo_list_section = []
    for s in sezioni:
        photo_list_section.append(user[s])

    return photo_list_section


def probability_section(user, categorie, section_number):

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
        p_campioni_dict[categorie[i]] = sezione_label.count(categorie[i]) / num_answers

    return p_campioni_dict
