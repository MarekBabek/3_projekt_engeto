# 3. projekt_engeto
Program election_scrapper.py slouží k extrahování výsledků voleb z roku 2017 (odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)).

Doporučuji vytvořit si čisté/nové virtuální prostředí pro tento projekt.

# Vytvoření virtuálního prostředí

### Vytvoření příkazem pip:
Ve Vámi zvoleném IDE, pro vytvoření nového virtuálního prostředí, si otevřeme terminál a zadáme následovné:

- Nápověda příkazu pip: > pip install --help

```
C:\> python -m venv virtualni_prostredi
(vytvoření virtuálního prostředí s názvem: virtualni_prostredi)

C:\> virtualni_prostredi\Scripts\activate
(aktivace nového virtuálního prostředí))

(virtualni_prostredi) C:\>  pip3 --version
(začátek řádku značí, které virtuální prostředí je právě aktivní + příkaz pro zjištění verze)

pip 21.2.3 from ...\lib\site-packages\pip (python 3.10)
(verze příkazu pip)
```

### Doporučuji vytvoření příkazem conda:

Co je conda: [Zde](https://docs.conda.io/en/latest/).

Instalace: [Zde](https://docs.conda.io/en/latest/miniconda.html).

Conda příkazy ve zkratce: [conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

- Nápověda příkazu conda: conda install --help

V conda cheatsheet je jednoduše popsán každý krok:

```
conda create --name virtualní_prostredi2 python
(založení virtuálního prostředí)

conda activate virtualní_prostredi2 
(aktivace virtuálního prostředí)

conda install beautifulsoup4
(nahrání knihovny, například beautifulsoup4)

conda list
(zjištění aktuálních knihoven a jejich verzí)

conda deactivate
(deaktivace virtuálního prostředí)
```

# Nahrání souboru s knihovnami (requirements.txt)

Do nově vytvořeného virtuálního prostředí je potřeba nahrát soubor (requirements.txt), který obsahuje soupis všech knihoven a jejich verzí, které jsou v programu použity.

Pro nahrání requirements.txt zadejte do terminálu:

```
pip3 install -r requirements.txt
conda install --file requirements.txt
```

# Spuštění programu

### Program election_scrapper.py požaduje 2 argumenty ke spuštění
```
1. argument: url daného okresu (např. Kladno): "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103"

2. argument: Váš název csv souboru (např. Kladno_nazev): "Kladno.csv"
```

### Ukázka spuštění:

python3 election_scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103" "Kladno.csv"

Stahuji data ze zadaneho url: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103"

Ukladam do souboru: Kladno.csv

Soubor: Kladno.csv je hotovy ve Vasem adresari

Ukoncuji program: election_scrapper

# Část výstupu programu (Kladno.csv)

```
code,location,registered,votes,envelopes,validvotes,...
533173,Barchovice,185,132,132,8,0,0,11,0,14,11,0,0,2,1,0,27,0,0,8,37,0,2,2,0,1,0,1,7,0
533181,Bečváry,822,492,491,41,0,1,32,0,94,48,3,3,3,0,0,34,0,0,10,167,0,3,6,0,2,0,2,41,1
533190,Bělušice,229,123,123,9,0,0,12,0,16,18,0,1,0,0,0,8,0,0,0,46,0,0,1,0,0,0,0,12,0
533211,BřežanyI,251,147,147,9,0,0,4,0,34,5,2,4,2,0,0,7,0,0,1,51,0,0,11,0,0,0,0,16,1
533220,BřežanyII,567,328,328,42,2,0,22,0,31,19,7,7,6,0,0,48,1,0,16,91,0,0,8,0,3,2,1,20,2
```
