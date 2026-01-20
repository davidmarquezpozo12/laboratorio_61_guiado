# ============================================================
# IMPORTACIONES: TRAER FUNCIONES DE LOS MÓDULOS
# ============================================================
from modules.gui_manager import crear_ventana
# Importa: función que crea la interfaz gráfica

from modules.audio_manager import escuchar
# Importa: función que graba, sube y transcribe audio
from modules.command_processor import procesar_comando
# Importa: función que procesa comandos
import tkinter as tk
# Tkinter para widgets adicionales si es necesario
# ============================================================
# FUNCIÓN PRINCIPAL: main()
# ============================================================
def main():
    """
    Función principal que orquesta toda la aplicación.

    Flujo:
    1. Crear la interfaz gráfica
    2. Obtener referencias a todos los widgets
    3. Definir función que se ejecuta al pulsar botón
    4. Crear botón "Escuchar"
    5. Iniciar bucle de eventos
    """

    # ============================================================
    # PASO 1: CREAR INTERFAZ GRÁFICA
    # ============================================================

    # Llama a la función que crea toda la GUI
    # Retorna todos los widgets necesarios
    (ventana, canvas, rojo, amarillo, verde,
     texto_label, resultado_label) = crear_ventana()

    # ============================================================
    # PASO 2: DEFINIR FUNCIÓN DEL BOTÓN
    # ============================================================

    def ejecutar_reconocimiento():
        """
        Se ejecuta automáticamente al pulsar el botón "Escuchar".

        Flujo:
        1. Cambiar texto a "Escuchando..."
        2. Actualizar interfaz (ventana.update())
        3. Grabar y transcribir audio
        4. Cambiar texto a "Procesando..."
        5. Procesar el comando reconocido
        6. Actualizar semáforo según el comando
        """

        # Cambiar etiqueta a "Escuchando..."
        texto_label.config(text=" Escuchando... Habla ahora")
        ventana.update()
        # ventana.update() fuerza a Tkinter a dibujar los cambios inmediatamente

        # ============================================================
        # GRABAR, SUBIR Y TRANSCRIBIR CON ASSEMBLYAI
        # ============================================================

        # Llama a la función escuchar() del módulo audio_manager.py
        # Esta función hace TODO: grabar → subir → transcribir → polling
        text = escuchar()

        # ============================================================
        # MOSTRAR LO QUE EL SISTEMA INTERPRETÓ
        # ============================================================

        # Actualiza la etiqueta con el texto reconocido
        if text:
            # Si hay texto transcrito, mostrarlo
            texto_label.config(text=f"Interpretado: {text}")
        else:
            # Si no hay texto (error o silencio)
            texto_label.config(text="No se entendió, intenta de nuevo...")

        ventana.update()
        # Actualiza la interfaz para mostrar el texto transcrito

        # ============================================================
        # PROCESAR COMANDO Y ACTUALIZAR SEMÁFORO
        # ============================================================

        # Llama a función que interpreta el comando
        procesar_comando(
            text, # Texto transcrito
            canvas, # Canvas del semáforo
            (rojo, amarillo, verde), # IDs de las luces
            resultado_label, # Etiqueta de resultado
            ventana # Ventana (para cerrar si es necesario)
        )


    # ============================================================
    # PASO 3: CREAR BOTÓN "ESCUCHAR"
    # ============================================================

    boton = tk.Button(
        ventana, # Contenedor padre
        text=" Escuchar", # Texto del botón
        command=ejecutar_reconocimiento, # Función que se ejecuta al hacer clic
        font=("Arial", 14), # Fuente: Arial tamaño 14
        bg="#00ffcc", # Fondo: cian
        fg="black", # Texto: negro
        width=15, # Ancho: 15 caracteres
        height=2 # Alto: 2 líneas
    )
    boton.pack(pady=20)
    # Coloca el botón con 20 píxeles de espacio vertical


    # ============================================================
    # PASO 4: INICIAR BUCLE DE EVENTOS (MAINLOOP)
    # ============================================================

    # mainloop() es FUNDAMENTAL en cualquier aplicación Tkinter
    # Mantiene la ventana abierta y escucha eventos del usuario
    # Bloquea la ejecución hasta que se cierre la ventana
    ventana.mainloop()
# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================
if __name__ == "__main__":
 # Este bloque se ejecuta SOLO si este archivo se ejecuta directamente
 # NO se ejecuta si el archivo se importa como módulo en otro programa
 # Esto es una buena práctica en Python

 main() # Llama a la función principal