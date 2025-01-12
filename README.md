# Projeto: Monitoramento de Preços com Envio de E-mails

Este projeto monitora o preço de um produto no Mercado Livre e envia e-mails automaticamente quando o preço atinge um valor alvo.

## Estrutura
- `main.py`: Ponto de entrada do projeto.
- `scraper.py`: Lógica para buscar o preço do produto.
- `email_sender.py`: Lógica para envio de e-mails.
- `config.py`: Configurações gerais do projeto.
- `tests/test_email.py`: Teste do envio de e-mails.
- `requirements.txt`: Dependências do projeto.

## Configuração
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
