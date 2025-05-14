# Gramáticas Probab. Independ. del Contexto
import nltk # Importar la biblioteca NLTK para el procesamiento de lenguaje natural
from nltk import CFG # Importar la gramática libre de contexto (Context-Free Grammar)
from nltk.parse.generate import generate # Importar la función para generar oraciones a partir de la gramática
from nltk import ProbabilisticProduction, Nonterminal, PCFG # Importar la gramática probabilística de contexto libre (Probabilistic Context-Free Grammar)

# Definir las reglas de producción con probabilidades
pcfg_grammar = PCFG.fromstring('''
  S -> NP VP [1.0]
  VP -> V NP [0.7] | V [0.3]
  NP -> 'she' [0.5] | 'he' [0.5]
  V -> 'eats' [0.6] | 'sleeps' [0.4]
''')

# Crear un parser probabilístico usando la PCFG
parser = nltk.ViterbiParser(pcfg_grammar)

# Frase de ejemplo
sentence = ['she', 'eats']

# Parsear la oración y mostrar el árbol sintáctico
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()