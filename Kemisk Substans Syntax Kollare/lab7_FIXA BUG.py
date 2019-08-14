#!/usr/bin/env python
# -*- coding: latin-1 -*-

__author__ = 'HARIZ'

# 14 november 2013
# Syntax Lab 7
# BNF f�r programmet finns nederst p� sidan.

from LinkedQ import *
from molgrafik import *
from Atomload import *
from LinkedStack import *
from molgrafik import Molgrafik,Ruta

# Todo Fixa ordning alla kommentarer, stapla och ta bort alla on�diga.
# Todo ta bort alla on�diga T'odo's.
# Todo Ta bort allt skrap pa botten
#

class Syntaxfel(Exception):              #Ett s�dant objekt skapas varje g�ng ett felmeddelande visas.
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
class Formelklass():                #Skall anv�ndas rekursivt vid utr�kning av vikten. Anv�nd data som finnes i lab 5.
    def __init__(self,atom="",molekyl="",vikt=""):
        self.atom         = atom
        self.molekyl      = molekyl
        self.vikt         = vikt
        self.antal        = 1
        self.molekylantal = 1

def swap(somelist):             # Byter plats p� l�mpliga None's och ()n's .
    """
    Swappar alla None och ()'s
    Detta g�rs s� att man enkelt kan l�nka ihop allting med next pekare.
    """
    tempstack = Stack()
    counter = -1
    for i in somelist:
        counter += 1
        if i == None:
            somelist[counter] = tempstack.pop()
        elif i.atom == "()":
            tempstack.push(i)
            somelist[counter] = None
def enlink(somelist):           # S�tter plats p� l�nkarna d� listan �r perfekt ordnad.
    """
    L�nkar samman alla element som kommer fr�n en lista. Ger slutgiltig framst�llning av l�nkad struktur.
    """
    while len(somelist) > 0:       #Medans listan INTE �r tom.
        temp = somelist.pop()
        if temp != None:
            if temp.atom != "()":
                temp.next = enlink(somelist)
            else:
                temp.down = enlink(somelist)     #Ty en ()'s kan ha b�de ned och next barn.
                temp.next = enlink(somelist)
        else:
            return

        return temp         #Returnerar slutgiltig l�nkad formel, efter att hela rekursions maskineriet i "enlink" �r f�rdigt.

def  readFormel():

    if q.isEmpty():                         #Kollar k�n �r tom. (Vilket den aldrig kommer vara)
        print("\n")                         #OM k� �r tom s� �r programmet f�rdigt (Anropas aldrig i denna version, kan tas bort)
    else:                                   #Annars unders�ker den aktuell molekyl. Detta ska returneras till huvudprogrammet.
        readMol()
        swap(prototyplista)
        finallist = enlink(prototyplista)
        vikt = weight(finallist)
        return [finallist,vikt]                     #Denna ska sedan matas in i grafikmodulen


def readMol():
    #                           Fe(Ca33(COOOH)2)4(H12O)7
    #                           Fe (Ca33 (COOOH)2 )4 (H12O)7
    mol = readGroup()

    if q.peek() is not None:
        readMol()               ##### �ndra ej n�got inne i denna funktion ovanf�r detta OBS OBS OBS

    prototyplista.append(mol)

    return
def readGroup():
    rutan = Ruta()
    if q.peek().data in bsletter:
        atomgrupp = Formelklass()           #Skapar specifik klass f�r detta objekt ifall det skulle beh�vas l�ngre ner. (Men f�r tillf�llet anv�nds den endast inom denna if-sats.
        atomgrupp.atom = readAtom()
        if q.peek() is not None:            #tillh�r f�rsta delen av group i BNF definitionen
            if q.peek().data in numbers:
                antalatomer = readNum()       #Ger talet direkt efter atomen. Skall returnera till grafik?
                atomgrupp.antal = float(antalatomer)    #namn och vikt returneras, direkt efter en atom och dess multipel.

        rutan.atom = atomgrupp.atom
        rutan.num  = atomgrupp.antal     #Sammanfattas f�r enkelhets skull

        return rutan            # ENDAST: "Atom OCH siffra returneras" i ett objekt. Detta �r utanf�r paranteser. ENDAST MED SIFFRA/OR
    elif q.peek().data in ["("]:            #men ska du inte plocka ut parantesen ocks�?
        paranQ.put(q.get)                 #paranQ �r parantes pseudo-k� som plockar ut et element varje g�ng det dyker upp en slutparantes.
        if q.peek() is not None:
            if q.peek().data in [")"]:      #Om slutparantes kommer direkt efter startparantes, s� visas felmeddelande.
                raise Syntaxfel("Saknas molekyl mellan paranteser f�re ")

            tempmol = readMol()             #Annars s� l�ses molekylen in.

            return tempmol                #Skickar tillbaka molekylgruppen till toppen d� det l�sts f�rdigt.
            if not paranQ.isEmpty():        #om paranQ �r tom efter att molekylen l�sts in s� �r inmatningen fel. Ty paranQ ska ju inneh�lla en enda parantes.
                raise Syntaxfel("Fattas slutparantes p� radslutet")
        else:
            raise Syntaxfel("Fattas slutparantes p� radslutet")

    elif q.peek().data in [")"] and not paranQ.isEmpty():
        q.get
        paranQ.get
        if q.peek() is not None:
            if q.peek().data in numbers:
                molekylstorlek = readNum()                #Ger talet efter parantesen. Skall returnera till grafik?
                rutan.num = molekylstorlek
                return rutan
            else: raise Syntaxfel("Saknad siffra vid radslutet ")       #Det kan vara s� att formeln r�kat ta slut precis efter en parantes
        else: raise Syntaxfel("Saknad siffra vid radslutet ")           #Eller s� har det blivit fel p� s� s�tt att det INTE dykt upp en siffra efter slutparantes
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
def readAtom():
    tempchars = ""
    if q.peek().data in bletter:
            newatom = readBletter()              #Kan komma till nytta senare, ifall hela molekylen innanf�r parantesen s�kes.

            if q.peek() is not None:
                if q.peek().data in sletter:        #Om atomen inneh�ller en ytterligare liten bokstav i sitt namn?
                    newatom += q.get
            atomExists(newatom)                   #En mindre indentering eftersom det finns atomer med en stor bokstav.
            return newatom
    else: raise Syntaxfel("Saknad stor bokstav vid radslutet ")
def readBletter():
    character = q.get
    if character is None or character in [""]:
        raise Syntaxfel("Fel syntax, f�rv�ntades text:")
    elif character in bletter:                  #F�ljande 3 funktioner �r enkla anrop som kollar ifall karakt�r �r i lista
        return character
    else:
        raise Syntaxfel("Fel syntax, f�rv�ntades stor bokstav:" + character)
def readSletter():
    character = q.get
    if character is None:
        raise Syntaxfel("Fel, syntax, f�rv�ntades text (med liten bokstav f�rst)")
    elif character in sletter:
        return character
    else:
        raise Syntaxfel("Fel syntax, f�rv�ntades liten bokstav (gemen). Gavs: " + character)
def readNum():                              # Lite speciellare �n bletter och sletter funktionen
    character = ""                          # Skapar tilf�llig variabel
    if int(q.peek().data) > 1:             # om f�rsta siffran �r st�rre �n 2
        while q.peek().data in numbers:     # S� staplas resten av siffrorna upp i en str�ng
            character += q.get
            if q.peek() is None:            # om hela listan tar slut s� ska while loopen omedelbart brytas
                break
        return character        #Returnerar ett tal �ver 2 eller ett flersiffrigt tal
    elif q.peek().data == "1":
        character = str(q.get)
        if q.peek() is not None:
            if q.peek().data in numbers:
                while q.peek().data in numbers:     # S� staplas resten av siffrorna upp i en str�ng
                    character += str(q.get)
                    if q.peek() is None:            # om hela listan tar slut s� ska while loopen omedelbart brytas
                        break
                return  character
            else: raise Syntaxfel("F�r litet tal vid radslutet ")
        else: raise Syntaxfel("F�r litet tal vid radslutet ")
    elif q.get in ["0"]: raise Syntaxfel("F�r litet tal vid radslutet ")
    else:
        raise Syntaxfel("Fel syntax, f�rv�ntades siffra. Gavs: " + q.get)   #TODO SIFFRA ELLER TAL? WHAT?
def atomExists(atom):
    for element in atomlista:
        if element.split()[0] == atom:          # eftersom Atomlista = ["H 1.0079" , ... ] s� ger element.split() en liten minilista f�r varje element
            return
    raise Syntaxfel("Ok�nd atom vid radslutet ")
def inlasning(formel):
    if formel == "":
        raise Syntaxfel("Ingen inmatning")
    else:
        for character in formel:                                                #OBS, Sista tecknet m�ste ha ett mellanslag och punkt. TODO FIXA detta! FIXAD?
            q.put(character)
        return
def atomweight(atom):       #TODO: fixa hashtabell ist�llet
    """Ange atom som str�ng"""
    if atom != None:
        for element in atomlista:
            if element.split()[0] == atom:          # eftersom Atomlista = ["H 1.0079" , ... ] s� ger element.split() en liten minilista f�r varje element
                return float(element.split()[1])
    elif atom == None:
        return 0

    print("Ok�nd atom vid radslutet ")
def weight(mol):    #Denna rekursiva funktion fungerar lite som enlink funktionen
    vikt = 0

    if mol == None:         # Om mol �r None, d� �r det den sista positionen, och den skall d� returners.
        return vikt

    if mol.atom == "()":       #Om n�sta �r en molekyl. #Ber�knar allting "under" molekylen
        tempvikt = float(weight(mol.down))
        if tempvikt == 0:
            tempvikt = 1

        vikt = float(mol.num)*tempvikt     #Molekylgruppens nummer g�nger vikten av allting innanf�r

        if mol.next!= None:                #R�knar ut vikten till h�ger om parantesen
            nextvikt = weight(mol.next)
            vikt += nextvikt
    if mol.atom != "()":        #om n�sta position �r en atom #Ber�knar allting under och till h�ger om parantesen. Eller atomen om det bara �r en atom.
        vikt = vikt + float(mol.num)*float(atomweight(mol.atom)) + float(weight(mol.next))

    return vikt

def runsyntax(formel):                                                  #Anv�nds i mainloopen f�r att anropa en massa saker fr�n
    try:
        inlasning(formel)
        if formel != "#":
            finalform = readFormel()            #Finalform �r en lista med tv� element. Ett formelobjekt, och dess vikt i float.
            print(" Formeln �r syntaktiskt korrekt")
            print("  Vikten �r: ", finalform[1])
            mg.show(finalform[0])
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

#Globaler f�r programmet
mg = Molgrafik()                        #Beh�ver bara laddas en g�ng.
bletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sletter = "abcdefghijklmnopqrstuvwxyz"
bsletter = bletter+sletter
firstnumbers = "23456789"
numbers = "1234567890"
alfanum = bsletter + numbers
prototyplista = []
paranQ = ListQ()            #Anv�nds f�r att h�lla koll p� start-slut parantes. ")" plockar ut ett element ur pseudo-stacken, ty det beh�vs bara vetas ifall datastrukturen blir tom p� slutet. Annars hade en riktig stack varit mer l�mplig

#Globaler som importeras (vid k�rning)
#atomlista = ["H 1.005" , "He 2.0234", ...etc]  . Dvs inneh�ller varje atomnamn och dess vikt.

#Nedan f�ljer samma procedur som exempel i f�rel 10

while 1:                                                #Main loopen som fr�gar samma fr�ga om och om igen.
    q = ListQ()                                         #Bygger upp listan igen, s� att gamla ord f�rsvinner fr�n den.
    paranQ =ListQ()

    formel = input("\n Molekyl: ")       #Fr�gar efter formel.
    oldword = formel
    runsyntax(formel)                                   #

#Konfirmera f�ljande
#Testfall: Si(C3(COOH)2)4(H2O)7        OK
#          C(Xx4)5                     EJ OK
#          C(OH4)C                     EJ OK
#          C(OH4C                      EJ OK
#          Si(C3(COOH)2)4(H2O          EJ OK
#          ()2                         EJ OK
#          (COOH)1                     EJ OK
#------------------------------------------------------
# Further Try:
    # (Fe23)43(COOH)5
    #
    #
    #
    #

#
#
#TIPS:
#Anv�nd downpekaren effektivt. Anv�nd den s� fort det dyker upp en �ppnar-parantes.
#anv�nd:
#
#def __init__(self)
#    self.right
#    self.down           #Kan vara none. Bara parantes utryck har en "down-pekare"
#
#weight()  ska anv�ndas f�r att r�kna ut vikten
#anv�nd show()  , den ges p� lydelsen.
#"""
