import argparse
import fugashi
from pysubparser import parser
from jamdict import Jamdict
from furigana_solver import solve_furigana
from japanese_test import string_contains_kanji
from text_filter import filter_text

jam = Jamdict()

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Converts Japanese subtitles to anki cards.')
    argparser.add_argument('filename', metavar='InFile', type=str, nargs='+',
                        help='file to get subtitle from')
    argparser.add_argument('--knownlist', metavar='KnownListFile', help='file to load/store list of known words')
    argparser.add_argument('--out', metavar='OutFile', help='file to store resulting csv', required=True)
    args = argparser.parse_args()

    knownlist = []

    if args.knownlist != None:
        try:
            with open(args.knownlist, "r", encoding="utf-8") as f:
                knownlist = [line.rstrip() for line in f]
        except EnvironmentError:
            pass

    lines = []
    files = args.filename

    # Read all lines from all provided subtitle file
    for file in files:
        subtitles = parser.parse(file)
        for subtitle in subtitles:
            lines.append([subtitle.text, file])

    # Filter input text
    lines = [[filter_text(line[0]), line[1]] for line in lines]

    # Parse lines into words with fugashi
    words = []
    tagger = fugashi.Tagger()
    for line in lines:
        for word_tag in tagger(line[0]):
            # orthBase is vocabulary form that uses same script as input (kanji/kana)
            word = str(word_tag.feature.orthBase)
            if string_contains_kanji(word) and word not in words:
                words.append([word, line[1]])

    # Look up each word in vocabulary
    cards = []
    for word in words:
        lookup = jam.lookup(word[0])
        if len(lookup.entries) > 0:
            entry = lookup.entries[0]
            cardWord = str(entry.kanji_forms[0])
            if cardWord in knownlist:
                continue
            knownlist.append(cardWord)
            cardMeaning = str('; '.join([', '.join([gloss.text for gloss in sense.gloss]) for sense in entry.senses])).strip()
            cardFurigana = solve_furigana(cardWord, str(entry.kana_forms[0]))
            cards.append([cardWord, cardMeaning, cardFurigana, word[1]])

    with open(args.out, "w", encoding="utf-8") as f:
        f.write('\n'.join(['^'.join(card) for card in cards]))

    if args.knownlist != None:
        with open(args.knownlist, "w", encoding="utf-8") as f:
            f.write('\n'.join(knownlist))
