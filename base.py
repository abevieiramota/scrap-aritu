# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from itertools import product
from selenium.common.exceptions import TimeoutException, WebDriverException
import codecs

# TODO: tratar paginação do resultado da pesquisa
# TODO: salvar dicionário dos índices utilizados nos nomes dos arquivos
# TODO: logging

WAIT_TIME = 30
RESULT_FILE_NAME_TEMPLATE = "[%d][%d][%d][%d].html"
ITEM_FILE_NAME_TEMPLATE = "[%d][%d][%d][%d][%d].html"

# exercicio 0 -> 2015, 1 -> 2014 ...
# mes 0 -> Janeiro, 1 -> Fevereiro ...
# dia 0 -> 1, 1 -> 2 ...
# tipo_despesa 0 -> empenho, 1 -> liquidado, 2 -> pago

def wait_presence(driver, by, value):

    WebDriverWait(driver, WAIT_TIME).until(EC.presence_of_element_located((by, value)))

driver = webdriver.Chrome(executable_path=r"C:\Users\abelardomota\Downloads\chromedriver_win32\chromedriver.exe")

for exercicio_i, mes_i, dia_i, tipo_despesa_i in product(xrange(2, -1, -1), xrange(12), xrange(31), xrange(3)):

    exercicio_item_id = "ContentPlaceHolder1_ddlExercicio_DDD_L_LBI%dT0" % exercicio_i
    mes_item_id = "ContentPlaceHolder1_ddlMes_DDD_L_LBI%dT0" % mes_i
    dia_item_id = "ContentPlaceHolder1_ddlDia_DDD_L_LBI%dT0" % dia_i
    tipo_despesa_item_id = "ContentPlaceHolder1_ddlTipoDespesa_DDD_L_LBI%dT0" % tipo_despesa_i

    driver.get("http://187.11.133.15/PortaldaTransparencia/")

    # Passo 1 - tela de pesquisa -> resultado da pesquisa

    # selecionando exercício
    exercicio_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlExercicio_B-1Img")
    exercicio_drop.click()

    wait_presence(driver, By.ID, exercicio_item_id)
    exercicio = driver.find_element_by_id(exercicio_item_id)
    try:
        exercicio.click()
    except WebDriverException:

        print "Exercício de id %d não encontrado" % exercicio_i

    driver.implicitly_wait(1)

    # selecionando mês
    mes_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlMes_B-1Img")
    mes_drop.click()

    wait_presence(driver, By.ID, mes_item_id)
    mes = driver.find_element_by_id(mes_item_id)
    try:
        mes.click()
    except WebDriverException:

        print "Mes de id %d não encontrado" % mes_i

    driver.implicitly_wait(1)

    # selecionando dia
    dia_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlDia_B-1Img")
    dia_drop.click()

    wait_presence(driver, By.ID, dia_item_id)
    dia = driver.find_element_by_id(dia_item_id)
    try:
        dia.click()
    except WebDriverException:

        print "Dia de id %d não encontrado" % dia_i

    driver.implicitly_wait(1)

    # selecionando tipo de despesa
    tipo_despesa_drop = driver.find_element_by_id("ContentPlaceHolder1_ddlTipoDespesa_B-1Img")
    tipo_despesa_drop.click()

    wait_presence(driver, By.ID, tipo_despesa_item_id)
    tipo_despesa = driver.find_element_by_id(tipo_despesa_item_id)
    try:
        tipo_despesa.click()
    except WebDriverException:

        print "Tipo de despesa de id %d não encontrado" % tipo_despesa_i

    # submetendo
    pesquisar_btn = driver.find_element_by_id("ContentPlaceHolder1_btnEnviar")
    pesquisar_btn.click()

    # Passo 2 - resultado da pesquisa -> item do resultado

    try:
        wait_presence(driver, By.CLASS_NAME, "dxgv__cci")
    except TimeoutException:

        print "oi"

    finally:

        with open(RESULT_FILE_NAME_TEMPLATE % (exercicio_i, mes_i, dia_i, tipo_despesa_i), 'wb') as f:

            f.write(driver.page_source)
    if "No data to display" in driver.page_source:

        pass

    notas = driver.find_elements_by_tag_name('a')[2:]

    for i in range(len(notas)):

        notas = driver.find_elements_by_tag_name('a')[2:]

        notas[i].click()

        # report
        wait_presence(driver, By.ID, "ContentPlaceHolder1_wucRelatorioPreview_repView_ContentFrame")
        driver.switch_to_frame(driver.find_element_by_id("ContentPlaceHolder1_wucRelatorioPreview_repView_ContentFrame"))

        wait_presence(driver, By.ID, "report_div")

        with codecs.open(ITEM_FILE_NAME_TEMPLATE % (exercicio_i, mes_i, dia_i, tipo_despesa_i, i), mode='wb', encoding="iso-8859-1") as f:

            f.write(driver.page_source)

        driver.back()

driver.close()
