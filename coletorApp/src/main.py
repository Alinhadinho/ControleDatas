import flet as ft
from app.main import main
import os
from openpyxl import Workbook
from fastapi import FastAPI
from fastapi.responses import FileResponse

# --- LÓGICA ORIGINAL DO SEU RUN.PY ---

# Caminho para o template do inventário na pasta de dados
INVENTARIO_TEMPLATE_PATH = os.path.join("data", "inventario_principal.xlsx")
REPORTS_DIR = "reports" # Definindo o diretório de relatórios

def setup_initial_files():
    """Garante que as pastas e o arquivo de template existam."""
    os.makedirs("data", exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True) # Usa a constante
    
    if not os.path.exists(INVENTARIO_TEMPLATE_PATH):
        try:
            wb = Workbook()
            # Adiciona o cabeçalho inicial conforme o arquivo CSV de exemplo
            ws = wb.active
            ws.title = "Planilha1"
            ws.append(["Datas", "", "", ""]) # Linha 1 do CSV
            ws.append(["Código", "Produto", "Data", "Quantidade"]) # Linha 2
            
            wb.save(INVENTARIO_TEMPLATE_PATH)
            print(f"Arquivo '{INVENTARIO_TEMPLATE_PATH}' criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o arquivo de inventário: {e}")

# --- FIM DA LÓGICA ORIGINAL ---


# --- NOVA INTEGRAÇÃO FASTAPI + FLET ---

# 1. Configura o app Flet (com assets_dir, como no seu original)
flet_app = ft.app(target=main, assets_dir="assets")

# 2. Configura o FastAPI
fastapi_app = FastAPI(title="ColetorApp API")

@fastapi_app.get("/reports/{filename}")
async def get_report(filename: str):
    """
    Endpoint para baixar relatórios XLSX da pasta 'reports'.
    Ex: /reports/relatorio_20251020_123000.xlsx
    """
    file_path = os.path.join(REPORTS_DIR, filename)
    if not os.path.exists(file_path):
        return {"error": "Arquivo não encontrado."}
    
    return FileResponse(
        file_path, 
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=filename # Garante o nome correto no download
    )

# 3. Monta o Flet DENTRO do FastAPI
# O Flet cuidará de todas as rotas (/) exceto /reports/{filename}
fastapi_app.mount("/", flet_app)

# 4. Define o asgi_app que o Render/Uvicorn usará
# (Garante que os arquivos iniciais sejam criados antes de tudo)
setup_initial_files()
asgi_app = fastapi_app


# O bloco if __name__ == "__main__" é usado apenas para desenvolvimento local
# Em produção (Render), o `asgi_app` acima é usado.
if __name__ == "__main__":
    print("Executando em modo de desenvolvimento local...")
    # setup_initial_files() # Já chamado acima
    
    # Para rodar localmente com o FastAPI, você usaria:
    # uvicorn run:asgi_app --host 0.0.0.0 --port 8000
    
    # Para rodar localmente APENAS O FLET (sem o endpoint /reports):
    ft.app(target=main, assets_dir="assets", port=8000, view=ft.AppView.WEB_BROWSER)
