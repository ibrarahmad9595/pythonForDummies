from model.Impiegato import Impiegato
class Azienda:
    def __init__(self, nome):
        self.nome = nome;
        self.impiegati = []

    def aggiungiImpiegato(self, nome, cognome, matricola):
        imp = Impiegato(nome, cognome, matricola, self)
        self.impiegati.append(imp)
        print(self.impiegati)

    def __len__(self):
        return len(self.impiegati)
