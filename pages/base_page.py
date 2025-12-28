import allure
from utils.urls import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс страницы, предоставляющий основные методы для взаимодействия с веб-страницей.
    """
    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: экземпляр Selenium WebDriver для взаимодействия с браузером.
        """
        self.driver = driver

    def find_element(self, locator, time=10):
        """
        Ожидает появления элемента по локатору и возвращает его.

        :param locator: кортеж в формате (By, locator), например (By.ID, "id элемента").
        :param time: время ожидания в секундах.
        :return: веб-элемент, найденный по локатору.
        :raises TimeoutException: если элемент не найден за указанное время.
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Ожидает появления всех элементов по локатору и возвращает список элементов.

        :param locator: кортеж в формате (By, locator).
        :param time: время ожидания в секундах.
        :return: список веб-элементов, найденных по локатору.
        :raises TimeoutException: если элементы не найдены за указанное время.
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        """
        Открывает страницу по указанному или предопределенному URL.

        :param url: URL страницы. Если None, откроется страница по умолчанию (Urls.MAIN_PAGE).
        """
        if url is None:
            url = Urls.MAIN_PAGE
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        """
        Получает текущий URL страницы.
        """
        return self.driver.current_url