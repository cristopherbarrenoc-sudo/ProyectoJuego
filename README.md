# TRES EN RAYA

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo B

Juego por turnos para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

## Integrantes

- Christopher Barreno
- Marcos Castillo
- Ismael Moya

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta del repositorio:

```
python juego.py          (menú)
python game_logic.py     (validación de la jugada y fin de la partida)
```

## Estructura del repositorio

| Archivo | Qué hace | Estado |
|---|---|---|
| `juego.py` | Es la parte que corresponde y muestra el menú hasta que el usuario mediante las diferentes opciones decida salir. Es la parte DF1 del programa. | Terminado |
| `game_logic.py` | Es la parte encargada de revisar toda la parte lógica y que se encarga de verificar si el espacio de una ficha está disponible para jugar o si se necesita ocupar otro espacio(DF2). Tambien verifica el final de la partida, comprueba si durante la partida, el usuario no ha logrado completar 3 ficha en una fila y en caso de hacerlo mostrar el mensaje de ganador(DF3).  | Terminado |
| `server.py` | Será el encargado de abrir un socket donde ambos equipos puedan jugar, se esperará al jugador 2, y al momento de empezar la jugada se enviará el estado de mesa y recibiran las jugadas. | Pendiente |
| `client.py` | Será el encargado de conectarse al servidor mediante una diracción IP seleccionada por nosotros,va a mostrar la mesa y enviará las jugadas realizadas al jugador2. | Pendiente |
| `diseno/` | Diagramas `.rap` de la Fase 2 | Subido |

## Del diseño al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió al traducirlo |
|---|---|---|
| DF1 Partida completa (solo el menú) | `juego.py`, líneas 1-7 | En RAPTOR usamos la variable while pararepetir el menú y que esta salga en el momento que el resultado sea false. En python usamos la variable while True para que el menú pueda seguir repitiendose hasta que exista la opción de salir o break. Mediante el uso de input() se guarda lo que los jugadores escriben mediante texto, comparandose de esta manera con "1" y no con el número uno en el momento del bucle, y para la opción jugar solo pusimos print("Juego") para que eso logre ver el usuario por el momento. |
| DF2 Validación de la jugada | `game_logic.py`, líneas 1-6 y 16-33 | En RAPTOR el ciclo se repite hasta que la condición se cumple, pero en pyhton el while se sigue repitiendo mientras la condición se cumple. Por eso al realizar el programa hacemos uso de dos variables, como lo son numero y casillas_validas, las cuales tienen un valor de false y la única forma de cambiar es cuando el valor es correcto volviendose true. Hacemos uso del for para crear la tabla con espacion y creamos una lista en pythin para poder usarla, al momento de verificar si lo que escribimos es correcto usamos .isdigit() y después un int() para pasar el resultado a un númore entero. |
| DF3 Fin de la partida | `game_logic.py`, líneas 8-15 y 37-64 | En el diagrama el cilo termina cuando gana == 1 or jugadas == 9, ya que en python el while funciona al revés, al pasarlo al código lo cambiamos a while gana !=  1and jugadas != 9. Tambien se agregaran variables al inicio como lo son: actual, jugador1 y jugador2 y también colocamos que si un jugador escribe algo que no es un número, y valga 0 con el fin que el programa no se caiga debido a esto. |

<!-- El bucle de turnos de DF1 (la partida completa) se programa en la Fase 4. -->

<!-- Ejemplo (dominó): DF2 · game_logic.py, líneas 20-31 · El Loop de RAPTOR pasó a ser un while que se repite
mientras el número de ficha no esté en la mano del jugador o no encaje en un extremo. -->

## Video explicativo

[https://youtu.be/flracy9UQKM] (máximo 5 minutos: el menú, la validación con una jugada inválida, el fin de la partida y cómo
tradujimos un diagrama a código).

## Licencia

Este proyecto se distribuye bajo la licencia [MIT]. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos
citados en la sección «Créditos».

## Créditos

| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| Pygame | Comunidad de Pygame (originalmente Pete Shinners) | Ventana gráfica, menú de selección de modo(local/en linea) y tablero | LGPL |
| Socket | Python Software Foundation (biblioteca estándar de Python) | Conexión cliente-servidor y envío de jugadas en el modo en línea | PSF License |
| Threading | Python Software Foundation (biblioteca estándar de Python) | Recepción de datos de red en segundo plano sin congelar la ventana gráfica | PSF License |

### Uso de IA

<!-- Si no usaron IA, escriban: «No se usaron herramientas de IA». -->

| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| GEMINI IA | Ayudó a corregir validaciones en ciertos while que daba error. | Cambiamos ciertos while que nos producía un error lógico al momento de ejecutar el programa. |
