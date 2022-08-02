# 3. projekt_engeto
Program election_scrapper.py slouží k extrahování výsledku voleb 2017 (odkaz [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)).

Doporučuji vytvořit si čisté/nové virtuální prostředí pro tento projekt.


# Vytvoření virtuálního prostředí

## Vytvoření příkazem pip:
Ve Vámi zvoleném IDE, pro vytvoření nového virtuálního prostředí, si otevřeme terminál a zadáme následovné:

1. C:\> python -m venv virtualni_prostredi
2. C:\> virtualni_prostredi\Scripts\activate
3. (virtualni_prostredi) C:\>  pip3 --version
4. pip 21.2.3 from ...\lib\site-packages\pip (python 3.10)

- '1. Řádek' - vytvoření virtuálního prostředí s názvem: virtualni_prostredi
- '2. Řádek' - aktivace nového virtuálního prostředí
- '3. Řádek' - začátek řádku značí, které virtuální prostředí je právě aktivní + příkaz pro zjištění verze
- '4. Řádek' - verze příkazu pip3

## Doporučuji vytvoření příkazem conda:

Co je conda + instalace: [Instalace](https://docs.conda.io/en/latest/miniconda.html).
Conda prikazy ve zkratce: [conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

V conda cheatsheet, je jednoduše popsán každý krok:

- založení virtuálního prostředí: conda create --name virtualní_prostredi2 python
- aktivace: conda activate virtualní_prostredi2
- nahrání knihovny: conda install beautifulsoup4 ... nebo .... conda install requests ... atd.
- zjištění aktuálních knihoven a jejich verzí: conda list
- deaktivace: conda deactivate
  




