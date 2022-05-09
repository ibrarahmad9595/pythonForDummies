from model.Rubrica import Rubrica

rubricaAmici = Rubrica("Thux")
rubricaAmici.aggiungiContatto("ahmad","ibrar","123456789");
rubricaAmici.aggiungiContatto("flaca","bruno","987654321");
rubricaAmici.aggiungiContatto("salva","bruno","123123123");
rubricaAmici.aggiungiContatto("test","new","123123124");
rubricaAmici.getContatto(1);
rubricaAmici.eliminaContatto(1);
rubricaAmici.elencoContatti();
rubricaAmici.cercaContatto(123456789)




