#!/usr/bin/env python
# -*- coding: latin-1 -*-

__author__ = 'HARIZ'

# 14 november 2013
# Syntax Lab 7
# BNF för programmet finns nederst på sidan.

from LinkedQ import *
from molgrafik import *
from Atomload import *
from LinkedStack import *
from molgrafik import Molgrafik,Ruta

# Todo Fixa ordning alla kommentarer, stapla och ta bort alla onödiga.
# Todo ta bort alla onödiga T'odo's.
# Todo Ta bort allt skrap pa botten
#

class Syntaxfel(Exception):              #Ett sådant objekt skapas varje gång ett felmeddelande visas.
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
class Formelklass():                #Skall användas rekursivt vid uträkning av vikten. Använd data som finnes i lab 5.
    def __init__(self,atom="",molekyl="",vikt=""):
        self.atom         = atom
        self.molekyl      = molekyl
        self.vikt         = vikt
        self.antal        = 1
        self.molekylantal = 1

def swap(somelist):             # Byter plats på lämpliga None's och ()n's .
    """
    Swappar alla None och ()'s
    Detta görs så att man enkelt kan länka ihop allting med next pekare.
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
def enlink(somelist):           # Sätter plats på länkarna då listan är perfekt ordnad.
    """
    Länkar samman alla element som kommer från en lista. Ger slutgiltig framställning av länkad struktur.
    """
    while len(somelist) > 0:       #Medans listan INTE är tom.
        temp = somelist.pop()
        if temp != None:
            if temp.atom != "()":
                temp.next = enlink(somelist)
            else:
                temp.down = enlink(somelist)     #Ty en ()'s kan ha både ned och next barn.
                temp.next = enlink(somelist)
        else:
            return

        return temp         #Returnerar slutgiltig länkad formel, efter att hela rekursions maskineriet i "enlink" är färdigt.

def  readFormel():

    if q.isEmpty():                         #Kollar kön är tom. (Vilket den aldrig kommer vara)
        print("\n")                         #OM kö är tom så är programmet färdigt (Anropas aldrig i denna version, kan tas bort)
    else:                                   #Annars undersöker den aktuell molekyl. Detta ska returneras till huvudprogrammet.
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
        readMol()               ##### Ändra ej något inne i denna funktion ovanför detta OBS OBS OBS

    prototyplista.append(mol)

    return
def readGroup():
    rutan = Ruta()
    if q.peek().data in bsletter:
        atomgrupp = Formelklass()           #Skapar specifik klass för detta objekt ifall det skulle behövas längre ner. (Men för tillfället används den endast inom denna if-sats.
        atomgrupp.atom = readAtom()
        if q.peek() is not None:            #tillhör första delen av group i BNF definitionen
            if q.peek().data in numbers:
                antalatomer = readNum()       #Ger talet direkt efter atomen. Skall returnera till grafik?
                atomgrupp.antal = float(antalatomer)    #namn och vikt returneras, direkt efter en atom och dess multipel.

        rutan.atom = atomgrupp.atom
        rutan.num  = atomgrupp.antal     #Sammanfattas för enkelhets skull

        return rutan            # ENDAST: "Atom OCH siffra returneras" i ett objekt. Detta är utanför paranteser. ENDAST MED SIFFRA/OR
    elif q.peek().data in ["("]:            #men ska du inte plocka ut parantesen också?
        paranQ.put(q.get)                 #paranQ är parantes pseudo-kö som plockar ut et element varje gång det dyker upp en slutparantes.
        if q.peek() is not None:
            if q.peek().data in [")"]:      #Om slutparantes kommer direkt efter startparantes, så visas felmeddelande.
                raise Syntaxfel("Saknas molekyl mellan paranteser före ")

            tempmol = readMol()             #Annars så läses molekylen in.

            return tempmol                #Skickar tillbaka molekylgruppen till toppen då det lästs färdigt.
            if not paranQ.isEmpty():        #om paranQ är tom efter att molekylen lästs in så är inmatningen fel. Ty paranQ ska ju innehålla en enda parantes.
                raise Syntaxfel("Fattas slutparantes på radslutet")
        else:
            raise Syntaxfel("Fattas slutparantes på radslutet")

    elif q.peek().data in [")"] and not paranQ.isEmpty():
        q.get
        paranQ.get
        if q.peek() is not None:
            if q.peek().data in numbers:
                molekylstorlek = readNum()                #Ger talet efter parantesen. Skall returnera till grafik?
                rutan.num = molekylstorlek
                return rutan
            else: raise Syntaxfel("Saknad siffra vid radslutet ")       #Det kan vara så att formeln råkat ta slut precis efter en parantes
        else: raise Syntaxfel("Saknad siffra vid radslutet ")           #Eller så har det blivit fel på så sätt att det INTE dykt upp en siffra efter slutparantes
    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet ")
def readAtom():
    tempchars = ""
    if q.peek().data in bletter:
            newatom = readBletter()              #Kan komma till nytta senare, ifall hela molekylen innanför parantesen sökes.

            if q.peek() is not None:
                if q.peek().data in sletter:        #Om atomen innehåller en ytterligare liten bokstav i sitt namn?
                    newatom += q.get
            atomExists(newatom)                   #En mindre indentering eftersom det finns atomer med en stor bokstav.
            return newatom
    else: raise Syntaxfel("Saknad stor bokstav vid radslutet ")
def readBletter():
    character = q.get
    if character is None or character in [""]:
        raise Syntaxfel("Fel syntax, förväntades text:")
    elif character in bletter:                  #Följande 3 funktioner är enkla anrop som kollar ifall karaktär är i lista
        return character
    else:
        raise Syntaxfel("Fel syntax, förväntades stor bokstav:" + character)
def readSletter():
    character = q.get
    if character is None:
        raise Syntaxfel("Fel, syntax, förväntades text (med liten bokstav först)")
    elif character in sletter:
        return character
    else:
        raise Syntaxfel("Fel syntax, förväntades liten bokstav (gemen). Gavs: " + character)
def readNum():                              # Lite speciellare än bletter och sletter funktionen
    character = ""                          # Skapar tilfällig variabel
    if int(q.peek().data) > 1:             # om första siffran är större än 2
        while q.peek().data in numbers:     # Så staplas resten av siffrorna upp i en sträng
            character += q.get
            if q.peek() is None:            # om hela listan tar slut så ska while loopen omedelbart brytas
                break
        return character        #Returnerar ett tal över 2 eller ett flersiffrigt tal
    elif q.peek().data == "1":
        character = str(q.get)
        if q.peek() is not None:
            if q.peek().data in numbers:
                while q.peek().data in numbers:     # Så staplas resten av siffrorna upp i en sträng
                    character += str(q.get)
                    if q.peek() is None:            # om hela listan tar slut så ska while loopen omedelbart brytas
                        break
                return  character
            else: raise Syntaxfel("För litet tal vid radslutet ")
        else: raise Syntaxfel("För litet tal vid radslutet ")
    elif q.get in ["0"]: raise Syntaxfel("För litet tal vid radslutet ")
    else:
        raise Syntaxfel("Fel syntax, förväntades siffra. Gavs: " + q.get)   #TODO SIFFRA ELLER TAL? WHAT?
def atomExists(atom):
    for element in atomlista:
        if element.split()[0] == atom:          # eftersom Atomlista = ["H 1.0079" , ... ] så ger element.split() en liten minilista för varje element
            return
    raise Syntaxfel("Okänd atom vid radslutet ")
def inlasning(formel):
    if formel == "":
        raise Syntaxfel("Ingen inmatning")
    else:
        for character in formel:                                                #OBS, Sista tecknet måste ha ett mellanslag och punkt. TODO FIXA detta! FIXAD?
            q.put(character)
        return
def atomweight(atom):       #TODO: fixa hashtabell istället
    """Ange atom som sträng"""
    if atom != None:
        for element in atomlista:
            if element.split()[0] == atom:          # eftersom Atomlista = ["H 1.0079" , ... ] så ger element.split() en liten minilista för varje element
                return float(element.split()[1])
    elif atom == None:
        return 0

    print("Okänd atom vid radslutet ")
def weight(mol):    #Denna rekursiva funktion fungerar lite som enlink funktionen
    vikt = 0

    if mol == None:         # Om mol är None, då är det den sista positionen, och den skall då returners.
        return vikt

    if mol.atom == "()":       #Om nästa är en molekyl. #Beräknar allting "under" molekylen
        tempvikt = float(weight(mol.down))
        if tempvikt == 0:
            tempvikt = 1

        vikt = float(mol.num)*tempvikt     #Molekylgruppens nummer gånger vikten av allting innanför

        if mol.next!= None:                #Räknar ut vikten till höger om parantesen
            nextvikt = weight(mol.next)
            vikt += nextvikt
    if mol.atom != "()":        #om nästa position är en atom #Beräknar allting under och till höger om parantesen. Eller atomen om det bara är en atom.
        vikt = vikt + float(mol.num)*float(atomweight(mol.atom)) + float(weight(mol.next))

    return vikt

def runsyntax(formel):                                                  #Används i mainloopen för att anropa en massa saker från
    try:
        inlasning(formel)
        if formel != "#":
            finalform = readFormel()            #Finalform är en lista med två element. Ett formelobjekt, och dess vikt i float.
            print(" Formeln är syntaktiskt korrekt")
            print("  Vikten är: ", finalform[1])
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

#Globaler för programmet
mg = Molgrafik()                        #Behöver bara laddas en gång.
bletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sletter = "abcdefghijklmnopqrstuvwxyz"
bsletter = bletter+sletter
firstnumbers = "23456789"
numbers = "1234567890"
alfanum = bsletter + numbers
prototyplista = []
paranQ = ListQ()            #Används för att hålla koll på start-slut parantes. ")" plockar ut ett element ur pseudo-stacken, ty det behövs bara vetas ifall datastrukturen blir tom på slutet. Annars hade en riktig stack varit mer lämplig

#Globaler som importeras (vid körning)
#atomlista = ["H 1.005" , "He 2.0234", ...etc]  . Dvs innehåller varje atomnamn och dess vikt.

#Nedan följer samma procedur som exempel i förel 10

while 1:                                                #Main loopen som frågar samma fråga om och om igen.
    q = ListQ()                                         #Bygger upp listan igen, så att gamla ord försvinner från den.
    paranQ =ListQ()

    formel = input("\n Molekyl: ")       #Frågar efter formel.
    oldword = formel
    runsyntax(formel)                                   #

#Konfirmera följande
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
#Använd downpekaren effektivt. Använd den så fort det dyker upp en öppnar-parantes.
#använd:
#
#def __init__(self)
#    self.right
#    self.down           #Kan vara none. Bara parantes utryck har en "down-pekare"
#
#weight()  ska användas för att räkna ut vikten
#använd show()  , den ges på lydelsen.
#"""
