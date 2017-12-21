import argparse
import os
import re
from hparams import hparams, hparams_debug_string
from synthesizer import Synthesizer


sentences = [
#    'SIL AY VOWEL7 N EH VOWEL1 V ER VOWEL4 sp S EH VOWEL4 D sp SH IY VOWEL4 sp S T OW VOWEL2 L sp M AY VOWEL6 sp M AH VOWEL3 N IY VOWEL5 sp SIL', #STOLE
#    'SIL AY VOWEL7 N EH VOWEL1 V ER VOWEL4 sp SIL S EH VOWEL4 D sp SH IY VOWEL4 sp S T OW VOWEL4 L sp M AY VOWEL4 sp M AH VOWEL4 N IY VOWEL5 sp SIL', #NEVer
#    'SIL AY VOWEL7 N EH VOWEL1 V ER VOWEL4 sp S EH VOWEL2 D sp SH IY VOWEL4 sp S T OW VOWEL4 L sp M AY VOWEL1 sp M AH VOWEL3 N IY VOWEL3 sp SIL', #MY
#    'SIL AY VOWEL7 N EH VOWEL1 V ER VOWEL4 sp S EH VOWEL4 D sp SH IY VOWEL4 sp S T OW VOWEL4 L sp M AY VOWEL6 sp M AH VOWEL1 N IY VOWEL5 sp SIL', #MONey
'SIL HH AH VOWEL4 L OW VOWEL5 sp SIL IH VOWEL7 T S sp M IY VOWEL5 sp SIL', # singing
'SIL HH EH VOWEL1 L OW VOWEL5 sp IH VOWEL4 T S sp M IY VOWEL5 sp SIL', # not singing
#   'SIL AH VOWEL7 N AH VOWEL6 DH ER VOWEL5 sp AO VOWEL2 R AH VOWEL1 N JH sp SIL', #aNOTHer
#   'SIL AH VOWEL6 N AH VOWEL4 DH ER VOWEL4 sp AO VOWEL4 R AH VOWEL1 N JH sp SIL', #aNOTHer
#    'SIL DH IH VOWEL6 S sp P R AA VOWEL6 JH EH VOWEL4 K T sp W EH VOWEL4 N T sp W EY VOWEL2 sp B EH VOWEL4 T ER VOWEL6 sp DH AH VOWEL6 N sp AY VOWEL6 IH VOWEL6 K S P EH VOWEL3 K T IH VOWEL3 D sp SIL', #WAY
#    'SIL DH IH VOWEL4 S sp P R AA VOWEL4 JH EH VOWEL6 K T sp W EH VOWEL4 N T sp W EY VOWEL1 sp B EH VOWEL4 T ER VOWEL4 sp DH AH VOWEL4 N sp AY VOWEL4 IH VOWEL1 K S P EH VOWEL4 K T IH VOWEL3 D sp SIL', #exPECted
]


def get_output_base_path(checkpoint_path):
  base_dir = os.path.dirname(checkpoint_path)
  m = re.compile(r'.*?\.ckpt\-([0-9]+)').match(checkpoint_path)
  name = 'eval-%d' % int(m.group(1)) if m else 'eval'
  return os.path.join(base_dir, name)


def run_eval(args):
  print(hparams_debug_string())
  synth = Synthesizer()
  synth.load(args.checkpoint)
  base_path = get_output_base_path(args.checkpoint)
  for i, text in enumerate(sentences):
    path = '%s-%d.wav' % (base_path, i)
    print('Synthesizing: %s' % path)
    with open(path, 'wb') as f:
      f.write(synth.synthesize(text))


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--checkpoint', required=True, help='Path to model checkpoint')
  parser.add_argument('--hparams', default='',
    help='Hyperparameter overrides as a comma-separated list of name=value pairs')
  args = parser.parse_args()
  os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
  hparams.parse(args.hparams)
  run_eval(args)


if __name__ == '__main__':
  main()
