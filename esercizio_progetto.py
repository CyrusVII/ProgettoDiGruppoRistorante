
# Creare una classe Ristorante
class Ristorante:  # Dichiaro la classe
    # costruttore
    def __init__(self, nome_ristorante, tipo_cucina):  # Metodo costruttore per inizializzare l'oggetto
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
        self.nome_ristorante = nome_ristorante  # Attributo di istanza 
        self.tipo_cucina = tipo_cucina  # Attributo di istanza 
    
    #descrivi_ristorante-> stampare una frase descrivendo il ristorante
    
    def descrivi_ristorante(self):
        print(f"Il Ristorante {self.nome_ristorante} offre questo il seguente tipo di cucina: {self.tipo_cucina}")
    
    # metodo che stampa se il risporante è chiuso o aperto 
    
    def stato_apertura(self):
        if self.aperto == True:
            stato="aperto"
            print(f"Il ristorante {self.nome_ristorante} attualmente è {stato}")
        else:
            stato="chiuso"
            print(f"Il ristorante {self.nome_ristorante} attualmente è {stato}")
    # metodo per impostare attributo true e stampa
    def apri_risporante(self):
        self.aperto=True
        print(f"Il ristorante {self.nome_ristorante} è aperto")
    # metodo per impostare attributo aperto=F e stampa che il ristorante è chiuso 
    def chiudi_ristorante(self):
        self.aperto=False
        print(f"Il ristorante {self.nome_ristorante} è chiuso")
    # metodo per aggiungere piatti al menu   
    def aggiungi_al_menu(self,piatto,prezzo):
                self.menu[piatto]=prezzo
                print(f"{piatto} è stato aggiunto al menu al prezzo")
    # metodo per togliere piatti dal menu               
    def togli_dal_menu(self,piatto):
        if piatto in self.menu: 
            del self.menu[piatto]
            print(f"Piatto '{piatto}' rimosso dal menu.")
        else:
            print(f"Piatto '{piatto}' non è presente nel menu.")
    # stampa il menu       
    def stampa_menu(self):
        print("Menu del ristorante {self.ristorante}")
        for chiave,valore in self.menu.items():
            print(f"{chiave}:{valore}")

#Test
ristorante=Ristorante("Domò Sushi","Sushi")
ristorante.descrivi_ristorante()

from datetime import datetime

# Ottieni l'ora corrente
current_time = datetime.now()
current_hour = current_time.hour

if (12 <= current_hour < 16) or (19 <= current_hour < 23):
    ristorante.apri_risporante()
else:
    ristorante.chiudi_ristorante()

print("1. Aggiungi al menu")
print("2. Togli dal menu")
print("3. Stampa menu")
opzione=int(input("Scegli tra le opzioni: "))   
match opzione:
    case 1:
        piatto=input("Inserire il nome del piatto: ")
        #Ebi Tempura
        prezzo=float(input("Inserire il prezzo: "))
        ristorante.aggiungi_al_menu(piatto, prezzo)
    case 2:
        piatto=input("Inserire il nome del piatto: ")
        #Ramen Miso
        ristorante.togli_dal_menu(piatto)
    case 3:
        ristorante.stampa_menu()
        



         
        
        
         
        