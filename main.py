import schedule
import time
from scraper import obter_preco
from email_sender import enviar_email
from config import URL, PRECO_ALVO

def verificar_preco():
    preco_atual = obter_preco()
    if preco_atual is not None:
        print(f"Preço atual: R$ {preco_atual:.2f}")
        if preco_atual <= PRECO_ALVO:
            enviar_email(preco_atual)
        else:
            print("O preço ainda não atingiu o valor alvo.")
    else:
        print("Não foi possível verificar o preço.")

# Agendar a verificação a cada 20 minutos
schedule.every(20).minutes.do(verificar_preco)

if __name__ == "__main__":
    print("Monitorando o preço do produto...")
    while True:
        schedule.run_pending()
        time.sleep(1)
