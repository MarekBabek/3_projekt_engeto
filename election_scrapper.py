"""
projekt_3.py: tøetí projekt do Engeto Online Python Akademie

author: Marek Bábek

email: marek.babek@&centrum.cz

discord: Pixoun #0920
"""

import sys
import csv
from bs4 import BeautifulSoup
import requests


# funkce - Spuštìní celého programu
def main():
    check_arguments()
    code_region_url = code_region_url_list()
    print(f'Stahuji data ze zadaneho url: {sys.argv[1]}')
    print(f'Ukladam do souboru: {sys.argv[2]}')
    create_csv_file(code_region_url)


# funkce - Scrapování url pomocí importované beautifulsoup knihovny
def url_tool(url1) -> BeautifulSoup:
    req = requests.get(url1)
    return BeautifulSoup(req.text, 'html.parser')


# funkce - Kontrola zadaných argumentù
def check_arguments():
    if len(sys.argv) != 3:
        print('Program need 2 arguments, <url> <file name>, exiting the program...')
        exit()
    elif 'https://volby.cz/pls/ps2017nss/' not in sys.argv[1]:
        print('Wrong first argument, exiting the program...')
        exit()
    elif not sys.argv[2].endswith('.csv'):
        print('Wrong file suffix, exiting the program.')
        exit()


# funkce - Vyscrapované kódy regionù pøidává do listu
def get_region_code(soup) -> list:
    region_code_list = []

    tab_header = soup.find('div', {'id': 'inner'})
    for code in tab_header.find_all('td', {'class': 'cislo'}):
        code_tab = code.find('a')
        region_code_list.append(code_tab.get_text())
    return region_code_list


# funkce - Vyscrapované jména regionù pøidává do listu
def get_region_name(soup) -> list:
    region_name_list = []

    tab_header = soup.find('div', {'id': 'inner'})
    for name in tab_header.find_all('td', {'class': 'overflow_name'}):
        region_name_list.append(name.get_text())
    return region_name_list


# funkce - Pøidává jednotlivé url obcí do listu
# Po scrapování url, najde øádek s url obce (výsledkem jsou 2 øádky s url pro 1 obec)
# následnì vybere pouze 1 øádek a pøídá k univerzální url (výsledekem je url obce)
def get_region_url(soup) -> list:
    primary_url = 'https://volby.cz/pls/ps2017nss/'
    region_url_list = []

    url_header = soup.find('div', {'id': 'inner'})

    for number, town_url in enumerate(url_header.find_all('a')):
        if number % 2 == 0:
            region_url = str(town_url.get('href'))
            full_url = primary_url + region_url
            region_url_list.append(full_url)
    return region_url_list


# funkce - Odstranìní kódu \xa0
def decode(string):
    return string.replace(u'\xa0', u' ')


# funkce - Scrapuje volièe v seznamu + vydané obálky + platné hlasy obcí a pøidává do listu
# Ze stringu na integer, odstranìní kódu \xa0, odstranìní mezery v èísle, pøidání do listu
def registered_envelopes_valid(soup) -> list:
    headers = ['sa2', 'sa3', 'sa6']
    r_e_v_list = []
    for x in headers:
        value = soup.find('td', {'headers': f'{x}'})
        y = decode(value.text)
        r_e_v_list.append(int(y.replace(' ', '')))
    return r_e_v_list


# funkce - Scrapuje názvy stran obcí a pøidává do listu
def parties_names(soup) -> list:
    statement_list = []
    for row in soup.find_all('td', {'class': 'overflow_name'}):
        statement_list.append(row.get_text(''))
    return statement_list


# funkce - Vytvoøení záhlaví
def create_header(soup) -> list:
    heading_list1 = ['code', 'location', 'registered votes', 'envelopes', 'valid votes']
    heading_list2 = parties_names(soup)
    return heading_list1 + heading_list2


# funkce - Získá platné hlasy každé strany (1. tabulky a následnì 2. tabulky) a pøidá výsledky postupnì do listu
# Pokud "text" neobsahuje (-, neboli prázdné místo v tabulce),
# získá "text", odstraní \xa0 kód + mezeru a pøidá do listu
def parties_votes(soup) -> list:
    parties_votes_list = []

    vote_tab_one = soup.find_all('td', attrs={'headers': 't1sa2 t1sb3'})
    vote_tab_two = soup.find_all('td', attrs={'headers': 't2sa2 t2sb3'})

    for vote in vote_tab_one:
        if vote.text != '-':
            x = decode(vote.text)
            parties_votes_list.append(int(x.replace(' ', '')))

    for vote in vote_tab_two:
        if vote.text != '-':
            y = decode(vote.text)
            parties_votes_list.append(int(y.replace(' ', '')))
    return parties_votes_list


# funkce - výsledné kódy, jména a url regionù zazipuje do listu
# ukázka: [(506761, Alojzov, url_obce), (589268, Bedihoš, url_obce), (atd...)]
def code_region_url_list() -> list:
    url = sys.argv[1]

    soup = url_tool(url)
    region_codes = get_region_code(soup)
    region_name = get_region_name(soup)
    region_urls = get_region_url(soup)
    return list(zip(region_codes, region_name, region_urls))


# funkce - Spojení volièe v seznamu + vydané obálky + platné hlasy + platné hlasy stran (celý øádek s výsledky obce)
# ukázka pro okres: Prostìjov, obec: Alojzov
# (https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103)
# (205, 145, 144, 29, 0, 0, 9, 0, 5, 17, 4, 1, 1, 0, 0, 18, 0, 5, 32, 0, 0, 6, 0, 0, 1, 1, 15, 0)
def connection(soup):
    return registered_envelopes_valid(soup) + parties_votes(soup)


# funkce - Vytvoøení csv soboru: scrapování url, vepsání záhlaví, scrapování každé url obce + výpis údajù
# postupnì vpisuje øádky: kód, název obce a dále postupnì celý øádek pro danou obci (viz. def connection výše)
def create_csv_file(code_region_url) -> csv:
    primary_url = sys.argv[1]
    file_name = sys.argv[2]

    soup_primary_url = url_tool(primary_url)
    region_urls = get_region_url(soup_primary_url)
    single_url = url_tool(region_urls[0])

    header = create_header(single_url)

    with open(f'{file_name}', mode='w', encoding="UTF-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for x in code_region_url:
            url2 = x[2]
            soup = url_tool(url2)
            statement_together = connection(soup)
            writer.writerow([x[0], x[1]] + statement_together)
        print(f'Soubor {file_name} je hotovy ve Vasem adresari')
        print(f'Ukoncuji program: {sys.argv[0]}')


if __name__ == '__main__':
    main()
