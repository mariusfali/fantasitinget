#Test 1
from politiker import Politiker

import json

fil = open("politikere.json")
ordbokpolitikere = json.load(fil)
fil.close

politikere = ordbokpolitikere["representanter_oversikt"]["representanter_liste"]["representant"]

listepolitikere = []

for politiker in politikere:
    listepolitikere.append(Politiker(politiker["fornavn"], politiker["etternavn"], politiker["parti"]["navn"],"2"))








