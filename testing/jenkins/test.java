import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class MedicInfoTest {
    public static void main(String[] args) {
        // Configurar la ubicación del controlador de Chrome
        System.setProperty("webdriver.chrome.driver", "/ruta/al/controlador/chromedriver");

        // Opciones adicionales para Chrome
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--start-maximized");

        // Inicializar el navegador Chrome
        WebDriver driver = new ChromeDriver(options);

        // Abrir la URL en el navegador
        driver.get("http://localhost:5173/");

        // Esperar hasta que aparezca el elemento "Revisa Aquí"
        WebDriverWait wait = new WebDriverWait(driver, 10);
        WebElement revisaAquiLink = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[contains(text(),'Revisa Aquí')]")));

        // Hacer clic en el elemento "Revisa Aquí"
        revisaAquiLink.click();

        // Esperar hasta que aparezca el elemento "Información"
        WebElement informacionLink = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//a[contains(text(), 'Información')]")));

        // Hacer clic en el elemento "Información"
        informacionLink.click();

        // Esperar hasta que aparezca el elemento "Credencial"
        WebElement credencialElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath("//p[contains(text(), 'Credencial')]")));

        // Capturar una captura de pantalla de la página
        driver.getScreenshotAs(OutputType.FILE);

        // Esperar 5 segundos
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Cerrar el navegador
        driver.quit();
    }
}
