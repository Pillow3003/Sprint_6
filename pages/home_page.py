import allure
from pages.base_page import BasePage
from utils.locators import BasePageLocator
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import YaScooterHomePageLocator as Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class YaScooterHomePage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(Locators.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(Locators.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в FAQ')
    def click_faq_question(self, question_number: int):
        elems = self.find_elements(Locators.FAQ_BUTTONS)
        try:
            elems[question_number].click()
        except IndexError:
            raise AssertionError(f"Вопрос с номером {question_number} не найден среди FAQ.")

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_index: int = 1):
        handles = self.driver.window_handles
        if window_index >= len(handles):
            raise AssertionError(f"Вкладка с индексом {window_index} не существует. Всего вкладок: {len(handles)}.")
        self.driver.switch_to.window(handles[window_index])

    def wait_url_until_not_about_blank(self, timeout: int = 10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.url_changes(self.driver.current_url))
            # Или более точно: ждать until URL не станет 'about:blank'
            wait.until(lambda driver: driver.current_url != 'about:blank')
        except TimeoutException:
            raise AssertionError("Страница всё ещё загружена как 'about:blank' после ожидания.")

    @allure.step('Перейти на страницу Яндекса')
    def click_yandex_button(self):
        return self.find_element(BasePageLocator.YANDEX_SITE_BUTTON).click()

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.find_element(BasePageLocator.COOKIE_ACCEPT_BUTTON).click()