class Politiker:
    def __init__(self, fornavn, etternavn, parti, verdi):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.parti = parti
        self.verdi = verdi
        self.poeng = 0
        self.navn = fornavn + " " + etternavn

    def hent_navn(self):
        return self.navn

    def hent_parti(self):
        return self.parti

    def gi_poeng(self, n):
        self.poeng += n
