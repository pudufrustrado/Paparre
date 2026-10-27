# Sesión 1: XML de los 12 vídeos ligeros (Pascual Ariño)

**Archivo:** `Pascual_Sesion1_12_Videos_Ligeros_1080x1920.xml` (FCP7 `xmeml` v4 para Premiere Pro)
Contiene una bin con **2 secuencias** (1080x1920, 25 fps, píxel cuadrado). Dentro de cada una, los reels van seguidos con **2 s de negro** entre ellos. Al inicio de cada reel hay un marcador con su nombre, las 3 opciones de header y la nota de montaje, y cada empalme interno lleva un marcador `· CORTE`.

**`PASCUAL S1 - 15 REELS (MASTER)`** (duración 10:39). Posición de cada reel en la línea de tiempo (mm:ss:ff):

| Reel | Inicio | Fin | Reel | Inicio | Fin |
|---|---|---|---|---|---|
| 01 | 00:00:00 | 00:15:21 | 07C | 04:33:00 | 05:13:19 |
| 02 | 00:17:21 | 00:30:06 | 08 | 05:15:19 | 06:07:08 |
| 03 | 00:32:06 | 00:55:10 | 09 | 06:09:08 | 06:50:16 |
| 04 | 00:57:10 | 01:50:17 | 10 | 06:52:16 | 07:43:10 |
| 05 | 01:52:17 | 02:14:22 | 11 | 07:45:10 | 08:19:19 |
| 06 | 02:16:22 | 02:48:11 | 12A | 08:21:19 | 09:33:19 |
| 07A | 02:50:11 | 03:35:22 | 12B | 09:35:19 | 10:39:04 |
| 07B | 03:37:22 | 04:31:00 | | | |

**`PASCUAL S1 - ALTERNATIVAS (ALT)`** (duración 1:52):

| Reel | Inicio | Fin |
|---|---|---|
| 01-ALT | 00:00:00 | 00:10:19 |
| 02-ALT | 00:12:19 | 00:28:02 |
| 06-ALT | 00:30:02 | 00:55:15 |
| 10-ALT | 00:57:15 | 01:27:21 |
| 11-ALT | 01:29:21 | 01:52:20 |

Para exportar cada reel: marca In/Out sobre sus límites (o usa los marcadores) y exporta el rango.

## Cómo está armado cada reel
| Pista | Contenido |
|---|---|
| V1 | Mate de color negro (#000000) en toda la secuencia |
| V2 | Vídeo original. Escala 56,25 % (un 1920x1080 ajustado a 1080 de ancho), centro Y = +0,05 |
| V3 | Generador de texto con el **Header principal** (2 líneas, `&#13;`). Origen Y = −0,32, Inter Bold 52, blanco |
| V4 | **Desactivada.** PNG del mismo header con emojis en color (`headers/HEADER_xx.png`). Es el respaldo por si Premiere no muestra los emojis del generador: actívala y desactiva V3 |
| A1/A2 | Audio estéreo del original, vinculado al vídeo |

**Marcadores de secuencia:**
- En el frame 0: las 3 opciones de header y una nota de montaje.
- En cada empalme: qué se dice en ese tramo.

**Revinculación:** el XML apunta a `0 - Brutos/TANDA LIGERA/<nombre>.mp4` **sin el sufijo `_1`**. Los nombres conservan la normalización Unicode (NFD) de los archivos subidos, que es la habitual en macOS. Si Premiere pide localizar el medio, basta con apuntar a la carpeta de los originales.

## Cómo se verificó
- Transcribí los 12 proxies con ASR palabra a palabra (Parakeet v3) y afiné cada punto de entrada y salida sobre la energía del audio, buscando el silencio en la rejilla de 25 fps.
- Identifiqué a Pascual visualmente plano a plano.
- Re-transcribí el inicio y el final de cada corte ya montado para confirmar que empieza y termina en las palabras correctas. Los resultados están en la tabla.

## Tabla final (tiempos del bruto)
| Sec. | Dur. | Cortes (IN → OUT) | Cambios respecto al brief |
|---|---|---|---|
| 01 | 15,8 s | 00:01.04 → 00:16.88 | Quita ruido de 0–1 s |
| 01-ALT | 10,8 s | 00:06.12 → 00:16.88 | Alternativa del brief |
| 02 (HOOK) | 12,4 s | 00:00.00 → 00:12.40 | Termina en "...un millón y medio" |
| 02-ALT | 15,3 s | 00:00.00 → 00:12.40 + 00:13.76 → 00:16.68 | **Hallazgo:** Pascual sí responde ("Gracias a los bancos, poquito a poco... un piso cada año") |
| 03 | 23,2 s | 00:11.64 → 00:34.80 | El brief entraba en 9,82 s, a mitad de frase. Ahora entra en "¿Qué beneficios...?" |
| 04 | 53,3 s | 00:00.20 → 00:53.48 | El brief (53,00 s) cortaba "depende de cómo lo mires" |
| 05 | 22,2 s | 00:08.60 → 00:25.96 + 00:30.44 → 00:35.28 | En 30,84 s se perdía "Viendo...". Sale antes del "Pero sigo" de Afra |
| 06 | 31,6 s | 00:00.00 → 00:25.52 + 00:48.88 → 00:54.92 | ⚠️ Ver aviso 1 |
| 06-ALT | 25,5 s | 00:00.00 → 00:25.52 | Cierre garantizado en Pascual ("...las recompensas") |
| 07A | 45,4 s | 00:00.00 → 00:38.60 + 00:45.80 → 00:52.64 | Bordes ajustados a silencios |
| 07B | 53,1 s | 01:14.52 → 01:32.24 + 01:42.16 → 02:17.56 | En 1:42,72 se perdía "¿Cuáles...?" |
| 07C | 40,8 s | 02:47.88 → 03:28.64 | Cierra en "para no depender solo de mi nómina" (el brief seguía con despedidas hasta 3:32,56) |
| 08 | 51,6 s | 00:00.00 → 00:51.56 | Igual que el brief |
| 09 | 41,3 s | 00:02.48 → 00:12.36 + 00:20.24 → 00:51.68 | La pregunta de Pascual empieza en 30,98 s (no 32,32 s). El tramo va continuo y conserva "quitarse la careta" (1 s) para no partir la pregunta. Salida antes de "No me entiendes" |
| 10 | 50,8 s | 00:00.00 → 00:50.76 | El brief (51,60 s) metía "Pero tú reconoces..." del tertuliano |
| 10-ALT | 30,2 s | 00:20.52 → 00:50.76 | Versión directa del brief |
| 11 | 34,4 s | 00:00.00 → 00:12.32 + 01:04.44 → 01:19.84 + 00:39.36 → 00:46.00 | Ver aviso 2 |
| 11-ALT | 23,0 s | 00:23.04 → 00:46.00 | Cronológico, corta en seco tras Pascual |
| 12A | 72,0 s | 00:00.00 → 01:12.00 | El brief cortaba en 1:09,04, a mitad de frase |
| 12B | 63,4 s | 01:13.48 → 02:16.88 | Entra en "muchas veces nos conformamos". Sale antes de la despedida |

## ⚠️ Avisos
1. **V06, la frase final.** Entre 53,3 y 54,9 s el plano es un primer plano del **camarero** con la boca en movimiento. "Por eso no se contrata y ya está" podría ser suya y no de Pascual. Hay que comprobarlo de oído en el original. Si es del camarero, usa **06-ALT**.
2. **V11.** Los tiempos del brief no cuadraban con el audio:
   - Carmen cortaba a mitad de "patronales" (14,18 s).
   - Su clip 2 llegaba hasta 1:25,52 e incluía al presentador ("tiene que ser veinte segundos").
   - Pascual habla de 39,5 a 46,0 s, no de 38,44 a 46,76 s.

   Ya está corregido. Carmen pisa la última sílaba de "empresa" (46,0 s), así que conviene un fundido de audio de 2–3 frames.
3. **Frecuencia de fotogramas.** Los proxies salieron a 30 fps (07 a 25 fps). Asumo que los originales son de 25 fps, como pide el brief y es lo normal en laSexta. Si alguno de los originales es de 30 fps, avisa y regenero esa secuencia.
4. **Resolución.** Asumo originales de 1920x1080, de ahí la escala del 56,25 %. Si alguno es 1280x720, la escala correcta sería 84,375 %.

## Recursos que faltan
- Para empalmar la respuesta de Pascual en el reel 02 (prevista en el brief para la Sesión 2) falta:
  - `0 - Brutos/TANDA PESADA/0427 (1)(1).mp4`, tramo 01:00,6–01:30,8
  - `0 - Brutos/TANDA PESADA/Minuto 30 Enfrentamiento Gonzalo Bernardos.mp4`, tramo 00:07,0–00:38,7
- Los mp3 de `Audios_Extraidos/...` no hacen falta: el audio va dentro de cada mp4.
