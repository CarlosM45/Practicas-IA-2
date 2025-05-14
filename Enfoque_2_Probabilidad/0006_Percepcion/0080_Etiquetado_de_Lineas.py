# Etiquetados de Líneas
import cv2 # OpenCV es una biblioteca de visión por computadora
import numpy as np # Numpy es una biblioteca de Python para computación científica y arreglo de datos

# Cargar la imagen
img = cv2.imread("msc.png") 

# Preprocesar la imagen
gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY) 

# Aplicar el filtro Gaussiano 7x7
blurred = cv2.GaussianBlur(gray_img, (7, 7), 0) 

# Aplicar el umbral Otsu
# El umbral Otsu es un método de binarización automática
threshold = cv2.threshold(blurred, 0, 255, 
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] 

# Aplicar la dilatación para unir componentes
analysis = cv2.connectedComponentsWithStats(threshold, 
											4, 
											cv2.CV_32S) 
(totalLabels, label_ids, values, centroid) = analysis 

# Inicializar una nueva imagen de salida
# La imagen de salida tendrá el mismo tamaño que la imagen original
output = np.zeros(gray_img.shape, dtype="uint8") 

# Hacer un bucle sobre los componentes
# Ignorar el primer componente (fondo)
for i in range(1, totalLabels): 
	
	# Área del componente
	area = values[i, cv2.CC_STAT_AREA] 
	
	if (area > 140) and (area < 400): 
		componentMask = (label_ids == i).astype("uint8") * 255
		output = cv2.bitwise_or(output, componentMask) 


cv2.imshow("Image", img) 
cv2.imshow("Filtered Components", output) 
cv2.waitKey(0)