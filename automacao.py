# Automacao de Atendimento ao Cliente
# Este script automatiza o registro de produtos

import pyautogui
pyautogui.press("win") # Pressiona a tecla "Windows" para abrir o menu iniciar
pyautogui.hotkey("ctrl", "alt", "t")

print("Hello World")
#pyautogui.click-> Clica em um ponto específico da tela
#pyautogui.write-> Escreve um texto
#pyautogui.press -> Pressiona uma tecla
#pyautogui.hotkey('ctrl', 'alt', 't') Abre um atalho (ex: abrir terminal)

#Passo 1: Entrar no sistema da empresa
#Passo 2: Abrir o navegador e acessar o site 
#Passo 3: Fazer login
#Passo 4: Abrir a base de dados de produtos
#Passo 5: Cadastrar um novo produto
#Passo 6: Salvar as informações do produto
#Passo 7: Repetir o processo até acabar a lista de produtos