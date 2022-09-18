# AnkiSubEasy

`AnkiSubEasy` is a small python script, that parses Japanese subtitles and makes Anki cards with words from that subtitles

Algorithm:
* Read all lines from all provided subtitle files
* Filter input text
  * Remove text in parenthesis (assuming those mainly include names that we don't want to generate cards for)
* Parse lines into separate words with `fugashi`
  * Unlike most other languages, Japanese doesn't use spaces to separate words
  * In the process, words are getting conjugated into vocabulary form
  * Discard any words that don't contain kanji (assuming those can't be reliably looked up in the dictionary or are already widely known, also helps filter out non-Japanese text, and auto-parsing artifacts)
* Look up each word in the vocabulary
  * Discard any words that can't be looked up in the dictionary
  * Discard any words that are in the known list
  * Generate furigana for word
  * Finally, makes a card and adds the word to the known list

Also notably, `furigana_solver.py` is a library that parses the content of dictionaries - word in kanji form and word in hiragana form and outputs kanji form with attached furigana.
This solver doesn't require any kind of dictionary and solves the problem by pattern matching, so there are some edge cases when it can't decide between multiple possible options, e.g. `'好き嫌い','すききらい'` will get 2 possible solutions - `好[す]き　嫌[きら]い` and `好[すき]き　嫌[ら]い`.
Though such edge cases can be further disambiguated by using a dictionary.

```
usage: main.py [-h] [--knownlist KnownListFile] --out OutFile InFile [InFile ...]

Converts Japanese subtitles to anki cards.

positional arguments:
  InFile                file to get subtitle from

options:
  -h, --help            show this help message and exit
  --knownlist KnownListFile
                        file to load/store list of known words
  --out OutFile         file to store resulting csv
```