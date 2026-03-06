# Automacao de Atendimento ao Cliente
#Este script automatiza o registro de produtos

import time
import pyautogui
import pandas
#pyautogui.click-> Clica em um ponto específico da tela
#pyautogui.write-> Escreve um texto
#pyautogui.press -> Pressiona uma tecla
#pyautogui.hotkey('ctrl', 'alt', 't') Abre um atalho (ex: abrir terminal)
#Passo 1: Abrir o navegador e acessar o site
pyautogui.PAUSE = 1 # Define uma pausa de 0.5 segundos entre as ações para evitar erros
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win") # Pressiona a tecla "Windows" para abrir o menu iniciar
time.sleep(1) # Aguarda 1 segundo para o menu iniciar abrir
pyautogui.write("Chrome") # Escreve "Google Chrome" para buscar o navegador
time.sleep(1) # Aguarda 1 segundo para o resultado da busca aparecer
pyautogui.press("enter") # Pressiona "Enter" para abrir o navegador
pyautogui.write(link) # Escreve o link do site
pyautogui.press("enter") # Pressiona para acessar o site
time.sleep(3) # Aguarda 3 segundos para Troca de fornecedor 

#Passo 2: Fazer login
time.sleep(2) # Aguarda 2 segundos para garantir que o campo de email esteja visível
pyautogui.click(x=515, y=403) # Clica no campo de email
pyautogui.write("seuemail@gmail.com") # Escrever o email
pyautogui.press("tab") # Pressiona "Tab" para ir para o campo de senha
pyautogui.write("45667865424bl") # Escreve a senha
pyautogui.press("tab") # Pressiona "Tab" para ir para o botão de login
pyautogui.press("enter") # Pressiona "Enter" para fazer login

#Passo 3: Abrir a base de dados de produtos + pandas library
tabela = pandas.read_csv("produtos.csv") # Lê a base de dados de produtos a partir de um arquivo CSV
#print(tabela) # Exibe a tabela de produtos para verificar se foi carregada

for linha in tabela.index: # Itera sobre cada linha da tabela de produtos
#Passo 4: Cadastrar um novo produto
    #código:    
    pyautogui.click(x=623, y=289) # Clica no botão "Cadastrar Novo Produto" (exemplo de coordenadas)
    codigo = str(tabela.loc[linha, "codigo"]) # Obtém o código do produto da tabela
    pyautogui.write(codigo) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #marca:
    marca = str(tabela.loc[linha, "marca"]) # Obtém a marca do produto da tabela
    pyautogui.write(marca) # Escreve a marca do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #tipo:
    tipo = str(tabela.loc[linha, "tipo"]) # Obtém o tipo do produto da tabela
    pyautogui.write(tipo) # Escreve o tipo do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #categoria:
    categoria = str(tabela.loc[linha, "categoria"]) # Obtém a categoria do produto da tabela
    pyautogui.write(categoria) # Escreve a categoria do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #preco_unitario:
    preco_unitario = str(tabela.loc[linha, "preco_unitario"]) # Obtém o preço do produto da tabela
    pyautogui.write(preco_unitario) # Escreve o preço do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #custo:
    custo = str(tabela.loc[linha, "custo"]) # Obtém o custo do produto da tabela
    pyautogui.write(custo) # Escreve o custo do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o próximo campo
    #obs:   
    obs = str(tabela.loc[linha, "obs"]) # Obtém as observações do produto da tabela
if obs != "nan": # <--- Só escreve se NÃO for vazio
    pyautogui.write(obs)
    pyautogui.write(obs) # Escreve as observações do produto

#Passo 5: Salvar as informações do produto
    pyautogui.press("tab") # Pressiona "Tab" para ir para o botão de salvar
    pyautogui.press("enter") # Pressiona "Enter" para salvar o produto

#Passo 6: Scrool para o próximo produto seja cadastrado no topo da página
    pyautogui.scroll(5000) # Rola a página para cima

#Passo 6: Repetir o processo para o próximo produto
# so até acabar a lista de produtos

#time.sleep(5) # Aguarda 5 segundos para o usuário posicionar o mouse no local desejado para o clique
#print(pyautogui.position()) # Retorna a posição atual do mouse (x, y) para ajudar a identificar as coordenadas corretas para os cliques.
