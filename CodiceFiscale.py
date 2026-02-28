import requests
from datetime import datetime
from datetime import date

#COLONNA A -> Damian Alex

def chiediDataNascita ():
    print ("SEPARA LE INFORMAZIONI TRAMITE '/' (es: 30/09/2009)")
    valido = False
    while not valido:
        try:
            data = input ("Inserisci la data di nascita: (gg/mm/yyyy): ")
            data = datetime.strptime(data, "%d/%m/%Y")
            if data.day == 29 and data.month == 2:
                if not data.year % 4 == 0:
                    raise
            oggi = data.today ()
            if data.day <= 31 and data.month <= 12 and data.year <= oggi.year:
                return data
            else:
                raise
        except:
            print ("Data inserita non valida!")

def chiediCognome():
    cognome = input("Inserisci il tuo cognome: ")
    if len(cognome) == 0 or len(cognome) < 3:
        raise NameError
    else:
        rimuoviLettereAccentate(cognome)
        rimuoviSpazi(cognome)
        return cognome
            
def calcolaCodiceComune(comune: str):
    cod_comune = requests.get (f"https://api.tcdev.xyz/comune/{comune}")
    cod_comune = cod_comune.json()
    return cod_comune ["codiceCatastale"]

def calcolaCodiceAnno(anno: str, mese: str, giorno:str):
    cod = anno[2] + anno [3] + mese + giorno
    return cod

def calcolaCodiceCognome(cognome: str):
    cons = []
    voc = []
    for let in cognome:
        if let not in ["a","e","i","o","u","A","E","I","O","U"]:
            cons.append(let)
        else:
            voc.append(let)
    if len(cons) + len(voc) > 3:
        if len(cons) >= 3:
            consonanti = cons[0] + cons[1] + cons[2]
            return consonanti
        elif len(cons) == 2:
            consonanti = cons[0] + cons[1] + voc[0]
            return consonanti
        elif len(cons) == 1:
            consonanti = cons[0] + voc[0] + voc[1]
            return consonanti
    else:
        codiceminoredi3 = cons[0] + voc[0] + "X"
        return codiceminoredi3

#COLONNA B -> Foppa Michele

def chiediNome():
    nome = input("Inserisci il tuo nome: ")
    if len(nome) == 0 or len(nome) < 3:
        raise NameError
    else:
        rimuoviLettereAccentate(nome)
        rimuoviSpazi(nome)
        return nome

def chiediSesso():
    sesso=input('Inserisci il tuo sesso(f/m)').strip().lower()
    if sesso!='f' and sesso!='M' and sesso!='F' and sesso!='m':
        raise Exception
    else:
        return sesso.lower()

def calcolaCodiceGiorno(data:datetime,sesso:str):
    if sesso=='m':
        giorno='0'+str(data.day)
    else:
        giorno=str(data.day+40)
    return giorno

def calcoloCIN(cf:str):
    dispari = {
    '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19,
    '9': 21, 'A': 1, 'B': 0, 'C': 5, 'D': 9, 'E': 13, 'F': 13, 'G': 15, 'H': 17,
    'I': 19, 'J': 21, 'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 17,
    'R': 8, 'S': 12, 'T': 14, 'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }

    pari = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }

    resto= {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
    7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N',
    14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
    21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'
    }
    tot=0
    for i in range(len(cf)):
        if (i+1)%2==0:
            tot+=pari[cf[i].upper()]  
        else:
            tot+=dispari[cf[i].upper()]             
    Cin=tot%26
    return resto[Cin]

def genera_CF(Cnome,Ccognome,Cdata,Ccomune,Cin):
    return Ccognome+Cnome+Cdata+Ccomune+Cin

#COLONNA C -> Carrara Alessandro

def rimuoviLettereAccentate(Parola: str):
    return Parola.lower().replace ("à", "a").replace("ò", "o").replace ("è", "e").replace("é", "e").replace ("ì", "i").replace ("ù", "u")

def chiediComune ():
    comune_valido = False
    while not comune_valido:
        try:
            comune = input ("Inserisci il comnune: ").strip().title()
            comuni = requests.get (f"https://api.tcdev.xyz/comune/{comune}")
            comuni = comuni.json()
            if comuni["codiceCatastale"] == "null":
                raise
            else:
                return comune
        except:
            print ("Comune inserito non valido!")

def calcolaCodiceMese (data: datetime):
    cod_mese = None
    mese = data.month
    if mese == 1:
        cod_mese = "A"
    elif mese == 2:
        cod_mese = "B"
    elif mese == 3:
        cod_mese = "C"
    elif mese == 4:
        cod_mese = "D"
    elif mese == 5:
        cod_mese = "E"
    elif mese == 6:
        cod_mese = "H"
    elif mese == 7:
        cod_mese = "L"
    elif mese == 8:
        cod_mese = "M"
    elif mese == 9:
        cod_mese = "P"
    elif mese == 10:
        cod_mese = "R"
    elif mese == 11:
        cod_mese = "S"
    elif mese == 12:
        cod_mese = "T"
    return cod_mese

def calcolaCodiceNome (nome: str):
    cons = []
    voc = []
    cod_nome = ""
    for let in nome:
        if not (let == "a" or let == "e" or let == "i" or let == "o" or let == "u"):
            cons.append (let)
        else:
            voc.append (let)
    if len(cons) >= 4:
        cod_nome += cons[0] + cons[2] + cons[3]
    elif len (cons) == 3:
        cod_nome += cons[0] + cons[1] + cons[2]
    elif len (cons) == 2:
        if len(voc) >= 1:
            cod_nome += cons [0] + cons [1] + voc [0]
        elif len (voc) == 0:
            cod_nome += cons [0] + cons[1] + "x"
    elif len (cons) == 1:
        if len(voc) >= 2:
            cod_nome += cons [0] + voc[0] + voc[1]
        elif len(voc) == 1:
            cod_nome += cons[0] + voc[0] + "x"
        elif len (voc) == 0:
            cod_nome += cons[0] + "xx"
    elif len(cons) == 0:
        if len (voc) >= 3:
            cod_nome += voc [0] + voc[1] + voc[2]
        elif len (voc) == 2:
            cod_nome += voc[0] + voc[1] + "x"
        elif len (voc) == 1:
            cod_nome += voc[0] + "xx"
        elif len(voc) == 0:
            cod_nome += "xxx"
    return cod_nome.upper()

def rimuoviSpazi (Parola: str):
    return Parola.replace (" ", "")

#MAIN
while True:
    cog = chiediCognome ()
    cod_cog = calcolaCodiceCognome (cog)
    nome = chiediNome()
    cod_nome = calcolaCodiceNome (nome)
    data = chiediDataNascita ()
    s = chiediSesso()
    giorno = calcolaCodiceGiorno (data, s)
    mese = calcolaCodiceMese (data)
    cod_nascita = calcolaCodiceAnno (str(data.year), mese, giorno)
    com = chiediComune ()
    cod_com = calcolaCodiceComune (com)
    cin = calcoloCIN (cod_cog + cod_nome + cod_nascita + cod_com)
    cf = genera_CF (cod_nome, cod_cog, cod_nascita, cod_com, cin)
    print (f"Il tuo codice fiscale è: {cf.upper()}")