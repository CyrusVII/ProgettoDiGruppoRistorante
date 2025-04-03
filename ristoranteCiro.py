# Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base
# Requisiti:
# 1. Definizione della Classe:
# • Creare una classe chiamata Ristorante.
# • La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo cucina (tipo di cucina offerta).
# • Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
# • Un dizionario menu dove dentro ci sono i piatti e prezzi che ha il ristorante
# 2. Metodi della Classe:
# • descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
# stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
# • apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
# • chiudi ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
# aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
# • togli_dal_menu(): Un metodo per togliere piatti al menu
# • stampa_menu(): Un metodo per stampare il menu
# 3. Testare la Classe:
# • Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
# • Testare tutti i metodi creati per assicurarsi che funzionino come previsto.

class Ristorante:
    def __init__(self, nome, tipo_cucina):
        # Inizializza il ristorante con nome, tipo di cucina e stato chiuso di default
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.stato = False  # False indica che il ristorante è chiuso
        
        # Dizionario che rappresenta il menu con piatti e relativi prezzi
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
    
    def descrivi_ristorante(self):
        # Stampa le informazioni del ristorante
        print(f"Benvenuti al {self.nome}, il tipo di ristorante è {self.tipo_cucina}")
    
    def stato_apertura(self):
        # Controlla e stampa se il ristorante è aperto o chiuso
        print("Il ristorante è aperto") if self.stato else print("Il ristorante è chiuso")
    
    def apri_ristorante(self):
        # Cambia lo stato a 'aperto'
        self.stato = True
        self.stato_apertura()
    
    def chiudi_ristorante(self):
        # Cambia lo stato a 'chiuso'
        self.stato = False
        self.stato_apertura()
    
    def stampa_menu(self):
        # Stampa l'elenco dei piatti disponibili nel menu
        for chiave, valore in self.menu.items():
            print(f"{chiave} : {valore}")
    
    def aggiungi_al_menu(self):
        # Permette di aggiungere nuovi piatti al menu tramite input utente
        while True:
            piatto = input("Inserisci nome piatto: ")  # Nome del piatto
            prezzo = float(input("Inserisci prezzo: "))  # Prezzo del piatto
            if piatto in self.menu:
              print('Piatto gia presente nel menu')
            else:
              self.menu[piatto] = prezzo  # Aggiunge il piatto al menu
              
            # Chiede all'utente se vuole aggiungere un altro piatto
            if input('Vuoi inserire un altro piatto? (s/n) ---> ').lower().strip() == 'n':
                break
        
        self.stampa_menu()  # Stampa il menu aggiornato
    
    def togli_dal_menu(self):
        self.stampa_menu()
        
        # Permette di rimuovere un piatto dal menu
        piatto = input("Inserisci nome piatto da togliere: ")
        
        # Controlla se il piatto è presente nel menu prima di rimuoverlo
        if piatto in self.menu:
            del self.menu[piatto]  # Rimuove il piatto dal menu
            print(f"Piatto '{piatto}' rimosso dal menu.")
        else:
            print(f"Errore: il piatto '{piatto}' non è nel menu.")
        
        self.stampa_menu()  # Stampa il menu aggiornato


#classe di gestione
class Start():
  
  def __init__(self):
      pass
  def menu(self):
    # Creazione di un'istanza della classe Ristorante
    rist = Ristorante('Da Mirko', 'Giapponese')
    # Ciclo infinito per gestire il menu interattivo
    while True:
        ch = int(input(
            "--- MENU ---\n 1) Descrizione Ristorante \n 2) Stato Apertura \n 3) Apri Ristorante \n 4) Chiudi Ristorante \n 5) Visualizza Menu \n 6) Aggiungi al Menu \n 7) Togli al Menu\n ---> "
        ))
        
        # Struttura match-case per eseguire l'operazione scelta dall'utente
        match ch:
            case 1:
                rist.descrivi_ristorante()
            case 2:
                rist.stato_apertura()
            case 3:
                rist.apri_ristorante()
            case 4:
                rist.chiudi_ristorante()
            case 5:
                rist.stampa_menu()
            case 6:
                rist.aggiungi_al_menu()
            case 7:
                rist.togli_dal_menu()
        # Controllo se l'utente vuole uscire dal menu
        if input('Vuoi tornare al menu? (s/n) ---> ').lower().strip() == 'n':
            break

#avvio programma
s = Start()
s.menu()