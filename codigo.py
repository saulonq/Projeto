import pyautogui
import time
pyautogui.PAUSE = 1

#Start
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=934, y=110)
# Login Site 
time.sleep(0.5)

pyautogui.click(x=742, y=357)
pyautogui.write("saulo.ie")
pyautogui.press("tab")
pyautogui.write("pythonbot")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.click(x=766, y=244)

#Put data
import pandas   

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    
    pyautogui.click(x=766, y=244)
    
    #code
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #brand

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #type

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #category

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #Unity Price

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #Coast product

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write("obs")
    pyautogui.press("tab")

    #Send

    pyautogui.press("enter")

    #Begin
    pyautogui.scroll(5000)
    pyautogui.click(x=775, y=243)