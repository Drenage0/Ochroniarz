# Ochroniarz

<div style="max-width: 700px; margin: 0 auto">

## Zasada działania

Ochroniarz jest programem do wykrywania treści niebezpiecznych oraz wrażlwych danych. Aby uruchomić program należy użyć w terminalu komendy: <br>
`python ochroniarz text/(wybranyplik.txt)`. <br>
W folderze text zawarte są dwa pliki tekstowe: `text1.txt` oraz`text2.txt`.

Inną możliwością jest otwarcie Jupiter notebooka "ochroniarz.ipynb", gdzie zawarte są poszczególne fragmenty kodu, które można testować.

#### = ❗Wymagany klucz API OpenAI❗

Do pełnego działania programu wymagane jest dostarczenie działającego klucza API w pliku o nazwie API_KEY, w przeciwnym wypadku wyświetlony zostanie komunikat: <br>
`Error: Błędny klucz API, czy chcesz kontynuować bez sprawdzania mowy nienawiści?` <br>
W razie odpowiedzi: Y(yes), program sprawdzi tylko obecność wrażliwych treści.

#### = Wymagane biblioteki =

Do instalacji bibliotek można użyć komendy:

    pip install -r requirements.txt

Lub zainstalować biblioteki ręcznie:

    pip install spacy
    python -m spacy download en_core_web_sm
    pip install openai
    pip install jupyterlab

#### = Brak wykrycia wrażliwych danych =

Po uruchomieniu program sprawdzi tekst pod kątem wrażliwych danych oraz szkodliwych treści. Jeśli nic nie zostanie wykryte wyświetlą się komunikaty:

<p style="color: lightgreen">✅Nie znaleziono wrażliwych danych </p>
<p style="color: lightgreen">✅Nie znaleziono mowy nienawiści/gróźb/zastraszania/molestowania"</p>

#### = Wykrycie treści niebezpiecznych =

W razie wykrycia szkodliwych danych wyświetlony zostany rodzaj oraz stopień występowania niepożądanej treści w skali od 0 do 1

<p style="color: red">❗Wykryto (nieporządane treści) <span style="color: white">wynik w skali od 0 do 1 </span></p>

#### = Wykrycie wrażliwych danych =

W razie wykrycia wrażliwych danych pojawi się komunikat:

<p style="color: red">❗Wykryto wrażliwe dane </p>

Następnie na podstawie danych utworzony zostanie słownik z kluczami będącymi odnalezionymi wrażliwymi danymi, wartościami natomiast będą placeholdery z unikalnym indeksem.

Kolejnym krokiem będzie zamienienie wrażliwych danych placeholderami ze słownika. Wyświetlony zostanie tekst przed i po zamianie.

Na końcu wyświetli się zapytanie: <br>
`Czy chcesz utworzyć plik \"result.txt\" z placeholderami na wrażliwe dane?` <br>
W razie odpowiedzi N(no), program zostanie zakończony. Jeśli natomiast wpisane zostanie Y(yes), utworzony zostanie plik `result.txt` (lub nadpisany) zawierający zamieniony tekst i utworzony wcześniej słownik.

<p style="color: lightgreen">✅Utworzono plik "result.txt"</p>

## Opis plików

- pliki :

  - `ochroniarz.py` - główny plik python
  - `helpers.py` - pomocnicze funkcje
  - `ochroniarz.ipynb` - główny plik jupyter notebook
  - `API_KEY` - miejsce na klucz API
  - `README` - README
  - `result.txt` - plik z zamienionym tekstem i słownikiem zawierającym wykryte wrażliwe treści i placeholdery
  - `requirements.txt` - wersje używanych przeze mnie bibliotek
  - `RAMBLING.md` - mój rambling

- foldery:
  - `txt/` - zawiera 2 przykładowe pliki txt
  - `img/` - ramblingowe screenshoty

## Użyte narzędzia

- text moderation API OpenAI - treści ofensywne
- spacy library (imiona, nazwiska, segregowanie wyrazów)

## Pole do poprawy

- wykrywanie mowy nienawiści w języku polskim jest co najwyżej średnie. Lepiej działa to nawet jeśli wcześniejszy tekst przetłumaczy się w google translate i ponownie przeładuje do sprawdzenia. Możnaby skorzystać z API google translate do wcześniejszego tłumaczenia na angielski jeśli wykryje jakiś inny język
- lepsza segregacja danych w słowniku. Każda wartość mogłaby być ponumerowana dla każdej grupy eg. PERSON[0], PERSON[1] itd... umożliwiłoby to lepszą segregację danych
- praca nad zminimalizowaniem wykrywania fałszywie pozytywnych wrażliwych danych przez Spacy, użycie własnych filtrów do wyszukiwania, np z uzyciem `RegEx`
- bardziej dokładna obsługa błędów uwzględnienie np. błędów odczytu, zapisu, czy problemy z połączeniem sieciowym

</div>
