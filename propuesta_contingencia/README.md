# Propuesta gráfica · Contingencia (Días 1 a 4) · 4:5

Esta propuesta sigue la línea gráfica aprobada en la serie 01–24: fondo claro con bandas diagonales, titulares en Montserrat Black sobre bloques amarillos, píldora "29 NOV", pie navy con franjas morada y amarilla. Todas las piezas miden 1080×1350 y se exportan a @2x (2160×2700).

## Descargables
- `Propuesta_Contingencia_Fortaleza_Medica_4x5.pdf`: las 17 piezas, una por página.
- `Propuesta_Contingencia_PNG_4x5.zip`: los PNG en alta (2160×2700).
- `vista_general.jpg`: todas las piezas en una sola imagen.
- `png/`: los PNG sueltos.
- `fuente_html/`: las fuentes editables. Corre `python3 generar.py` y luego `node render.js`.

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
- `req 1`: frame de la entrevista en RPP (La Rotativa del Aire), usado en D-03.
- `req 2`: retratos de Muñoz, Tarazona y Falero, usados en D-05, D-06, D-07 y D-09B.
- `req 3`: Comité Ejecutivo Nacional, usado en D-09A.

Pendientes (subir a /paparre):
1. **Recorte de El Peruano** con la resolución de la Lista CR III Lima y su fecha de publicación (D-05).
2. **Equipo Lima**: nombre y foto de Finanzas, Ética, Asuntos Contenciosos y Acción Médica, más la especialidad y una línea de trayectoria de cada uno (incluidos Falero y Soto) (D-07).
3. **Fotos laterales** para los ejes de Lima (D-08): médico joven en servicio, una asamblea y una capacitación. Opcional: si no llegan, las cambio por retratos de Muñoz.
4. **Datos de la asamblea**: fecha, hora y enlace (D-04).
5. Opcional: el logo en vector (SVG/AI).

La campaña de Lima no tiene redes propias, así que la lámina 5 de D-07 cierra con el equipo y la invitación "Comparte con un colega".

## Verificar antes de publicar
- **D-02**: el plan dice "de 428 firmas… solo validaron 7 y anularon el 70%". 7 de 428 es el 1,6% validado, así que el "70% anulado" no cuadra con esa cifra. Hay que confirmar los dos números.
- **D-01**: el cuerpo del comunicado es un borrador de redacción y necesita la aprobación del Dr. Tarazona.
- **"Lista N"**: se mantiene como marcador hasta el sorteo del 4 de noviembre, igual que en la serie aprobada.
