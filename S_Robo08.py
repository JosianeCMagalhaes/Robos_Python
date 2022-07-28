from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time as t

navegador = Chrome()
navegador.get("https://gru.inpi.gov.br/pePI/servlet/LoginController?action=login")
navegador.maximize_window()
t.sleep(1)
avancar = navegador.find_element_by_id("details-button")
avancar.click()
t.sleep(1)
navegador.find_element_by_id("proceed-link").click()
t.sleep(3)
navegador.find_element_by_xpath("//map/area[2]").click()
t.sleep(3)
navegador.find_element_by_name("ExpressaoPesquisa").send_keys("03768202000176")
t.sleep(0.5)
navegador.find_element_by_xpath("//select[2]/option[4]").click()
t.sleep(1)
navegador.find_element_by_css_selector('input[type="submit"]').click()
navegador.quit()
