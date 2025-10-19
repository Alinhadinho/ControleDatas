import flet as ft
from app.main import main
import os
from openpyxl import Workbook

# Caminho para o template do inventário na pasta de dados
INVENTARIO_TEMPLATE_PATH = os.path.join("data", "inventario_principal.xlsx")

def setup_initial_files():
    """Garante que as pastas e o arquivo de template existam."""
    # Estas pastas serão criadas DENTRO do contêiner
    os.makedirs("data", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    
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

if __name__ == "__main__":
    setup_initial_files()
    
    # --- MODIFICAÇÃO PARA DEPLOY ---
    # Pega a porta do ambiente (fornecida pelo Render/Docker) ou usa 8080 como padrão
    port = int(os.getenv("PORT", 8080))

    # Roda o app como um serviço WEB na porta correta
    ft.app(
        target=main, 
        assets_dir="assets",
        port=port,
        view=ft.AppView.WEB_BROWSER,
        # O host '0.0.0.0' permite conexões de fora do contêiner
        host="0.0.0.0" 
    )