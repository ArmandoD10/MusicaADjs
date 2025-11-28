document.documentElement.classList.add("dark");

// Evento del botón de cambio de tema
document.getElementById("btnTema").addEventListener("click", function () {
    document.documentElement.classList.toggle("dark");
});

document.getElementById("btnLogin").addEventListener("click", login);

async function login() {
    let correo = document.getElementById("usuario").value.trim();
    let password = document.getElementById("contrasena").value.trim();

    if (correo === "" || password === "") {
        alert("Debe llenar todos los campos.");
        return;
    }

    const { data, error } = await window.supabase
    .from("usuario")
    .select("*")
    .eq("Correo", correo)
    .single();

    if (error || !data) {
        alert("Correo no encontrado.");
        return;
    }

    if (data.Contrasena !== password) {
        alert("Contraseña incorrecta.");
        return;
    }

    // Login exitoso
    alert("Bienvenido " + data.Correo);
    window.location.href = "Menu.html"; // crea esta página
}
