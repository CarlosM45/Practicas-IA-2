import cv2 # OpenCV es una biblioteca de visión por computadora

imagen = cv2.imread("zenless.png") # Cargar la imagen
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) # Convertir la imagen a escala de grises
canny = cv2.Canny(grises, 50, 200) # Aplicar el detector de bordes Canny
cv2.imshow("Canny", canny) # Mostrar la imagen con bordes detectados
cv2.waitKey(0) # Esperar a que se presione una tecla
cv2.destroyAllWindows() # Cerrar todas las ventanas de OpenCV
