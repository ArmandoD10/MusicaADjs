document.getElementById("btnGuardarCancion").addEventListener("click", async () => {
    const nombre = document.getElementById("songName").value.trim();
    const artista = document.getElementById("songartist").value.trim();
    const duracion = document.getElementById("songDuration").value.trim();
    const imagenInput = document.getElementById("songImage");

    if (!nombre || !artista || !duracion || !imagenInput.files[0]) {
        alert("Todos los campos son obligatorios.");
        return;
    }

    // Subir imagen al backend
    const formData = new FormData();
    formData.append("imagen", imagenInput.files[0]);

    const respImagen = await fetch("/api/agregar-cancion", {
        method: "POST",
        body: formData
    });

    const data = await respImagen.json();
    console.log(data);

    if (data.success) {
        alert("Canción guardada correctamente 🎶");
    } else {
        alert("Error al guardar la canción");
    }
});
