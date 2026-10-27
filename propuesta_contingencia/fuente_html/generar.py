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

TARAZONA = "../assets/tarazona_provisional.jpg"
SOTO = "../assets/soto_provisional.jpg"

pieces = {}

# ---------------------------------------------------------------- D-01
pieces["01_D01_comunicado_apelacion"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:34px">Comunicado oficial</div>
<div style="margin-top:18px">{hl(["La verdad y la razón", "están con nosotros"], "md")}</div>
<div class="center h2" style="margin:34px 90px 0;font-size:38px;line-height:1.2">
  Presentamos apelación con sólidos argumentos ante el Jurado Electoral
</div>
<div class="card abs" style="left:64px;right:64px;top:700px;padding:44px 48px 44px">
  <p class="body" style="font-size:27px">
    <b>Fortaleza Médica</b> ingresó formalmente su apelación para defender la
    participación de nuestra <b>Lista Nacional</b>. Lo hacemos con serenidad, con
    firmeza jurídica y con el respaldo de las firmas de miles de médicos del Perú.
    Confiamos en que se resolverá conforme a derecho.
  </p>
  <div class="sign" style="margin-top:28px">
    <div class="n">Dr. Augusto Tarazona</div>
    <div class="r">Coordinador Nacional · Fortaleza Médica</div>
  </div>
</div>
{seal("right:40px;top:560px;transform:rotate(-12deg)", 170, 1)}
<div class="abs center" style="left:0;right:0;bottom:104px;font-weight:800;font-size:28px;letter-spacing:.5px">
  #EnDefensaDelVotoMédico
</div>
""")

# ---------------------------------------------------------------- D-02
def bar_row(label, req, pres, maxv=5191):
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
  {bar_row("Nacional", 3632, 5191)}
  {bar_row("Lima", 2180, 2952)}
  {bar_row("Regiones", 1452, 2239)}
</div>
<div class="abs row" style="left:64px;right:64px;top:1004px;background:var(--navy);color:#fff;border-radius:22px;padding:24px 30px;gap:22px;align-items:center">
  {ICON["alert"]}
  <div style="font-weight:600;font-size:23px;line-height:1.3">
    De <b class="yl" style="font-weight:900">428 firmas</b> de Lima en segunda entrega, solo validaron
    <b class="yl" style="font-weight:900">7</b> y anularon el <b class="yl" style="font-weight:900">70%</b>
    sin justificación técnica válida.
  </div>
</div>
<div class="abs center" style="left:60px;right:60px;bottom:96px;font-weight:800;font-size:28px;line-height:1.25">
  Exigimos transparencia y respeto a las firmas<br>de los médicos del Perú
</div>
""")

# ---------------------------------------------------------------- D-03
pieces["03_D03_quote_rpp_tarazona"] = page(f"""
{logo("corner")}
<div class="abs" style="top:66px;right:56px"><span class="tag big">En medios</span></div>
<div class="abs" style="left:64px;right:64px;top:200px;height:540px;border-radius:26px;background:var(--navy);padding:14px;box-shadow:0 18px 40px rgba(1,41,111,.18)">
  {ph("Frame limpio de la entrevista", "Dr. Augusto Tarazona en RPP Noticias · captura 16:9 en alta", "width:100%;height:100%;border-radius:16px")}
</div>
<div class="abs" style="left:96px;top:706px"><span class="tag navy" style="font-size:20px">Entrevista · RPP Noticias</span></div>
<div class="abs quote" style="left:64px;right:64px;top:790px">
  <span><b class="gm" style="background:none">«</b>No permitiremos que</span>
  <span>irregularidades dejen sin</span>
  <span>representación a los médicos<b class="gm" style="background:none;padding:0 0 0 6px">»</b></span>
</div>
<div class="abs sign" style="left:64px;bottom:110px">
  <div class="n" style="font-size:30px">Dr. Augusto Tarazona</div>
  <div class="r" style="font-size:22px">Médico Infectólogo · Exviceministro de Salud<br>Coordinador Nacional de Fortaleza Médica</div>
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
{ph("Foto Dr. Danny Muñoz", "Retrato recortado · bata blanca · sin fondo", "position:absolute;right:0;top:150px;width:560px;height:930px;border-radius:0;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 25%)", person=True)}
{logo("corner")}
<div class="abs" style="left:64px;top:230px"><span class="tag navy big">Lima · Consejo Regional III</span></div>
<div class="abs" style="left:64px;top:300px">{hl(["¡Es", "oficial!"], "xl", "left")}</div>
<div class="abs h2" style="left:64px;top:610px;width:560px;font-size:40px;line-height:1.18">
  La Lista Regional de Lima encabezada por el <span style="background:linear-gradient(transparent 62%,var(--yellow) 62%)">Dr. Danny Muñoz</span> está inscrita y lista para el cambio
</div>
<div class="abs" style="left:64px;top:880px;width:460px;height:210px;transform:rotate(-3deg)">
  <div class="card" style="padding:12px;height:100%;border-radius:12px">
    {ph("Recorte El Peruano", "Resolución de inscripción · Lista CR III Lima", "height:100%;border-radius:6px;background:linear-gradient(160deg,#F1F1EE,#DCDCD6)")}
  </div>
  <div class="abs" style="right:-34px;top:-34px;width:96px;height:96px;filter:drop-shadow(0 8px 16px rgba(0,0,0,.2))">{ICON["check"]}</div>
</div>
<div class="abs" style="right:64px;top:900px;width:350px">
  <div class="card center" style="padding:22px 20px">
    <div style="font-weight:800;font-size:21px;letter-spacing:.5px">PUBLICADA EN</div>
    <div style="font-weight:900;font-size:34px;margin-top:4px">El Peruano</div>
    <div style="font-weight:600;font-size:18px;margin-top:4px">[fecha de publicación]</div>
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
  {ph("Foto Dr. Danny Muñoz", "Recorte sin fondo · mirando a la derecha", "position:absolute;left:40px;bottom:0;width:470px;height:560px;border-radius:30px 30px 0 0", person=True)}
  <div class="photo fade-b" style="right:40px;bottom:0;width:470px;height:560px;background-image:url({TARAZONA});border-radius:30px 30px 0 0;background-size:118%;background-position:30% 0"></div>
  <div class="abs" style="left:40px;bottom:-4px;width:470px;padding:16px 22px;background:var(--navy);color:#fff;border-left:8px solid var(--yellow)">
    <div style="font-weight:800;font-size:27px">Dr. Danny Muñoz</div>
    <div style="font-weight:500;font-size:19px">Candidato a Decano Regional · Lima</div>
  </div>
  <div class="abs" style="right:40px;bottom:-4px;width:470px;padding:16px 22px;background:var(--navy);color:#fff;border-left:8px solid var(--yellow)">
    <div style="font-weight:800;font-size:27px">Dr. Augusto Tarazona</div>
    <div style="font-weight:500;font-size:19px">Coordinador Nacional</div>
  </div>
</div>
<div class="abs center" style="left:0;right:0;bottom:84px;height:62px;line-height:62px;font-weight:900;font-size:30px">
  Fortaleza Médica <span style="font-weight:500">–</span> <span style="background:var(--yellow);padding:4px 14px">Siempre contigo</span>
</div>
""")

# ---------------------------------------------------------------- D-07 carrusel
def ficha(role, name, spec, line, photo=None):
    if photo:
        img = f'<div style="width:250px;height:300px;border-radius:20px;background:url({photo}) center 8%/cover;flex:none"></div>'
    else:
        img = ph("Foto", "recorte", "width:250px;height:300px;border-radius:20px;flex:none", person=True)
    return f"""<div class="card row" style="gap:30px;align-items:center;padding:26px">
  {img}
  <div>
    <span class="tag" style="font-size:19px">{role}</span>
    <div style="font-weight:900;font-size:36px;margin-top:14px;line-height:1.08;letter-spacing:-.5px">{name}</div>
    <div style="font-weight:700;font-size:23px;margin-top:8px;color:var(--purple)">{spec}</div>
    <div class="body" style="font-size:22px;margin-top:10px">{line}</div>
  </div>
</div>"""


def ficha_page(n, a, b):
    return page(f"""
{logo("corner")}
<div class="page">Equipo Lima · {n} de 5</div>
<div class="kicker" style="margin-top:190px;text-align:left;padding-left:64px;font-size:32px">Conoce al equipo de Lima</div>
<div style="padding:16px 64px 0">{hl(["Experiencia que respalda"], "sm", "left")}</div>
<div class="abs" style="left:64px;right:64px;top:410px;display:flex;flex-direction:column;gap:26px">
  {a}
  {b}
</div>
<div class="abs swipe" style="right:64px;bottom:96px">Desliza →</div>
""")


pieces["07_D07_equipo_lima_1-5_portada"] = page(f"""
{ph("Foto Dr. Danny Muñoz", "Retrato principal · sin fondo · plano medio", "position:absolute;left:0;right:0;top:330px;height:760px;border-radius:0;-webkit-mask-image:linear-gradient(to top,transparent 0,#000 20%)", person=True)}
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

pieces["07_D07_equipo_lima_2-5"] = ficha_page(2,
    ficha("Secretaría General", "Dr(a). [Nombre Apellido]", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]"),
    ficha("Finanzas", "Dr(a). [Nombre Apellido]", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]"))
pieces["07_D07_equipo_lima_3-5"] = ficha_page(3,
    ficha("Ética", "Dr(a). [Nombre Apellido]", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]"),
    ficha("Asuntos Contenciosos", "Dr(a). [Nombre Apellido]", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]"))
pieces["07_D07_equipo_lima_4-5"] = ficha_page(4,
    ficha("Acción Médica", "Dr(a). [Nombre Apellido]", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]"),
    ficha("Incidencia en Salud Pública", "Dr. Leslie Soto", "[Especialidad]", "[Trayectoria en una línea: sede, cargo, años de servicio]", SOTO))

pieces["07_D07_equipo_lima_5-5_cierre"] = page(f"""
{logo()}
<div class="page">5 de 5</div>
<div class="kicker" style="margin-top:40px">Sigue nuestras propuestas para Lima</div>
<div style="margin-top:16px">{hl(["El cambio", "empieza en Lima"], "md")}</div>
<div class="abs" style="left:64px;right:64px;top:640px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  <div class="card"><span class="tag" style="font-size:18px">Facebook</span><div style="font-weight:800;font-size:28px;margin-top:12px">[Fortaleza Médica Lima]</div></div>
  <div class="card"><span class="tag" style="font-size:18px">Instagram</span><div style="font-weight:800;font-size:28px;margin-top:12px">@[usuario]</div></div>
  <div class="card"><span class="tag" style="font-size:18px">TikTok</span><div style="font-weight:800;font-size:28px;margin-top:12px">@[usuario]</div></div>
  <div class="card"><span class="tag" style="font-size:18px">WhatsApp</span><div style="font-weight:800;font-size:28px;margin-top:12px">[+51 900 000 000]</div></div>
</div>
{pill("lima")}
""")

# ---------------------------------------------------------------- D-08 ejes
EJES = [
    ("Defensa legal", "permanente", "Asesoría para cada médico",
     "Defensa y asesoría legal permanente para médicos jóvenes y especialistas.",
     "Foto lateral<br>médico joven en servicio"),
    ("Cuentas claras", "en el CR III", "Transparencia financiera",
     "Rendición de cuentas abierta y periódica del Consejo Regional III.",
     "Foto lateral<br>reunión / asamblea médica"),
    ("Bienestar", "médico", "Cuidar a quien cuida",
     "Programas de salud ocupacional y capacitación continua para los médicos de Lima.",
     "Foto lateral<br>capacitación / taller"),
]


def eje_page(i, e):
    t1, t2, tagline, desc, foto = e
    return page(f"""
{logo()}
<div class="kicker" style="margin-top:28px">Propuestas para Lima · {i} de 3</div>
<div style="margin-top:16px">{hl([t1, t2], "")}</div>
{ph(foto, "fundida a la izquierda", "position:absolute;right:0;top:560px;width:470px;height:520px;border-radius:0;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 30%)")}
<div class="abs" style="left:64px;top:610px;width:560px">
  <span class="tag">Eje {i} · Consejo Regional III</span>
  <div class="h2" style="margin-top:22px">{tagline}.</div>
  <p class="body" style="margin-top:20px">{desc}</p>
  <div class="sign" style="margin-top:30px">
    <div class="n">Dr. Danny Muñoz</div>
    <div class="r">Candidato a Decano Regional · Lima</div>
  </div>
</div>
{pill("lima")}
""")


for i, e in enumerate(EJES, 1):
    pieces[f"08_D08_ejes_lima_{i}-3"] = eje_page(i, e)


def eje_row(n, t, d):
    return f"""<div class="card row" style="gap:28px;align-items:center;padding:28px 34px">
  <div style="flex:none;width:96px;height:96px;background:var(--yellow);display:flex;align-items:center;justify-content:center;font-weight:900;font-size:60px">{n}</div>
  <div><div style="font-weight:900;font-size:32px;letter-spacing:-.3px">{t}</div>
  <div class="body" style="font-size:23px;margin-top:6px">{d}</div></div>
</div>"""


pieces["08_D08_ejes_lima_resumen"] = page(f"""
{logo()}
<div class="kicker" style="margin-top:28px">Consejo Regional III · Lima</div>
<div style="margin-top:16px">{hl(["3 ejes para", "cambiar Lima"], "md")}</div>
<div class="abs" style="left:64px;right:64px;top:600px;display:flex;flex-direction:column;gap:22px">
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
<div style="margin-top:16px">{hl(["¡Triunfó", "la verdad!"], "xl")}</div>
<div class="center" style="margin:30px 80px 0;font-weight:800;font-size:40px;line-height:1.18">
  Nuestra Lista Nacional<br>vuelve a la contienda
</div>
{ph("Foto del equipo nacional completo", "Grupal · celebración · alta resolución", "position:absolute;left:64px;right:64px;top:770px;height:300px;border-radius:26px")}
{seal("right:40px;top:690px;transform:rotate(14deg)", 150, 2)}
<div class="abs" style="left:64px;right:64px;bottom:104px;height:140px;background:var(--yellow);color:var(--navy-ink);border-radius:46px;display:flex;align-items:center;justify-content:center;gap:26px">
  <div style="font-weight:900;font-size:86px;letter-spacing:-4px">29</div>
  <div style="font-weight:900;font-size:30px;line-height:1">DE<br>NOV.</div>
  <div style="width:3px;height:90px;background:var(--navy)"></div>
  <div style="font-weight:800;font-size:30px;line-height:1.15">Vota completo:<br><b style="font-weight:900">Nacional + Regional</b></div>
</div>
""", dark=True)

# ---------------------------------------------------------------- D-09B
pieces["10_D09B_cierre_filas_lima"] = page(f"""
{ph("Foto Dr. Danny Muñoz", "Recorte sin fondo · gesto firme", "position:absolute;right:-20px;top:300px;width:600px;height:800px;border-radius:0;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 30%),linear-gradient(to top,transparent 0,#000 18%);-webkit-mask-composite:source-in", person=True)}
{logo("corner", dark=True)}
<div class="abs" style="left:64px;top:250px">{hl(["Más firmes", "que nunca"], "", "left")}</div>
<div class="abs" style="left:64px;top:510px;width:560px;font-weight:800;font-size:44px;line-height:1.15">
  El cambio empieza en <span class="yl">Lima</span> con el Dr. Danny Muñoz
</div>
<div class="abs" style="left:64px;top:760px;width:520px;border-left:8px solid var(--yellow);padding-left:22px">
  <p class="body" style="color:#fff;font-size:27px">No vamos a ceder los consejos regionales a <b>los mismos de siempre</b>. En Lima y en cada región, seguimos de pie.</p>
</div>
{pill("lima")}
""", dark=True)


for name, html in pieces.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
print(f"{len(pieces)} piezas generadas en {OUT}")
