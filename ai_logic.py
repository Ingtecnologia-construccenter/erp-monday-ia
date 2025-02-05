import openai

openai.api_key = "TU_API_KEY_AQUI"

def analizar_tarea(texto):
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Cambié gpt-4 por gpt-3.5-turbo
        messages=[{"role": "user", "content": texto}]
    )
    return respuesta["choices"][0]["message"]["content"]

if __name__ == "__main__":
    tarea = "Revisar cotización de proveedor."
    print("🔹 Sugerencia de IA:", analizar_tarea(tarea))