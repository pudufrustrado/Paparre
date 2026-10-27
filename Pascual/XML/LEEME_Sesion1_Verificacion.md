# Sesión 1: XML de los 12 vídeos ligeros (Pascual Ariño) · v3

**Archivo:** `Pascual_Sesion1_12_Videos_Ligeros_1080x1920.xml` (FCP7 `xmeml` v4 para Premiere Pro)

Contiene **una sola secuencia, `PASCUAL S1 - 15 REELS`**, en 1080x1920 a 25 fps con píxel cuadrado. Los 15 reels van seguidos, separados por 2 s de negro. No hay alternativas: queda una versión por reel.

## Pistas
| Pista | Contenido |
|---|---|
| V1 | Mate de color negro en toda la secuencia |
| V2 | Vídeo original. Escala 56,25 % (un 1920x1080 ajustado a 1080 de ancho), centro Y = +0,05 |
| V3 | **Línea A** del header: texto de una sola línea, generador de texto (no es un gráfico esencial). Y = −0,345 |
| V4 | **Línea B** del header: texto de una sola línea, en su propia pista para darle formato por separado. Y = −0,300 |
| A1/A2 | Audio estéreo del original. Cada reel termina con un fundido de audio corto (3–10 frames) para que no corte en seco |

**Marcadores:**
- Al inicio de cada reel: su nombre, las 3 opciones de header y la nota.
- En cada empalme interno: un marcador `· CORTE`.

**Revinculación:** apunta a `0 - Brutos/TANDA LIGERA/<nombre>.mp4`, **sin el sufijo `_1`**.

`headers/` guarda PNG con los emojis en color como referencia visual. No están en la secuencia.

## Reels (posición en la secuencia en mm:ss:ff · cortes en tiempos del bruto)
| Reel | Inicio | Fin | Dur. | Cortes del bruto | Nota |
|---|---|---|---|---|---|
| 01 | 00:00:00 | 00:16:24 | 17,0 s | 00:00.00 → 00:16.96 | Bruto completo: el archivo dura 17 s y no da para más |
| 02 | 00:18:24 | 00:35:17 | 16,7 s | 00:00.00 → 00:16.72 | Intervención de Bernardos completa ("milagro de los panes y los peces... un millón y medio"), el "silencio" del moderador y la réplica de Pascual: "Gracias a los bancos, poquito a poco... un pisito cada año" |
| 03 | 00:37:17 | 01:01:03 | 23,4 s | 00:11.64 → 00:35.08 | |
| 04 | 01:03:03 | 01:56:15 | 53,5 s | 00:00.20 → 00:53.68 | Tras "depende de cómo lo mires" el host pasa a otro invitado: no hay más de Pascual |
| 05 | 01:58:15 | 02:25:07 | 26,7 s | 00:08.60 → 00:35.28 | Ahora es continuo, sin salto. Se oye la frase de Afra a la que responde Pascual |
| 06 | 02:27:07 | 02:52:19 | 25,5 s | 00:00.00 → 00:25.48 | Versión única: termina en "...pueden venir las recompensas". Se quitó el final del camarero |
| 07A | 02:54:19 | 03:40:19 | 46,0 s | 00:00.00 → 00:38.60 + 00:45.80 → 00:53.20 | El 07B va justo detrás si se quieren unir |
| 07B | 03:42:19 | 04:37:05 | 54,4 s | 01:14.52 → 01:32.24 + 01:42.16 → 02:18.88 | Ahora incluye "...dejando de ganar" completo y la entrada de la música |
| 07C | 04:39:05 | 05:22:18 | 43,5 s | 02:47.88 → 03:31.40 | Cierra con "Muchas gracias. Pues bueno, Adriano..." para que lo de "mi nómina" no quede cortado |
| 08 | 05:24:18 | 06:16:07 | 51,6 s | 00:00.00 → 00:51.56 | |
| 09 | 06:18:07 | 06:56:00 | 37,7 s | 00:06.08 → 00:12.36 + 00:20.24 → 00:51.68 | Empieza en "Te has formado en España" |
| 10 | 06:58:00 | 07:48:23 | 50,9 s | 00:00.00 → 00:50.92 | Termina en la última cifra (30.000 € de sociedades). Después solo hay un "Así que..." y entra el tertuliano |
| 11 | 07:50:23 | 08:25:07 | 34,4 s | 00:00.00 → 00:12.32 + 01:04.44 → 01:19.84 + 00:39.36 → 00:46.00 | Montaje invertido: Pascual cierra. El fundido suaviza que Carmen pise el final |
| 12A | 08:27:07 | 09:39:07 | 72,0 s | 00:00.00 → 01:12.00 | |
| 12B | 09:41:07 | 10:44:20 | 63,5 s | 01:13.48 → 02:17.00 | Funciona por sí solo |

## Verificación
- Transcripción palabra a palabra de los proxies (Parakeet v3), contrastada con `Transcripciones_Clips_Pascual.docx`.
- Las entradas y salidas se ajustaron a silencios en la rejilla de 25 fps. Los finales dejan aire hasta justo antes de que entre otra voz.
- Supuesto: originales en 1920x1080 a 25 fps. Si alguno es de 30 fps o de 720p, avisa y lo ajusto.

## Recursos que faltan
Para una respuesta larga de Pascual a Bernardos en el reel 02:
- `0 - Brutos/TANDA PESADA/0427 (1)(1).mp4` (tramo 01:00,6–01:30,8)
- `0 - Brutos/TANDA PESADA/Minuto 30 Enfrentamiento Gonzalo Bernardos.mp4` (tramo 00:07,0–00:38,7)
