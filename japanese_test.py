Kana_Ranges = [
  {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
  {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
]

Kanji_Ranges = [
  {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},         # CJK Unified Ideographs
  {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},         # CJK Unified Ideographs Extension A
  {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")}, # CJK Unified Ideographs Extension B
  {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")}, # CJK Unified Ideographs Extension C
  {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")}, # CJK Unified Ideographs Extension D
  {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # CJK Unified Ideographs Extension E
]

Japanese_Ranges = Kana_Ranges + Kanji_Ranges

def is_japanese_char(char):
  return any([range["from"] <= ord(char) <= range["to"] for range in Japanese_Ranges])

def string_contains_japanese(string):
  return any([is_japanese_char(char) for char in string])

def is_kana_char(char):
  return any([range["from"] <= ord(char) <= range["to"] for range in Kana_Ranges])

def string_contains_kana(string):
  return any([is_kana_char(char) for char in string])

def is_kanji_char(char):
  return any([range["from"] <= ord(char) <= range["to"] for range in Kanji_Ranges])

def string_contains_kanji(string):
  return any([is_kanji_char(char) for char in string])