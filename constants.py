num_answers = 10
num_rows = 10
num_columns = 4
sezioni = ("Sezione 1", "Sezione 2", "Sezione 3", "Sezione 4")

categorie = {0: ("Cane", "Gatto"), 1: ("Auto", "Moto"),
             2: ("Quadro", "Scultura"), 3: ("Soleggiato", "Coperto")}


# Questi sono gli array di connessione tra le foto che ha scelto e le label.
# Ogni foto del questionario ha una label, e qui sostanzialmente abbiamo definito la label
# quindi se per es. le foto sono nell'ordine Cane, Cane, Gatto, nel questionario
# ci sarà nell'array la label "Cane", "Cane", "Gatto"
sezione1 = ("Cane", "Gatto", "Cane", "Gatto", "Cane",
            "Gatto", "Cane", "Gatto", "Cane", "Gatto",
            "Cane", "Gatto", "Cane", "Gatto", "Cane",
            "Gatto", "Cane", "Gatto", "Cane", "Gatto")

sezione2 = ("Auto", "Moto", "Auto", "Moto", "Auto",
            "Moto", "Auto", "Moto", "Auto", "Moto",
            "Auto", "Moto", "Auto", "Moto", "Auto",
            "Moto", "Auto", "Moto", "Auto", "Moto")

sezione3 = ("Quadro", "Scultura", "Quadro", "Scultura", "Quadro",
            "Scultura", "Quadro", "Scultura", "Quadro", "Scultura",
            "Quadro", "Scultura", "Quadro", "Scultura", "Quadro",
            "Scultura", "Quadro", "Scultura", "Quadro", "Scultura")

sezione4 = ("Soleggiato", "Coperto", "Soleggiato", "Coperto", "Soleggiato",
            "Coperto", "Soleggiato", "Coperto", "Soleggiato", "Coperto",
            "Soleggiato", "Coperto", "Soleggiato", "Coperto", "Soleggiato",
            "Coperto", "Soleggiato", "Coperto", "Soleggiato", "Coperto")


sezioni_label = (sezione1, sezione2, sezione3, sezione4)