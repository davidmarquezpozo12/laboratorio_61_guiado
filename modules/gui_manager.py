import tkinter as tk
# Tkinter es la librería estándar de Python para GUI
# ============================================================
# FUNCIÓN PRINCIPAL: CREAR VENTANA GRÁFICA
# ============================================================
def crear_ventana():
    """
    Crea la ventana principal de la aplicación con el semáforo
    tricolor y todos los widgets necesarios.

    Estructura visual:
    - TÍTULO (CONTROL POR VOZ - SEMÁFORO TRICOLOR)
    - CANVAS con semáforo (3 luces redondas)
    - INSTRUCCIONES (Pulsa 'Escuchar' y da un comando)
    - RESULTADO (Mostrar comandos reconocidos)

    Retorna:
    tuple: (ventana, canvas, rojo, amarillo, verde,
    texto_label, resultado_label)

    Cada elemento de la tupla es un widget necesario
    para que main.py pueda controlarlo.
    """

    # ============================================================
    # CREAR VENTANA PRINCIPAL
    # ============================================================

    ventana = tk.Tk()
    # Crea la ventana raíz principal de Tkinter

    ventana.title(" Semáforo controlado por voz")
    # Título que aparece en la barra de ventana

    ventana.geometry("400x500")
    # Tamaño de la ventana: 400 píxeles de ancho, 500 de alto

    ventana.config(bg="#1e1e1e")
    # Fondo oscuro (#1e1e1e = gris muy oscuro casi negro)


    # ============================================================
    # CREAR TÍTULO PRINCIPAL
    # ============================================================

    titulo = tk.Label(
        ventana, # Contenedor padre
        text="CONTROL POR VOZ - SEMÁFORO TRICOLOR", # Texto mostrado
        font=("Arial", 16, "bold"), # Fuente: Arial, tamaño 16, negrita
        bg="#1e1e1e", # Fondo: gris oscuro (igual al fondo
        fg="#00ffcc" # Color de texto: cian/turquesa
    )
    titulo.pack(pady=10)
    # pack() coloca el widget automáticamente
    # pady=10 añade 10 píxeles de espacio vertical arriba y abajo


    # ============================================================
    # CREAR CANVAS (LIENZO) PARA EL SEMÁFORO
    # ============================================================

    # Canvas es como un "papel en blanco" donde podemos dibujar formas
    canvas = tk.Canvas(
        ventana, # Ventana contenedora
        width=150, # Ancho: 150 píxeles
        height=400, # Alto: 400 píxeles
        bg="#111", # Fondo: gris casi negro (simula cuerpo del semáforo)
        highlightthickness=0 # Elimina borde por defecto para aspecto limpio
    )
    canvas.pack(pady=20)
    # pady=20 añade 20 píxeles de espacio vertical


    # ============================================================
    # DIBUJAR LUCES DEL SEMÁFORO EN EL CANVAS
    # ============================================================

    # Crear óvalo (círculo) para la luz ROJA
    # create_oval(x1, y1, x2, y2) dibuja un óvalo dentro del rectángulo
    # definido por (x1,y1) esquina superior izquierda y (x2,y2) inferior derecha
    rojo = canvas.create_oval(
        25, 30, # Esquina superior izquierda (25, 30)
        125, 130, # Esquina inferior derecha (125, 130)
        fill="grey20" # Color inicial: gris oscuro (apagada)
    )
    # Se guarda el ID del óvalo en variable 'rojo' para poder modificarlo luego

    # Crear óvalo para la luz AMARILLA (debajo de la roja)
    amarillo = canvas.create_oval(
        25, 150, # Coordenadas: más abajo que la roja
        125, 250,
        fill="grey20" # Inicialmente apagada
    )

    # Crear óvalo para la luz VERDE (debajo de la amarilla)
    verde = canvas.create_oval(
        25, 270, # Coordenadas: más abajo que la amarilla
        125, 370,
        fill="grey20" # Inicialmente apagada
    )


    # ============================================================
    # CREAR ETIQUETA DE INSTRUCCIONES
    # ============================================================

    texto_label = tk.Label(
        ventana,
        text=" Pulsa 'Escuchar' y da un comando.",
        font=("Arial", 12), # Fuente mediana
        bg="#1e1e1e", # Fondo oscuro
        fg="white" # Texto blanco
    )
    texto_label.pack(pady=10)


    # ============================================================
    # CREAR ETIQUETA DE RESULTADO
    # ============================================================

    # Esta etiqueta mostrará lo que el sistema ha interpretado
    resultado_label = tk.Label(
        ventana,
        text="...", # Texto inicial
        font=("Arial", 14, "bold"),
        bg="#1e1e1e",
        fg="#00ffcc" # Color cian para destacar
    )
    resultado_label.pack(pady=10)


    # ============================================================
    # RETORNAR TODOS LOS WIDGETS
    # ============================================================

    # Retorna una tupla con todos los widgets que main.py necesita
    # en el orden: ventana principal, canvas, y IDs de las 3 luces,
    # más las etiquetas de texto y resultado
    return ventana, canvas, rojo, amarillo, verde, texto_label, resultado_label