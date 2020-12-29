# Team PhotoX

# Team:
Emanuele Fittipaldi,
Emanuele Mezzi,
Paolo Plomitallo.

# Obiettivi del progetto:
Il team Photox si impegna nella progettazione e realizzazione di un programma web based caratterizzato da un'interfaccia che permetta all'utente di visualizzare una matrice di immagini che rispecchiano la categoria psicologica propria del suddetto che verrà individuata attraverso un questionario sottoposto al momento dell'iscrizione al sito.

# Fasi del progetto e Algoritmo: 

1) Individuare le categorie psicologiche all'interno delle quali incasellare i diversi utenti. Queste sono preesistenti(da decidere quali devono essere).
2) Individuare uno o più dataset di immagini.
3) Ciscuna immagine sarà ovviamente corrispondente a un precisa categoria. Questa categoria è rappresentata dal metadato abbinato all'immagine. L'estrazione      dei metadati potrà avvenire con: 
      - reti neurali, 
      - altri algoritmi (a condizione di trovare foto con metadati categorizzanti già stabiliti e solo da estrarre) 

4) A ciascuna profilo psicologico corrisponderà una differente proporzione nel numero di foto mostrate per ciasuna categoria

5) L'individuazione delle categorie di foto e delle proporzioni con le quali suddividere suddette foto da abbinare alle diverse categorie psicologiche sarà      suddivisa in due fasi: 
   
   1) Sottomissione di questionari a un determinato numero di persone (saranno probabilmente studenti e familiari). 
       I questionari saranno suddivisi in due parti: 
         - domande per stabilire la categoria psicologica del soggetto, 
         - selezione di un determinato numero di foto da parte del soggetto. In questa fase il soggetto sceglierà foto da 4 sezioni. Le 4 sezioni individuate                sono veicoli (auto e moto), animali (cani e gatti), paesaggi (soleggiati e nuvolosi) e opere (sculture e quadri)
   
   2) Per ciascuna categoria integrazione dei dati raccolti dai diversi utenti appartenenti a quella specifica categoria (questa fase è fondamentale per             capire i gusti preponderanti e non, di ciascuna categoria psicologica)

6)  L'utente che si iscriverà alla piattaforma risponderà alle medesime domande alle quali avranno risposto gli utenti profilati e in base a quelle risposte verrà catalogato e gli verranno mostrate immagini appartenenti alle categorie e nelle proporzioni categoriali individuate per quel profilo psicologico.

# Esempio: 

1) Si individuano 4 categorie psicologiche: leone, lontra, golden retrievers, castoro

2) Dataset di immagini: 
    - dataset di quadri e sculture
    - dataset di auto e moto
    - dataset di cani e gatti 
    - dataset di paesaggi nuvolosi e soleggiati
    
    Ogni dataset corrisponde a una sezione all'interno del questionario da un punto di vista di scelta di foto. 
 
3) Ogni immagine di questi dataset corrisponderà a una categoria, denotate da un metadata che sarà una stringa: 
    - immagini di quadri: metadato "quadro"
    - immagini di sculture: metadato "scultura"
    - immagini di moto: metadato "moto"
    - immagini di auto: metadato "auto"
    - immagini di cani: metadato "cane"
    - immagini di gatto: metadato "gatto"
    - immagini di paesaggi soleggiati: metadato "soleggiato"
    - immagini di paesaggi nuvolosi: metadato "coperto"
    
  Come sempre l'estrazione del metadato categoriale avverà con reti neurali oppure con altri algoritmi, dipendentemente dalle condizioni esplicate in           precedenza nella sezione # Fasi del progetto e Algoritmo sezione 3. 

4) Sottomissione dei questionari composti da domande e foto. Le foto per ciascuna sezione saranno mostrate in maniera equilibrata. Ad esempio per la prima sezione (animali) ci saranno 10 foto di gatti e 10 foto di cani. 

5) Gli utenti ai quali sarà sottoposto il questionario sono 100 di cui:   
    - 30 leoni
    - 50 lontre
    - 75 golden retrievers
    - 35 castori

6) Per ciascuna categoria adesso si individua un pattern comune nella selezione delle immagini: 
    - leoni: 60% immagini di quadri, 40% di sculture, 10% auto, 90% moto, 30% cani, 70% gatti, 20% soleggiato, 80% coperto
    - lontre: 50% immagini di quadri, 50% di sculture, 10% auto, 90% moto, 30% cani, 70% gatti, 20% soleggiato, 80% coperto
    - golden retriever: 60% immagini di quadri, 40% di sculture, 50% auto, 50% moto, 30% cani, 70% gatti, 40% soleggiato, 60% coperto
    - castori: 40% immagini di quadri, 60% di sculture, 50% auto, 50% moto, 70% cani, 30% gatti, 40% soleggiato, 60% coperto
    
7) L'utente Emanuele Fittipaldi nel registrarsi risponde al questionario e ricade nella categoria "golden retrievers" e quindi la matrice delle immagini sarà
formata per la categoria delle opere d'arte dal 60% di quadri e dal 40% di sculture 50% per moto e auto per la sezione veicoli, 30% cani e 70% gatti per la sezione animali e 40% soleggiato e 60% coperto per la sezione paesaggi. 


