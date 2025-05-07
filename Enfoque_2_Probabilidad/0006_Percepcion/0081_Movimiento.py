# Carlos Alejandro Mercado Villalvazo
import cv2

input_video = "video.mp4"


def vid_inf(vid_path):
    # Crear objeto de captura
    cap = cv2.VideoCapture(vid_path)
    # Obtener ancho y altura
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_size = (frame_width, frame_height)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output_video = "output_recorded.mp4"

    out = cv2.VideoWriter(output_video, fourcc, fps, frame_size)

    # Crear el objeto para eliminar el fondo
    backSub = cv2.createBackgroundSubtractorMOG2()

    # Checar si se abrió la cámara
    if not cap.isOpened():
        print("Error opening video file")
    count = 0
    # Leer el video
    while cap.isOpened():
        # Capturar frame por frame
        ret, frame = cap.read()

        if ret:
            # Aplicar eliminación del fondo
            fg_mask = backSub.apply(frame)

            # Aplicar filtro par ignorar las sombras
            retval, mask_thresh = cv2.threshold(fg_mask, 180, 255, cv2.THRESH_BINARY)

            # Configurar el kernel
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            # Aplicar erosión
            mask_eroded = cv2.morphologyEx(mask_thresh, cv2.MORPH_OPEN, kernel)

            # Encontrar bordes
            contours, hierarchy = cv2.findContours(mask_eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            min_contour_area = 500  # Definir valor mínimo para bordes
            # Filtrar bordes
            large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
            frame_out = frame.copy()
            for cnt in large_contours:
                x, y, w, h = cv2.boundingRect(cnt)
                frame_out = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

            # Guardar el video
            out.write(frame_out)

            # Mostrar el frame resultante
            cv2.imshow("Frame_final", frame_out)

            # Presionar Q para salir
            if cv2.waitKey(30) & 0xFF == ord("q"):
                break
        else:
            break

    # Al terminar, soltar video y objeto
    cap.release()
    out.release()
    # Cierra las ventanas
    cv2.destroyAllWindows()


vid_inf(input_video)