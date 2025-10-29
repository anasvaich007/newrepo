# Lesson 10 - Allure Reporting

## Описание проекта

Проект содержит автотесты:

1. Форма регистрации(`test_form_fields.py`)
2. Онлайн-калькулятор(`test_calculator_sum.py`)
3. Интернет-магазин(`test_checkout_total.py`)

Запустите все тесты и сохраните результаты для Allure:
pytest --alluredir=allure-results

Результаты сохраняются в папку allure-results.

Запускать нужно из корня проекта


После запуска сформировать отчет:
allure serve allure-results

Отчет:

-Все тесты и их статус (успешно / провалено)

-Шаги тестов (with allure.step)

-Названия тестов и описания (@allure.title, @allure.description)

-Разделение по функционалу (@allure.feature)

-Уровень важности теста (@allure.severity)

Для закрытия Ctrl + C
