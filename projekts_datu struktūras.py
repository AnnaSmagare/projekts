import requests
from bs4 import BeautifulSoup
import re

def pēc_fārenheita_uz_celsiju(f):
    return round((f - 32) * 5/9, 1)
def jūdzes_stundā_uz_km_stundā(mph):
    return round(mph * 1.60934, 1)

def iegūt_koordinātas(pilsēta):
    url = "https://nominatim.openstreetmap.org/search"
    parametri = {'q': pilsēta, 'format': 'json', 'limit': 1}
    atbilde = requests.get(url, params=parametri, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    })
    dati = atbilde.json()
    if dati:
        return dati[0]['lat'], dati[0]['lon']
    return None, None

def iegūt_laika_datus(pilsēta):
    platums, garums = iegūt_koordinātas(pilsēta)
    if not platums or not garums:
        print("Neizdevās atrast.")
        return
    saite = f"https://weather.com/weather/today/l/{platums},{garums}"
    galvenes = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
    }
    atbilde = requests.get(saite, headers=galvenes)
    if atbilde.status_code != 200:
        print("Neizdevās ielādēt laika lapu.")
        return

    soup = BeautifulSoup(atbilde.text, 'html.parser')
    temp_spans = soup.find('span', attrs={'data-testid':'TemperatureValue'})
    if not temp_spans:
        print("Nav datu.")
        return

    try:
        temperatura_f = float(temp_spans.text.strip().replace('°',''))
    except:
        print("Nav datu.")
        return
    temp_celsijs = pēc_fārenheita_uz_celsiju(temperatura_f)

    apraksts_div = soup.find('div', attrs={'data-testid':'wxPhrase'})
    apraksts = apraksts_div.text if apraksts_div else "Nav apraksta"

    vēja_span = soup.find('span', attrs={'data-testid':'Wind'})
    vējš = "Nav vēja datu"
    if vēja_span:
        vēja_teksts = vēja_span.text.strip()
        sakritība = re.match(r"(\d+)\s*(km/h|mph)", vēja_teksts)
        if sakritība:
            ātrums = int(sakritība.group(1))
            mērvienība = sakritība.group(2)
            if mērvienība == 'mph':
                ātrums = jūdzes_stundā_uz_km_stundā(ātrums)
            vējš = f"{ātrums} km/h"

    print(f"{pilsēta.capitalize()}:")
    print(f"Temperatūra: {temp_celsijs}°C")
    print(f"Laika apraksts: {apraksts}")
    print(f"Vēja ātrums: {vējš}")

if __name__ == "__main__":
    pilsēta = input("Ievadiet pilsētas nosaukumu: ")
    iegūt_laika_datus(pilsēta)
