from politiker import Politiker
class Parti:
    def __init__(self, navn):
        self.politikere = []
        self.poengsum = 0
        self.penger = 1000
        self.navn = navn

    def tell_poeng(self):
        self.poengsum = 0
        for i in self.politikere:
            self.poengsum += i.poeng
        return self.poengsum

    def legg_til_spiller(self, spiller):
        if len(self.politikere) >= 12:
            return f"Ditt lag er fullt"
        else:
            if spiller.navn == "Jonas Gahr Støre":
                self.penger -= 200
                self.politikere.append(spiller)
            else:
                self.penger -= spiller.verdi
                self.politikere.append(spiller)
                #if spiller.verdi == 150:
                #    self.penger -= 150
                #    self.politikere.append(spiller)
                #elif spiller.verdi == 100:
                #    self.penger -= 100
                #    self.politikere.append(spiller)
                #elif spiller.verdi == 50:
                #    self.penger -= 50
                #    self.politikere.append(spiller)
            return f"Spiller lagt til"
    
    def fjern_spiller(self, spiller):
        for i in self.politikere:
            if i.navn == spiller.navn:
                self.penger += spiller.verdi
                self.politikere.remove(spiller)
                return f"Spiller solgt"
            return f"Du har ikke denne spilleren"

    def bytt_spillere(self, gammel, ny):
        self.politikere.remove(gammel)
        self.penger += gammel.verdi
        self.politikere.append(ny)
        self.penger -= ny.verdi
