  // Obtener el usuario desde localStorage
  const nombre = localStorage.getItem("usuario");

  // Mostrarlo en la página
  if (nombre) {
    document.getElementById("nombreUsuario").textContent = nombre;
  } else {
    // Si no hay usuario, redirige a login
    window.location.href = "index.html";
  }

  // Si quieres que el botón de cerrar sesión borre el usuario
  document.querySelector('.btn_logout').addEventListener('click', function() {
    localStorage.removeItem("usuario");
  });

  document.querySelectorAll('.toggle-submenu').forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault(); // Evita que recargue la página
      const submenu = this.nextElementSibling;
      submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
    });
  });