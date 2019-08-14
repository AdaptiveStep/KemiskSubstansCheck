import pickle
formelmolekyl = pickle.loads(b'\x80\x03cmolgrafik\nRuta\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00numq\x03X\x01\x00\x00\x002q\x04X\x04\x00\x00\x00nextq\x05NX\x04\x00\x00\x00downq\x06h\x00)\x81q\x07}q\x08(h\x03G@\x00\x00\x00\x00\x00\x00\x00h\x05h\x00)\x81q\t}q\n(h\x03K\x01h\x05Nh\x06NX\x04\x00\x00\x00atomq\x0bX\x01\x00\x00\x00Oq\x0cubh\x06Nh\x0bX\x01\x00\x00\x00Hq\rubh\x0bX\x02\x00\x00\x00()q\x0eub.')
atomlista = pickle.loads(b'\x80\x03]q\x00(X\n\x00\x00\x00H  1.00794q\x01X\x0b\x00\x00\x00He 4.002602q\x02X\x08\x00\x00\x00Li 6.941q\x03X\x0b\x00\x00\x00Be 9.012182q\x04X\t\x00\x00\x00B  10.811q\x05X\n\x00\x00\x00C  12.0107q\x06X\n\x00\x00\x00N  14.0067q\x07X\n\x00\x00\x00O  15.9994q\x08X\r\x00\x00\x00F  18.9984032q\tX\n\x00\x00\x00Ne 20.1797q\nX\x0e\x00\x00\x00Na 22.98976928q\x0bX\n\x00\x00\x00Mg 24.3050q\x0cX\r\x00\x00\x00Al 26.9815386q\rX\n\x00\x00\x00Si 28.0855q\x0eX\x0c\x00\x00\x00P  30.973762q\x0fX\t\x00\x00\x00S  32.065q\x10X\t\x00\x00\x00Cl 35.453q\x11X\n\x00\x00\x00K  39.0983q\x12X\t\x00\x00\x00Ar 39.948q\x13X\t\x00\x00\x00Ca 40.078q\x14X\x0c\x00\x00\x00Sc 44.955912q\x15X\t\x00\x00\x00Ti 47.867q\x16X\n\x00\x00\x00V  50.9415q\x17X\n\x00\x00\x00Cr 51.9961q\x18X\x0c\x00\x00\x00Mn 54.938045q\x19X\t\x00\x00\x00Fe 55.845q\x1aX\n\x00\x00\x00Ni 58.6934q\x1bX\x0c\x00\x00\x00Co 58.933195q\x1cX\t\x00\x00\x00Cu 63.546q\x1dX\x08\x00\x00\x00Zn 65.38q\x1eX\t\x00\x00\x00Ga 69.723q\x1fX\x08\x00\x00\x00Ge 72.64q X\x0b\x00\x00\x00As 74.92160q!X\x08\x00\x00\x00Se 78.96q"X\t\x00\x00\x00Br 79.904q#X\t\x00\x00\x00Kr 83.798q$X\n\x00\x00\x00Rb 85.4678q%X\x08\x00\x00\x00Sr 87.62q&X\x0b\x00\x00\x00Y  88.90585q\'X\t\x00\x00\x00Zr 91.224q(X\x0b\x00\x00\x00Nb 92.90638q)X\x08\x00\x00\x00Mo 95.96q*X\x05\x00\x00\x00Tc 98q+X\t\x00\x00\x00Ru 101.07q,X\x0c\x00\x00\x00Rh 102.90550q-X\t\x00\x00\x00Pd 106.42q.X\x0b\x00\x00\x00Ag 107.8682q/X\n\x00\x00\x00Cd 112.411q0X\n\x00\x00\x00In 114.818q1X\n\x00\x00\x00Sn 118.710q2X\n\x00\x00\x00Sb 121.760q3X\x0c\x00\x00\x00I  126.90447q4X\t\x00\x00\x00Te 127.60q5X\n\x00\x00\x00Xe 131.293q6X\x0e\x00\x00\x00Cs 132.9054519q7X\n\x00\x00\x00Ba 137.327q8X\x0c\x00\x00\x00La 138.90547q9X\n\x00\x00\x00Ce 140.116q:X\x0c\x00\x00\x00Pr 140.90765q;X\n\x00\x00\x00Nd 144.242q<X\x06\x00\x00\x00Pm 145q=X\t\x00\x00\x00Sm 150.36q>X\n\x00\x00\x00Eu 151.964q?X\t\x00\x00\x00Gd 157.25q@X\x0c\x00\x00\x00Tb 158.92535qAX\n\x00\x00\x00Dy 162.500qBX\x0c\x00\x00\x00Ho 164.93032qCX\n\x00\x00\x00Er 167.259qDX\x0c\x00\x00\x00Tm 168.93421qEX\n\x00\x00\x00Yb 173.054qFX\x0b\x00\x00\x00Lu 174.9668qGX\t\x00\x00\x00Hf 178.49qHX\x0c\x00\x00\x00Ta 180.94788qIX\t\x00\x00\x00W  183.84qJX\n\x00\x00\x00Re 186.207qKX\t\x00\x00\x00Os 190.23qLX\n\x00\x00\x00Ir 192.217qMX\n\x00\x00\x00Pt 195.084qNX\r\x00\x00\x00Au 196.966569qOX\t\x00\x00\x00Hg 200.59qPX\x0b\x00\x00\x00Tl 204.3833qQX\x08\x00\x00\x00Pb 207.2qRX\x0c\x00\x00\x00Bi 208.98040qSX\x06\x00\x00\x00Po 209qTX\x06\x00\x00\x00At 210qUX\x06\x00\x00\x00Rn 222qVX\x06\x00\x00\x00Fr 223qWX\x06\x00\x00\x00Ra 226qXX\x06\x00\x00\x00Ac 227qYX\x0c\x00\x00\x00Pa 231.03588qZX\x0c\x00\x00\x00Th 232.03806q[X\x06\x00\x00\x00Np 237q\\X\x0c\x00\x00\x00U  238.02891q]X\x06\x00\x00\x00Am 243q^X\x06\x00\x00\x00Pu 244q_X\x06\x00\x00\x00Cm 247q`X\x06\x00\x00\x00Bk 247qaX\x06\x00\x00\x00Cf 251qbX\x06\x00\x00\x00Es 252qcX\x06\x00\x00\x00Fm 257qdX\x06\x00\x00\x00Md 258qeX\x06\x00\x00\x00No 259qfX\x06\x00\x00\x00Lr 262qgX\x06\x00\x00\x00Rf 265qhX\x06\x00\x00\x00Db 268qiX\x06\x00\x00\x00Hs 270qjX\x06\x00\x00\x00Sg 271qkX\x06\x00\x00\x00Bh 272qlX\x06\x00\x00\x00Mt 276qmX\x06\x00\x00\x00Rg 280qnX\x06\x00\x00\x00Ds 281qoX\x06\x00\x00\x00Cn 285qpe.')

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

    if mol.atom == "( )":       #Om nästa är en molekyl. #Beräknar allting "under" molekylen
        tempvikt = float(weight(mol.down))
        if tempvikt == 0:
            tempvikt = 1
        
        vikt = float(mol.num)*tempvikt     #Molekylgruppens nummer gånger vikten av allting innanför

        if mol.next!= None:                #Räknar ut vikten till höger om parantesen
            nextvikt = weight(mol.next)
            vikt += nextvikt
    if mol.atom != "( )":        #om nästa position är en atom #Beräknar allting under och till höger om parantesen. Eller atomen om det bara är en atom.
        vikt = vikt + float(mol.num)*float(atomweight(mol.atom)) + float(weight(mol.next))



    return vikt
