from common import waitPresent, BaseTest, driver_init
import time



class TestSuit(BaseTest):

    # XPath для элементов
    field_A = "//*[contains(text(), 'Сторона А')]/..//input[@type = 'text']"
    field_B = "//*[contains(text(), 'Сторона Б')]/..//input[@type = 'text']"
    field_C = "//*[contains(text(), 'Сторона В')]/..//input[@type = 'text']"
    button_ok = "//*[@type = 'button'][text()='OK']"
    result_isosceles = "//*[@class = 'answerLabel'][text()='Равнобедренный']"
    result_rectangular = "//*[@class = 'answerLabel'][text()='Прямоугольный']"
    result_equilateral = "//*[@class = 'answerLabel'][text()='Равносторонний']"
    result_text = "//*[@class = 'parameterLabel'][contains(text(),'Результат')]"
    result_not_triangle = "//*[@class = 'answerLabel'][text()='Не треугольник']"
    empty_field_error = "(//*[@class = 'validationError']//*[text()='Поле не должно быть пустым'])[{}]"
    bad_input_text = """//*[@class = 'validationError']//*[text()="'{}'не является допустимым числом"]"""

    def test_if_page_exists(self):

        # Существует ли страница с элементами
        self.driver.get('https://team.cft.ru/triangle/zadanie/triangle.html?token=45eaca3781834a1eb18691309e45a3f7')
        page = waitPresent(self.driver, "//*[@class = 'panel panel-primary']")
        assert page == True, ('Невозможно открыть страницу или на странице нет элементов')

    def test_input_fields(self):

        # Существуют ли поля для ввода c названиями
        input_A = waitPresent(self.driver, self.field_A)
        assert input_A == True, ('Поля для ввода стороны А не существует')

        input_B = waitPresent(self.driver, self.field_B)
        assert input_B == True, ('Поля для ввода стороны Б не существует')

        input_C = waitPresent(self.driver, self.field_C)
        assert input_C == True, ('Поля для ввода стороны В не существует')

    def test_isosceles_triangle(self):

        # Проверяем равнобедренный треугольник, вводим данные
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()
        input_A.send_keys('5')

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()
        input_B.send_keys('5')

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()
        input_C.send_keys('8')

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем надпись результат
        result_text = waitPresent(self.driver, self.result_text)
        assert result_text == True, ("Надписи 'Результат' нет или написана с ошибками")

        # Проверяем надпись 'Равнобедренный'
        answer = waitPresent(self.driver, self.result_isosceles)
        assert answer == True, ("Не найдена запись о результате расчета или надпись не 'Равнобедренный'")

    def test_rectangular_triangle(self):
        # Проверяем прямоугольный треугольник, вводим данные
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()
        input_A.send_keys('3')

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()
        input_B.send_keys('4')

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()
        input_C.send_keys('5')

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем надпись результат
        result_text = waitPresent(self.driver, self.result_text)
        assert result_text == True, ("Надписи 'Результат' нет или написана с ошибками")

        # Проверяем надпись 'Прямоугольный'
        answer = waitPresent(self.driver, self.result_rectangular)
        assert answer == True, ("Не найдена запись о результате расчета или надпись не 'Прямоугольный'")

    def test_equilateral_triangle(self):

        # Проверяем равносторонний треугольник, вводим данные
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()
        input_A.send_keys('5')

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()
        input_B.send_keys('5')

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()
        input_C.send_keys('5')

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем надпись результат
        result_text = waitPresent(self.driver, self.result_text)
        assert result_text == True, ("Надписи 'Результат' нет или написана с ошибками")

        # Проверяем надпись 'Равносторонний'
        answer = waitPresent(self.driver, self.result_equilateral)
        assert answer == True, ("Не найдена запись о результате расчета или надпись не 'Равносторонний'")

    def test_not_triangle(self):

        # Проверяем не треугольник, вводим данные
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()
        input_A.send_keys('123')

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()
        input_B.send_keys('54')

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()
        input_C.send_keys('5')

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем надпись результат
        result_text = waitPresent(self.driver, self.result_text)
        assert result_text == True, ("Надписи 'Результат' нет или написана с ошибками")

        # Проверяем надпись 'Не треугольник'
        answer = waitPresent(self.driver, self.result_not_triangle)
        assert answer == True, ("Не найдена запись о результате расчета или надпись не 'Не треугольник'")

    def test_empty_input(self):

        # Проверяем пустые поля ввода
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем 3 надписи Поле не должно быть пустым
        for i in range (1, 4):
            result_text = waitPresent(self.driver, self.empty_field_error.format(i))
            assert result_text == True, ("Надписи 'Поле должно быть пустым нет в {} строчке' ".format(i))

    def test_bad_input(self):

        # Проверяем валидацию полей
        input_A = self.driver.find_element_by_xpath(self.field_A)
        input_A.clear()
        input_A.send_keys('234=')

        input_B = self.driver.find_element_by_xpath(self.field_B)
        input_B.clear()
        input_B.send_keys('7sd')

        input_C = self.driver.find_element_by_xpath(self.field_C)
        input_C.clear()
        input_C.send_keys('12*')

        # Проверяем кнопку 'ОК', нажимаем
        button_ok = waitPresent(self.driver, self.button_ok)
        assert button_ok == True, ("Кнопки 'ОК' нет")
        self.driver.find_element_by_xpath(self.button_ok).click()

        # Проверяем надписи о недопустимом числе
        bad_input_first = waitPresent(self.driver, self.bad_input_text.format('234='))
        assert bad_input_first == True, ("Надписи: '{}'не является допустимым числом, нет ".format('234='))

        bad_input_second = waitPresent(self.driver, self.bad_input_text.format('7sd'))
        assert bad_input_second == True, ("Надписи: '{}'не является допустимым числом, нет ".format('7sd'))

        bad_input_third = waitPresent(self.driver, self.bad_input_text.format('12*'))
        assert bad_input_third == True, ("Надписи: '{}'не является допустимым числом, нет ".format('12*'))