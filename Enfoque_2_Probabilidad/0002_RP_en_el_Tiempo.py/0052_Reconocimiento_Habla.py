# Reconocimiento del Habla
import speech_recognition as sr # Librería para reconocimiento de voz

# Inicializar clase de reconocimiento
r = sr.Recognizer()

# Leyendo el micrófono como entrada
# Escuchando el habla y guardando en audio_text
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # Recognize dará un error si no puede reconocer el habla debido a la falta de conexión con la API

    try:
        # Usando Google Speech Recognition
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")