import requests
from config import MONDAY_URL, HEADERS

def obtener_tableros():
    query = """
    {
      boards {
        id
        name
      }
    }
    """
    response = requests.post(MONDAY_URL, json={"query": query}, headers=HEADERS)
    return response.json()

if __name__ == "__main__":
    print(obtener_tableros())  # Prueba de conexión
