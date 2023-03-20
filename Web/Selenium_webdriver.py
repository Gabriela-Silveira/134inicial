# Configura
# Bibliotecas
import
# Dados de Entrada
from webdriver_manager.drivers.chrome import ChromeDriver

origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultado Esperado
titulo_passagens_esperado = 'Flights from São Paolo to New Yourk:'
mensagem_de_agradecimento_esperada = 'Thank you for your purchase today!:'
preco_passagem_esperado = '555 USD'


# Executa
class Testes:
    # Início
    def setup_method(self):
        # instanciar a biblioteca / motor / engine
        # Informar onde está o WebDriver

        self.driver = ChromeDriver('C:\\Users\\franc\\PycharmProjects\\134inicial\\venv\\chromedriver.exe')

    # Fim
    def teardown_method(self):
        # Destruir o objeto da biblioteca utilizada
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a pont
        # Página Inicial (Home)
        self.driver.get('https://www,blazedemo.com')
        lista = self.driver.find_element(By.NAME('fromPort'))
        lista.click()
        lista.find_element(By.XPATH('//option[ .= "São Paolo"]'))
        lista = self.driver.find_element(By.NAME('toPort'))
        lista.click()
        lista.find_element(By.XPATH('//option[ .= "New York"]'))

        self.driver.find_element(By.CSS_SELECTOR('input.btn

    # Página Lista de passagens

    # Pagina de Compra

    # Pagina de Obrigado
    # Executa

    # Valida
