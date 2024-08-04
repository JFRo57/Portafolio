import cv2

#Es necesario tener instalado el opencv si no esta instalado ejecutar lo siguiente en la ventana de console
#pip install opencv-python
#pip install numpy

def cargar_imagen(): #Cargar la imagen es el método que necesita que el usuario introduzca la ruta de la imagen a usar
    ruta_imagen = input("Ingrese la ruta de la imagen: ")
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print("No se pudo cargar la imagen.")# Mensaje de error por si la carga no se realiza correctamente
    else:
        cv2.imshow("Imagen Original", imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        propiedades(imagen)
    return imagen

def convertir_a_grises(img):   #Este método convierte a gris la imagen leída
    img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gris = cv2.resize(img_gris, (300, 300))  # Redimensionar la imagen en escala de grises
    cv2.imshow("Imagen en escala de grises", img_gris)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    propiedades(img)

def aplicar_filtro(img): #Este método aplica un filtro de detecciion de bordes usando el algortimo de canny
    img_filtro = cv2.Canny(img, 100, 200)
    cv2.imshow("Imagen con detección de borde", img_filtro)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    propiedades(img)

def propiedades(img): #Este método nos ayuda a mostrar las características haciendo uso de la función shape
    alto, ancho, canales = img.shape
    print("Dimensiones de la imagen:", ancho, "x", alto)
    print("Canales de colores:", canales)
    input("Presiona Enter para continuar...")

def guardar_imagen(img): # Este método nos ayuda a guardar la imagen, de nuevo debemos introducir la ruta
    opcion_guardar = input("¿Desea guardar esta modificación? Escriba 's' para sí o 'n' para no en minúsculas: ")
    if opcion_guardar.lower() == "s":
        ruta_guardar = input("Pega la ruta y el nombre del archivo para guardar la imagen (por ejemplo, 'C:\\documentos\\perromodificado.jpg'): ")
        cv2.imwrite(ruta_guardar, img)
        print("La imagen ha sido guardada en:", ruta_guardar)

def rotar_imagen(img): # Este método simplemente hace uso del rotate para girar la imagen
    img_rotada = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Imagen rotada a 90 grados", img_rotada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    guardar_imagen(img_rotada)

def menu(): #Este es el cuerpo proicipal del programa
    print("1)    Cargar y mostrar la imagen")
    print("2)   Convertir la imagen a escala de grises")
    print("3)   Aplicar un filtro de detección de bordes")
    print("4)   Rotar la imagen")
    print("5)   Mostrar propiedades de la imagen")
    print("6)   Guardar la imagen procesada")
    print("7)   Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    imagen = None
    while True: #Bucle para el pequeño menú
        opcion = menu()

        if opcion == "1":
            imagen = cargar_imagen()
        elif opcion == "2":
            if imagen is not None:
                convertir_a_grises(imagen)
            else:
                print("Primero cargue una imagen.")
        elif opcion == "3":
            if imagen is not None:
                aplicar_filtro(imagen)
            else:
                print("Primero cargue una imagen.")
        elif opcion == "4":
            if imagen is not None:
                rotar_imagen(imagen)
            else:
                print("Primero cargue una imagen.")
        elif opcion == "5":
            if imagen is not None:
                propiedades(imagen)
            else:
                print("Primero cargue una imagen.")
        elif opcion == "6":
            if imagen is not None:
                guardar_imagen(imagen)
            else:
                print("Primero procese una imagen.")
        elif opcion == "7":
            print("Gracias por usar Rafaga Soft")
            break
        else:
            print("Opción no válida. Por favor, seleccione otra opción listada.")

#https://es.from-locals.com/python-opencv-pillow-image-size/
#https://programacionpython80889555.wordpress.com/2022/03/15/transformaciones-geometricas-basicas-en-imagenes-con-pil-y-opencv-rotacion-y-escalado/
#https://docs.opencv.org/4.x/examples.html
#https://imaginaformacion.com/tutoriales/opencv-en-python
