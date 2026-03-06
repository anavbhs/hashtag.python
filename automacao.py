# Automacao de Atendimento ao Cliente
#Este script automatiza o registro de produtos

import pyautogui
import time
#pyautogui.click-> Clica em um ponto específico da tela
#pyautogui.write-> Escreve um texto
#pyautogui.press -> Pressiona uma tecla
#pyautogui.hotkey('ctrl', 'alt', 't') Abre um atalho (ex: abrir terminal)

#Passo 1: Abrir o navegador e acessar o site
pyautogui.PAUSE = 1 # Define uma pausa de 0.5 segundos entre as ações para evitar erros
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win") # Pressiona a tecla "Windows" para abrir o menu iniciar
pyautogui.write("Chrome") # Escreve "Google Chrome" para buscar o navegador
pyautogui.press("enter") # Pressiona "Enter" para abrir o navegador
pyautogui.write(link) # Escreve o link do site
pyautogui.press("enter") # Pressiona "Enter" para acessar o site
time.sleep(3) # Aguarda 3 segundos para o site carregar

#Passo 2: Fazer login
time.sleep(1) # Aguarda 1 segundo
pyautogui.click(x=515, y=403) # Clica no campo de email
pyautogui.write("seuemail@gmail.com") # Escreve o email
pyautogui.press("tab") # Pressiona "Tab" para ir para o campo de senha
pyautogui.write("45667865424bl") # Escreve a senha

#Passo 3: Abrir a base de dados de produtos
#Passo 4: Cadastrar um novo produto
#Passo 5: Salvar as informações do produto
#Passo 6: Repetir o processo até acabar a lista de produtos

#time.sleep(5) # Aguarda 5 segundos para o usuário posicionar o mouse no local desejado para o clique
#print(pyautogui.position()) # Retorna a posição atual do mouse (x, y) para ajudar a identificar as coordenadas corretas para os cliques.