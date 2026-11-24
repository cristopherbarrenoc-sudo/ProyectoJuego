# ==============================================================================
# PROYECTO INTEGRADOR - FASE 3: ENTORNO DE TRABAJO
# Equipo: Los tres cruzados
# Archivo: client.py (Cliente - Jugador 2 "O")
# ==============================================================================

# ESTADO ACTUAL (FASE 3):
# Archivo marcador de posición (solo comentarios). La conexión real por red 
# LAN se programará en la Fase 4.

# CONFIGURACIÓN DE RED (Diseño Fase 2):
# - Máquina Virtual: VM 2 | IP propia: 192.168.56.11
# - IP Servidor: 192.168.56.10 | Puerto: 5000 | Protocolo: TCP

# ¿QUÉ HARÁ ESTE ARCHIVO EN LA FASE 4?
# 1. Crear un socket TCP y conectarse al servidor (192.168.56.10:5000).
# 2. Pedir el nombre del Jugador 2, validar formato (RF-02) y enviarlo.
# 3. Mostrar en pantalla el tablero 3x3 y los mensajes de turno (RF-03).
# 4. Pedir la casilla (1-9) en el turno de "O", validar formato (RF-05) y 
#    enviarla al servidor.
# 5. Recibir y mostrar el resultado final de victoria o empate (RF-07, RF-08).
