# Gramáticas Probabilísticas Lexicalizadas
import nltk
from nltk import Nonterminal, PCFG

# Definir una gramática PCFG lexicalizada
pcfg_grammar = PCFG.fromstring('''
  S -> NP VP [1.0]
  VP -> V NP [0.7] | V [0.3]
  NP -> 'she' [0.5] | 'he' [0.5]
  V -> 'eats' [0.6] | 'sleeps' [0.4]
''')

# Información léxica añadida (palabra "ancla" con sus categorías sintácticas)
lexical_items = {
    ('eats', 'V'): 0.6,
    ('sleeps', 'V'): 0.4,
    ('she', 'NP'): 0.5,
    ('he', 'NP'): 0.5
}

# Analizador Viterbi que incorpora la información léxica
parser = nltk.ViterbiParser(pcfg_grammar)

# Frase de ejemplo
sentence = ['she', 'eats']

# Parsear la oración con la gramática lexicalizada
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()