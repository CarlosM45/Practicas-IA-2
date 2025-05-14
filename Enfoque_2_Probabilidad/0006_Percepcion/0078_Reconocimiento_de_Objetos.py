# Reconocimiento de objetos
import cv2 # OpenCV es una biblioteca de visión por computadora
from ultralytics import YOLO # YOLO es un modelo de detección de objetos

# Cargar el modelo YOLO
yolo = YOLO('yolov8s.pt')

# Cargar captura de video
videoCap = cv2.VideoCapture(0)

# Función para obtener colores
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)


while True:
    ret, frame = videoCap.read()
    if not ret:
        continue
    results = yolo.track(frame, stream=True)


    for result in results:
        # Obtener los nombres de las clases
        classes_names = result.names

        # Iterar sobre las cajas detectadas
        for box in result.boxes:
            # Verificar si la confianza es mayor que 0.4
            if box.conf[0] > 0.4:
                # Obtener las coordenadas de la caja
                [x1, y1, x2, y2] = box.xyxy[0]
                # Convertir las coordenadas a enteros
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                # Obtener la clase
                cls = int(box.cls[0])

                # Obtener el nombre de la clase
                class_name = classes_names[cls]

                # Obtener el color respectivo
                colour = getColours(cls)

                # Dibujar el rectángulo alrededor del objeto
                cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)

                # Poner el texto con el nombre de la clase y la confianza
                cv2.putText(frame, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, colour, 2)
                
    # Mostrar la imagen
    cv2.imshow('frame', frame)

    # Romper el bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Desconectar la cámara y cerrar todas las ventanas
videoCap.release()
cv2.destroyAllWindows()