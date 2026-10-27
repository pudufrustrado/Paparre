#!/usr/bin/env python3
"""Genera los HTML 1080x1350 (4:5) de la propuesta de contingencia.

Cada pieza es un HTML independiente en ./piezas/ que usa ./assets/styles.css.
Los textos entre [corchetes] son datos por completar.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "piezas"
OUT.mkdir(exist_ok=True)

FOOT = '<div class="foot">“Por la defensa del médico, la ética, la ciencia y la salud pública”</div>'


def page(body, dark=False):
    cls = "canvas dark" if dark else "canvas"
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<link rel="stylesheet" href="../assets/styles.css">
</head><body><div class="{cls}">
{body}
{FOOT}
</div></body></html>"""


def logo(pos="center", dark=False):
    src = "logo_white.png" if dark else "logo_color.png"
    return f'<img class="logo {pos}" src="../assets/{src}">'


def hl(lines, size="", align=""):
    spans = "".join(f"<span>{l}</span>" for l in lines)
    return f'<div class="hl {size} {align}">{spans}</div>'


def ph(label, sub="", style="", person=False, extra=""):
    cls = "ph person" if person else "ph"
    s = f"<small>{sub}</small>" if sub else ""
    return f'<div class="{cls} {extra}" style="{style}"><div class="lbl">{label}{s}</div></div>'


def pill(scope="nacional"):
    if scope == "lima":
        vote = '<div class="a">EN LIMA, VOTA POR</div><div class="b">FORTALEZA MÉDICA</div>'
        lista = '<div class="t">LISTA</div><div class="n">N</div><div class="s">CR III</div>'
    else:
        vote = '<div class="a">VOTA POR</div><div class="b">FORTALEZA MÉDICA</div>'
        lista = '<div class="t">LISTA</div><div class="n">N</div>'
    return f"""<div class="pill">
  <div class="date"><span class="este">Este</span><span class="d">29</span><span class="m">DE<br>NOV.</span></div>
  <div class="vote">{vote}</div>
  <div class="lista">{lista}</div>
</div>"""


SEAL = """<svg class="abs" style="{style}" viewBox="0 0 200 200" width="{w}" height="{w}">
  <defs><path id="c{i}" d="M100,100 m-72,0 a72,72 0 1,1 144,0 a72,72 0 1,1 -144,0"/></defs>
  <circle cx="100" cy="100" r="96" fill="#FEC41B"/>
  <circle cx="100" cy="100" r="88" fill="none" stroke="#01296F" stroke-width="3"/>
  <circle cx="100" cy="100" r="52" fill="#01296F"/>
  <text font-family="Montserrat" font-weight="900" font-size="19" fill="#01296F">
    <textPath href="#c{i}" startOffset="0" textLength="446" lengthAdjust="spacing">EN DEFENSA DEL VOTO MÉDICO •</textPath>
  </text>
  <path d="M100 66 l26 10 v20 c0 18-12 30-26 36 c-14-6-26-18-26-36 v-20z" fill="#FEC41B"/>
  <path d="M88 99 l9 9 l17-19" fill="none" stroke="#01296F" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""


def seal(style, w=200, i=0):
    return SEAL.format(style=style, w=w, i=i)


ICON = {
    "cal": '<svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="#01296F" stroke-width="2.2" stroke-linecap="round"><rect x="3" y="5" width="18" height="16" rx="2.5"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="#01296F" stroke-width="2.2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></svg>',
    "video": '<svg viewBox="0 0 24 24" width="54" height="54" fill="none" stroke="#01296F" stroke-width="2.2" stroke-linejoin="round"><rect x="2.5" y="6" width="13" height="12" rx="2.5"/><path d="M15.5 10.5 21.5 7v10l-6-3.5z"/></svg>',
    "check": '<svg viewBox="0 0 24 24" width="100%" height="100%"><circle cx="12" cy="12" r="12" fill="#1FA45A"/><path d="M6.5 12.5l3.6 3.6 7.4-8" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" width="64" height="64"><path d="M12 2 23 21H1z" fill="#FEC41B"/><path d="M12 9v5" stroke="#01296F" stroke-width="2.6" stroke-linecap="round"/><circle cx="12" cy="17.4" r="1.4" fill="#01296F"/></svg>',
}

TARAZONA = "../assets/tarazona.jpg"
MUNOZ = "../assets/munoz.jpg"
FALERO = "../assets/falero.jpg"
L = "../assets/lima/"

pieces = {}

# ---------------------------------------------------------------- D-01
pieces["01_D01_comunicado_apelacion"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:34px">Comunicado oficial</div>
<div style="margin-top:18px">{hl(["La verdad y la razón", "están con nosotros"], "md")}</div>
<div class="center h2" style="margin:34px 110px 0;font-size:36px;line-height:1.2">
  Presentamos un documento impugnatorio ante el Jurado Electoral Nacional del CMP
</div>
<div class="card abs" style="left:64px;right:64px;top:700px;padding:44px 48px 44px">
  <p class="body" style="font-size:27px">
    <b>Fortaleza Médica</b> defiende la participación de su <b>Lista Nacional</b>,
    respaldada por <b>5,200 firmas</b> de médicos de todo el país. Exigimos una
    explicación técnica documentada y la revisión transparente de las firmas
    observadas.
  </p>
  <div class="sign" style="margin-top:28px">
    <div class="n">Dr. Augusto Tarazona</div>
    <div class="r">Candidato a Decano Nacional · Fortaleza Médica</div>
  </div>
</div>
{seal("right:34px;top:600px;transform:rotate(-12deg)", 150, 1)}
<div class="abs center" style="left:0;right:0;bottom:104px;font-weight:800;font-size:28px;letter-spacing:.5px">
  #EnDefensaDelVotoMédico
</div>
""")

# ---------------------------------------------------------------- D-02
def bar_row(label, req, pres, maxv=5200):
    pct = round((pres / req - 1) * 100)
    wr = req / maxv * 100
    wp = pres / maxv * 100
    return f"""
<div style="margin-bottom:26px">
  <div class="row" style="justify-content:space-between;align-items:baseline">
    <div style="font-weight:800;font-size:30px">{label}</div>
    <div class="tag" style="font-size:20px">+{pct}% sobre la meta</div>
  </div>
  <div style="margin-top:12px;display:grid;grid-template-columns:150px 1fr;row-gap:8px;align-items:center">
    <div style="font-weight:600;font-size:19px">Requeridas</div>
    <div class="row" style="align-items:center;gap:12px"><div style="height:30px;width:{wr:.1f}%;background:#C9D3E8;border-radius:4px"></div><b style="font-size:24px">{req:,}</b></div>
    <div style="font-weight:600;font-size:19px">Presentadas</div>
    <div class="row" style="align-items:center;gap:12px"><div style="height:30px;width:{wp:.1f}%;background:var(--navy);border-radius:4px"></div><b style="font-size:24px">{pres:,}</b></div>
  </div>
</div>"""


pieces["02_D02_infografia_firmas"] = page(f"""
{logo("corner")}
<div class="abs" style="top:66px;right:56px"><span class="tag navy big">Transparencia</span></div>
<div style="margin-top:210px">{hl(["Los números reales", "de nuestras firmas"], "md")}</div>
<div class="card abs" style="left:64px;right:64px;top:430px;padding:34px 40px 10px">
  {bar_row("Firmas de respaldo", 3632, 5200)}
  <div style="border-top:2px solid #E3E8F3;margin:4px 0 0;padding:26px 0 30px" class="row">
    <div style="flex:none;padding-right:30px;border-right:3px solid var(--yellow)">
      <div style="font-weight:700;font-size:24px">casi</div>
      <div style="font-weight:900;font-size:96px;line-height:.95;letter-spacing:-3px;color:var(--red)">2,000</div>
    </div>
    <div style="padding-left:30px;align-self:center">
      <div style="font-weight:800;font-size:32px;line-height:1.15">firmas invalidadas</div>
      <div class="body" style="font-size:23px;margin-top:8px">mediante un procedimiento cuyos criterios no han sido explicados de manera clara, suficiente y verificable.</div>
    </div>
  </div>
</div>
<div class="abs row" style="left:64px;right:64px;top:852px;background:var(--navy);color:#fff;border-radius:22px;padding:24px 30px;gap:22px;align-items:center">
  {ICON["alert"]}
  <div style="font-weight:600;font-size:23px;line-height:1.3">
    De un paquete de <b class="yl" style="font-weight:900">428 firmas</b> entregadas, se invalidó el
    <b class="yl" style="font-weight:900">98 %</b> sin justificación sustentada y comunicada.
  </div>
</div>
<div class="abs" style="left:0;right:0;bottom:118px">{hl(["Exigimos transparencia", "y respeto a las firmas", "de los médicos del Perú"], "sm")}
</div>
""")

# ---------------------------------------------------------------- D-03
pieces["03_D03_quote_rpp_tarazona"] = page(f"""
{logo("corner")}
<div class="abs" style="top:66px;right:56px"><span class="tag big">En medios</span></div>
<div class="abs" style="left:64px;right:64px;top:200px;height:540px;border-radius:26px;background:var(--navy);padding:14px;box-shadow:0 18px 40px rgba(1,41,111,.18)">
  <div style="width:100%;height:100%;border-radius:16px;background:url(../assets/rpp_frame.jpg) center/cover"></div>
</div>
<div class="abs" style="left:96px;top:706px"><span class="tag navy" style="font-size:20px">Entrevista · RPP · La Rotativa del Aire</span></div>
<div class="abs quote" style="left:64px;right:64px;top:790px">
  <span><b class="gm" style="background:none">«</b>No permitiremos que</span>
  <span>irregularidades dejen sin</span>
  <span>representación a los médicos<b class="gm" style="background:none;padding:0 0 0 6px">»</b></span>
</div>
<div class="abs sign" style="left:64px;bottom:110px">
  <div class="n" style="font-size:30px">Dr. Augusto Tarazona</div>
  <div class="r" style="font-size:22px">Médico Infectólogo · Exviceministro de Salud<br>Candidato a Decano Nacional</div>
</div>
""")

# ---------------------------------------------------------------- D-04
def info_card(icon, tag, val, sub):
    return f"""<div class="card row" style="align-items:center;gap:22px;padding:26px 28px">
  <div style="width:96px;height:96px;border-radius:24px;background:#FFF3CC;display:flex;align-items:center;justify-content:center">{icon}</div>
  <div><span class="tag" style="font-size:18px">{tag}</span>
    <div style="font-weight:900;font-size:40px;margin-top:8px;letter-spacing:-.5px">{val}</div>
    <div style="font-weight:500;font-size:22px;margin-top:2px">{sub}</div></div>
</div>"""


pieces["04_D04_convocatoria_asamblea"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:30px">Asamblea virtual · Médicos del Perú</div>
<div style="margin-top:16px">{hl(["Unidad, firmeza", "y coordinación", "permanente"], "md")}</div>
<div class="abs" style="left:64px;right:64px;top:640px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
  {info_card(ICON["cal"], "Fecha", "[Día 00/00]", "Abierta a todos")}
  {info_card(ICON["clock"], "Hora", "[00:00] h", "Hora de Lima")}
  <div style="grid-column:1/3">{info_card(ICON["video"], "Plataforma", "Zoom / Meet", "Enlace: [link de la reunión]")}</div>
</div>
<div class="abs center" style="left:64px;right:64px;bottom:100px;background:var(--navy);color:#fff;border-radius:46px;padding:24px 30px;font-weight:800;font-size:29px;line-height:1.2">
  Súmate a la defensa democrática<br><span class="yl" style="font-weight:900">de nuestro gremio</span>
</div>
""")

# ---------------------------------------------------------------- D-05
pieces["05_D05_lista_lima_inscrita"] = page(f"""
<div class="photo" style="right:0;top:130px;width:580px;height:690px;background-image:url(../assets/munoz_busto.jpg);background-size:cover;background-position:center top;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 24%),linear-gradient(to top,transparent 0,#000 24%);-webkit-mask-composite:source-in"></div>
{logo("corner")}
<div class="abs" style="left:64px;top:190px"><span class="tag navy big">Lima · Consejo Regional III</span></div>
<div class="abs" style="left:64px;top:256px">{hl(["¡Es", "oficial!"], "xl", "left")}</div>
<div class="abs h2" style="left:64px;top:560px;width:560px;font-size:38px;line-height:1.18">
  La Lista Regional de Lima encabezada por el <span style="background:linear-gradient(transparent 62%,var(--yellow) 62%)">Dr. Danny Muñoz</span> está inscrita y lista para el cambio
</div>
<div class="abs" style="left:56px;top:792px;width:500px;height:300px;transform:rotate(-2deg)">
  <div class="card" style="padding:10px;height:100%;border-radius:10px;box-shadow:0 18px 40px rgba(1,41,111,.22)">
    <div style="height:100%;border-radius:4px;background:#ECEAE4 url(../assets/publicacion_lima.jpg) center/contain no-repeat"></div>
  </div>
  <div class="abs" style="right:-34px;top:-34px;width:96px;height:96px;filter:drop-shadow(0 8px 16px rgba(0,0,0,.2))">{ICON["check"]}</div>
</div>
<div class="abs" style="right:56px;top:880px;width:380px">
  <div class="card center" style="padding:22px 20px">
    <div style="font-weight:800;font-size:20px;letter-spacing:.5px">PUBLICACIÓN OFICIAL</div>
    <div style="font-weight:900;font-size:28px;margin-top:6px;line-height:1.1">Jurado Electoral<br>Regional CR III</div>
    <div style="font-weight:600;font-size:19px;margin-top:6px">Periodo 2027 – 2030</div>
  </div>
</div>
{pill("lima")}
""".replace('class="pill"', 'class="pill" style="bottom:96px;height:140px"'))

# ---------------------------------------------------------------- D-06
pieces["06_D06_dupla_munoz_tarazona"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:26px">Unidos por un Colegio Médico</div>
<div style="margin-top:14px">{hl(["Transparente, digno", "y al servicio", "de los médicos"], "sm")}</div>
<div class="abs" style="left:0;right:0;top:640px;height:560px">
  <div class="photo fade-b" style="left:40px;bottom:0;width:470px;height:560px;background-image:url({MUNOZ});border-radius:30px 30px 0 0;background-size:auto 112%;background-position:46% 0"></div>
  <div class="photo fade-b" style="right:40px;bottom:0;width:470px;height:560px;background-image:url({TARAZONA});border-radius:30px 30px 0 0;background-size:auto 112%;background-position:24% 0"></div>
  <div class="abs" style="left:40px;bottom:-4px;width:470px;padding:16px 22px;background:var(--navy);color:#fff;border-left:8px solid var(--yellow)">
    <div style="font-weight:800;font-size:27px">Dr. Danny Muñoz</div>
    <div style="font-weight:500;font-size:19px">Candidato a Decano Regional · Lima</div>
  </div>
  <div class="abs" style="right:40px;bottom:-4px;width:470px;padding:16px 22px;background:var(--navy);color:#fff;border-left:8px solid var(--yellow)">
    <div style="font-weight:800;font-size:27px">Dr. Augusto Tarazona</div>
    <div style="font-weight:500;font-size:19px">Candidato a Decano Nacional</div>
  </div>
</div>
<div class="abs center" style="left:0;right:0;bottom:84px;height:62px;line-height:62px;font-weight:900;font-size:30px">
  Fortaleza Médica <span style="font-weight:500">–</span> <span style="background:var(--yellow);padding:4px 14px">Siempre contigo</span>
</div>
""")

# ---------------------------------------------------------------- D-07 carrusel
# Equipo según la publicación del Jurado Electoral Regional CR III (listas lima.jpeg)
def miembro(photo, name, role):
    if photo:
        img = f'<div style="width:210px;height:236px;border-radius:18px;background:url({photo}) center 0/cover;margin:0 auto"></div>'
    else:
        img = ph("Foto", "pendiente", "width:210px;height:236px;border-radius:18px;margin:0 auto", person=True)
    return f"""<div class="card center" style="padding:24px 20px 22px">
  {img}
  <div style="font-weight:900;font-size:29px;margin-top:16px;line-height:1.08;letter-spacing:-.3px">{name}</div>
  <div class="tag" style="font-size:16px;margin-top:10px;line-height:1.25">{role}</div>
</div>"""


def grid_page(n, title, members):
    cards = "\n  ".join(miembro(*m) for m in members)
    return page(f"""
{logo("corner")}
<div class="page">Equipo Lima · {n} de 5</div>
<div class="kicker" style="margin-top:184px;text-align:left;padding-left:64px;font-size:30px">Comité Ejecutivo Regional III · Lima</div>
<div style="padding:14px 64px 0">{hl([title], "sm", "left")}</div>
<div class="abs" style="left:64px;right:64px;top:390px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
  {cards}
</div>
<div class="abs swipe" style="right:64px;bottom:90px">Desliza →</div>
""")


pieces["07_D07_equipo_lima_1-5_portada"] = page(f"""
<div class="photo" style="left:0;right:0;top:330px;height:760px;background-image:url({MUNOZ});background-size:auto 100%;background-position:center top;-webkit-mask-image:linear-gradient(to top,transparent 0,#000 22%)"></div>
{logo()}
<div class="page">1 de 5</div>
<div style="margin-top:28px">{hl(["Conoce al equipo", "de Lima"], "md")}</div>
<div class="abs" style="left:64px;bottom:200px;padding:22px 28px;background:var(--navy);color:#fff;border-left:10px solid var(--yellow);border-radius:0 18px 18px 0">
  <div style="font-weight:900;font-size:40px">Dr. Danny Muñoz</div>
  <div style="font-weight:500;font-size:24px;margin-top:4px">Candidato a Decano · Consejo Regional III Lima</div>
</div>
<div class="abs center" style="left:0;right:0;bottom:104px;font-weight:700;font-size:26px">
  Un equipo con trayectoria, especialidad y compromiso gremial <b class="swipe" style="margin-left:10px">→</b>
</div>
""")

pieces["07_D07_equipo_lima_2-5"] = grid_page(2, "Experiencia que respalda", [
    (FALERO, "Dra. Judith Falero", "Secretaría General"),
    (L + "rodriguez.jpg", "Dr. Junnyor Rodríguez", "Economía y Finanzas"),
    (L + "vasquez.jpg", "Dra. Eva Vásquez", "Desarrollo Profesional<br>y Científico"),
    (L + "soto_t.jpg", "Dr. Leslie Soto", "Incidencia en<br>Salud Pública"),
])
pieces["07_D07_equipo_lima_3-5"] = grid_page(3, "Ética, defensa y gestión", [
    (L + "calvo.jpg", "Dr. Armando Calvo", "Ética y Deontología"),
    (L + "zorrilla.jpg", "Dr. Loel Zorrilla", "Asuntos Contenciosos<br>y Administrativos"),
    (L + "vargas.jpg", "Dra. Karin Vargas", "Administración"),
    (None, "Dra. Jelsy Sánchez", "Médico Joven"),
])
pieces["07_D07_equipo_lima_4-5"] = page(f"""
{logo("corner")}
<div class="page">Equipo Lima · 4 de 5</div>
<div class="kicker" style="margin-top:184px;text-align:left;padding-left:64px;font-size:30px">Comité Ejecutivo Regional III · Lima</div>
<div style="padding:14px 64px 0">{hl(["Un equipo completo"], "sm", "left")}</div>
<div class="abs" style="left:64px;right:64px;top:390px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
  {miembro(L + "sanchez.jpg", "Dra. Elizabeth Sánchez", "Accesitaria")}
  {miembro(L + "calderon.jpg", "Dr. Jorge Calderón", "Accesitario")}
</div>
<div class="abs card row" style="left:64px;right:64px;top:840px;gap:26px;align-items:center;padding:26px 30px">
  <div style="flex:none;width:76px;height:76px">{ICON["check"]}</div>
  <div>
    <div style="font-weight:900;font-size:30px;line-height:1.15">11 médicos, una sola lista para Lima</div>
    <div class="body" style="font-size:22px;margin-top:6px">Publicada por el Jurado Electoral Regional del CR III · Periodo 2027 – 2030</div>
  </div>
</div>
<div class="abs swipe" style="right:64px;bottom:90px">Desliza →</div>
""")


def mini(photo, name, role):
    return f"""<div class="center">
  <div style="width:260px;height:300px;border-radius:22px;background:url({photo}) center 0/cover;margin:0 auto;box-shadow:0 14px 30px rgba(1,41,111,.15)"></div>
  <div style="font-weight:900;font-size:27px;margin-top:16px">{name}</div>
  <div style="display:inline-block;margin-top:6px" class="tag">{role}</div>
</div>"""


pieces["07_D07_equipo_lima_5-5_cierre"] = page(f"""
{logo()}
<div class="page">5 de 5</div>
<div class="kicker" style="margin-top:40px">Este 29 de noviembre, en Lima</div>
<div style="margin-top:16px">{hl(["El cambio", "empieza en Lima"], "md")}</div>
<div class="abs row" style="left:40px;right:40px;top:600px;justify-content:space-between">
  {mini(MUNOZ, "Dr. Danny Muñoz", "Decano Regional")}
  {mini(FALERO, "Dra. Judith Falero", "Secretaría General")}
  {mini(L + "soto_t.jpg", "Dr. Leslie Soto", "Incidencia en Salud Pública")}
</div>
<div class="abs center" style="left:64px;right:64px;top:1010px;font-weight:800;font-size:28px">
  ¿Eres colegiado en Lima? <span style="background:var(--yellow);padding:2px 12px">Comparte con un colega</span>
</div>
{pill("lima")}
""".replace('class="pill"', 'class="pill" style="bottom:90px;height:140px"'))

# ---------------------------------------------------------------- D-08 ejes
# Ejes sugeridos en el plan (pendientes de validar), firmados por el secretario afín
EJES = [
    ("Defensa legal", "permanente", "Asesoría para cada médico",
     "Defensa y asesoría legal permanente para médicos jóvenes y especialistas.",
     L + "zorrilla.jpg", "Dr. Loel Zorrilla", "Secretaría de Asuntos Contenciosos y Administrativos"),
    ("Cuentas claras", "en el CR III", "Transparencia financiera",
     "Rendición de cuentas abierta y periódica del Consejo Regional III.",
     L + "rodriguez.jpg", "Dr. Junnyor Rodríguez", "Secretaría de Economía y Finanzas"),
    ("Bienestar", "médico", "Cuidar a quien cuida",
     "Programas de salud ocupacional y capacitación continua para los médicos de Lima.",
     L + "vasquez.jpg", "Dra. Eva Vásquez", "Secretaría de Desarrollo Profesional y Científico"),
]


def eje_page(i, e):
    t1, t2, tagline, desc, photo, name, role = e
    return page(f"""
{logo()}
<div class="kicker" style="margin-top:28px">Propuestas para Lima · {i} de 3</div>
<div style="margin-top:16px">{hl([t1, t2], "")}</div>
<div class="photo" style="right:0;top:540px;width:460px;height:540px;background-image:url({photo});background-position:center top;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 30%),linear-gradient(to top,transparent 0,#000 16%);-webkit-mask-composite:source-in"></div>
<div class="abs" style="left:64px;top:600px;width:560px">
  <span class="tag">Eje {i} · Consejo Regional III</span>
  <div class="h2" style="margin-top:22px">{tagline}.</div>
  <p class="body" style="margin-top:20px">{desc}</p>
  <div class="sign" style="margin-top:30px">
    <div class="n">{name}</div>
    <div class="r">{role}</div>
  </div>
</div>
{pill("lima")}
""")


for i, e in enumerate(EJES, 1):
    pieces[f"08_D08_ejes_lima_{i}-3"] = eje_page(i, e)


def eje_row(n, t, d):
    return f"""<div class="card row" style="gap:32px;align-items:center;padding:28px 38px">
  <div style="flex:none;width:112px;height:112px;background:var(--yellow);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:70px">{n}</div>
  <div><div style="font-weight:900;font-size:37px;letter-spacing:-.4px">{t}</div>
  <div class="body" style="font-size:26px;margin-top:8px">{d}</div></div>
</div>"""


pieces["08_D08_ejes_lima_resumen"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:28px">Consejo Regional III · Lima</div>
<div style="margin-top:16px">{hl(["3 ejes para", "cambiar Lima"], "md")}</div>
<div class="abs" style="left:64px;right:64px;top:480px;display:flex;flex-direction:column;gap:22px">
  {eje_row(1, "Defensa legal permanente", "Asesoría para médicos jóvenes y especialistas.")}
  {eje_row(2, "Cuentas claras en el CR III", "Transparencia financiera y rendición de cuentas.")}
  {eje_row(3, "Bienestar médico", "Salud ocupacional y capacitación continua.")}
</div>
{pill("lima")}
""")

# ---------------------------------------------------------------- D-09A
pieces["09_D09A_victoria_lista_nacional"] = page(f"""
{logo("center", dark=True)}
<div class="kicker" style="margin-top:30px;color:var(--yellow)">Apelación favorable</div>
<div style="margin-top:16px">{hl(["¡Triunfó", "la verdad!"], "")}</div>
<div class="center" style="margin:22px 80px 0;font-weight:800;font-size:36px;line-height:1.18">
  Nuestra Lista Nacional vuelve a la contienda
</div>
<div class="abs" style="left:56px;right:56px;top:610px;height:505px;background:#fff;border-radius:26px;padding:14px;box-shadow:0 20px 50px rgba(0,0,0,.25)"><div style="width:100%;height:100%;border-radius:14px;background:url(../assets/comite_nacional.jpg) center/contain no-repeat"></div></div>
{seal("right:28px;top:540px;transform:rotate(14deg)", 140, 2)}
<div class="abs" style="left:64px;right:64px;bottom:90px;height:120px;background:var(--yellow);color:var(--navy-ink);border-radius:46px;display:flex;align-items:center;justify-content:center;gap:26px">
  <div style="font-weight:900;font-size:86px;letter-spacing:-4px">29</div>
  <div style="font-weight:900;font-size:30px;line-height:1">DE<br>NOV.</div>
  <div style="width:3px;height:90px;background:var(--navy)"></div>
  <div style="font-weight:800;font-size:30px;line-height:1.15">Vota completo:<br><b style="font-weight:900">Nacional + Regional</b></div>
</div>
""", dark=True)

# ---------------------------------------------------------------- D-09B
pieces["10_D09B_cierre_filas_lima"] = page(f"""
<div class="abs" style="right:56px;top:470px;width:430px;height:580px;border-radius:26px;border:8px solid var(--yellow);background:url({MUNOZ}) 46% 0/auto 105% #F5F6FB;box-shadow:0 20px 50px rgba(0,0,0,.35)"></div>
<div class="abs" style="right:56px;top:1000px;width:430px;padding:12px 20px;background:var(--yellow);color:var(--navy-ink);border-radius:0 0 22px 22px;font-weight:900;font-size:22px;text-align:center">Dr. Danny Muñoz · CR III Lima</div>
{logo("corner", dark=True)}
<div class="abs" style="left:64px;top:250px">{hl(["Más firmes", "que nunca"], "", "left")}</div>
<div class="abs" style="left:64px;top:490px;width:480px;font-weight:800;font-size:42px;line-height:1.15">
  El cambio empieza en <span class="yl">Lima</span> con el Dr. Danny Muñoz
</div>
<div class="abs" style="left:64px;top:780px;width:470px;border-left:8px solid var(--yellow);padding-left:22px">
  <p class="body" style="color:#fff;font-size:27px">No vamos a ceder los consejos regionales a <b>los mismos de siempre</b>. En Lima y en cada región, seguimos de pie.</p>
</div>
{pill("lima")}
""", dark=True)


# ---------------------------------------------------------------- Pronunciamiento (27 oct 2026)
# Tipografía: Poppins Medium (500) = títulos, cifras, porcentajes y frases destacadas
#             Poppins Light (300)  = cuerpos de texto y párrafos descriptivos
def ppage(body):
    return page(body).replace('<div class="canvas">', '<div class="canvas pp">')


pieces["00_Pronunciamiento_1-2_cifras"] = ppage(f"""
{logo()}
<div class="hlp" style="margin-top:34px">
  <span>La democracia institucional</span><span>exige transparencia</span><span>y respeto</span>
</div>
<div class="abs" style="left:64px;right:64px;top:490px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  <div class="card stat"><div class="num">5,200</div><div class="lab">firmas de adherentes presentadas</div></div>
  <div class="card stat"><div class="num">3,632</div><div class="lab">firmas exigidas</div></div>
  <div class="stat neg"><div class="lab" style="margin:0 0 4px">casi</div><div class="num">2,000</div><div class="lab">firmas invalidadas</div></div>
  <div class="stat neg"><div class="lab" style="margin:0 0 8px">De un paquete de 428 firmas entregadas, se invalidó el</div><div class="num">98 %</div></div>
</div>
<div class="abs center" style="left:84px;right:84px;top:960px;font-weight:300;font-size:27px;line-height:1.45">
  Expresamos nuestra profunda preocupación ante la decisión de excluir a la lista <b class="m">FORTALEZA MÉDICA</b> del proceso electoral del Colegio Médico del Perú.
</div>
<div class="abs row" style="left:64px;right:64px;bottom:96px;justify-content:space-between;align-items:center">
  <div style="font-weight:300;font-size:21px">Lima, 27 de octubre del 2026 · <b class="m">Comité Ejecutivo Nacional</b></div>
  <div class="m" style="font-size:22px">Pronunciamiento 1/2 →</div>
</div>
""")

pieces["00_Pronunciamiento_2-2_texto"] = ppage(f"""
{logo("corner")}
<div class="abs" style="top:62px;right:56px"><span class="tag navy big m" style="font-weight:500">Pronunciamiento 2/2</span></div>
<div class="abs" style="left:64px;right:64px;top:178px;display:flex;flex-direction:column;gap:15px">
  <p class="txt">Habiendo presentado <b>5,200 firmas de respaldo</b>, frente a las <b>3,632 exigidas</b>, resulta preocupante que <b>casi 2,000</b> hayan sido invalidadas mediante un procedimiento cuyos criterios y fundamentos no han sido explicados de manera clara, suficiente y verificable en los documentos que nos han hecho entrega. Como ejemplo, de un paquete de <b>428 firmas</b> entregadas, se han invalidado el <b>98 %</b> de ellas sin justificación sustentada y comunicada.</p>
  <p class="txt">Como <b>FORTALEZA MÉDICA</b> recogimos firmas cara a cara, con ética y honestidad, recorriendo hospitales y centros de salud de todo el país. Nuestro respaldo es auténtico, exclusivo y creciente porque nace de la confianza de miles de colegas médicos. <b>No cuestionamos la obligación de verificar las firmas. Cuestionamos la falta de transparencia que compromete la confianza en el proceso electoral.</b> La democracia institucional exige reglas claras, debido procedimiento y respeto a los derechos de participación de los colegiados.</p>
  <p class="txt">Por ello, <b>hemos presentado un documento impugnatorio ante el Jurado Electoral Nacional del CMP</b>, y exigimos una explicación técnica documentada, la revisión transparente de las firmas observadas y las garantías necesarias para un proceso electoral legítimo y justo, con igualdad de oportunidades para todos.</p>
  <p class="txt">Como médicos, defendemos <b>la ética, la justicia y la transparencia</b>, por lo que nuestro Colegio debe ser ejemplo de estos principios.</p>
  <div style="background:var(--yellow);padding:16px 24px;margin-top:4px">
    <div class="m" style="font-size:27px;line-height:1.35;color:var(--navy-ink)">¡Que sean los médicos, a través de su voto, quienes decidan quien debe asumir la conducción de nuestro Colegio Médico!</div>
  </div>
  <div class="row" style="justify-content:space-between;align-items:flex-end;margin-top:8px">
    <div class="sign" style="border-left-width:5px">
      <div class="m" style="font-size:25px">Dr. Augusto Tarazona</div>
      <div class="m" style="font-size:21px">Candidato a Decano Nacional</div>
    </div>
    <div style="text-align:right">
      <div class="l" style="font-size:21px">Lima, 27 de octubre del 2026</div>
      <div class="m" style="font-size:25px">Comité Ejecutivo Nacional</div>
    </div>
  </div>
</div>
""")


for name, html in pieces.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
print(f"{len(pieces)} piezas generadas en {OUT}")
