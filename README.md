# 3. projekt_engeto
Program election_scrapper.py slouží k extrahování výsledku voleb 2017 (odkaz [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)).

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

- Nápověda příkazu conda: > conda install --help

V conda cheatsheet, je jednoduše popsán každý krok:

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

# Spustění programu

### Program election_scrapper.py požaduje 2 argumenty ke spuštění
```
1. argument - url daného okresu (např. Beroun): "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"

2. argument - Váš název csv souboru (např. Beroun_nazev): "Beroun_nazev.csv"
```

# Ukázka spuštění:

python3 election_scrapper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102" "Beroun_nazev.csv"

Získávám data z url: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102"

Ukládám do souboru: Beroun_nazev

Hotovo, soubor csv je ulozen...

