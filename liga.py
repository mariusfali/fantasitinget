from parti import Parti
class Liga:
    def __init__(self):
        self.alle_partier = []

    def legg_til_parti(self, parti):
        if parti not in self.alle_partier:
            self.alle_partier.append(parti)
        else:
            return f"Dette partiet deltar allerede i ligaen"

    def fjern_parti(self, parti):
        if parti in self.alle_partier:
            self.alle_partier.remove(parti)
        else:
            return f"Dette partiet deltar ikke i ligaen"

    def poengtavle(self):
        #sortert = self.alle_partier.sort()
        alle_lag = []
        for i in self.alle_partier:
            alle_lag.append(i.navn + " - " + str(i.tell_poeng()))
        return alle_lag