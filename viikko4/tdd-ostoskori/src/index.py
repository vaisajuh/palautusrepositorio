from ostoskori import Ostoskori
from tuote import Tuote


kori = Ostoskori()
maito = Tuote("Maito", 3)

kori.lisaa_tuote(maito)
kori.lisaa_tuote(maito)

for i in kori.ostokset():
    print(i.lukumaara())

print(kori.ostokset())
    
