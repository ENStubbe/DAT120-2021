# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:20:31 2021

@author: eirik

b)Som del av et spørrespill skal du lage en klasse for flervalgspørsmål (hele spillet er muligens øving 9 og 10). 
Et flervalgspørsmål skal ha en spørsmålstekst, 
ei liste med svaralternativer (hvert svaralternativ er en tekststreng), 
og et tall som sier hvilket av svaralternativene som er korrekt.
Klassen skal ha en __str__ metode som returnerer en streng som inneholder spørsmålsteksten og nummerte svaralternativer på et lett leselig format. 
Klassen skal ha en sjekk_svar metode som tar som parameter et heltall som representerer hvilket svar brukeren velger. 
Sjekk_svar metoden skal sjekke om svaret brukeren har oppgitt er korrekt. 

"""
ferdig = True
listeMedSpørsmål = ["Alternativ1", "Alternatv2", "alternativ3"]
listeMedSpørsmål2 = ["Alternativ1", "Alternativ2", "Alternativ3", "Alternativ"]

class FlervalgSpørsmål:
    def __init__(self, svaralternativListe, riktigSvar):
        self.riktigSvar = riktigSvar
        self.svaralternativListe = svaralternativListe
        self.printStreng = "Vennligst svar med et heltall hvilket alternativ er riktig \n"
        aIndex = 1
        for alternativ in self.svaralternativListe:
            self.printStreng = self.printStreng + f"{aIndex}: {alternativ} \n"
            aIndex = aIndex +1
        self.printStreng = self.printStreng + "Ditt svar: "
    
    def __str__(self):
        return f"{self.printStreng}"
        
    
    def sjekk_svar(self, svar):
        if svar == self.riktigSvar:
            return "Svaret ditt er riktig"
        else:
            return "Svaret ditt er feil"

def sjekkLovligInput(inputFraBruker):
    while ferdig != False:
        try:
            intFraBruker = int(inputFraBruker)
            return intFraBruker
        except:
            inputFraBruker = input("Vennligst skriv inn et heltall. \n Prøv igjen: ")
"""
gjør litt mer i denne funksjonen enn jeg vanligvis hadde gjort
Dette var for å gjøre koden litt mer skalerbar
"""

if __name__== "__main__":
    
    spørsmål1 = FlervalgSpørsmål(listeMedSpørsmål, 3)
    print(spørsmål1.sjekk_svar(sjekkLovligInput(input(spørsmål1))))
    
    spørsmål2 = FlervalgSpørsmål(listeMedSpørsmål2, 2)
    print(spørsmål2.sjekk_svar(sjekkLovligInput(input(spørsmål2))))
    
    """
    Ble veldig kompakt kode her, men hadde lyst å gjøre det så det var så lite kode som mulig å oppdatere for å legge til flere spørsmål
    En mer skalerbar måte hadde vært å ha svarsalternativene med svarene i en fil som scriptet laster inn
    """
    