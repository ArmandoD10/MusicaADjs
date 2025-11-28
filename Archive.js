document.documentElement.classList.add("dark");

// Evento del botón de cambio de tema
document.getElementById("btnTema").addEventListener("click", function () {
    document.documentElement.classList.toggle("dark");
});

function login() {
    const correo = "armandodiaz1020158@gmail.com";
    const contrasena = "1020158ad";

    var corr = document.getElementById("usuario").value;
    var contra = document.getElementById("contrasena").value;

    if(corr == correo){
        alert("Bienvenido! Armando")
        window.location.href = "Menu.html"; 
        document.getElementById("contrasena").value = "";
        document.getElementById("usuario").value = "";
    }else{
        alert("Correo o contrasena incorrectos!");
        document.getElementById("contrasena").value = "";
        document.getElementById("usuario").value = "";
    }

}