# Modelado de lenguaje de n-gramas en NLTK
# Importar las bibliotecas necesarias
import nltk # NLTK es una biblioteca de procesamiento de lenguaje natural
from nltk import bigrams, trigrams # Bigrams y trigrams son funciones de NLTK para crear n-gramas
from nltk.corpus import reuters # Reuters es un corpus de NLTK que contiene noticias
from collections import defaultdict # defaultdict es una subclase de dict que devuelve un valor predeterminado si la clave no existe

# Descargar los recursos necesarios de NLTK
nltk.download('reuters') # Reuters es un corpus de NLTK que contiene noticias
nltk.download('punkt_tab') # Punkt es un tokenizador de NLTK que utiliza un modelo de lenguaje para dividir el texto en oraciones y palabras

# Tokenizar el texto del corpus Reuters en palabras
words = nltk.word_tokenize(' '.join(reuters.words()))

# Crear trigrams a partir de las palabras tokenizadas
# Trigrams son secuencias de tres palabras consecutivas
tri_grams = list(trigrams(words))

# Construir el modelo de lenguaje trigram
# El modelo es un diccionario que almacena la frecuencia de co-ocurrencia de palabras
model = defaultdict(lambda: defaultdict(lambda: 0)) # lambda es una función anónima que devuelve 0 si la clave no existe
# defaultdict es una subclase de dict que devuelve un valor predeterminado si la clave no existe

# Contar frecuencia de co-ocurrencia de palabras
# Para cada trigram, se cuenta la frecuencia de co-ocurrencia de las dos primeras palabras con la tercera
for w1, w2, w3 in tri_grams:
    model[(w1, w2)][w3] += 1

# Transformar las frecuencias en probabilidades
# Para cada par de palabras (w1, w2), se calcula la probabilidad de que w3 siga a (w1, w2)
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# Función para predecir la siguiente palabra
# Esta función toma dos palabras como entrada y devuelve la palabra más probable que sigue a esas dos palabras
def predict_next_word(w1, w2):
    """
    Argumentos:
    w1 (str): Primer palabra.
    w2 (str): Segunda palabra.

    Regresa:
    str: La proxima palabra más probable.
    """
    next_word = model[w1, w2]
    if next_word:
        predicted_word = max(next_word, key=next_word.get)  # Elegir la palabra con la probabilidad más alta
        return predicted_word
    else:
        return "No prediction available"

# Ejemplo de uso
print("Next Word:", predict_next_word('the', 'stock'))