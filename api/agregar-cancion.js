import { createClient } from "@supabase/supabase-js";
import formidable from "formidable";
import fs from "fs";

export const config = {
    api: {
        bodyParser: false, // obligatorio para recibir archivos
    },
};

const supabase = createClient(
    process.env.SUPABASE_URL,
    process.env.SUPABASE_SERVICE_KEY
);

export default async function handler(req, res) {
    if (req.method !== "POST") {
        return res.status(405).json({ error: "Método no permitido" });
    }

    const form = formidable({ multiples: false });

    form.parse(req, async (err, fields, files) => {
        if (err) return res.status(500).json({ error: "Error procesando archivo" });

        const file = files.imagen;
        const fileData = fs.readFileSync(file.filepath);
        const fileName = `portadas/${Date.now()}-${file.originalFilename}`;

        // 1. Subir imagen a Supabase Storage
        const { error: uploadError } = await supabase.storage
            .from("imagenes")
            .upload(fileName, fileData, { contentType: file.mimetype });

        if (uploadError) {
            return res.status(500).json({ error: "Error subiendo imagen" });
        }

        // 2. Obtener URL pública
        const { data: urlData } = supabase.storage
            .from("imagenes")
            .getPublicUrl(fileName);

        const rutaImagen = urlData.publicUrl;

        // Guardar en la tabla cancion
        const { error: insertError } = await supabase.from("cancion").insert({
            nombre: fields.nombre,
            artista: fields.artista,
            duracion: fields.duracion,
            ruta: rutaImagen
        });

        if (insertError) {
            return res.status(500).json({ error: "Error guardando en DB" });
        }

        return res.status(200).json({ success: true, rutaImagen });
    });
}
