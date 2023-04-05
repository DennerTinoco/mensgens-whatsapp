import time
import random
import pandas as pd
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Definir os horários em que as mensagens podem ser enviadas
HORA_INICIAL = 8
HORA_FINAL = 18

# Ler a planilha
df = pd.read_excel('./Lista de ennvio - teste.xlsx')

# Obter a lista de links e mensagens
links = df['link'].tolist()
mensagens = df['mensagem'].tolist()

# Inicializar o navegador
driver = webdriver.Chrome('caminho_para_o_driver_do_chrome.exe')
driver.get('https://web.whatsapp.com/')

# Esperar até que o usuário faça login
input('Faça login no WhatsApp Web e pressione Enter')

# Loop pelos contatos e enviar as mensagens
for link, mensagem in zip(links, mensagens):

  # Verificar se é dia útil e hora válida para enviar a mensagem
  agora = datetime.now()
  if agora.weekday() < 5 and HORA_INICIAL <= agora.hour < HORA_FINAL:

    # Abrir o link e enviar a mensagem
    driver.get(link)
    time.sleep(5)
    caixa_de_mensagem = driver.find_element_by_xpath(
      '//div[@contenteditable="true"][@data-tab="1"]')
    caixa_de_mensagem.send_keys(mensagem)
    caixa_de_mensagem.send_keys(Keys.ENTER)

    # Gerar um intervalo de tempo aleatório entre 30 segundos e 10 minutos
    tempo_aleatorio = random.randint(30, 600)

    # Esperar o tempo aleatório antes de enviar a próxima mensagem
    time.sleep(tempo_aleatorio)

# Fechar o navegador
driver.quit()
