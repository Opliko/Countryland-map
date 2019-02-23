# kosci-sithow
Bot pozwalający na rzucanie kośćmi w grupach na jeja.pl

# Instalacja
+ sklonuj repozytorium korzystając z polecenia 
```git clone https://github.com/oplik0/kosci-sithow.git```
+ zainstaluj wymagane biblioteki przechodząc do folderu `kosci_sithow` i uruchamiając polecenie
```pip install -r requirements.txt```
+ dostosuj listę url w `kosci_sithow.py` (10 linijka, wzór pierwszego url już jest i wymaga tylko zmiany numeru i nazwy tematu)
+ dostosuj konto bota - nie daję stąd (oczywiście) dostępu do kąta kosci_sithow, więc musisz mieć do tego własne konto. Wstaw dane logowania w określone miejsce (12 i 13 linijka w `kosci_sithow.py`)

# Użytkowanie
### uruchamianie skryptu:
  uruchomić skrypt możesz np. przez zwykłe `python kosci_sithow.py`
  
### koszystanie z bota na jeja:
  1. napisz jakiś post w tym temacie. Nie jest ważne co w nim jest - możesz umieścić link do tematu, informację za co rzucasz itp.
  2. w miejscu gdzie chcesz mieć rzut wstaw [dice]xky[/dice] - gdzie x zastępujesz liczbą kości, a y liczbą "oczek" w jednej kości. np. [dice]1k6[/dice] rzuci 1 kością o 6 ścianach.
  Kości k4, k6, k8, k10, k12 i k20 mają swoją reprezentację graficzną. Inne wartości są po prostu tekstem
  3. czekaj aż bot się uaktywni - usunie twój post i wstawi swój z zamienionymi tagami [dice] na wyniki rzutów. Bot sprawdza stronę raz na 3 minuty i dodatkowo nie działa od 4 do 6 rano (by ograniczyć liczbę zapytań gdy te nie są potrzebne; możliwe zmiany)
  4. Ciesz się ładnym rzutem :)
