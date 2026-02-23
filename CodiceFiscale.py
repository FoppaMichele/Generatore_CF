import requests
def trova_lettere_CF(stringa):
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    CFname=''
    count=0
    for c in stringa:
        if c in consonanti and count<3:
            CFname+=c
            count+=1
    return CFname


def get_codice_catastale(nome_comune):
    url = "https://raw.githubusercontent.com/matteocontrini/comuni-json/master/comuni.json"
    response = requests.get(url)
    response.raise_for_status()
    
    comuni = response.json()
    nome_comune = nome_comune.upper().strip()
    
    for comune in comuni:
        if comune["nome"].upper() == nome_comune:
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