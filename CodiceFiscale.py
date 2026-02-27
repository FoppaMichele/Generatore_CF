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
            return data
        except:
            print ("Formato data non valido!")

def chiediCognome():
    cognome = input("Inserisci il tuo cognome: ")
    if len(cognome) == 0 or len(cognome) < 3:
        raise NameError
    else:
        rimuoviLettereAccentate(cognome)
        rimuoviSpazi(cognome)
        return cognome
            
def calcolaCodiceComune():
    pass

def calcolaCodiceAnno():
    pass

def calcolaCodiceCognome():
    pass

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
def calcolaCodiceControllo():
    nome=calcolaCodiceNome(chiediNome())
    cognome=calcolaCodiceCognome(chiediCognome())
    data=chiediDataNascita()
    sesso=chiediSesso()
    data_cf=f"{calcolaCodiceGiorno(data,sesso)}/{calcolaCodiceMese(data)}/{calcolaCodiceAnno(data)}"
    codice_comune=calcolaCodiceComune(chiediComune())
    print(data_cf)

#COLONNA C -> Carrara Alessandro

def rimuoviLettereAccentate(Parola: str):
    return Parola.lower().replace ("à", "a").replace("ò", "o").replace ("è", "e").replace("é", "e").replace ("ì", "i").replace ("ù", "u")

def chiediComune ():
    comune_valido = False
    while not comune_valido:
        comune = input ("Inserisci il comnune: ").strip().title()
        com_dati = requests.get ("https://comuni-ita.nicolorebaioli.dev/comuni")
        com_dati = com_dati.json()
        trovato = False
        for c in com_dati:
            if c ["nome"] == comune:
                trovato = True
        if trovato:
            return comune
        else:
            print ("Comune non trovato! riprovare")

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
#Da fare alla fine 
data=chiediDataNascita()
sesso=chiediSesso()
data_cf=f"{calcolaCodiceGiorno(data,sesso)}/{calcolaCodiceMese(data)}/{calcolaCodiceAnno(data)}"
print(data_cf)