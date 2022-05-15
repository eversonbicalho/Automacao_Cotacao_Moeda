#Automação de um programa para BUSCAR A COTAÇÃO: DOLAR E EURO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime


#___________________________________________________________________________
#Configurando data e hora de Hoje
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")



#___________________________________________________________________________
#Colocar dentro do parenteses o "caminho" do executavel "chromedriver.exe"
driver = webdriver.Chrome(executable_path=r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.2.3\bin\chromedriver.exe")

#Maximiza tela
driver.maximize_window()


#Pesquisa pela cotação da moeda desejada
#______________________________________________DOLAR___________________________________________________________________________
#DOLAR
driver.get("https://www.google.com.br/")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

#Seleciona valor e imprime
cotação_do_dolar = driver.find_element(By.XPATH,
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/'
                                       'span[1]').get_attribute('data-value')

#DEFINIR FLOAT PARA FORMATAR NUMEROS
cotação_do_dolar = float(cotação_do_dolar)

print('')
print('__________________________________________________________________________________________')
print('A cotação do DOLAR para hoje,',data_e_hora_em_texto,'hrs','é de', round(cotação_do_dolar,2),".")



#______________________________________________EURO___________________________________________________________________________
#EURO
driver.get("https://www.google.com.br/")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Seleciona valor e imprime
cotação_do_euro = driver.find_element(By.XPATH,
                                       '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/'
                                       'span[1]').get_attribute('data-value')

#DEFINIR FLOAT PARA FORMATAR NUMEROS
cotação_do_euro = float(cotação_do_euro)

print('')
#print('__________________________________________________________________________________________')
print('A cotação do EURO para hoje,',data_e_hora_em_texto,'hrs','é de:', round(cotação_do_euro,2),".")



driver.close()


