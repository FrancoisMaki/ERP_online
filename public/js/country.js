document.addEventListener("DOMContentLoaded", () => {
  const sections = {
    "add-country": document.getElementById("section-add"),
    "view-country": document.getElementById("section-view"),
    "edit-country": document.getElementById("section-edit"),
    "delete-country": document.getElementById("section-delete"),
  };

  // Oculta todas las secciones
  function hideAllSections() {
    Object.values(sections).forEach(section => section.classList.add("hidden"));
  }

  // Muestra solo la que corresponde
  function showSection(id) {
    hideAllSections();
    if (sections[id]) {
      sections[id].classList.remove("hidden");
    }
  }

  // Asocia cada botón con su sección
  Object.keys(sections).forEach(btnId => {
    const btn = document.getElementById(btnId);
    if (btn) {
      btn.addEventListener("click", () => showSection(btnId));
    }
  });
});

document.getElementById("form-add").addEventListener("submit", async (e) => {
  e.preventDefault();
  const nuevoPais = {
    paisid: document.getElementById("paisid").value.trim(),
    iso3: document.getElementById("iso3").value.trim(),
    nombre: document.getElementById("nombre").value.trim(),
    nombre_ingles: document.getElementById("nombre_ingles").value.trim(),
    codigo_numerico: Number(document.getElementById("codigo_numerico").value) || null,
    prefijo_telefono: document.getElementById("prefijo_telefono").value.trim(),
    continente: document.getElementById("continente").value.trim()
  };

  try {
    const res = await fetch('/api/paises', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(nuevoPais)
    });
    const data = await res.json();
    document.getElementById("mensaje-add").textContent = data.message || "País guardado.";
  } catch (err) {
    document.getElementById("mensaje-add").textContent = "Error al guardar el país.";
    console.error(err);
  }
});


