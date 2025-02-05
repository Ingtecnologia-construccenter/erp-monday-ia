from flask import Flask, request
from monday_api import obtener_tableros, crear_tarea
from ai_logic import analizar_tarea

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def recibir_webhook():
    datos = request.json
    print("📩 Evento recibido:", datos)

    if "event" in datos and datos["event"]["type"] == "update_column_value":
        tarea = datos["event"]["value"]
        sugerencia = analizar_tarea(tarea)
        print(f"🔹 Sugerencia de IA: {sugerencia}")
    
    return {"status": "ok"}, 200

if __name__ == '__main__':
    print("🔹 Tableros en Monday:", obtener_tableros())
    app.run(port=5000)