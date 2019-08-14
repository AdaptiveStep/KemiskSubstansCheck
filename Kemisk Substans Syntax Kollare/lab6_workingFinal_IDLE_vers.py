#!/usr/bin/env python
# -*- coding: latin-1 -*-

__author__ = 'HARIZ'

# 9 november 2013
# Syntax Lab 6
# BNF för programmet finns nederst på sidan.


from sys import *
import time

class ListQ(object):

    def __init__(self):
        self.items = []

    def __str__(self):
        def __str__(self):
            s = ""
            p = self.first
            while p != None:
                s = s + str(p.value)
                p = p.next
            return s

    def put(self,x):
        self.items.insert(0,x)

    @property
    def get(self):
        if self.items == []:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if self.items == []:
            return None
        else:
            return self.items[len(self.items)-1]        #Visar vad som finns längst åt höger, dvs sista elementet.
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Syntaxfel(Exception):              #Ett sådant objekt skapas varje gång ett felmeddelande visas.
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
class Formelklass():
    def __init(self):
        self.atom = ""
        self.molekyl = ""
        self.vikt = ""
def  readFormel():
    if q.isEmpty():                         #Kollar kön är tom.
        print("\n")                         #OM kö är tom så är programmet färdigt
    else:                                     #Annars undersöker den aktuell molekyl
        readMol()
def readMol():
    readGroup()                            #undersöker grupp
    if not q.isEmpty():                     #Om grupp är undersökt OCH kö ej tom
        readMol()                           #Så ska vi undersöka molekylen igen

def readGroup():
    if q.peek() in bsletter:
        readAtom()
        if q.peek() is not None:        #tillhör första delen av group i BNF definitionen
            if q.peek() in numbers:
                readNum()
    elif q.peek() in ["("]:      #men ska du inte plocka ut parantesen också?
        paranQ.put(q.get)
        if q.peek() is not None:
            if q.peek() in [")"]:
                raise Syntaxfel("Felaktig gruppstart vid radslutet ")
            readMol()
            if not paranQ.isEmpty():
                raise Syntaxfel("Saknad högerparentes vid radslutet ")
        else:
            raise Syntaxfel("Saknad högerparentes vid radslutet ")

    elif q.peek() in [")"] and not paranQ.isEmpty():
        q.get
        paranQ.get
        if q.peek() is not None:
            if q.peek() in numbers:
                readNum()
                return
            else: raise Syntaxfel("Saknad siffra vid radslutet ")       #Det kan vara så att formeln råkat ta slut precis efter en parantes
        else: raise Syntaxfel("Saknad siffra vid radslutet ")           #Eller så har det blivit fel på så sätt att det INTE dykt upp en siffra efter slutparantes
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
def readAtom():
    character = q.peek()
    if character in bletter:
        readBletter()
        if q.peek() is not None:
            if q.peek() in sletter:
                character += q.peek()
                readSletter()
        atomExists(character)                   #En mindre indentering eftersom det finns atomer med en stor bokstav.
    else: raise Syntaxfel("Saknad stor bokstav vid radslutet ")
def readBletter():
    character = q.get
    if character is None or character in [""]:
        raise Syntaxfel("Fel syntax, förväntades text:")
    elif character in bletter:                  #Följande 3 funktioner är enkla anrop som kollar ifall karaktär är i lista
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + character)
def readSletter():
    character = q.get
    if character is None:
        raise Syntaxfel("Saknad liten bokstav vid radslutet ")
    elif character in sletter:
        return
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet " + character)
def readNum():                              # Lite speciellare än bletter och sletter funktionen
    character = ""                          # Skapar tilfällig variabel
    if int(q.peek()) > 1:             # om första siffran är större än 2
        while q.peek() in numbers:     # Så staplas resten av siffrorna upp i en sträng
            character += q.get
            if q.peek() is None:            # om hela listan tar slut så ska while loopen omedelbart brytas
                break
        return
    elif q.peek() == "1":
        character = str(q.get)
        if q.peek() is not None and str(q.peek()) in numbers:
            while q.peek() in numbers:     # Så staplas resten av siffrorna upp i en sträng
                character += str(q.get)
                if q.peek() is None:            # om hela listan tar slut så ska while loopen omedelbart brytas
                    break
            return
        else: raise Syntaxfel("För litet tal vid radslutet ")
    elif q.get in ["0"]: raise Syntaxfel("För litet tal vid radslutet ")
    else:
        raise Syntaxfel("Saknad siffra vid radslutet " + q.get)   #TODO SIFFRA ELLER TAL? WHAT
def atomExists(atom):
    if atom in atomlista: return
    else: raise Syntaxfel("Okänd atom vid radslutet ")

def inlasning(formel):
    if formel == "":
        raise Syntaxfel("Ingen inmatning")
    else:
        for character in formel:                                                #OBS, Sista tecknet måste ha ett mellanslag och punkt. TODO FIXA detta! FIXAD?
            q.put(character)
        return

def runsyntax(formel):                                                  #Används i mainloopen för att anropa en massa saker från
    try:
        inlasning(formel)
        if formel != "#":       #Denna koll sker två gånger i koden, borde tas bort.
            readFormel()
            print(" Formeln är syntaktiskt korrekt")
    except Syntaxfel as msg:

        print(str(msg) , end="")
        newchar = ""
        while not newchar is None:
            newchar = q.get
            if newchar is not None:
                print(str(newchar), end="")
            else:
                break
        print("")


bletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sletter = "abcdefghijklmnopqrstuvwxyz"
bsletter = bletter+sletter
firstnumbers = "23456789"
numbers = "1234567890"
atomlista = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","Ba","Fe"]
paranQ = ListQ()

#Nedan följer samma procedur som exempel i förel 10

open("data.txt",'r')

while 1:                                                #Main loopen som frågar samma fråga om och om igen.

    q = ListQ()                                         #Bygger upp listan igen, så att gamla ord försvinner från den.
    paranQ =ListQ()

    formel = input("\n\t Ange en formel: \n\n >>>>> ")       #Frågar efter formel.
    tiden1 = time.clock()
    if formel == "#":
        break
    else:
        oldword = formel
        runsyntax(formel)                                   #

    tiden2 = time.clock()
    tiden3 = tiden2 - tiden1
    print(tiden3)
#####################################################################################

#                         BNF MODELL FÖR PROGRAMM

#                   < formel >::= < mol > \n
#                   < mol >::= < group > | < group > < mol >
#                   < group >::= < atom > | < atom > < num > | ( < mol >) < num >
#                   < atom >::= < LETTER > | < LETTER > < letter >
#                   < LETTER >::= A | B | C | ... | Z
#                   < letter >::= a | b | c | ... | z
#                   < num >::= 2 | 3 | 4 | ...

###################
#"""
#TIPS för inläsning av talet:
# - Kolla att det inte börjar med ()
# - Sen: plocka en siffra i taget från kön
#     - (så länge peek ser en siffra, spara i en sträng) , tex "301"
#     - Konvertera till heltal med int()... (talet används i lab 7)
# ---------------
#
# Man behöver inte räkna "(" och ")"
# Om det kommer en "(" så gör ett rekursivt anrop av mol-inläsningsfunktionen efter anropet: Kolla om "(".
# ---------------
# Regler till lab: Använd aldrig Exception rakt av.
# """
#   Behöver klara av:
#
#   H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar

#Konfirmera följande
#Testfall: Si(C3(COOH)2)4(H2O)7        OK
#          C(Xx4)5                     EJ OK
#          C(OH4)C                     EJ OK
#          C(OH4C                      EJ OK
#          Si(C3(COOH)2)4(H2O          EJ OK
#          ()2                         EJ OK
#          (COOH)1                     EJ OK
