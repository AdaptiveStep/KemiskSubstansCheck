class Hashtabell:                                       #Lägg in denna i en egen modul senare.
    def __init__(self,storlek):
        self.size = storlek * 2
        self.slots = [None]*storlek*2                   #i denna lista lagras alla nycklar
        self.data = [None]*storlek*2                    #i denna lista lagras all data

    def put(self,nyckel,data):                          #item = nyckel,,,, data = data.
        hashvalue = self.hashfunction(nyckel)

        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = nyckel
            self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue)
            while self.slots[nextslot] is not None:
                if hashvalue == self.rehash(nextslot):  #Om vi har gått ett varv, så är ju självklart hashtabellen full
                    print('Hashtabell full')
                    return None
                nextslot = self.rehash(nextslot)        #Ger en ny koordinat om slotten är upptagen
            self.slots[nextslot] = nyckel                   #När "tom koordinat" hittats, så ansätts given data på denna slot
            self.data[nextslot] = data

    def get(self,nyckel):
        startslot = self.hashfunction(nyckel)

        data = None
        stop = False
        found = False
        position = startslot                            #Denna kommer ändras för varje hashnings iteration

        while (self.slots[position] is not None) and (not found) and (not stop):
            if self.slots[position] == nyckel:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)        #ger en ny koordinat varje gång det visar sig att slotten är upptagen
                if position == startslot:               #Om vi har sökt igenom ett varv, så ska vi sluta söka.
                    stop = True
        return data

    def hashfunction(self,nyckel):                      #Hashar koordinaten för objektet i listan
        """kapar en första hashning åt nyckel"""
        summ =0
        for pos in range(len(nyckel)):
            summ += ord(nyckel[pos])
        hashval = summ % self.size
        return hashval
    def rehash(self,oldhash):                           #en enkel "probning" används för kollision
        newhash = (oldhash + 1) % self.size
        return newhash                                  #Hashar en ((hashad kordinat)+1) för att få en ny koordinat för payload

    def __setitem__(self, nyckel, data):                # definierar användning av tex H["14"] = "morotskaka". där 14 är nyckel
        assert isinstance(data, object)
        self.put(nyckel,data)
    def __getitem__(self, nyckel):                # H["14] skulle då ge "morotskaka"
        return self.get(nyckel)