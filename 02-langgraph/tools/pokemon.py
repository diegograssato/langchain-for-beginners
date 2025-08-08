from mcp.server.fastmcp import FastMCP
import requests


mcp = FastMCP("pokemon", port=8080)

@mcp.tool()
async def get_context(input: str) -> dict:
    """Consulta a API de Pokémon e retorna dados relevantes."""
    nome = input.lower().strip()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            "nome": data["name"],
            "altura": data["height"],
            "peso": data["weight"],
            "tipos": [t["type"]["name"] for t in data["types"]],
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao buscar Pokémon '{nome}': {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
