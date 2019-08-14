import pickle
from LinkedStack import *
listan = pickle.loads(b'\x80\x03]q\x00(cmolgrafik\nRuta\nq\x01)\x81q\x02}q\x03(X\x04\x00\x00\x00atomq\x04X\x02\x00\x00\x00()q\x05X\x04\x00\x00\x00nextq\x06NX\x03\x00\x00\x00numq\x07X\x01\x00\x00\x007q\x08X\x04\x00\x00\x00downq\tNubh\x01)\x81q\n}q\x0b(h\x04X\x01\x00\x00\x00Oq\x0ch\x06Nh\x07K\x01h\tNubh\x01)\x81q\r}q\x0e(h\x04X\x01\x00\x00\x00Hq\x0fh\x06Nh\x07G@(\x00\x00\x00\x00\x00\x00h\tNubNh\x01)\x81q\x10}q\x11(h\x04h\x05h\x06Nh\x07X\x01\x00\x00\x004q\x12h\tNubh\x01)\x81q\x13}q\x14(h\x04h\x05h\x06Nh\x07X\x01\x00\x00\x002q\x15h\tNubh\x01)\x81q\x16}q\x17(h\x04h\x0fh\x06Nh\x07K\x01h\tNubh\x01)\x81q\x18}q\x19(h\x04h\x0ch\x06Nh\x07K\x01h\tNubh\x01)\x81q\x1a}q\x1b(h\x04h\x0ch\x06Nh\x07K\x01h\tNubh\x01)\x81q\x1c}q\x1d(h\x04h\x0ch\x06Nh\x07K\x01h\tNubh\x01)\x81q\x1e}q\x1f(h\x04X\x01\x00\x00\x00Cq h\x06Nh\x07K\x01h\tNubNh\x01)\x81q!}q"(h\x04X\x02\x00\x00\x00Caq#h\x06Nh\x07G@@\x80\x00\x00\x00\x00\x00h\tNubNh\x01)\x81q$}q%(h\x04X\x02\x00\x00\x00Feq&h\x06Nh\x07K\x01h\tNube.')

########################################################################

class Ruta:
    def __init__(self, atom = "()", num = 1):
        self.atom = atom
        self.num = num
        self.next=None
        self.down=None

def swap():             # Byter plats på lämpliga None's och ()n's .
    """
    hitta först alla none och ()s och returnerna deras positioner i en dubbellista
     ta none med lägst indext och swappa det med ()'s som har högst index.
     ta none med lite högre index och swappa det med ()'s som har lägre index.
    fortsätt så tils pekarna mött mittpunkten. Då är swapprocessen avslutad.

    Det som returneras är en lista, där första elementet innehåller none-positionerna, \
    och andra elementet innehåller grupp-positionerna.
    """
    tempstack = Stack()
    counter = -1
    for i in listan:
        counter += 1
        if i == None:
            listan[counter] = tempstack.pop()
        elif i.atom == "()":
            tempstack.push(i)
            listan[counter] = None

def enlink():           # Sätter plats på länkarna då listan är perfekt ordnad.

    while len(listan) >0:       #Medans listan INTE är tom.
        temp = listan.pop()
        if temp != None:
            if temp.atom != "()":
                temp.next = enlink()
            else:
                temp.down= enlink()     #Ty en ()'s kan ha både ned och next barn.
                temp.next = enlink()
        else:
            return
                
        return temp         #Returnerar slutgiltig länkad formel, efter att hela rekursions maskineriet i "enlink" är färdigt.


def printer(somelist):
    for i in somelist:
        if i != None:
            None
            print(i.atom, i.num, "|", end=" ")
        else:
            None
            print(i, "|", end = " ")

swap()
finalthing = enlink()
