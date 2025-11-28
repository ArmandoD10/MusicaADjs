from flask import Flask, request, jsonify, render_template
import os
from datetime import datetime

# Inicializa Flask
app = Flask(__name__)

# Define la ruta al archivo de registro
REGISTRO_FILE = 'registro.txt'
# Inicializamos un contador simple para IDs (puede ser mejorado)
next_id = 1 

# --- Función para obtener el siguiente ID y cargar datos existentes ---
def get_next_id():
    global next_id
    if not os.path.exists(REGISTRO_FILE):
        return 1

    try:
        with open(REGISTRO_FILE, 'r') as f:
            lines = f.readlines()
            if lines:
                # Encuentra el ID más grande existente y le suma 1
                last_line = lines[-1].split(';')
                last_id = int(last_line[0])
                next_id = last_id + 1
                return next_id
            else:
                return 1
    except Exception as e:
        print(f"Error al leer IDs del registro: {e}")
        return 1

# Aseguramos que el ID se calcule al iniciar
next_id = get_next_id()

@app.route('/')
def index():
    # Esta ruta simplemente renderiza tu archivo HTML (debe llamarse index.html)
    # y sirve como punto de entrada.
    return render_template('index.html')

@app.route('/api/guardar-cancion', methods=['POST'])
def guardar_cancion():
    global next_id
    
    # 1. Recibir los datos del formulario JSON
    data = request.json
    
    # Validaciones básicas
    if not all(k in data for k in ('name', 'artist', 'duration', 'imageSrc')):
        return jsonify({"error": "Datos incompletos"}), 400

    # 2. Formatear la nueva línea del registro
    # Formato: codigo;nombre cancion;artista;duracion;ruta de la imagen
    new_record = (
        f"{next_id};"
        f"{data['name']};"
        f"{data['artist']};"
        f"{data['duration']};"
        f"{data['imageSrc']}\n"  # Usamos la ruta o Base64 que envíe JS
    )
    
    # 3. Escribir en el archivo .txt
    try:
        with open(REGISTRO_FILE, 'a') as f:
            f.write(new_record)
        
        # Incrementar el ID para la próxima vez
        next_id += 1
        
        return jsonify({
            "success": True, 
            "message": "Canción guardada con éxito",
            "new_id": next_id - 1 # Devolvemos el ID que acabamos de usar
        }), 200
        
    except Exception as e:
        return jsonify({"error": f"Error al escribir en el archivo: {str(e)}"}), 500

@app.route('/api/obtener-canciones')
def obtener_canciones():
    """Ruta para que JavaScript obtenga las tarjetas existentes."""
    songs = []
    if os.path.exists(REGISTRO_FILE):
        try:
            with open(REGISTRO_FILE, 'r') as f:
                for line in f:
                    parts = line.strip().split(';')
                    if len(parts) == 5:
                        songs.append({
                            "id": parts[0],
                            "name": parts[1],
                            "artist": parts[2],
                            "duration": parts[3],
                            "imageSrc": parts[4].strip()
                        })
        except Exception as e:
            return jsonify({"error": f"Error al leer el archivo: {str(e)}"}), 500

    return jsonify(songs), 200


if __name__ == '__main__':
    # Necesitas que tu archivo HTML se llame 'index.html' y esté en una carpeta 'templates'
    # o ejecutar Flask en modo de desarrollo simple si el HTML está en el mismo nivel.
    app.run(debug=True)