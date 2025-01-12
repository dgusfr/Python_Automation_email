from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configurações do e-mail
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA = os.getenv("SENHA")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")

# Configurações do produto
URL = "https://www.mercadolivre.com.br/sony-console-playstation-5-digital-slim-branco-1tb-returnal-e-ratchet-e-clank-controle-sem-fio-dualsense-branco/p/MLB37494438"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
PRECO_ALVO = 3200.00
