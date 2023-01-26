import json
from politiker import Politiker
from parti import Parti
from liga import Liga
from scrapping import sjekk_poeng

fil = open("politikere.json")
politikere = json.load(fil)
fil.close()

#print(politikere)



p1 = Politiker("Jonas", "Gahr Støre", "AP", 200)
p2 = Politiker("Erna", "Solberg", "Hoyre", 150)
p3 = Politiker("Tom", "Hanks", "Vet ikke", 100)

parti1 = Parti("hei")
parti1.legg_til_spiller(p1)
parti1.legg_til_spiller(p2)
parti2 = Parti("tapere")
parti2.legg_til_spiller(p2)
print(parti1.penger)


liga1 = Liga()
liga1.legg_til_parti(parti1)
liga1.legg_til_parti(parti2)
print(liga1.poengtavle())

p3.tell_poeng()
print(p3.poeng)