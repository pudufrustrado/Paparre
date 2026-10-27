# Propuesta gráfica · Contingencia (Días 1 a 4) · 4:5

Esta propuesta sigue la línea gráfica aprobada en la serie 01–24: fondo claro con bandas diagonales, titulares en Montserrat Black sobre bloques amarillos, píldora "29 NOV", pie navy con franjas morada y amarilla. Todas las piezas miden 1080×1350 y se exportan a @2x (2160×2700).

## Descargables
- `Propuesta_Contingencia_Fortaleza_Medica_4x5.pdf`: las 17 piezas, una por página.
- `Propuesta_Contingencia_PNG_4x5.zip`: los PNG en alta (2160×2700).
- `vista_general.jpg`: todas las piezas en una sola imagen.
- `png/`: los PNG sueltos.
- `fuente_html/`: las fuentes editables. Corre `python3 generar.py` y luego `node render.js`.

## Pronunciamiento (27 oct 2026)
En `pronunciamiento/` están las 2 imágenes en Poppins Medium/Light y su especificación tipográfica (`especificacion_tipografica.md`).

## Piezas
| # | Código | Pieza | Eje |
|---|---|---|---|
| 01 | D-01 | Comunicado de apelación + sello "En defensa del voto médico" | Nacional |
| 02 | D-02 | Infografía "Los números reales de nuestras firmas" | Nacional |
| 03 | D-03 | Quote RPP – Dr. Augusto Tarazona | Nacional |
| 04 | D-04 | Convocatoria a asamblea virtual | Nacional |
| 05 | D-05 | ¡Es oficial! Lista Lima inscrita (El Peruano) | Lima |
| 06 | D-06 | Dupla Muñoz – Tarazona | Lima |
| 07 | D-07 | Carrusel "Conoce al equipo de Lima" (5 láminas) | Lima |
| 08 | D-08 | Ejes programáticos Lima (3 láminas + resumen en una pieza) | Lima |
| 09 | D-09A | ¡Triunfó la verdad! (si la apelación sale favorable) | Contingencia |
| 10 | D-09B | Más firmes que nunca (si la apelación es rechazada) | Contingencia |

## Insumos
Ya integrados:
- `req 1`: frame de la entrevista en RPP, usado en D-03.
- `req 2`: retratos de Muñoz, Tarazona y Falero, usados en D-05, D-06, D-07 y D-09B.
- `req 3`: Comité Ejecutivo Nacional, usado en D-09A.
- `req 5`: fotos del Comité Ejecutivo Regional III Lima, usadas en el carrusel D-07 y en los ejes D-08.
- `listas lima.jpeg`: publicación del Jurado Electoral Regional CR III, usada en D-05. Muestra solo la lista de Fortaleza Médica y **no incluye la columna de DNI**.

Decisiones tomadas:
- D-04 queda como plantilla, porque todavía no hay asamblea programada.
- D-08: los 3 ejes vienen del plan y son una sugerencia por validar. Cada eje lo firma el secretario afín (Zorrilla, Rodríguez y Vásquez).
- La campaña de Lima no tiene redes propias, así que D-07 cierra con "Comparte con un colega".

## Verificar antes de publicar
- **Secretaría del Médico Joven**: la publicación oficial dice "Dra. Jelsy Sánchez Villogas", pero `req 5` dice "Dr. Víctor Hernández". En el carrusel usé el nombre oficial, con la foto pendiente.
- **D-05**: la publicación indica que las listas "han superado la etapa de depuración" y que admite tachas hasta el 28 de octubre. Conviene publicar "¡Es oficial!" después de esa fecha, o suavizar el texto.
- **Cargo de Tarazona**: ahora es "Candidato a Decano Nacional" en todas las piezas (D-01, D-03, D-06 y la firma del pronunciamiento).
- **D-02**: se actualizó con las cifras del pronunciamiento del 27 de octubre (5,200 presentadas, 3,632 exigidas, casi 2,000 invalidadas y 98 % del paquete de 428). Se retiró el desglose Lima/Regiones (2,952 + 2,239 = 5,191), porque ya no cuadra con el total de 5,200.
- **D-01**: el cuerpo se alineó con el pronunciamiento (documento impugnatorio ante el Jurado Electoral Nacional del CMP, 5,200 firmas). Sigue siendo un borrador que debe aprobar el Dr. Tarazona.
- **"Lista N"**: se mantiene como marcador hasta el sorteo del 4 de noviembre, igual que en la serie aprobada.
