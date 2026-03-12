// =============================================================
// DESAYUNOS CON AMOR - CRM Google Sheets
// =============================================================
// INSTRUCCIONES:
// 1. Ve a https://script.google.com
// 2. Crea un nuevo proyecto
// 3. Pega TODO este codigo
// 4. Click en "Implementar" > "Nueva implementacion"
// 5. Tipo: "Aplicacion web"
// 6. Ejecutar como: "Yo"
// 7. Acceso: "Cualquier persona"
// 8. Click en "Implementar" y copia la URL
// 9. Pega la URL en la app (variable SCRIPT_URL)
// =============================================================

const SHEET_NAME = "Pedidos";
const HEADERS = [
  "ID", "Fecha Pedido", "Estado",
  "Producto", "Precio Producto", "Adiciones", "Precio Adiciones",
  "Color", "Tematica", "Mensaje", "Foto",
  "Destinatario", "Telefono", "Envia",
  "Fecha Entrega", "Hora Entrega", "Direccion", "Ubicacion",
  "Zona", "Costo Envio",
  "TOTAL", "WhatsApp Enviado"
];

function doGet(e) {
  return handleRequest(e);
}

function doPost(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  try {
    // Handle CORS preflight
    var output = ContentService.createTextOutput();
    output.setMimeType(ContentService.MimeType.JSON);

    var params;
    // Check e.parameter first (works for both form POST and GET query params)
    if (e.parameter && e.parameter.action) {
      params = e.parameter;
    } else if (e.postData) {
      try {
        params = JSON.parse(e.postData.contents);
      } catch(parseErr) {
        // If not JSON, use e.parameter as fallback
        params = e.parameter || {};
      }
    } else {
      return output.setContent(JSON.stringify({
        status: "ok",
        message: "CRM Desayunos con Amor activo"
      }));
    }

    var action = params.action || "add";

    if (action === "add") {
      return output.setContent(JSON.stringify(addOrder(params)));
    } else if (action === "list") {
      return output.setContent(JSON.stringify(listOrders()));
    } else if (action === "update") {
      return output.setContent(JSON.stringify(updateStatus(params)));
    }

    return output.setContent(JSON.stringify({ status: "error", message: "Accion no valida" }));

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

const SPREADSHEET_ID = "17Ut5cAB0XkUNflr1xc9Kjda6P7RVZXz4kxzPBVcil9I";

function getOrCreateSheet() {
  var ss;
  try { ss = SpreadsheetApp.getActiveSpreadsheet(); } catch(e) { ss = null; }
  if (!ss) ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  var sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    // Add headers
    sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]);

    // Format header row
    var headerRange = sheet.getRange(1, 1, 1, HEADERS.length);
    headerRange.setBackground("#be185d");
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");

    // Freeze header
    sheet.setFrozenRows(1);

    // Set column widths
    sheet.setColumnWidth(1, 80);   // ID
    sheet.setColumnWidth(2, 140);  // Fecha Pedido
    sheet.setColumnWidth(3, 100);  // Estado
    sheet.setColumnWidth(4, 200);  // Producto
    sheet.setColumnWidth(5, 120);  // Precio Producto
    sheet.setColumnWidth(6, 250);  // Adiciones
    sheet.setColumnWidth(7, 120);  // Precio Adiciones
    sheet.setColumnWidth(12, 160); // Destinatario
    sheet.setColumnWidth(15, 120); // Fecha Entrega
    sheet.setColumnWidth(17, 250); // Direccion
    sheet.setColumnWidth(21, 120); // TOTAL

    // Add conditional formatting for Estado column
    var statusRange = sheet.getRange("C2:C1000");
    var rules = [];

    // Nuevo = Yellow
    rules.push(SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("Nuevo")
      .setBackground("#fef3c7")
      .setFontColor("#92400e")
      .setRanges([statusRange])
      .build());

    // En preparacion = Blue
    rules.push(SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("En preparacion")
      .setBackground("#dbeafe")
      .setFontColor("#1e40af")
      .setRanges([statusRange])
      .build());

    // En camino = Purple
    rules.push(SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("En camino")
      .setBackground("#ede9fe")
      .setFontColor("#6d28d9")
      .setRanges([statusRange])
      .build());

    // Entregado = Green
    rules.push(SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("Entregado")
      .setBackground("#d1fae5")
      .setFontColor("#065f46")
      .setRanges([statusRange])
      .build());

    // Cancelado = Red
    rules.push(SpreadsheetApp.newConditionalFormatRule()
      .whenTextEqualTo("Cancelado")
      .setBackground("#fee2e2")
      .setFontColor("#991b1b")
      .setRanges([statusRange])
      .build());

    sheet.setConditionalFormatRules(rules);

    // Add data validation for Estado
    var validation = SpreadsheetApp.newDataValidation()
      .requireValueInList(["Nuevo", "En preparacion", "En camino", "Entregado", "Cancelado"])
      .setAllowInvalid(false)
      .build();
    statusRange.setDataValidation(validation);
  }

  return sheet;
}

function addOrder(data) {
  var sheet = getOrCreateSheet();
  var lastRow = sheet.getLastRow();
  var id = "DCA-" + String(lastRow).padStart(4, "0");

  var now = new Date();
  var fecha = Utilities.formatDate(now, Session.getScriptTimeZone(), "yyyy-MM-dd HH:mm:ss");

  var adiciones = data.adiciones || "";
  var precioAdiciones = data.precioAdiciones || 0;

  var row = [
    id,
    fecha,
    "Nuevo",
    data.producto || "",
    data.precioProducto || 0,
    adiciones,
    precioAdiciones,
    data.color || "",
    data.tematica || "",
    data.mensaje || "",
    data.foto || "",
    data.destinatario || "",
    data.telefono || "",
    data.envia || "",
    data.fechaEntrega || "",
    data.horaEntrega || "",
    data.direccion || "",
    data.ubicacion || "",
    data.zona || "",
    data.costoEnvio || 0,
    data.total || 0,
    data.whatsapp || "No"
  ];

  sheet.appendRow(row);

  // Format currency columns for the new row
  var newRow = sheet.getLastRow();
  sheet.getRange(newRow, 5).setNumberFormat("$#,##0");  // Precio Producto
  sheet.getRange(newRow, 7).setNumberFormat("$#,##0");  // Precio Adiciones
  sheet.getRange(newRow, 20).setNumberFormat("$#,##0"); // Costo Envio
  sheet.getRange(newRow, 21).setNumberFormat("$#,##0"); // TOTAL

  // Create Google Calendar event for delivery
  var calEventId = null;
  if (data.fechaEntrega && data.horaEntrega) {
    calEventId = createCalendarEvent(data, id);
  }

  return {
    status: "ok",
    message: "Pedido registrado" + (calEventId ? " y agregado al calendario" : ""),
    orderId: id,
    fecha: fecha,
    calendarEvent: calEventId
  };
}

function listOrders() {
  var sheet = getOrCreateSheet();
  var lastRow = sheet.getLastRow();

  if (lastRow <= 1) {
    return { status: "ok", orders: [], total: 0 };
  }

  var data = sheet.getRange(2, 1, lastRow - 1, HEADERS.length).getValues();
  var orders = data.map(function(row) {
    var obj = {};
    HEADERS.forEach(function(h, i) {
      obj[h] = row[i];
    });
    return obj;
  });

  return { status: "ok", orders: orders, total: orders.length };
}

function updateStatus(data) {
  var sheet = getOrCreateSheet();
  var lastRow = sheet.getLastRow();

  if (lastRow <= 1) {
    return { status: "error", message: "No hay pedidos" };
  }

  var ids = sheet.getRange(2, 1, lastRow - 1, 1).getValues();
  for (var i = 0; i < ids.length; i++) {
    if (ids[i][0] === data.orderId) {
      sheet.getRange(i + 2, 3).setValue(data.estado);
      return { status: "ok", message: "Estado actualizado a: " + data.estado };
    }
  }

  return { status: "error", message: "Pedido no encontrado: " + data.orderId };
}

// ===================== GOOGLE CALENDAR =====================

function parseTimeRange(dateStr, timeStr) {
  // dateStr: "2026-03-15", timeStr: "8:00-9:00 AM" or "12:00-1:00 PM"
  var parts = dateStr.split("-");
  var year = parseInt(parts[0]);
  var month = parseInt(parts[1]) - 1; // 0-indexed
  var day = parseInt(parts[2]);

  // Parse time range like "8:00-9:00 AM" or "12:00-1:00 PM"
  var match = timeStr.match(/(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})\s*(AM|PM)/i);
  if (!match) {
    // Fallback: create all-day event times
    return {
      start: new Date(year, month, day, 8, 0),
      end: new Date(year, month, day, 9, 0)
    };
  }

  var startH = parseInt(match[1]);
  var startM = parseInt(match[2]);
  var endH = parseInt(match[3]);
  var endM = parseInt(match[4]);
  var ampm = match[5].toUpperCase();

  // Convert to 24h format
  if (ampm === "PM") {
    if (startH < 12) startH += 12;
    if (endH < 12) endH += 12;
  } else {
    if (startH === 12) startH = 0;
    if (endH === 12) endH = 0;
  }

  return {
    start: new Date(year, month, day, startH, startM),
    end: new Date(year, month, day, endH, endM)
  };
}

function createCalendarEvent(data, orderId) {
  try {
    var cal = CalendarApp.getDefaultCalendar();
    var times = parseTimeRange(data.fechaEntrega || "", data.horaEntrega || "");

    // TITULO: Producto + Nombre quien envia + Telefono quien envia
    var title = (data.producto || "Pedido") + " | " + (data.envia || "Sin remitente") + " | " + (data.telefono || "");

    // DESCRIPCION
    var desc = "";
    // Quien recibe + telefono
    desc += "Recibe: " + (data.destinatario || "") + " - Tel: " + (data.telefono || "") + "\n\n";
    // Producto + adicionales + ocasion + decoracion
    desc += "Producto: " + (data.producto || "") + "\n";
    if (data.adiciones) desc += "Adicionales: " + data.adiciones + "\n";
    if (data.tematica) desc += "Ocasion: " + data.tematica + "\n";
    if (data.color) desc += "Decoracion: " + data.color + "\n";
    if (data.mensaje) desc += "Mensaje: " + data.mensaje + "\n";
    desc += "\n";
    // Direccion
    desc += "Direccion: " + (data.direccion || "") + (data.zona ? ", " + data.zona : "") + "\n\n";
    // Rango de hora
    desc += "Hora: " + (data.horaEntrega || "") + "\n";
    // Total
    desc += "\nTotal: $" + (data.total || 0) + " | Pedido: " + orderId;

    var location = (data.direccion || "") + (data.zona ? ", " + data.zona : "");

    var event = cal.createEvent(title, times.start, times.end, {
      description: desc,
      location: location
    });

    // Set event color to grape/purple
    event.setColor("3");

    return event.getId();
  } catch (err) {
    Logger.log("Error creando evento calendar: " + err.toString());
    return null;
  }
}

// ===================== SETUP =====================

// Run this once to initialize the sheet
function setup() {
  getOrCreateSheet();
  Logger.log("Sheet created successfully!");
}
