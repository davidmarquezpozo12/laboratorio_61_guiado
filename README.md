# Laboratorio 62: Semáforo Tricolor Controlado por Voz con AssemblyAI
## Descripción
Aplicación de control remoto de un semáforo industrial tricolor simulado
mediante reconocimiento de voz en tiempo real usando AssemblyAI como motor
de transcripción cloud.
## Objetivo Educativo
Integrar reconocimiento de voz online (AssemblyAI) con interfaz gráfica
(Tkinter) para controlar un semáforo industrial tricolor simulado,
reforzando conceptos de automatización en Industria 4.0.
## Comandos Disponibles
- "enciende luz roja" → Enciende solo la luz roja
- "enciende luz amarilla" → Enciende solo la luz amarilla
- "enciende luz verde" → Enciende solo la luz verde
- "apaga todas las luces" → Apaga todas las luces
- "salir" → Cierra la aplicación
## Instalación
1. Instalar dependencias:
 pip install -r requirements.txt
2. Configurar API key:
 $env:AAI_API_KEY="tu_clave_api"
3. Ejecutar la aplicación:
 python main.py
## Requisitos
- Python 3.8+
- Micrófono funcional
- Conexión a internet (para AssemblyAI)
- Cuenta en AssemblyAI con API key válida