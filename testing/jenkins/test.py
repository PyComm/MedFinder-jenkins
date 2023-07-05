from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Configuración inicial
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

try:
    # Test Case: Open MedicInfo
    driver.get("https://6943-186-78-252-47.ngrok-free.app/")
    driver.maximize_window()
    
    # Esperar a que el enlace "Revisa Aquí" sea clicable
    visit_site_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Visit Site')]")))
    visit_site_link.click()

    # Esperar a que el enlace "Revisa Aquí" sea clicable
    revisa_aqui_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Revisa Aquí')]")))
    revisa_aqui_link.click()

    # Esperar a que el enlace "Información" sea clicable
    informacion_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Información')]")))
    informacion_link.click()

    # Esperar a que el párrafo con texto "Credencial" esté presente en la página
    credencial_paragraph = wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Credencial')]")))

    # Capturar captura de pantalla
    driver.save_screenshot("screenshot.png")

    time.sleep(5)

finally:
    # Cerrar el navegador incluso si se produce una excepción
    driver.quit()
