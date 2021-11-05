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

class FlervalgSpørsmål:
    def __init__(self,spørsmål, riktigSvar, svaralternativListe):
        self.spørsmål = spørsmål
        self.riktigSvar = riktigSvar
        self.svaralternativListe = svaralternativListe
        self.printStreng = f"Vennligst svar med et heltall hvilket alternativ er riktig \n{spørsmål} \n"
        aIndex = 1
        for alternativ in self.svaralternativListe:
            self.printStreng = self.printStreng + f"{aIndex}: {alternativ} \n"
            aIndex = aIndex +1
        self.printStreng = self.printStreng + "Ditt svar: "
    
    def __str__(self):
        return f"{self.printStreng}"
    
    def sjekk_svar(self, svar):
        if svar == self.riktigSvar:
            return True
        else:
            return False

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
            
            for b in linjeListe[2]:
                print(b)
            
            
            listen.append(FlervalgSpørsmål(linjeListe[0], linjeListe[1], linjeListe[2]))
        except:
            print(f"Problem med behandlig av spørsmål {linjeListe[0]} \nKoden forsetter, men uten dette spørsmålet")
        
    return listen


if __name__== "__main__":
    
    oppgaveFil = lesInnOppgaveFil()
    oppgaveListen = lagOppgaveListen(oppgaveFil)
    
    print(oppgaveListen[2])
    
    
    print("yes")    
    oppgaveFil.close()