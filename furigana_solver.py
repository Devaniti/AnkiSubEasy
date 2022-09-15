from japanese_test import is_digit_char, is_kanji_char

def is_kanji_or_digit_char(char):
    return is_kanji_char(char) or is_digit_char(char)

def solve_furigana_internal(kanji_form, kana_form):
    if len(kanji_form) == 0 and len(kana_form) == 0:
        return [""]
    if len(kanji_form) == 0 or len(kana_form) == 0:
        return []

    if not is_kanji_or_digit_char(kanji_form[0]):
        if kanji_form[0] != kana_form[0]:
            return []
        return [kanji_form[0] + line for line in (solve_furigana_internal(kanji_form[1:], kana_form[1:]))]
    
    i = 0
    for char in kanji_form:
        if not is_kanji_or_digit_char(char):
            break
        i = i + 1
    
    kanji_len = i
    current_kanji = kanji_form[:kanji_len]
    kanji_form_leftover = kanji_form[kanji_len:]

    kanji_form_chars_left = len(kanji_form) - kanji_len
    minimum_reading_len = i
    maximum_reading_len = len(kana_form) - kanji_form_chars_left

    solutions = []

    for reading_len in range(minimum_reading_len, maximum_reading_len + 1):
        current_reading = kana_form[:reading_len]
        kana_form_leftover = kana_form[reading_len:]
        current_notation = ' ' + current_kanji + '[' + current_reading + ']'

        solutions.extend([current_notation + line for line in solve_furigana_internal(kanji_form_leftover, kana_form_leftover)])
    
    return solutions



def solve_furigana(kanji_form, kana_form):
    result = solve_furigana_internal(kanji_form, kana_form)
    if len(result) == 1:
        return result[0].lstrip()
    print("Failed to solve furigana for:[" + kanji_form + "," + kana_form + "]")
    return kanji_form + '[' + kana_form + ']'