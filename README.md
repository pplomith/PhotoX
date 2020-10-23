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
         - selezione di un determinato numero di foto da parte del soggetto. In questa fase nessuna categoria di foto sarà in maggioranza rispetto alle altre;            condivideranno tutte la stessa percentuale di foto di appartenenza  
   
   2) Per ciascuna categoria integrazione dei dati raccolti dai diversi utenti appartenenti a quella specifica categoria (questa fase è fondamentale per             capire i gusti preponderanti e non di ciascuna categoria psicologica)

6)  L'utente che si iscriverà alla piattaforma risponderà alle medesime domande alle quali avranno risposto gli utenti profilati in fase di progettazione e in     base a quelle risposte verrà catalogato e gli verranno mostrate immagini appartenenti alle categorie e nelle proporzioni categoriali individuate per quel     profilo psicologico 

# Esempio: 

1) Si individuano 5 categorie psicologiche: creativo, esecutivo, naturalista, scientifico, alternativo
2) Dataset di immagini: 
    - immagini di quadri 
    - immagini di moto 
    - immagini di auto
    - immagini di equazioni famose 
    - immagini di città
    - immagini di paesaggi naturali 
    - immagini di cibo 
 
3) Ogni immagini di questi dataset corrisponderà a una categoria, denotate da un metadata che sarà una stringa: 
    - immagini di quadri: metadato "quadro"
    - immagini di moto: metadato "moto"
    - "" auto: "" "auto"
    - "" equazioni famose: "" "equazione"
    - "" città: "" "città"
    - "" paesaggi naturali: "" "paesaggio"
    - "" cibo: "" "cibo"
    
  Come sempre l'estrazione del metadato categoriale avverà con reti neurali oppure con altri algoritmi, dipendentemente dalle condizioni esplicate in           precedenza nella sezione # Fasi del progetto e Algoritmo sezione 3. 

4) Sottomissione dei questionari composti da domande e foto. Le foto per ciascun utente saranno mostrate in maniera proporzionalmente equa relativamente alle    categorie di appartenenza. Dato che sono state individuate 7 categorie avremo che ciascuna categoria contribuirà con il 14.28% delle fotografie mostrate 

5) Gli utenti ai quali sarà sottoposto il questionario sono 200 di cui:   
    - 30 creativi 
    - 50 esecutivi 
    - 25 naturalisti 
    - 35 scientifici 
    - 60 alternativi

6) Per ciascuna categoria adesso si individua un pattern comune nella selezione delle immagini: 
    - creativi: 60% immagini di quadri, 20% immagini di cibo, 10% immagini di città, 10% immagini di auto
    - esecutivi: 70% immagini di equazioni famose, 5% immagini di moto, 15% immagini di auto
    - ... 
    - alternativi: 50% immagini di cibo, 30% immagini di città, 20% immagini di quadri 
    
7) L'utente Emanuele Fittipaldi nel registrarsi risponde al questionario e ricade nella categoria "creativo" e quindi la matrice delle immagini darà formata      al 60% di immagini di quadri, 20% di immagini di cibo, 10% immagini di città, 10% immagini di auto


