class Ristorante:
    def __init__(self, nome, tipo_cucina): # Inizializzazione della classe dove vengono i parametri
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.stato = False # Stato del ristorante impostato in falso come standard
        self.menu = {
        "Nigiri Salmone": 5.50,
        "Nigiri Tonno": 6.00,
        "Sashimi Misto": 12.00,
        "Uramaki Philadelphia": 8.50,
        "Uramaki California": 9.00,
        "Hosomaki Cetriolo": 4.50,
        "Temaki Salmone": 7.00,
        "Gunkan Ikura": 6.50,
        "Tartare di Tonno": 10.00,
        "Ramen Miso": 11.00
        }
        
    def descrivi_ristorante(self): # Stampa la descrizione del ristorante
            print(f"Il ristorante '{self.nome}' offre cucina {self.tipo_cucina}.")
        
    def stato_apertura(self): # Controlla self.stato per stabilire se il ristorante è aperto o chiuso
        if not self.stato:
            print("Il ristorante è chiuso!!!")
        print("Il ristorante è aperto!!!")
        
    def apri_ristorante(self): # Funzione per aprire il ristorante, modifica il valore di self.stato,
        self.stato = True
        print(f"{self.nome} è ora aperto!!!")
    
    def chiudi_ristorante(self): # Chiude il ristorante modificanto il valore di self.stato
        self.stato = False
        print(f"{self.nome} è ora chiuso!!!")
    
    def aggiungi_al_menu(self, piatto, prezzo): # Funzione per aggiungere un piatto al menù
        while True:
            piatto = input("Inserisci il nome del piatto da aggiungere: ")
            if piatto in self.menu: # Verifica se il piatto è già presente nel menù
                print("Il piatto è già presente nel menù")
                break
            prezzo = float(input("Inserisci il prezzo da aggiunere: "))
            self.menu[piatto] = prezzo
            print(f"{piatto} è stato aggiunto al menu a {prezzo}€.")
            
    def togli_dal_menu(self, piatto): # Toglie un elemento dal menù
        while True:  
            if piatto in self.menu:
                del self.menu[piatto] # Comando per eliminare un valore dal dizionario
                print(f"{piatto} è stato rimosso dal menu.")
            else:
                print(f"{piatto} non è presente nel menu.")
            whatdo = input("Vuoi togliere un altro piatto dal menù (s/n)").lower()
            if not whatdo == "s":
                break
    
    def stampa_menu(self): # Comando per stampare ogni elemento del dizionario menù
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            print("Menu del ristorante:")
            for piatto, prezzo in self.menu.items():
                print(f"- {piatto}: {prezzo}€")

# Creazione di un'istanza del ristorante
ristorante = Ristorante("La Bella Tavola", "Italiana")

while True: # Ciclo che si ripete finchè l'utente
    cosa_fare = int(input("Benvenuto nel tuo ristorante, cosa vuoi fare?\nVisionare la descrizione del ristorante (1)\nVisionare lo stato del tuo ristorante (2)\nApri il ristorante (3)\nChiudi il ristorante (4)\nAggiungi piatti al menù (5)\nTogli piatti dal menù (6)\nVisionare il menù (7)\n"))
    match cosa_fare:
        case 1:
            ristorante.descrivi_ristorante()
        case 2:
            ristorante.stato_apertura()
        case 3:
            ristorante.apri_ristorante()
        case 4:
            ristorante.chiudi_ristorante()
        case 5:
            ristorante.aggiungi_al_menu()
        case 6:
            ristorante.togli_dal_menu()
        case 7:
            ristorante.stampa_menu()
        case 8:
            print("Arrivederci!")
            break
        case _:
            print("Comando non riconosciuto, chiusura del programma..")
            break
