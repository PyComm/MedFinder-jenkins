from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Configuración inicial
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Test Case: Open MedicInfo
driver.get("https://6943-186-78-252-47.ngrok-free.app/")
driver.maximize_window()

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Revisa Aquí')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Información')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Credencial')]")))

# Capturar captura de pantalla
driver.save_screenshot("screenshot.png")

time.sleep(5)

# Cerrar el navegador
driver.quit()
