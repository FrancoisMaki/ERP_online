document.addEventListener("DOMContentLoaded", () => {
  const secciones = {
    add: document.getElementById("section-prov-add"),
    view: document.getElementById("section-prov-view"),
    edit: document.getElementById("section-prov-edit"),
    delete: document.getElementById("section-prov-delete")
  };

  const ocultarTodas = () => {
    Object.values(secciones).forEach(sec => sec.classList.add("hidden"));
  };

  // Mostrar la sección correspondiente al hacer clic
  document.getElementById("add-prov").addEventListener("click", () => {
    ocultarTodas();
    secciones.add.classList.remove("hidden");
  });

  document.getElementById("view-prov").addEventListener("click", () => {
    ocultarTodas();
    secciones.view.classList.remove("hidden");
    cargarProvincias();
  });

  document.getElementById("edit-prov").addEventListener("click", () => {
    ocultarTodas();
    secciones.edit.classList.remove("hidden");
  });

  document.getElementById("delete-prov").addEventListener("click", () => {
    ocultarTodas();
    secciones.delete.classList.remove("hidden");
  });

  // Cargar provincias en la tabla
  async function cargarProvincias() {
    try {
      const res = await fetch('/api/provincias');
      const provincias = await res.json();

      const tbody = document.querySelector("#tabla-provincias tbody");
      tbody.innerHTML = "";

      provincias.forEach(p => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${p.provinciaid}</td>
          <td>${p.nombre}</td>
          <td>${p.paisid}</td>
          <td>${p.codigo_iso || ""}</td>
        `;
        tbody.appendChild(row);
      });
    } catch (err) {
      console.error("Error al cargar provincias:", err);
    }
  }

  // Añadir provincia
  document.getElementById("form-prov-add").addEventListener("submit", async (e) => {
    e.preventDefault();
    const nuevaProvincia = {
      provinciaid: parseInt(document.getElementById("provinciaid").value),
      nombre: document.getElementById("nombre").value.trim(),
      paisid: document.getElementById("paisid").value.trim(),
      codigo_iso: document.getElementById("codigo_iso").value.trim()
    };

    try {
      const res = await fetch('/api/provincias', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevaProvincia)
      });
      const data = await res.json();
      document.getElementById("mensaje-prov-add").textContent = data.message || "Provincia guardada.";
      document.getElementById("form-prov-add").reset();
    } catch (err) {
      document.getElementById("mensaje-prov-add").textContent = "Error al guardar la provincia.";
      console.error(err);
    }
  });

  // Editar provincia
  document.getElementById("form-prov-edit").addEventListener("submit", async (e) => {
    e.preventDefault();
    const provinciaid = parseInt(document.getElementById("edit-provinciaid").value);
    const paisid = document.getElementById("edit-paisid").value.trim();
    const nombre = document.getElementById("edit-nombre").value.trim();
    const codigo_iso = document.getElementById("edit-codigo_iso").value.trim();

    const datosActualizados = {};
    if (nombre) datosActualizados.nombre = nombre;
    if (codigo_iso) datosActualizados.codigo_iso = codigo_iso;

    try {
      const res = await fetch(`/api/provincias/${provinciaid}/${paisid}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datosActualizados)
      });
      const data = await res.json();
      document.getElementById("mensaje-prov-edit").textContent = data.message || "Provincia actualizada.";
      document.getElementById("form-prov-edit").reset();
      cargarProvincias();
    } catch (err) {
      document.getElementById("mensaje-prov-edit").textContent = "Error al actualizar la provincia.";
      console.error(err);
    }
  });

  // Eliminar provincia
  document.getElementById("form-prov-delete").addEventListener("submit", async (e) => {
    e.preventDefault();
    const provinciaid = parseInt(document.getElementById("delete-provinciaid").value);
    const paisid = document.getElementById("delete-paisid").value.trim();

    try {
      const res = await fetch(`/api/provincias/${provinciaid}/${paisid}`, {
        method: 'DELETE'
      });
      const data = await res.json();
      document.getElementById("mensaje-prov-delete").textContent = data.message || "Provincia eliminada.";
      document.getElementById("form-prov-delete").reset();
      cargarProvincias();
    } catch (err) {
      document.getElementById("mensaje-prov-delete").textContent = "Error al eliminar la provincia.";
      console.error(err);
    }
  });
});
