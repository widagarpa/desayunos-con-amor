# 🌅 Desayunos con Amor - App de Pedidos

Aplicación web para gestión de pedidos de desayunos sorpresa en Pereira, Colombia.

## Características

- 📱 App web responsiva (mobile-first)
- 🛒 Catálogo de productos con imágenes
- 🎨 Personalización de pedidos (color, temática, mensaje)
- 📍 Selección de zona de entrega con costo automático
- ✨ Adiciones al pedido
- 📋 Resumen del pedido con cálculo de total
- 💾 CRM integrado con Google Sheets via Apps Script
- 📲 Envío de pedido por WhatsApp

## Arquitectura

- **Frontend**: Single-file HTML app (~545KB) con CSS/JS embebido e imágenes en base64
- **Backend CRM**: Google Apps Script desplegado como web app
- **Base de datos**: Google Sheets ("Pedidos")
- **Hosting**: Netlify (static site)
- **Build**: Python script (`build_app.py`) que genera el archivo HTML final

## Archivos

| Archivo | Descripción |
|---------|-------------|
| `index.html` | App completa lista para desplegar en Netlify |
| `build_app.py` | Script Python que genera `index.html` a partir de las imágenes y datos |
| `google_apps_script.js` | Código del backend CRM (Google Apps Script) |

## Despliegue

### Frontend (Netlify)
1. Subir `index.html` a [Netlify Drop](https://app.netlify.com/drop)
2. URL: https://desayunosconamor23.netlify.app

### Backend CRM (Google Apps Script)
1. Crear proyecto en [Google Apps Script](https://script.google.com)
2. Pegar el contenido de `google_apps_script.js`
3. Implementar como aplicación web (acceso: "Cualquier persona")
4. Actualizar la URL del deployment en `build_app.py`

## Flujo del Pedido

1. Cliente selecciona producto del catálogo
2. Completa datos de entrega (destinatario, dirección, fecha, hora)
3. Personaliza el pedido (color, temática, mensaje)
4. Agrega adiciones opcionales
5. Click en **"Enviar Pedido"**:
   - ✅ Valida campos obligatorios
   - 💾 Envía datos al CRM (Google Sheets)
   - 📲 Abre WhatsApp con el resumen del pedido

## Tecnologías

- HTML5, CSS3, JavaScript (vanilla)
- Python 3 (build script)
- Google Apps Script
- Google Sheets API
- Netlify (hosting)
