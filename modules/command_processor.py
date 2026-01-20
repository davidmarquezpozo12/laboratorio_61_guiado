def procesar_comando(text, canvas, luces, resultado_label, ventana):
    """
    Procesa el comando de voz transcrito e interpreta la intención
    del usuario, luego actualiza visualmente el semáforo.

    Args:
    text (str): Texto transcrito desde audio
    canvas (tk.Canvas): Canvas donde están dibujadas las luces
    luces (tuple): (rojo_id, amarillo_id, verde_id) - IDs de los óvalos
    resultado_label (tk.Label): Etiqueta para mostrar resultado
    ventana (tk.Tk): Ventana principal (para cerrar si es necesario)

    Flujo de procesamiento:
    1. Extrae tupla de IDs de luces
    2. Normaliza texto (minúsculas, quita espacios)
    3. Busca palabras clave
    4. Actualiza visualmente el semáforo
    5. Muestra mensaje de feedback

    Cambios visuales:
    - Luz APAGADA: fill="grey20" (gris oscuro)
    - Luz ROJA: fill="red" (rojo)
    - Luz AMARILLA: fill="yellow" (amarillo)
    - Luz VERDE: fill="green" (verde)
    """

    # Desempaqueta la tupla de IDs de las luces
    rojo, amarillo, verde = luces

    # Normaliza el texto a minúsculas para evitar errores de comparación
    text = text.lower()


    # ============================================================
    # COMANDO 1: ENCENDER LUZ ROJA
    # ============================================================

    if "enciende" in text and "roja" in text:
        # Si el texto contiene AMBAS palabras clave "enciende" y "roja"

        # Actualiza colores de las 3 luces
        canvas.itemconfig(rojo, fill="red") # Roja: ENCENDIDA
        canvas.itemconfig(amarillo, fill="grey20") # Amarilla: apagada
        canvas.itemconfig(verde, fill="grey20") # Verde: apagada

        # Muestra mensaje de confirmación
        resultado_label.config(text=" Luz roja encendida")


    # ============================================================
    # COMANDO 2: ENCENDER LUZ AMARILLA
    # ============================================================

    elif "enciende" in text and "amarilla" in text:
        # Si el texto contiene AMBAS palabras clave "enciende" y "amarilla"

        canvas.itemconfig(rojo, fill="grey20") # Roja: apagada
        canvas.itemconfig(amarillo, fill="yellow") # Amarilla: ENCENDIDA
        canvas.itemconfig(verde, fill="grey20") # Verde: apagada

        resultado_label.config(text=" Luz amarilla encendida")


    # ============================================================
    # COMANDO 3: ENCENDER LUZ VERDE
    # ============================================================

    elif "enciende" in text and "verde" in text:
        # Si el texto contiene AMBAS palabras clave "enciende" y "verde"

        canvas.itemconfig(rojo, fill="grey20") # Roja: apagada
        canvas.itemconfig(amarillo, fill="grey20") # Amarilla: apagada
        canvas.itemconfig(verde, fill="green") # Verde: ENCENDIDA

        resultado_label.config(text=" Luz verde encendida")


    # ============================================================
    # COMANDO 4: APAGAR TODAS LAS LUCES
    # ============================================================

    elif "apaga" in text or "todas" in text:
        # Si el texto contiene "apaga" O "todas"
        # (usuario podría decir "apaga todas las luces" o solo "apaga")

        canvas.itemconfig(rojo, fill="grey20") # Todas APAGADAS
        canvas.itemconfig(amarillo, fill="grey20")
        canvas.itemconfig(verde, fill="grey20")

        resultado_label.config(text=" Todas las luces apagadas")


    # ============================================================
    # COMANDO 5: SALIR / CERRAR APLICACIÓN
    # ============================================================

    elif "salir" in text:
        # Si el texto contiene "salir"

        resultado_label.config(text=" Cerrando programa...")

        # Espera 1 segundo (1000 milisegundos) antes de cerrar
        # para que el usuario vea el mensaje
        ventana.after(1000, ventana.destroy)


    # ============================================================
    # COMANDO NO RECONOCIDO (CASO POR DEFECTO)
    # ============================================================

    else:
        # Si ninguno de los comandos anteriores coincide
        resultado_label.config(text=" Comando no reconocido")