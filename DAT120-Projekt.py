# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:20:31 2021

@author: eirik



"""


ferdig = True
navnPåSpørsmålsfila = "sporsmaalsfil.txt"
"""
Endre på variabelen her oppe for å gjøre det letter å endre på den
"""
oppgaveListen = []
spiller1Poeng = 0
spiller2Poeng = 0
spiller1Svar = ""
spiller2Svar = ""
class Sporsmaal:
    def __init__(self,spørsmål, riktigSvar, svaralternativListe):
        self.spørsmål = spørsmål
        self.riktigSvar = riktigSvar
        self.svaralternativListe = svaralternativListe
        self.printStreng = f"Vennligst svar med et heltall hvilket alternativ er riktig \n{spørsmål} \n"
        aIndex = 1
        for alternativ in self.svaralternativListe:
            self.printStreng = self.printStreng + f"{aIndex}: {alternativ} \n"
            aIndex = aIndex +1
        """
        self.printStreng = self.printStreng + "Ditt svar: "
        """
    
    def __str__(self):
        return f"{self.printStreng}"
    
    def sjekk_svar(self, svar):
        if svar == self.riktigSvar + 1:
            return True
        else:
            return False
    
    def korrekt_svar_tekst(self): 
        return self.svaralternativListe[self.riktigSvar]

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

def lesInnOppgaveFil():
    try:
        fila = open(navnPåSpørsmålsfila, "r", encoding="UTF8")
        return fila
    except:
        print(f"Finner ikke fil: {navnPåSpørsmålsfila}")

def lagOppgaveListen(filMedOppgaver):
    listen = []

    for linje in filMedOppgaver:
        linjeListe = linje.split(":")
        
        try:
            linjeListe[1] = int(linjeListe[1])
            linjeListe[2] = linjeListe[2].translate({ord(i): None for i in '[]'})
            linjeListe[2] = linjeListe[2].split(',')
            """
            Ukomfortabel med denne måten å få inn den nøstede listen på
            Føler det burde være en bedre måte, men fant den ikke
            """
            listen.append(Sporsmaal(linjeListe[0], linjeListe[1], linjeListe[2]))
        except:
            print(f"Problem med behandlig av spørsmål {linjeListe[0]} \nKoden forsetter, men uten dette spørsmålet")
        
    return listen


if __name__== "__main__":
    
    oppgaveFil = lesInnOppgaveFil()
    oppgaveListen = lagOppgaveListen(lesInnOppgaveFil())
    
    print("Dette er et spill for 2 spillere \nVelg selv hvem som er spiller 1 og 2")
    for oppgave in oppgaveListen:
        print(oppgave)
        spiller1Svar = sjekkLovligInput(input("Spiller 1 sitt svar: "))
        spiller2Svar = sjekkLovligInput(input("Spiller 2 sitt svar: "))
        
        print(f"Riktig svar er: {oppgave}")
        
        if oppgave.sjekk_svar(spiller1Svar):
            print("Spiller 1: Riktig")
            spiller1Poeng = spiller1Poeng + 1
        else:
            print("Spiller 1: Feil")
            
        if oppgave.sjekk_svar(spiller2Svar):
            print("Spiller 2: Riktig\n")
            spiller2Poeng = spiller2Poeng + 1
        else:
            print("Spiller 2: Feil\n")
    
    print(f"Spiller 1 poengsum: {spiller1Poeng}")
    print(f"Spiller 2 poengsum: {spiller2Poeng}")
    
    if spiller1Poeng > spiller2Poeng:
        print("Spiller 1 Vinner!!")
    elif spiller2Poeng > spiller1Poeng:
        print("Spiller 2 Vinner!!")
    else:
        print("Det er uavgjort.")
    
    oppgaveFil.close()