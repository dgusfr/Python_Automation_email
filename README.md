# Monitoramento de Preços com Notificação por E-mail

Este projeto é uma aplicação Python que monitora o preço de um produto em um site de e-commerce e envia uma notificação por e-mail quando o preço cai para um valor definido pelo usuário.

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="images/python.png" alt="Logo Python" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto utiliza web scraping para monitorar o preço de um produto em um site de e-commerce (Mercado Livre). Quando o preço do produto atinge ou fica abaixo de um limite predefinido, o sistema envia um e-mail de notificação ao usuário com os detalhes do produto e o preço atual.

## Funcionalidades

- Monitora o preço de um produto em intervalos regulares.
- Envia um e-mail para o usuário quando o preço cai para o valor definido.
- Permite configuração de credenciais e preço alvo via arquivo `.env`.

<div align="center">
  <img src="images/logo.gif" alt="Imagem do Projeto" width="300">
</div>

## Explicação

O sistema funciona da seguinte maneira:
1. O **web scraper** acessa a página do produto e extrai o preço atual usando a biblioteca **BeautifulSoup**.
2. O preço extraído é comparado com o preço alvo definido pelo usuário.
3. Se o preço atual é menor ou igual ao preço alvo, o sistema dispara um e-mail para o usuário utilizando o servidor SMTP do Gmail.
4. O monitoramento ocorre em intervalos regulares definidos pelo usuário.

## Autor

Desenvolvido por Diego Franco

