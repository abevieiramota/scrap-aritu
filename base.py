# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\abelardomota\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://187.11.133.15/PortaldaTransparencia/")
# selecionando exercício
exercicio_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlExercicio_B-1Img")
exercicio_drop.click()

exercicio_2014 = driver.find_element_by_id("ContentPlaceHolder1_ddlExercicio_DDD_L_LBI1T0")
exercicio_2014.click()

# selecionando mês
mes_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlMes_B-1Img")
mes_drop.click()

mes_janeiro = driver.find_element_by_id("ContentPlaceHolder1_ddlMes_DDD_L_LBI0T0")
mes_janeiro.click()

# selecionando dia
dia_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlDia_B-1Img")
dia_drop.click()

dia_20 = driver.find_element_by_id("ContentPlaceHolder1_ddlDia_DDD_L_LBI19T0")
dia_20.click()

# selecionando tipo de despesa
tipo_despesa_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlTipoDespesa_B-1Img")
tipo_despesa_drop.click()

tipo_despesa_empenhado = driver.find_element_by_id("ContentPlaceHolder1_ddlTipoDespesa_DDD_L_LBI0T0")
tipo_despesa_empenhado.click()

# submetendo
pesquisar_btn = driver.find_element_by_id("ContentPlaceHolder1_btnEnviar")
pesquisar_btn.click()

raw_input()
driver.close()
