# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

WAIT_TIME = 30

def wait_presence(driver, by, value):

    WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((by, value)))


driver = webdriver.Chrome(executable_path=r"C:\Users\abelardomota\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://187.11.133.15/PortaldaTransparencia/")

# Passo 1 - tela de pesquisa -> resultado da pesquisa

# selecionando exercício
exercicio_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlExercicio_B-1Img")
exercicio_drop.click()

wait_presence(driver, By.ID, "ContentPlaceHolder1_ddlExercicio_DDD_L_LBI1T0")
exercicio_2014 = driver.find_element_by_id("ContentPlaceHolder1_ddlExercicio_DDD_L_LBI1T0")
exercicio_2014.click()

# selecionando mês
mes_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlMes_B-1Img")
mes_drop.click()

wait_presence(driver, By.ID, "ContentPlaceHolder1_ddlMes_DDD_L_LBI0T0")
mes_janeiro = driver.find_element_by_id("ContentPlaceHolder1_ddlMes_DDD_L_LBI0T0")
mes_janeiro.click()

# selecionando dia
dia_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlDia_B-1Img")
dia_drop.click()

wait_presence(driver, By.ID, "ContentPlaceHolder1_ddlDia_DDD_L_LBI19T0")
dia_20 = driver.find_element_by_id("ContentPlaceHolder1_ddlDia_DDD_L_LBI19T0")
dia_20.click()

# selecionando tipo de despesa
tipo_despesa_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlTipoDespesa_B-1Img")
tipo_despesa_drop.click()

wait_presence(driver, By.ID, "ContentPlaceHolder1_ddlTipoDespesa_DDD_L_LBI0T0")
tipo_despesa_empenhado = driver.find_element_by_id("ContentPlaceHolder1_ddlTipoDespesa_DDD_L_LBI0T0")
tipo_despesa_empenhado.click()

# submetendo
pesquisar_btn = driver.find_element_by_id("ContentPlaceHolder1_btnEnviar")
pesquisar_btn.click()

# Passo 2 - resultado da pesquisa -> item do resultado

driver.implicitly_wait(2)
wait_presence(driver, By.CLASS_NAME, "dxgv__cci")

notas = driver.find_elements_by_tag_name('a')[2:]

for i in range(len(notas)):

    notas = driver.find_elements_by_tag_name('a')[2:]

    notas[i].click()

    # report
    wait_presence(driver, By.ID, "ContentPlaceHolder1_wucRelatorioPreview_repView_ContentFrame")
    driver.switch_to_frame(driver.find_element_by_id("ContentPlaceHolder1_wucRelatorioPreview_repView_ContentFrame"))

    wait_presence(driver, By.ID, "report_div")

    content = driver.page_source

    with open('page%d.html' % i, 'wb') as f:

        f.write(content)

    driver.back()

driver.close()
