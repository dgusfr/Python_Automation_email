import sys
import os

# Adicionar o diretório pai ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from email_sender import enviar_email

if __name__ == "__main__":
    print("Enviando e-mail de teste...")
    enviar_email(3200.00)
