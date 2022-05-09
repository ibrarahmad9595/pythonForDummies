from model.Contatto import Contatto

class Rubrica:
    def __init__(self,nome):
        self.nome = nome;
        self.lista_contatti = []

    def aggiungiContatto(self, cognome, nome, telefono):
        cont = Contatto(cognome,nome,telefono)
        self.lista_contatti.append(cont);

    def getContatto(self, position):
        print("*********************************Informationi di contatto*********************************")
        try:
            # indice = self.lista_contatti[4]
            print(" Cognome: ", self.lista_contatti[position].cognome, "\n", "Nome: ", self.lista_contatti[position].nome,
              "\n", "telefono: ", self.lista_contatti[position].telefono);

        except IndexError:
            print("L'indice non e' presente")
    def eliminaContatto(self, position):
        print("\n*********************************Elimina Contatto*********************************")
        deleted = self.lista_contatti.pop(position)
        i =0;
        print("Eliminato contatto : Cognome: {}, Nome: {}, Telefono: {} ".format(deleted.cognome,deleted.nome,deleted.telefono))
        for x in self.lista_contatti:
            i=i+1
            print("Nuova Lista record {} :".format(i),x.cognome,x.nome,x.telefono)

    # restituisce una stringa con l'elenco delle voci della rubrica separate
    # da ", "; l'elenco inizia con "(" e termina con ")"
    def elencoContatti(self):
        new_list = []
        for x in self.lista_contatti:
            val = (x.cognome,x.nome,x.telefono);
            new_list.append(val)
        list_string = str(new_list)
        list_string = list_string.replace("[","");
        list_string = list_string.replace("]","");
        list_string = list_string.replace("(", "");
        list_string = list_string.replace(",","");
        list_string = list_string.replace(")", ",");
        list_string = list_string.replace("'", "");
        list_string = "("+ list_string + ")"
        list_string = list_string.replace(",)", ")");
        print("\n*********************************Elenco Contatti*********************************")
        print(list_string)

    #restituisce la stringa corrispondente alla prima voce che contiene
    # il parametro key come nome, cognome oppure telefono.
    def cercaContatto(self, key):
        # global lista_contatti
        for x in self.lista_contatti:
            if str(key) == str(x.telefono):
                print("\n*********************************Cerca Contatto*********************************")
                print("Contatto found --> Cognome: {}, Nome: {}, Telefono: {}".format(x.cognome,x.nome,x.telefono));
                break
            else:
                raise Exception("not found : ",key);




