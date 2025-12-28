import pytest
import allure
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ
from utils.locators import YaScooterHomePageLocator


@allure.epic('Эпик_Upgrade Main page / ui usability')
@allure.parent_suite('Parent_suite_Домашняя страница')
@allure.suite('Suite_FAQ')
class TestYaScooterFAQPage:
    @allure.feature('Фича_Аккордион с вопрос/ответ на Домашней странице')
    @allure.story('При нажатии на вопрос в разделе "Вопросы о важном" раскрывается ответ.')
    @allure.title('При нажатии на вопрос раскрывается ответ')
    @allure.description(
        'Проверка, что при нажатии на поле вопроса в блоке "Вопросы о важном", '
        'данный вопрос раскрывается и текст ответа соответствует ТЗ'
    )
    @pytest.mark.parametrize(
        "question_index, answer_index, expected_answer_text",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_question_shows_answer(
        self, driver, question_index, answer_index, expected_answer_text
    ):
        ya_scooter_home_page = YaScooterHomePage(driver)
        ya_scooter_home_page.go_to_site()
        ya_scooter_home_page.click_cookie_accept()
        ya_scooter_home_page.click_faq_question(question_number=question_index)
        answer_element = ya_scooter_home_page.find_element(
            YaScooterHomePageLocator.FAQ_ANSWER(answer_number=answer_index)
        )

        assert answer_element.is_displayed(), f"Ответ для вопроса {question_index} не отображается"
        actual_text = answer_element.text
        assert actual_text == expected_answer_text, (
            f"Текст ответа для вопроса {question_index} не совпадает. "
            f"Ожидаемый: '{expected_answer_text}', полученный: '{actual_text}'"
        )