#!/usr/bin/env python3
"""Generate all layer HTML pages for Made in Abyss fan site."""

import os

LAYERS = [
    {
        "file": "layer-1.html",
        "num_roman": "0",
        "num": "Superficie",
        "name": "La Entrada",
        "depth": "0 m",
        "curse": "Ninguna",
        "desc": "El abismo comienza en la superficie de la isla de Beoluska. Un enorme agujero de más de 10 metros de diámetro se abre en la tierra, rodeado por el Orfanato de la Cueva. La ciudad de Orth se extiende alrededor del borde, una comunidad entera construida alrededor del misterio del Abismo. Desde aquí, innumerables Silbatos han iniciado su descenso hacia lo desconocido. La vegetación es exuberante y la luz del sol aún calienta la piel, pero la oscuridad acecha justo debajo.",
        "danger": "Bajo",
        "creatures": "Pinzón Carmesí, Terror Crestado",
        "bg": "linear-gradient(180deg, #1a3a2a, #0d2818)",
        "accent": "#4ade80",
        "order": "0"
    },
    {
        "file": "layer-2.html",
        "num_roman": "I",
        "num": "1.ª Capa",
        "name": "Foso del Mundo Frágil",
        "depth": "0 – 1,350 m",
        "curse": "Mareos y náuseas leves",
        "desc": "La capa más superficial del Abismo, bañada aún por la luz del sol. Un exuberante ecosistema de flora y fauna única florece en sus paredes. Aquí la Maldición del Abismo es apenas perceptible: mareos y náuseas al ascender. Los Silbatos Rojos entrenan en esta capa, aprendiendo a moverse por el vertical mundo del Abismo. Es el hogar de los Pinzones Carmesí y el Terror Crestado. La gran góndola de la cascada transporta a los exploradores hasta los 600 metros de profundidad.",
        "danger": "Bajo - Moderado",
        "creatures": "Pinzón Carmesí, Terror Crestado, Sanguijuela Colgante",
        "bg": "linear-gradient(180deg, #1a3a2a, #0d2818, #0a1f12)",
        "accent": "#4ade80",
        "order": "1"
    },
    {
        "file": "layer-3.html",
        "num_roman": "II",
        "num": "2.ª Capa",
        "name": "Bosque de los Colgantes",
        "depth": "1,350 – 2,600 m",
        "curse": "Náuseas intensas, dolor de cabeza, entumecimiento",
        "desc": "Un bosque vertical donde la luz del sol apenas alcanza. Gigantescas raíces cuelgan desde las paredes del Abismo, creando un ecosistema invertido. A los 2,000 metros, el bosque se invierte completamente: los árboles crecen hacia abajo. Es el hogar de las mortales Sanguijuelas Colgantes y el esquivo Búho de Terciopelo. Aquí se encuentra el Campamento de Observación, donde Ozen, la Inamovible, entrena a los jóvenes exploradores. La temperatura desciende y el viento se vuelve impredecible.",
        "danger": "Moderado - Alto",
        "creatures": "Sanguijuela Colgante, Búho de Terciopelo, Corpse-Weeper",
        "bg": "linear-gradient(180deg, #0d2818, #061510, #030a08)",
        "accent": "#2dd4bf",
        "order": "2"
    },
    {
        "file": "layer-4.html",
        "num_roman": "III",
        "num": "3.ª Capa",
        "name": "Gran Grieta",
        "depth": "2,600 – 7,000 m",
        "curse": "Dolor corporal severo, sangrado",
        "desc": "Una grieta vertical de más de 4 kilómetros de profundidad. Las paredes están cubiertas de un mineral bioluminiscente que ilumina todo con un resplandor azulado y violáceo. Esta capa es un largo descenso tubular, con corrientes de aire extremadamente fuertes que dificultan el movimiento. Un sistema de cuevas entrelazadas en sus paredes sirve como hábitat para muchas especies. Aquí habita el temible Mandíbula Escarlata, una de las criaturas más peligrosas del Abismo. Solo los Silbatos Azules y superiores pueden explorarla.",
        "danger": "Alto",
        "creatures": "Mandíbula Escarlata, criaturas bioluminiscentes",
        "bg": "linear-gradient(180deg, #0a0a2e, #050520, #020210)",
        "accent": "#8b5cf6",
        "order": "3"
    },
    {
        "file": "layer-5.html",
        "num_roman": "IV",
        "num": "4.ª Capa",
        "name": "Estanque de los Sedientos",
        "depth": "7,000 – 12,000 m",
        "curse": "Dolor en todo el cuerpo, sangrado por orificios",
        "desc": "Un vasto lago subterráneo de aguas cristalinas rodeado de una húmeda jungla vertical. La presión atmosférica comienza a aumentar notablemente. Gigantescas enredaderas se entrelazan formando discos cóncavos que capturan el agua del aire, dándole nombre a la capa. A los 9,000 metros se encuentra el Jardín de las Flores de la Persistencia, un área llena de la flor característica del Abismo. La fauna aquí ha desarrollado bioluminiscencia avanzada. Es una de las capas más hermosas y traicioneras.",
        "danger": "Muy Alto",
        "creatures": "Turbid-dragon, criaturas acuáticas bioluminiscentes",
        "bg": "linear-gradient(180deg, #0a1628, #050d1a, #020810)",
        "accent": "#3b82f6",
        "order": "4"
    },
    {
        "file": "layer-6.html",
        "num_roman": "V",
        "num": "5.ª Capa",
        "name": "Mar de los Cadáveres",
        "depth": "12,000 – 15,500 m",
        "curse": "Alucinaciones severas, parálisis parcial",
        "desc": "Un vasto océano subterráneo de aguas heladas, salpicado de restos de expediciones pasadas. La luz del sol ya no existe aquí, y la temperatura desciende drásticamente. Es la capa más delgada verticalmente pero la más ancha horizontalmente. En sus orillas se encuentra Idofront, la fortaleza de Bondrewd, que sirve como puerta de entrada a la 6.ª Capa. La Maldición aquí causa alucinaciones severas y parálisis parcial del cuerpo. Solo los Silbatos Negros y Blancos pueden aventurarse aquí.",
        "danger": "Extremo",
        "creatures": "Criaturas abisales, Orbed-piercer",
        "bg": "linear-gradient(180deg, #0a0a1a, #050510, #020208)",
        "accent": "#f59e0b",
        "order": "5"
    },
    {
        "file": "layer-7.html",
        "num_roman": "VI",
        "num": "6.ª Capa",
        "name": "Ciudad Incorruptible",
        "depth": "15,500 – 20,000 m",
        "curse": "Pérdida de humanidad o muerte",
        "desc": "Las ruinas de una civilización antigua y misteriosa. Aquí la Maldición es extrema: causa pérdida total de la humanidad, transformando a quienes ascienden en Narehate, seres deformes sin forma humana, o incluso la muerte. Solo los Silbatos Blancos, los más poderosos exploradores, han logrado llegar y regresar con vida. En el corazón de esta capa se encuentra Ilblu, la villa de los Narehate, y la legendaria Ciudad Dorada. Es el punto de no retorno: una vez que se desciende aquí, no hay vuelta atrás siendo humano.",
        "danger": "Mortal",
        "creatures": "Narehate, Faputa, criaturas de Ilblu",
        "bg": "linear-gradient(180deg, #1a0a2e, #0d0518, #05020a)",
        "accent": "#d946ef",
        "order": "6"
    },
    {
        "file": "layer-8.html",
        "num_roman": "VII",
        "num": "7.ª Capa",
        "name": "El Fondo del Abismo",
        "depth": "20,000 m — ?",
        "curse": "Desconocida (probablemente mortal)",
        "desc": "Nadie ha llegado jamás al fondo del Abismo y regresado para contarlo. Se dice que allí yace el secreto definitivo del Abismo, el verdadero origen de la Maldición, las reliquias, y quizás... el lugar donde todo comenzó. La presión es inimaginable, la oscuridad absoluta, y los pocos que se han atrevido a descender nunca han regresado. En las profundidades de esta capa, según las leyendas, habita el Ser del Abismo, la entidad que otorga los Silbatos Blancos y exige el sacrificio definitivo.",
        "danger": "???",
        "creatures": "Desconocidas",
        "bg": "linear-gradient(180deg, #05050a, #030308, #000000)",
        "accent": "#dc2626",
        "order": "7"
    }
]

TEMPLATE = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__NUM__ — __NAME__ · Made in Abyss</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;900&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: 'Inter', system-ui, sans-serif;
  background: #05050a;
  color: #e2e8f0;
  overflow-x: hidden;
  min-height: 100vh;
}}

/* ── Hero ────────────────────────────────── */
.layer-hero {{
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background: __BG__;
  overflow: hidden;
}}
.layer-hero::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 50% 30%, rgba(255,255,255,0.03) 0%, transparent 70%);
  pointer-events: none;
}}
.layer-hero::after {{
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 0%, rgba(5,5,10,0.6) 80%, rgba(5,5,10,0.95) 100%);
  pointer-events: none;
}}

.layer-number {{
  font-family: 'Cinzel', serif;
  font-size: clamp(5rem, 15vw, 12rem);
  font-weight: 900;
  color: rgba(255,255,255,0.03);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  user-select: none;
}}

.hero-content {{
  position: relative;
  z-index: 1;
}}
.hero-label {{
  font-size: 0.8rem;
  color: __ACCENT__;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
  opacity: 0.6;
}}
.hero-name {{
  font-family: 'Cinzel', serif;
  font-size: clamp(2.5rem, 8vw, 6rem);
  font-weight: 600;
  color: #fff;
  margin-bottom: 0.5rem;
}}
.hero-depth {{
  font-family: 'Cinzel', serif;
  font-size: clamp(1rem, 2.5vw, 1.8rem);
  color: __ACCENT__;
  opacity: 0.7;
  letter-spacing: 0.1em;
}}

/* ── Stats ───────────────────────────────── */
.stats-bar {{
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
  margin-top: 3rem;
}}
.stat-item {{
  text-align: center;
}}
.stat-label {{
  font-size: 0.65rem;
  color: #64748b;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 0.3rem;
}}
.stat-value {{
  font-family: 'Cinzel', serif;
  font-size: 0.9rem;
  color: __ACCENT__;
}}

/* ── Scroll hint ─────────────────────────── */
.scroll-hint {{
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: #475569;
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  z-index: 1;
}}
.scroll-hint .arrow {{
  width: 16px;
  height: 16px;
  border-right: 1.5px solid #475569;
  border-bottom: 1.5px solid #475569;
  transform: rotate(45deg);
  animation: hintBounce 2s infinite;
}}
@keyframes hintBounce {{
  0%, 100% {{ transform: rotate(45deg) translateY(0); opacity: 0.5; }}
  50% {{ transform: rotate(45deg) translateY(6px); opacity: 1; }}
}}

/* ── Content ─────────────────────────────── */
.content-section {{
  padding: 5rem 2rem 6rem;
  max-width: 900px;
  margin: 0 auto;
}}
.content-section h3 {{
  font-family: 'Cinzel', serif;
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  color: __ACCENT__;
}}
.content-section p {{
  color: #94a3b8;
  line-height: 1.9;
  font-size: 1.05rem;
  margin-bottom: 1.5rem;
}}

/* ── Curse card ──────────────────────────── */
.curse-card {{
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 1rem;
  padding: 2rem;
  margin-bottom: 3rem;
}}
.curse-card h4 {{
  font-family: 'Cinzel', serif;
  color: __ACCENT__;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}}
.curse-card p {{ color: #94a3b8; font-size: 0.95rem; }}

/* ── Video ───────────────────────────────── */
.video-wrapper {{
  position: relative;
  width: 100%;
  padding-bottom: 56.25%;
  border-radius: 1rem;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.06);
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}}
.video-wrapper iframe {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}}

/* ── Back button ─────────────────────────── */
.back-btn {{
  position: fixed;
  top: 1.5rem;
  left: 1.5rem;
  z-index: 100;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 2rem;
  background: rgba(5,5,10,0.7);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  color: #94a3b8;
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-decoration: none;
  transition: all 0.3s ease;
}}
.back-btn:hover {{
  border-color: __ACCENT__;
  color: #fff;
  transform: translateX(-4px);
}}

/* ── Nav dots ────────────────────────────── */
.nav-dots {{
  position: fixed;
  right: 1.5rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  z-index: 100;
}}
.nav-dot {{
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  transition: all 0.3s ease;
  text-decoration: none;
}}
.nav-dot:hover,
.nav-dot.active {{ background: __ACCENT__; transform: scale(1.3); }}

/* ── Footer ──────────────────────────────── */
.footer {{
  text-align: center;
  padding: 2rem;
  border-top: 1px solid rgba(255,255,255,0.05);
  color: #475569;
  font-size: 0.8rem;
}}

@media (max-width: 768px) {{
  .nav-dots {{ display: none; }}
  .stats-bar {{ gap: 1rem; }}
  .content-section {{ padding: 3rem 1.5rem; }}
}}
</style>
</head>
<body>

<a href="index.html#abyss-map" class="back-btn">← Volver al Abismo</a>

<div class="nav-dots">
  <a href="layer-1.html" class="nav-dot" title="Superficie"></a>
  <a href="layer-2.html" class="nav-dot" title="1.ª Capa"></a>
  <a href="layer-3.html" class="nav-dot" title="2.ª Capa"></a>
  <a href="layer-4.html" class="nav-dot" title="3.ª Capa"></a>
  <a href="layer-5.html" class="nav-dot" title="4.ª Capa"></a>
  <a href="layer-6.html" class="nav-dot" title="5.ª Capa"></a>
  <a href="layer-7.html" class="nav-dot" title="6.ª Capa"></a>
  <a href="layer-8.html" class="nav-dot" title="7.ª Capa"></a>
</div>

<section class="layer-hero">
  <div class="layer-number">__NUM_ROMAN__</div>
  <div class="hero-content">
    <div class="hero-label">__NUM__</div>
    <h1 class="hero-name">__NAME__</h1>
    <div class="hero-depth">__DEPTH__</div>
    <div class="stats-bar">
      <div class="stat-item">
        <div class="stat-label">Peligrosidad</div>
        <div class="stat-value">__DANGER__</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Maldición</div>
        <div class="stat-value">__CURSE__</div>
      </div>
      <div class="stat-item">
        <div class="stat-label">Criaturas</div>
        <div class="stat-value">__CREATURES__</div>
      </div>
    </div>
  </div>
  <div class="scroll-hint">
    EXPLORAR
    <div class="arrow"></div>
  </div>
</section>

<div class="content-section">
  <h3>Descripción de la Capa</h3>
  <p>__DESC__</p>

  <div class="curse-card">
    <h4>☠ Maldición del Abismo</h4>
    <p>__CURSE_DESC__</p>
  </div>

  <h3>Video Explicativo</h3>
  <p style="margin-bottom:1.5rem; color:#64748b; font-size:0.9rem;">
    Un análisis detallado de esta capa y su importancia en el mundo de Made in Abyss.
  </p>
  <div class="video-wrapper">
    <iframe src="https://www.youtube.com/embed/9vuAYbaacJI?autoplay=0&rel=0" 
      title="Made in Abyss - All Layers Explained" 
      frameborder="0" 
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
      allowfullscreen>
    </iframe>
  </div>
</div>

<footer class="footer">
  <p>Fan page · Made in Abyss es propiedad de Akihito Tsukushi · Sin fines de lucro</p>
</footer>

<script>
// Highlight current layer dot
document.querySelectorAll('.nav-dot').forEach((dot, i) => {{
  const path = window.location.pathname.split('/').pop();
  if (dot.getAttribute('href') === path) {{
    dot.classList.add('active');
  }}
}});

// Smooth scroll
document.querySelector('.scroll-hint')?.addEventListener('click', () => {{
  window.scrollTo({{ top: window.innerHeight, behavior: 'smooth' }});
}});
</script>
</body>
</html>
'''

CURSE_DESCS = [
    "En la superficie no existe la Maldición. Los exploradores pueden ascender y descender libremente sin sufrir ningún efecto secundario. Es el único lugar del Abismo donde esto es posible.",
    "La Maldición en la 1.ª Capa es extremadamente leve. Quienes ascienden experimentan mareos y náuseas pasajeras, similares al vértigo. Los exploradores novatos pueden acostumbrarse con la práctica.",
    "Los síntomas se intensifican: náuseas severas, fuertes dolores de cabeza y entumecimiento de las extremidades. El ascenso debe hacerse con cuidado, haciendo pausas frecuentes para que el cuerpo se adapte.",
    "El dolor se vuelve debilitante. Sangrado por los oídos, la nariz y los ojos es común. El cuerpo entero duele como si estuviera siendo aplastado. Solo los exploradores experimentados pueden soportarlo.",
    "El dolor se extiende por todo el cuerpo, con sangrado profuso por todos los orificios. La presión interna se vuelve insoportable. Es necesario usar reliquias o medicamentos especializados para sobrevivir al ascenso.",
    "Alucinaciones vívidas y aterradoras se apoderan de la mente. El cuerpo sufre parálisis parcial. La línea entre la realidad y la pesadilla se desdibuja. Muchos exploradores han enloquecido aquí.",
    "La pérdida total de la humanidad. Quienes ascienden desde la 6.ª Capa se transforman en Narehate, seres deformes sin forma humana. En algunos casos, la muerte es el resultado más misericordioso. No hay retorno siendo humano.",
    "Desconocida. Nadie ha regresado jamás de esta profundidad para describir sus efectos. Se especula que la Maldición aquí es instantáneamente mortal, o que transforma al explorador en algo más allá de la comprensión humana."
]

os.chdir('/home/miku/made-in-abyss-web/layers')

for i, layer in enumerate(LAYERS):
    html = TEMPLATE
    html = html.replace('__NUM_ROMAN__', layer['num_roman'])
    html = html.replace('__NUM__', layer['num'])
    html = html.replace('__NAME__', layer['name'])
    html = html.replace('__DEPTH__', layer['depth'])
    html = html.replace('__DANGER__', layer['danger'])
    html = html.replace('__CURSE__', layer['curse'])
    html = html.replace('__CREATURES__', layer['creatures'])
    html = html.replace('__DESC__', layer['desc'])
    html = html.replace('__CURSE_DESC__', CURSE_DESCS[i])
    html = html.replace('__BG__', layer['bg'])
    html = html.replace('__ACCENT__', layer['accent'])
    html = html.replace('__ORDER__', layer['order'])

    with open(layer['file'], 'w') as f:
        f.write(html)
    print(f"✅ Created {layer['file']}")

print("\n🎉 All layer pages created!")
