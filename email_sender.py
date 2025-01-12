import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_REMETENTE, SENHA, EMAIL_DESTINATARIO, URL

def enviar_email(preco):
    assunto = "Produto Abaixou de Preço!"
    corpo = f"""
    Olá Diego,

    O produto X abaixou de preço para R$ {preco:.2f}. Não perca tempo e compre ele!

    Link do produto: {URL}
    """
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_REMETENTE, SENHA)
            servidor.send_message(mensagem)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")
