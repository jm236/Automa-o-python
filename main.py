# Passo a passo do projeto
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# pip install pyautogui

import pyautogui # biblioteca que realiza comandos do teclado, como apertar uma tecla ou clicar com o mouse
import time
# clicar: pyautogui.click
# escrever: pyautogui.write
# apertar uma tecla: pyautogui.press
# rolar: pyautogui.scroll(numero positivo para rolar pra cima, negativo para ir pra baixo)

pyautogui.PAUSE = 0.5

# 1 - Entrar no sistema da empresa
# comandos para abrir o navegador e entra no sistema
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(1)

# 2 - Fazer login
pyautogui.click(x=468, y=407)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(10)
print(pyautogui.position())
# 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# 4 - Cadastrar os produtos

for linha in tabela.index:

    pyautogui.click(x=539, y=289)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = tabela.loc[linha, "obs"] 
    if not pandas.isna(obs):
        pyautogui.write(obs)
        pyautogui.press("tab")

    pyautogui.press("enter")
    #       5.0pyautogui.click(x=1808, y=980)
    pyautogui.scroll(5000)
