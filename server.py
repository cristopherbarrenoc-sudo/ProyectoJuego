# ==============================================================================
# PROYECTO INTEGRADOR - FASE 3: ENTORNO DE TRABAJO
# Equipo: Los tres cruzados
# Archivo: server.py (Servidor - Jugador 1 "X")
# ==============================================================================

# ESTADO ACTUAL (FASE 3):
# Archivo marcador de posición (solo comentarios). La programación real de 
# los sockets y la partida completa se implementarán en la Fase 4.

# CONFIGURACIÓN DE RED (Diseño Fase 2):
# - Máquina Virtual: VM 1 | IP: 192.168.56.10 | Puerto: 5000 | Protocolo: TCP

# ¿QUÉ HARÁ ESTE ARCHIVO EN LA FASE 4?
# 1. Crear un socket TCP en 192.168.56.10:5000 y esperar conexión del Cliente.
# 2. Recibir el nombre del Jugador 2 ("CONECTAR|Nombre"), validar (RF-02) y 
#    enviar bienvenida + tablero vacío (RF-03).
# 3. Asignar ficha "X" al Servidor (Jugador 1) y "O" al Cliente (Jugador 2), 
#    alternando turnos tras cada jugada válida (RF-04).
# 4. Recibir la casilla (1-9) del cliente, validar rango y que no esté 
#    ocupada (RF-05).
# 5. Revisar las 8 líneas ganadoras tras cada jugada (RF-06).
# 6. Enviar el tablero actualizado y anunciar ganador o empate (RF-07, RF-08).
