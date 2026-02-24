import requests
def trova_lettere_CF(stringa):
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    CFname=''
    count=0
    for c in stringa:
        if c in consonanti:
            if count==1 or count==3 or count==4:
                CFname+=c
            count+=1
    return CFname


def get_codice_catastale(comune):
    url = "https://raw.githubusercontent.com/matteocontrini/comuni-json/master/comuni.json"
    response = requests.get(url)
    response.raise_for_status()
    
    comuni = response.json()
    comune = comune.upper().strip()
    
    for comune in comuni:
        if comune["nome"].upper() == comune:
            return comune["codiceCatastale"]
    
    return None
def get_dati_utente():
    cf=''
    nome=input("Inserisci il tuo nome:").upper()
    cf+=trova_lettere_CF(nome)    
    cognome=input("Inserisci il tuo cognome:").upper()
    cf+=trova_lettere_CF(cognome)
    print(cf)
get_dati_utente()