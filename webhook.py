from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def recibir_webhook():
    datos = request.json
    print("📩 Evento recibido:", datos)
    
    # Aquí puedes agregar lógica para procesar el evento
    if "event" in datos and datos["event"]["type"] == "update_column_value":
        print(f"📌 Se actualizó una columna: {datos['event']}")

    return {"status": "ok"}, 200

if __name__ == '__main__':
    app.run(port=5000)
