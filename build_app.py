import json, os

with open(r"C:\Users\widag\OneDrive\Escritorio\Desayunos con Amor\image_data_small.json", "r") as f:
    imgs = json.load(f)

img_js_parts = []
for k, v in imgs.items():
    img_js_parts.append('"' + k + '":"' + v + '"')
img_js = "{" + ",".join(img_js_parts) + "}"

html_top = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Desayunos con Amor 2026</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--pk:#be185d;--pk2:#db2777;--pkl:#fce7f3;--grn:#059669;--dk:#1a1a2e;--gy:#6b7280;--wh:#fff;--sh:0 4px 20px rgba(190,24,93,.12);--rd:16px;--gld:#d4a017}
body{font-family:'Poppins',sans-serif;background:linear-gradient(135deg,#fff0f6,#fdf2f8 50%,#fef3c7);min-height:100vh;color:#333}
.ctr{max-width:1100px;margin:0 auto;padding:12px}
.hd{text-align:center;padding:20px 10px 15px}.hd img{width:80px;filter:drop-shadow(0 2px 8px rgba(190,24,93,.3))}.hd h1{font-family:'Dancing Script',cursive;font-size:2.6em;color:var(--pk)}.hd .sub{font-size:.92em;color:var(--gy);letter-spacing:1px}.hd .soc{margin-top:6px;display:inline-flex;align-items:center;gap:6px;background:var(--pk);color:#fff;padding:5px 16px;border-radius:20px;font-size:.82em;font-weight:600}
.tabs{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:15px 0 20px;position:sticky;top:0;z-index:100;background:rgba(255,240,246,.95);backdrop-filter:blur(10px);padding:10px 0;border-radius:0 0 20px 20px}
.tb{padding:10px 22px;background:var(--wh);color:var(--pk);border:2px solid var(--pk);border-radius:25px;font-size:.88em;font-weight:600;cursor:pointer;transition:.3s;font-family:inherit}.tb:hover{transform:scale(1.05)}.tb.a{background:linear-gradient(135deg,var(--pk),var(--pk2));color:#fff;border-color:transparent}
.tc{display:none;animation:fu .4s}.tc.a{display:block}@keyframes fu{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}
.cf{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:20px}
.cb{padding:8px 18px;border-radius:20px;border:2px solid #e5e7eb;background:#fff;color:var(--gy);cursor:pointer;font-weight:600;font-size:.82em;transition:.3s;font-family:inherit}.cb:hover{border-color:var(--pk);color:var(--pk)}.cb.a{background:var(--pk);color:#fff;border-color:var(--pk)}
.cg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px}
.cd{background:var(--wh);border-radius:var(--rd);overflow:hidden;box-shadow:var(--sh);border:3px solid transparent;transition:.35s}.cd:hover{transform:translateY(-6px);box-shadow:0 12px 30px rgba(190,24,93,.18)}.cd.sel{border-color:var(--pk)}
.cd .ci{width:100%;height:200px;object-fit:cover;display:block;transition:.4s}.cd:hover .ci{transform:scale(1.05)}
.cd .cb2{padding:14px}.cd .bg{display:inline-block;padding:3px 12px;border-radius:12px;background:var(--pkl);color:var(--pk);font-size:.72em;font-weight:700;margin-bottom:6px}.cd .cn{font-size:1.1em;font-weight:700;color:var(--dk);margin-bottom:4px}.cd .cds{font-size:.78em;color:var(--gy);line-height:1.5;max-height:55px;overflow:hidden;position:relative;margin-bottom:8px}.cd .cds::after{content:'';position:absolute;bottom:0;left:0;right:0;height:20px;background:linear-gradient(transparent,#fff)}.cd .cp{font-size:1.25em;font-weight:800;color:var(--pk);margin-bottom:8px}.cd .cdl{font-size:.72em;color:var(--gy);margin-bottom:10px}.cd .cbt{display:flex;gap:8px}
.bs{flex:1;padding:10px;background:linear-gradient(135deg,var(--pk),var(--pk2));color:#fff;border:none;border-radius:12px;font-weight:700;cursor:pointer;font-family:inherit;font-size:.88em;transition:.3s}.bs:hover{box-shadow:0 4px 12px rgba(190,24,93,.4)}
.bd{padding:10px 14px;background:var(--pkl);color:var(--pk);border:none;border-radius:12px;font-weight:700;cursor:pointer;font-family:inherit;font-size:.88em;transition:.3s}.bd:hover{background:var(--pk);color:#fff}
.mo{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.6);z-index:1000;align-items:center;justify-content:center;padding:20px}.mo.sh{display:flex}
.ml{background:#fff;border-radius:var(--rd);max-width:500px;width:100%;max-height:85vh;overflow-y:auto;position:relative}.ml .mi{width:100%;height:250px;object-fit:cover;border-radius:var(--rd) var(--rd) 0 0}.ml .mb{padding:20px}.ml .mt{font-size:1.3em;font-weight:700;color:var(--dk);margin-bottom:4px}.ml .mp{font-size:1.4em;font-weight:800;color:var(--pk);margin-bottom:12px}.ml .md2{font-size:.88em;color:#555;line-height:1.7;margin-bottom:15px}
.mc{position:absolute;top:12px;right:12px;width:36px;height:36px;background:rgba(255,255,255,.9);border:none;border-radius:50%;font-size:1.2em;cursor:pointer;display:flex;align-items:center;justify-content:center}
.msb{width:100%;padding:14px;background:linear-gradient(135deg,var(--pk),var(--pk2));color:#fff;border:none;border-radius:12px;font-weight:700;font-size:1em;cursor:pointer;font-family:inherit}
.fs{background:#fff;border-radius:var(--rd);padding:24px;box-shadow:var(--sh);margin-bottom:18px}.fs h2{color:var(--pk);border-bottom:3px solid var(--gld);padding-bottom:10px;margin-bottom:18px;font-size:1.15em}
.fr{display:grid;grid-template-columns:1fr 1fr;gap:14px}.fg{margin-bottom:14px}.fg label{display:block;font-weight:600;color:var(--dk);font-size:.9em;margin-bottom:5px}.fg input,.fg textarea,.fg select{width:100%;padding:11px 14px;border:2px solid #e5e7eb;border-radius:10px;font-size:.95em;font-family:inherit;transition:.3s;background:#fafafa}.fg input:focus,.fg textarea:focus,.fg select:focus{outline:none;border-color:var(--pk);box-shadow:0 0 0 3px rgba(190,24,93,.1);background:#fff}.fg textarea{min-height:75px;resize:vertical}
.sb{background:linear-gradient(135deg,var(--pk),var(--pk2));color:#fff;padding:18px;border-radius:var(--rd);text-align:center;margin-bottom:18px;display:none}.sb.sh{display:block}.sb img{width:60px;height:60px;object-fit:cover;border-radius:50%;border:3px solid #fff;margin-bottom:6px}.sb .sn{font-size:1.2em;font-weight:700}.sb .sp2{font-size:1em;opacity:.9}
.ag{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}.ai{display:flex;align-items:center;gap:10px;padding:10px 12px;border:2px solid #e5e7eb;border-radius:12px;cursor:pointer;transition:.3s;background:#fafafa}.ai:hover{border-color:var(--pkl);background:var(--pkl)}.ai.ck{border-color:var(--pk);background:var(--pkl)}.ai input[type=checkbox]{accent-color:var(--pk);width:18px;height:18px}.ai img{width:40px;height:40px;border-radius:8px;object-fit:cover}.ai .an{font-weight:600;font-size:.85em}.ai .ap{font-size:.8em;color:var(--pk);font-weight:700}
.clp{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}.cc{width:38px;height:38px;border-radius:50%;border:3px solid transparent;cursor:pointer;transition:.3s;box-shadow:0 2px 6px rgba(0,0,0,.15)}.cc:hover{transform:scale(1.15)}.cc.s{border-color:var(--dk);transform:scale(1.2)}.tc2{padding:7px 16px;background:#f3f4f6;border:2px solid transparent;border-radius:20px;cursor:pointer;font-size:.85em;font-weight:500;transition:.3s}.tc2:hover{background:var(--pkl)}.tc2.s{border-color:var(--pk);background:var(--pk);color:#fff}
.zo{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}.zb{padding:12px 18px;border:2px solid #e5e7eb;border-radius:12px;cursor:pointer;transition:.3s;background:#fff;text-align:center;min-width:140px}.zb:hover{border-color:var(--pkl)}.zb.s{border-color:var(--pk);background:var(--pkl)}.zn{font-weight:700;font-size:.92em}.zp{font-size:.82em;color:var(--grn);font-weight:700}
.ps{background:#d1fae5;border:2px solid #86efac;border-radius:var(--rd);padding:20px;margin-bottom:18px}.ps h3{color:#166534;margin-bottom:12px}.pg{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}.pc{background:#fff;border-radius:12px;padding:14px;box-shadow:0 2px 8px rgba(0,0,0,.05)}.pc .bk{font-weight:700;font-size:.92em;margin-bottom:3px}.pc .hl{color:var(--gy);font-size:.82em}.pc .ac{color:var(--pk);font-weight:700;font-size:1em;margin-top:4px}
.bts{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:22px}.btn{padding:14px 28px;border:none;border-radius:25px;font-weight:700;font-size:.95em;cursor:pointer;transition:.3s;color:#fff;font-family:inherit;display:inline-flex;align-items:center;gap:8px}.btn:hover{transform:translateY(-2px)}.bsb{background:linear-gradient(135deg,#059669,#10b981)}.bwa{background:linear-gradient(135deg,#25d366,#128c7e)}.brs{background:linear-gradient(135deg,#ef4444,#dc2626)}
.sm{background:#fff;border-radius:var(--rd);padding:24px;box-shadow:var(--sh)}.sm h2{color:var(--pk);margin-bottom:18px;border-bottom:3px solid var(--gld);padding-bottom:10px}.ss{margin-bottom:18px}.ss h3{color:var(--pk);margin-bottom:10px;font-size:1em}.sr{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f3f4f6}.sr .l{font-weight:600;color:#555;font-size:.9em}.sr .v{color:var(--dk);text-align:right;max-width:60%;word-break:break-word;font-size:.9em}.st2{background:linear-gradient(135deg,var(--pk),var(--pk2));color:#fff;padding:16px;border-radius:12px;text-align:center;margin-top:15px;font-size:1.2em;font-weight:700}.no{text-align:center;color:#999;padding:40px}
.msg{padding:14px 18px;border-radius:12px;margin-bottom:14px;font-weight:600;text-align:center;display:none;font-size:.92em}.msg.ok{background:#d1fae5;color:#065f46;border:2px solid #10b981;display:block}.msg.er{background:#fee2e2;color:#991b1b;border:2px solid #ef4444;display:block}
@media(max-width:768px){.hd h1{font-size:2em}.fr{grid-template-columns:1fr}.bts{flex-direction:column;align-items:stretch}.btn{justify-content:center}.ctr{padding:8px}.cg{grid-template-columns:1fr 1fr}.cd .ci{height:150px}.ag,.pg{grid-template-columns:1fr}.zo{flex-direction:column}.tabs{gap:4px;padding:8px 4px}.tb{padding:8px 14px;font-size:.8em}}
@media(max-width:400px){.cg{grid-template-columns:1fr}.cd .ci{height:200px}}
</style>
</head>
<body>
<div class="ctr">
<div class="hd"><img id="lg" alt="Logo"><h1>Desayunos con Amor</h1><div class="sub">C A T &Aacute; L O G O &nbsp; 2 0 2 6</div><div class="soc">&#x1F4F8; @desayunosconamor_23</div></div>
<div class="tabs"><button class="tb a" onclick="sw('catalog',this)">&#x1F4CB; Cat&aacute;logo</button><button class="tb" onclick="sw('form',this)">&#x1F4DD; Pedido</button><button class="tb" onclick="sw('preview',this)">&#x1F441;&#xFE0F; Resumen</button><button class="tb" onclick="sw('pagos',this)">&#x1F4B3; Pagos</button></div>
<div id="catalog" class="tc a"><div class="cf" id="cF"></div><div class="cg" id="cG"></div></div>
<div id="form" class="tc"><div class="sb" id="sB"></div><div id="mA"></div>
<form id="oF" onsubmit="return false">
<div class="fs"><h2>&#x1F4CD; Informaci&oacute;n de Entrega</h2>
<div class="fr"><div class="fg"><label>Nombre de quien recibe *</label><input type="text" id="fR" required placeholder="Ej: Mar&iacute;a"></div><div class="fg"><label>Tel&eacute;fono de quien recibe *</label><input type="tel" id="fP" required placeholder="3001234567"></div></div>
<div class="fg"><label>Nombre de quien env&iacute;a *</label><input type="text" id="fS" required placeholder="Ej: Juan"></div>
<div class="fr"><div class="fg"><label>Fecha de entrega *</label><input type="date" id="fD" required></div><div class="fg"><label>Rango de hora *</label><select id="fT" required><option value="">Selecciona...</option><option>6:00-7:00 AM</option><option>7:00-8:00 AM</option><option>8:00-9:00 AM</option><option>9:00-10:00 AM</option><option>10:00-11:00 AM</option><option>11:00-12:00 PM</option><option>12:00-1:00 PM</option><option>1:00-2:00 PM</option><option>2:00-3:00 PM</option><option>3:00-4:00 PM</option><option>4:00-5:00 PM</option></select></div></div>
<div class="fg"><label>Direcci&oacute;n completa *</label><textarea id="fA" required placeholder="Calle, barrio, edificio..."></textarea></div>
<div class="fg"><label>&#x1F4CD; Ubicaci&oacute;n / Referencias</label><input type="text" id="fL" placeholder="Cerca al centro comercial..."></div>
<div class="fg"><label>&#x1F69A; Zona de entrega *</label><div class="zo"><div class="zb s" onclick="sZ('Pereira',0,this)"><div class="zn">&#x1F3E0; Pereira</div><div class="zp">Incluido</div></div><div class="zb" onclick="sZ('Dosquebradas',5000,this)"><div class="zn">&#x1F3D8;&#xFE0F; Dosquebradas</div><div class="zp">+$5,000</div></div><div class="zb" onclick="sZ('Santa Rosa',10000,this)"><div class="zn">&#x1F305; Santa Rosa</div><div class="zp">+$10,000</div></div></div></div></div>
<div class="fs"><h2>&#x1F3A8; Personalizaci&oacute;n</h2>
<div class="fg"><label>Color de decoraci&oacute;n</label><div class="clp"><div class="cc s" style="background:#ec4899" onclick="sC('Rosado',this)" title="Rosado"></div><div class="cc" style="background:#8b5cf6" onclick="sC('Morado',this)" title="Morado"></div><div class="cc" style="background:#ef4444" onclick="sC('Rojo',this)" title="Rojo"></div><div class="cc" style="background:#3b82f6" onclick="sC('Azul',this)" title="Azul"></div><div class="cc" style="background:#111827" onclick="sC('Negro',this)" title="Negro"></div><div class="cc" style="background:linear-gradient(135deg,#fbbf24,#f59e0b)" onclick="sC('Dorado',this)" title="Dorado"></div></div></div>
<div class="fg"><label>Tem&aacute;tica (opcional)</label><div class="clp"><div class="tc2" onclick="sT('Cumplea&ntilde;os',this)">&#x1F382; Cumplea&ntilde;os</div><div class="tc2" onclick="sT('Amor',this)">&#x2764;&#xFE0F; Amor</div><div class="tc2" onclick="sT('Amistad',this)">&#x1F91D; Amistad</div><div class="tc2" onclick="sT('Recuperaci&oacute;n',this)">&#x1F33F; Recuperaci&oacute;n</div><div class="tc2" onclick="sT('Personalizada',this)">&#x2728; Personalizada</div></div></div>
<div class="fg"><label>Mensaje personalizado *</label><textarea id="fM" required placeholder="Escribe el mensaje..."></textarea></div>
<div class="fg"><label>&#x1F4F7; Foto (descripci&oacute;n o link)</label><input type="text" id="fPh" placeholder="Describe la foto o pega un link"></div></div>
<div class="fs"><h2>&#x2728; Adiciones</h2><div class="ag" id="aG"></div></div>
<div class="bts"><button class="btn bwa" onclick="enviar()" style="flex:2">&#x1F4F2; Enviar Pedido</button><button class="btn brs" onclick="rst()">&#x1F5D1;&#xFE0F; Limpiar</button></div>
<div id="crmI" style="display:none;text-align:center;padding:10px 16px;border-radius:12px;background:#d1fae5;color:#065f46;font-weight:600;font-size:.88em;margin-top:12px">&#x2705; Registrado en CRM</div>
</form></div>
<div id="preview" class="tc"><div class="sm"><h2>&#x1F4CB; Resumen del Pedido</h2><div class="no" id="nO">Selecciona un producto del cat&aacute;logo &#x1F60A;</div><div id="sB2" style="display:none"></div></div></div>
<div id="pagos" class="tc"><div class="ps"><h3>&#x1F4B0; M&eacute;todos de Pago</h3><div class="pg"><div class="pc"><div class="bk">&#x1F3E6; BANCOLOMBIA</div><div class="hl">Valentina Castrill&oacute;n</div><div class="ac">723-646704-95</div><div class="hl">Ahorros &bull; Pagos internacionales</div></div><div class="pc"><div class="bk">&#x1F4F1; NEQUI</div><div class="hl">Juan Espitia</div><div class="ac">3232167091</div></div><div class="pc"><div class="bk">&#x1F4B3; DAVIPLATA</div><div class="hl">Juan Espitia</div><div class="ac">3232167091</div></div></div></div>
<div class="fs" style="text-align:center"><h2>&#x1F4E9; Env&iacute;a tu comprobante</h2><p style="color:var(--gy);margin-bottom:12px;font-size:.92em">Env&iacute;a el comprobante de pago junto con tu pedido por WhatsApp</p><button class="btn bwa" onclick="waFn()">&#x1F4F2; Enviar por WhatsApp</button></div></div>
</div>
<div class="mo" id="md" onclick="if(event.target===this)cMo()"><div class="ml"><button class="mc" onclick="cMo()">&#x2715;</button><img class="mi" id="mI"><div class="mb"><div class="bg" id="mB"></div><div class="mt" id="mT"></div><div class="mp" id="mP"></div><div class="md2" id="mD"></div><button class="msb" id="mSB">&#x1F6D2; Seleccionar este producto</button></div></div></div>
'''

html_script = '<script>\nconst I=' + img_js + ';\n'

html_script += r'''
// ===== CRM GOOGLE SHEETS =====
// PEGA AQUI la URL de tu Google Apps Script desplegado:
const SCRIPT_URL = "https://script.google.com/macros/s/AKfycbypd3JvIEnKElUyFHwvW_2kdxeL45df2Z6XqSZQXvl5lLQHfqWVPawkR_g_raDvHnp3Fg/exec";
// ==============================

const P=[
{id:"bandeja_dulce",n:"Bandeja Dulce/Frutas/Combinada",c:"bandejas",p:70000,i:"bandeja_dulce",d:"Solo Dulces, Solo Frutas o Combinada. Mensaje, Foto, Decoraci\u00f3n con cinta y mo\u00f1o.",dt:"<b>Incluye:</b><br>\u2022 Solo Dulces / Solo Frutas / Combinada<br>\u2022 Mensaje personalizado y Foto<br>\u2022 Decoraci\u00f3n con cinta y mo\u00f1o<br>\u2022 Colores: Rosado, morado, rojo, azul, negro"},
{id:"bandeja_salada",n:"Bandeja Salada",c:"bandejas",p:80000,i:"bandeja_salada",d:"Arma tu bandeja: Sanduche, Quesadillas, Yucas, Nuggets y m\u00e1s.",dt:"<b>6 opciones:</b><br>\u2022 Sanduche \u2022 Quesadillas \u2022 Yucas fritas<br>\u2022 Salchichas \u2022 Nuggets \u2022 Huevos codorniz<br>\u2022 Huevos rancheros \u2022 Frutas \u2022 Dulces"},
{id:"cajita",n:"Desayuno Cajita",c:"desayunos",p:70000,i:"cajita",d:"Pastel de pollo, bebida, postre, caja decorada.",dt:"<b>Incluye:</b><br>\u2022 Pastel de pollo<br>\u2022 Bebida: Jugo/Capuchino/Milo/Caf\u00e9<br>\u2022 Postre: Personal/Parfait<br>\u2022 Caja de cart\u00f3n decorada"},
{id:"caja_sorpresa",n:"Caja Sorpresa",c:"desayunos",p:85000,i:"caja_sorpresa",d:"Comida, bebida, postre, cerveza o dulces, cereal, yogurt.",dt:"<b>Incluye:</b><br>\u2022 1 comida \u2022 1 bebida \u2022 1 postre<br>\u2022 Cerveza coronita o Dulces<br>\u2022 Cereal y Yogurt<br>\u2022 Caja decorada"},
{id:"sorpresa1",n:"Desayuno Sorpresa #1",c:"desayunos",p:100000,i:"sorpresa1",d:"Comida, bebida, frutas, cereal, yogurt. Caja madera tipo picnic.",dt:"<b>Incluye:</b><br>\u2022 1 comida \u2022 1 bebida<br>\u2022 Frutas picadas \u2022 Cereal \u2022 Yogurt<br>\u2022 Chocolatina/Galletas Tosh<br>\u2022 Caja madera con bombas"},
{id:"sorpresa2",n:"Desayuno Sorpresa #2",c:"desayunos",p:115000,i:"sorpresa2",d:"Todo del #1 + postre y portarretrato con foto.",dt:"<b>Todo del #1 +:</b><br>\u2022 Postre: Tiramis\u00fa / Parfait<br>\u2022 Portarretrato con foto"},
{id:"sorpresa3",n:"Desayuno Sorpresa #3",c:"desayunos",p:125000,i:"sorpresa3",d:"2 bebidas, parfait, pinguinitos, dulces y portarretrato.",dt:"<b>Incluye:</b><br>\u2022 1 comida \u2022 2 bebidas<br>\u2022 Frutas, Pinguinitos, Parfait<br>\u2022 Dulces \u2022 Portarretrato<br>\u2022 Caja madera con bombas"},
{id:"sorpresa4",n:"Desayuno Sorpresa #4",c:"desayunos",p:150000,i:"sorpresa4",d:"El m\u00e1s completo: torta personal, dulces y portarretrato.",dt:"<b>Todo del #3 +:</b><br>\u2022 Torta personal decorada<br>\u2022 Dulces / frutos secos"},
{id:"saludable",n:"Desayuno Saludable",c:"desayunos",p:100000,i:"saludable",d:"Huevos rancheros, jugo natural, bowl grande con yogurt y frutas.",dt:"<b>Incluye:</b><br>\u2022 Huevos rancheros<br>\u2022 Jugo naranja natural<br>\u2022 Bowl: yogurt griego, avena, frutas, granola, ch\u00eda<br>\u2022 Galleta y Barra Tosh"},
{id:"especial",n:"Desayuno Especial",c:"desayunos",p:120000,i:"especial",d:"Huevos o burrito, jugo natural/verde, bowl frutas, mug, portarretrato.",dt:"<b>Incluye:</b><br>\u2022 Huevos rancheros o Burrito<br>\u2022 Jugo natural o verde<br>\u2022 Bowl frutas \u2022 Mug blanco<br>\u2022 Portarretrato con foto"},
{id:"doble",n:"Desayuno Doble",c:"desayunos",p:135000,i:"doble",d:"Para 2 personas: doble porci\u00f3n de todo. Caja madera.",dt:"<b>Incluye (x2):</b><br>\u2022 2 comidas \u2022 2 bebidas<br>\u2022 2 Cereal \u2022 2 Yogurt<br>\u2022 2 Frutas/Parfait \u2022 2 Chocolatinas<br>\u2022 Portarretrato: +$12,000"},
{id:"dulces",n:"Desayuno Dulces",c:"desayunos",p:110000,i:"dulces",d:"Torta Don Jacobo, Coca Cola, papas, Ferrero y m\u00e1s.",dt:"<b>Incluye:</b><br>\u2022 Torta Don Jacobo \u2022 Coca Cola<br>\u2022 3 papas \u2022 Hatsu/Corona<br>\u2022 Ponqu\u00e9 \u2022 3 Ferrero \u2022 3 chocolatinas<br>\u2022 Caja madera con bombas"},
{id:"detalle",n:"Detalle",c:"desayunos",p:100000,i:"detalle",d:"Tabla quesos, vino GatoNegro, mug/copa. M\u00ednimo 2 unidades.",dt:"<b>Incluye:</b><br>\u2022 Tabla de quesos<br>\u2022 Vino GatoNegro 187.5ml<br>\u2022 Mug o Copa<br>\u2022 <b>M\u00ednimo 2 unidades</b>"},
{id:"frutas",n:"Frutas / Recup\u00e9rate",c:"desayunos",p:110000,i:"frutas",d:"Pi\u00f1a, papaya, manzanas, uvas, bananos, fresas + globo burbuja.",dt:"<b>Incluye:</b><br>\u2022 Pi\u00f1a, papaya, 3 manzanas, pera<br>\u2022 Mandarinas, granadillas<br>\u2022 Uvas, bananos, fresas<br>\u2022 Globo burbuja Recup\u00e9rate"},
{id:"infantil",n:"Desayuno Infantil",c:"infantiles",p:75000,i:"infantil",d:"Pastel de pollo, Milo/jugo, frutas, Oreo. Caja decorada.",dt:"<b>Incluye:</b><br>\u2022 Pastel de pollo / Huevitos<br>\u2022 Milo / Jugo naranja<br>\u2022 Frutas \u2022 Galletas Oreo<br>\u2022 Caja cart\u00f3n decorada"},
{id:"infantil1",n:"Infantil #1",c:"infantiles",p:105000,i:"infantil1",d:"Huevitos, quesadillas, bebida, frutas, Alpinette, Bon Yurt.",dt:"<b>Incluye:</b><br>\u2022 Huevitos rancheros \u2022 Quesadillas<br>\u2022 Bebida \u2022 Frutas<br>\u2022 Alpinette \u2022 Bon Yurt<br>\u2022 Caja madera con globo y bombas"},
{id:"infantil2",n:"Infantil #2",c:"infantiles",p:125000,i:"infantil2",d:"Doble comida, bebidas, Bon Yurt, pinguinito y dulces.",dt:"<b>Incluye:</b><br>\u2022 Huevos + Pastel/Sanduche<br>\u2022 Milo y Jugo<br>\u2022 Frutas, Bon Yurt, Alpinette<br>\u2022 Pinguinito \u2022 Dulces<br>\u2022 Caja madera con globo y bombas"},
{id:"infantil3",n:"Infantil #3",c:"infantiles",p:150000,i:"infantil3",d:"El m\u00e1s completo: torta personal y portarretrato.",dt:"<b>Incluye:</b><br>\u2022 Comida, bebida, cereal, yogurt<br>\u2022 Frutas \u2022 Torta personal con velita<br>\u2022 Dulces \u2022 Portarretrato<br>\u2022 Caja madera con globo y bombas"},
{id:"torta_personal",n:"Torta Personal",c:"tortas",p:38000,i:"torta_personal",d:"Vainilla con arequipe, personalizada en crema. Domicilio $7,000.",dt:"<b>Mini Box:</b><br>\u2022 Vainilla con arequipe<br>\u2022 Personalizada en crema<br>\u2022 Domicilio: $7,000"},
{id:"meme_cake",n:"Meme Cake",c:"tortas",p:38000,i:"meme_cake",d:"Escoge colores, texto y dibujo. Vainilla con arequipe.",dt:"<b>Meme Cake:</b><br>\u2022 Vainilla con arequipe<br>\u2022 T\u00fa escoges todo<br>\u2022 Domicilio: $7,000"},
{id:"mini_cake",n:"Mini Cake",c:"tortas",p:38000,i:"mini_cake",d:"Decoraci\u00f3n en crema, colores y dise\u00f1o a tu gusto.",dt:"<b>Mini Cake:</b><br>\u2022 Vainilla con arequipe<br>\u2022 Decoraci\u00f3n en crema<br>\u2022 Domicilio: $7,000"},
{id:"cupcakes",n:"Caja x6 Cupcakes",c:"tortas",p:45000,i:"cupcakes",d:"6 cupcakes rellenos arequipe/chocolate. 2 d\u00edas anticipaci\u00f3n.",dt:"<b>Caja x6:</b><br>\u2022 Rellenos: arequipe o chocolate<br>\u2022 Dise\u00f1o personalizado<br>\u2022 Domicilio: $7,000<br>\u2022 <b>2 d\u00edas anticipaci\u00f3n</b>"}
];
const AD=[
{id:"bomba",n:"Bomba decorativa",p:6000,i:"bomba"},
{id:"globo",n:"Globo decorativo",p:8000,i:"globo_burbuja"},
{id:"bebida",n:"Bebida adicional",p:7000,i:"bowl_frutas"},
{id:"comida",n:"2da opci\u00f3n comida",p:8000,i:"bandeja_salada"},
{id:"porta",n:"Portarretrato c/foto",p:12000,i:"portarretrato"},
{id:"bowlG",n:"Bowl frutas grande",p:25000,i:"bowl_frutas"},
{id:"bowlP",n:"Bowl frutas peque\u00f1o",p:8000,i:"bowl_frutas"},
{id:"gb",n:"Globo Burbuja",p:12000,i:"globo_burbuja"},
{id:"gn",n:"Globo N\u00famero (c/u)",p:5000,i:"globo_numero"}
];
const CT=[{id:"todos",l:"\ud83c\udf1f Todos"},{id:"bandejas",l:"\ud83c\udf73 Bandejas"},{id:"desayunos",l:"\ud83c\udf81 Desayunos"},{id:"infantiles",l:"\ud83d\udc76 Infantiles"},{id:"tortas",l:"\ud83c\udf82 Tortas"}];
let sp=null,sz={n:'Pereira',e:0},sc='Rosado',st='',sa=[];
function init(){document.getElementById('lg').src=I.logo;rCF();rG('todos');rA();let d=new Date();d.setDate(d.getDate()+1);document.getElementById('fD').min=d.toISOString().split('T')[0]}
function rCF(){document.getElementById('cF').innerHTML=CT.map((c,i)=>'<button class="cb'+(i===0?' a':'')+'" onclick="fC(\''+c.id+'\',this)">'+c.l+'</button>').join('')}
function fC(c,b){document.querySelectorAll('.cb').forEach(x=>x.classList.remove('a'));b.classList.add('a');rG(c)}
function rG(c){const g=document.getElementById('cG');const it=c==='todos'?P:P.filter(x=>x.c===c);g.innerHTML=it.map(p=>'<div class="cd'+(sp&&sp.id===p.id?' sel':'')+'"><img class="ci" src="'+I[p.i]+'" alt="'+p.n+'" loading="lazy"><div class="cb2"><div class="bg">'+cL(p.c)+'</div><div class="cn">'+p.n+'</div><div class="cds">'+p.d+'</div><div class="cp">$'+fm(p.p)+'</div><div class="cdl">\ud83d\ude9a Domicilio Pereira incluido</div><div class="cbt"><button class="bs" onclick="sel(\''+p.id+'\')">Seleccionar</button><button class="bd" onclick="oM(\''+p.id+'\')">Ver m\u00e1s</button></div></div></div>').join('')}
function cL(c){return{bandejas:"\ud83c\udf73 Bandeja",desayunos:"\ud83c\udf81 Desayuno",infantiles:"\ud83d\udc76 Infantil",tortas:"\ud83c\udf82 Torta"}[c]||c}
function fm(n){return n.toLocaleString('es-CO')}
function sel(id){sp=P.find(x=>x.id===id);let ac=document.querySelector('.cb.a');rG(ac&&!ac.textContent.includes('Todos')?sp.c:'todos');uB();sw('form',document.querySelectorAll('.tb')[1])}
function oM(id){const p=P.find(x=>x.id===id);document.getElementById('mI').src=I[p.i];document.getElementById('mB').innerHTML=cL(p.c);document.getElementById('mT').textContent=p.n;document.getElementById('mP').textContent='$'+fm(p.p);document.getElementById('mD').innerHTML=p.dt;document.getElementById('mSB').onclick=()=>{cMo();sel(id)};document.getElementById('md').classList.add('sh')}
function cMo(){document.getElementById('md').classList.remove('sh')}
function uB(){const e=document.getElementById('sB');if(!sp){e.classList.remove('sh');return}e.innerHTML='<img src="'+I[sp.i]+'"><div class="sn">'+sp.n+'</div><div class="sp2">$'+fm(sp.p)+'</div>';e.classList.add('sh')}
function rA(){document.getElementById('aG').innerHTML=AD.map(a=>'<label class="ai" onclick="tA(\''+a.id+'\',this)"><input type="checkbox"><img src="'+I[a.i]+'" alt="'+a.n+'"><div><div class="an">'+a.n+'</div><div class="ap">+$'+fm(a.p)+'</div></div></label>').join('')}
function tA(id,el){const cb=el.querySelector('input');const i=sa.indexOf(id);if(i>-1){sa.splice(i,1);el.classList.remove('ck');cb.checked=false}else{sa.push(id);el.classList.add('ck');cb.checked=true}}
function sZ(n,e,b){document.querySelectorAll('.zb').forEach(x=>x.classList.remove('s'));b.classList.add('s');sz={n,e}}
function sC(c,e){document.querySelectorAll('.cc').forEach(x=>x.classList.remove('s'));e.classList.add('s');sc=c}
function sT(t,e){document.querySelectorAll('.tc2').forEach(x=>x.classList.remove('s'));e.classList.add('s');st=t}
function sw(id,b){document.querySelectorAll('.tc').forEach(t=>t.classList.remove('a'));document.querySelectorAll('.tb').forEach(x=>x.classList.remove('a'));document.getElementById(id).classList.add('a');b.classList.add('a');if(id==='preview')rS()}
function gT(){if(!sp)return 0;let t=sp.p+sz.e;sa.forEach(id=>{const a=AD.find(x=>x.id===id);if(a)t+=a.p});return t}
function rS(){const b=document.getElementById('sB2'),no=document.getElementById('nO');if(!sp){b.style.display='none';no.style.display='block';return}no.style.display='none';b.style.display='block';const ads=sa.map(id=>AD.find(x=>x.id===id)).filter(Boolean);b.innerHTML='<div class="ss"><h3>\ud83c\udf81 Producto</h3><div style="display:flex;gap:14px;align-items:center;margin-bottom:10px"><img src="'+I[sp.i]+'" style="width:70px;height:70px;border-radius:12px;object-fit:cover"><div><b>'+sp.n+'</b><br><span style="color:var(--pk);font-weight:700">$'+fm(sp.p)+'</span></div></div></div><div class="ss"><h3>\ud83d\udccd Entrega</h3>'+R('Destinatario',V('fR'))+R('Tel\u00e9fono',V('fP'))+R('Env\u00eda',V('fS'))+R('Fecha',V('fD'))+R('Hora',V('fT'))+R('Direcci\u00f3n',V('fA'))+R('Ubicaci\u00f3n',V('fL'))+R('Zona',sz.n+(sz.e?' (+$'+fm(sz.e)+')':' (incluido)'))+'</div><div class="ss"><h3>\ud83c\udfa8 Personalizaci\u00f3n</h3>'+R('Color',sc)+R('Tem\u00e1tica',st||'Sin especificar')+R('Mensaje',V('fM'))+R('Foto',V('fPh')||'No')+'</div>'+(ads.length?'<div class="ss"><h3>\u2728 Adiciones</h3>'+ads.map(a=>R(a.n,'+$'+fm(a.p))).join('')+'</div>':'')+'<div class="st2">TOTAL: $'+fm(gT())+'</div>'}
function R(l,v){return'<div class="sr"><span class="l">'+l+'</span><span class="v">'+(v||'-')+'</span></div>'}
function V(id){return document.getElementById(id)?.value||''}
function sendToCRM(viaWA){
if(!SCRIPT_URL){console.log('CRM no configurado');return}
const ads=sa.map(id=>AD.find(x=>x.id===id)).filter(Boolean);
const data={
action:'add',
producto:sp.n,
precioProducto:sp.p,
adiciones:ads.map(a=>a.n).join(', '),
precioAdiciones:ads.reduce((s,a)=>s+a.p,0),
color:sc,
tematica:st,
mensaje:V('fM'),
foto:V('fPh'),
destinatario:V('fR'),
telefono:V('fP'),
envia:V('fS'),
fechaEntrega:V('fD'),
horaEntrega:V('fT'),
direccion:V('fA'),
ubicacion:V('fL'),
zona:sz.n,
costoEnvio:sz.e,
total:gT(),
whatsapp:viaWA?'Si':'No'
};
try{
let ifr=document.getElementById('crmF');if(!ifr){ifr=document.createElement('iframe');ifr.id='crmF';ifr.name='crmF';ifr.style.display='none';document.body.appendChild(ifr)}
const f=document.createElement('form');f.method='POST';f.action=SCRIPT_URL;f.target='crmF';f.style.display='none';
Object.keys(data).forEach(k=>{const inp=document.createElement('input');inp.type='hidden';inp.name=k;inp.value=data[k];f.appendChild(inp)});
document.body.appendChild(f);f.submit();document.body.removeChild(f);
const ci=document.getElementById('crmI');if(ci){ci.innerHTML='\u2705 Registrado en CRM';ci.style.display='block';setTimeout(()=>ci.style.display='none',4000)}
}catch(e){console.log('CRM error:',e);const ci=document.getElementById('crmI');if(ci){ci.innerHTML='\u26a0\ufe0f CRM sin conexi\u00f3n';ci.style.background='#fef3c7';ci.style.color='#92400e';ci.style.display='block'}}
}
function enviar(){if(!sp){sM('er','Selecciona un producto primero');return}for(const id of['fR','fP','fS','fD','fT','fA','fM']){if(!V(id)){sM('er','Completa todos los campos obligatorios (*)');document.getElementById(id)?.focus();return}}sendToCRM(true);sw('preview',document.querySelectorAll('.tb')[2]);const ads=sa.map(id=>AD.find(x=>x.id===id)).filter(Boolean);let m='\ud83c\udf1f *PEDIDO DESAYUNOS CON AMOR* \ud83c\udf1f\n\n';m+='\ud83c\udf81 *Producto:* '+sp.n+'\n\ud83d\udcb0 *Precio:* $'+fm(sp.p)+'\n\n';m+='\ud83d\udccd *ENTREGA*\n';m+='Destinatario: '+V('fR')+'\nTel: '+V('fP')+'\nEnv\u00eda: '+V('fS')+'\nFecha: '+V('fD')+'\nHora: '+V('fT')+'\nDirecci\u00f3n: '+V('fA')+'\n';if(V('fL'))m+='Ubicaci\u00f3n: '+V('fL')+'\n';m+='Zona: '+sz.n+(sz.e?' (+$'+fm(sz.e)+')':'')+'\n\n';m+='\ud83c\udfa8 *PERSONALIZACI\u00d3N*\nColor: '+sc+'\n';if(st)m+='Tem\u00e1tica: '+st+'\n';m+='Mensaje: '+V('fM')+'\n';if(V('fPh'))m+='Foto: '+V('fPh')+'\n';if(ads.length){m+='\n\u2728 *ADICIONES*\n';ads.forEach(a=>{m+='\u2022 '+a.n+' (+$'+fm(a.p)+')\n'})}m+='\n\ud83d\udcb0 *TOTAL: $'+fm(gT())+'*';window.open('https://wa.me/573232167091?text='+encodeURIComponent(m),'_blank')}
function waFn(){enviar()}
function sM(t,x){const a=document.getElementById('mA');a.innerHTML='<div class="msg '+t+'">'+x+'</div>';setTimeout(()=>{a.innerHTML=''},5000)}
function rst(){sp=null;sa=[];st='';sc='Rosado';sz={n:'Pereira',e:0};document.getElementById('oF').reset();uB();rG('todos');rA();document.querySelectorAll('.zb').forEach((b,i)=>b.classList.toggle('s',!i));document.querySelectorAll('.cc').forEach((c,i)=>c.classList.toggle('s',!i));document.querySelectorAll('.tc2').forEach(c=>c.classList.remove('s'));sM('ok','Formulario limpiado')}
document.addEventListener('DOMContentLoaded',init);
</script>
</body></html>'''

out = r"C:\Users\widag\OneDrive\Escritorio\App Desayunos Con Amor\desayunos_app.html"
with open(out, 'w', encoding='utf-8') as f:
    f.write(html_top)
    f.write(html_script)

print(f"Done! Size: {os.path.getsize(out)} bytes ({os.path.getsize(out)//1024} KB)")
