document.addEventListener("DOMContentLoaded", () => {
  const secciones = {
    add: document.getElementById("section-add"),
    view: document.getElementById("section-view"),
    edit: document.getElementById("section-edit"),
    delete: document.getElementById("section-delete")
  };

  const ocultarTodas = () => {
    Object.values(secciones).forEach(sec => sec.classList.add("hidden"));
  };

  // Mostrar sección al hacer clic en los botones
  document.getElementById("add-country").addEventListener("click", () => {
    ocultarTodas();
    secciones.add.classList.remove("hidden");
  });

  document.getElementById("view-country").addEventListener("click", () => {
    ocultarTodas();
    secciones.view.classList.remove("hidden");
    cargarPaises();
  });

  document.getElementById("edit-country").addEventListener("click", () => {
    ocultarTodas();
    secciones.edit.classList.remove("hidden");
  });

  document.getElementById("delete-country").addEventListener("click", () => {
    ocultarTodas();
    secciones.delete.classList.remove("hidden");
  });

  // Función para cargar países en la tabla
  async function cargarPaises() {
    try {
      const res = await fetch('/api/paises');
      const paises = await res.json();

      const tbody = document.querySelector("#tabla-paises tbody");
      tbody.innerHTML = "";

      paises.forEach(pais => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${pais.paisid}</td>
          <td>${pais.iso3}</td>
          <td>${pais.nombre}</td>
          <td>${pais.continente}</td>
        `;
        tbody.appendChild(row);
      });
    } catch (err) {
      console.error("Error al cargar países:", err);
    }
  }

  // Crear país
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
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevoPais)
      });
      const data = await res.json();
      document.getElementById("mensaje-add").textContent = data.message || "País guardado.";
      document.getElementById("form-add").reset();
    } catch (err) {
      document.getElementById("mensaje-add").textContent = "Error al guardar el país.";
      console.error(err);
    }
  });

  // Editar país
  document.getElementById("form-edit").addEventListener("submit", async (e) => {
    e.preventDefault();
    const paisid = document.getElementById("edit-paisid").value.trim();
    const nombre = document.getElementById("edit-nombre").value.trim();
    const continente = document.getElementById("edit-continente").value.trim();

    const datosActualizados = { nombre, continente };

    try {
      const res = await fetch(`/api/paises/${paisid}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datosActualizados)
      });
      const data = await res.json();
      document.getElementById("mensaje-edit").textContent = data.message || "País actualizado.";
      document.getElementById("form-edit").reset();
      cargarPaises(); // Opcional: recargar listado si está visible
    } catch (err) {
      document.getElementById("mensaje-edit").textContent = "Error al actualizar país.";
      console.error(err);
    }
  });

  // Eliminar país
  document.getElementById("form-delete").addEventListener("submit", async (e) => {
    e.preventDefault();
    const paisid = document.getElementById("delete-paisid").value.trim();

    try {
      const res = await fetch(`/api/paises/${paisid}`, {
        method: 'DELETE'
      });
      const data = await res.json();
      document.getElementById("mensaje-delete").textContent = data.message || "País eliminado.";
      document.getElementById("form-delete").reset();
      cargarPaises();
    } catch (err) {
      document.getElementById("mensaje-delete").textContent = "Error al eliminar país.";
      console.error(err);
    }
  });
});
