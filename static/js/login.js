  document.getElementById("loginform").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario recargue la página

    // Obtenemos el valor del campo de usuario
    const usuario = document.querySelector("input[name='usuario']").value;

    // Guardamos el usuario en localStorage
    localStorage.setItem("usuario", usuario);

    // Redirigimos a la página post-login
    window.location.href = "/main";
  });