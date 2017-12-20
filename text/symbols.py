'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from text import cmudict

_pad        = '_'
_eos        = '~'
_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? '

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
# symbols = [_pad, _eos] + list(_characters) + _arpabet
symbols = [_pad, _eos] + [
  'AA',
  'AE',
  'AH',
  'AO',
  'AW',
  'AY',
  'B',
  'CH',
  'D',
  'DH',
  'EH',
  'ER',
  'EY',
  'F',
  'G',
  'HH',
  'IH',
  'IY',
  'JH',
  'K',
  'L',
  'M',
  'N',
  'NG',
  'NSN',
  'OW',
  'OY',
  'P',
  'R',
  'S',
  'SH',
  'SIL',
  'T',
  'TH',
  'UH',
  'UW',
  'V',
  'VOWEL0', 'VOWEL1', 'VOWEL2', 'VOWEL3', 'VOWEL4', 'VOWEL5', 'VOWEL6', 'VOWEL7',
  'W',
  'Y',
  'Z',
  'ZH',
  'sp'
]
