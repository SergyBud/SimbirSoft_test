from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from Seleniumbase import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class YandexSeacrhLocators:


    LOCATOR_YANDEX_AUGH_BUTTON = (By.CSS_SELECTOR, '[class="home-link desk-notif-card__login-new-item desk-notif-card__'
                                                   'login-new-item_enter home-link_black_yes home-link_hover_inherit"]')
    LOCATOR_YANDEX_AUGH_FIELD = (By.ID, 'passp-field-login')
    LOCATOR_YANDEX_AUGH_BUTTON_TWO = (By.ID, 'passp:sign-in')
    LOCATOR_YANDEX_PASS_FIELD = (By.ID, 'passp-field-passwd')
    LOCATOR_YANDEX_AUGH_BUTTON_PASS_THREE = (By.CSS_SELECTOR, '[class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit"]')
    LOCATOR_YANDEX_DISK_BUTTON = (By.CSS_SELECTOR, '[class ="home-link home-link_black_yes"]')
    LOCATOR_YANDEX_FILE_FOR_COPY = (By.CSS_SELECTOR, '[title="Файл для скачивания.docx"]')
    LOCATOR_YANDEX_CREATE_BUTTON = (By.CSS_SELECTOR, '[class="Button2 Button2_view_raised Button2_size_m Button2_width_max"]')
    LOCATOR_YANDEX_CREATE_BUTTON_FOLDER = (By.CSS_SELECTOR, '[aria-label="Папку"]')
    LOCATOR_YANDEX_ENTER_FOLDER_NAME = (By.CSS_SELECTOR, 'input[value="Новая папка"]')
    LOCATOR_YANDEX_SAVE_BUTTON = (By.CSS_SELECTOR, '[class="Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit "]')
    LOCATOR_YANDEX_COPY_BUTTON = (By.CSS_SELECTOR, '[class="Menu-Item Menu-Item_type_menuitem resources-actions-popup__action resources-actions-popup__action_type_copy"]')
    LOCATOR_YANDEX_CLICK_ON_THE_NAME_OF_FOLDER = (By.CSS_SELECTOR, '[title="Новая папка"]')
    LOCATOR_YANDEX_COPY_BUTTON_TWO = (By.CSS_SELECTOR, '[class="Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit "]')
    LOCATOR_YANDEX_DOUBLE_CLICK_ON_THE_FOLDER = (By.CSS_SELECTOR, '[aria-label="Новая папка"]')
    LOCATOR_YANDEX_CHECK_FILE_IN_FOLDER = (By.CSS_SELECTOR, '[aria-label="Файл для скачивания.docx"]')
    LOCATOR_YANDEX_CHECK_FILE_HAVE_NAME = (By.CSS_SELECTOR, '[title="Файл для скачивания.docx"]')
    LOCATOR_YANDEX_USER_BUTTON = (By.CSS_SELECTOR, '[class="PSHeader-User PSHeader-User_noUserName"]')
    LOCATOR_YANDEX_EXIT_BUTTON = (By.CSS_SELECTOR, '[class ="menu__item menu__item_type_link legouser__menu-item legouser__menu-item_action_exit"]')


class SearchHelper(BasePage):

    def search_element(self, selector):
        element = self.find_elements(selector)
        return element

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_AUGH_FIELD)
        search_field.click()
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def enter_password(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PASS_FIELD)
        search_field.click()
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def enter_folder_name(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_ENTER_FOLDER_NAME)
        search_field.click()
        search_field.clear()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=10).click()

    def check_file_contain_word(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_CHECK_FILE_HAVE_NAME, time=10)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def push_keyboard(self, button):
        self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PASS_FIELD).send_keys(button)

    def search_href(self, selector):
        return self.find_elements(selector)

    def click_on_the_pictures_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_LINK, time=10).click()

    def click_on_the_augh_button_one(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_AUGH_BUTTON, time=10).click()

    def click_on_the_augh_button_two(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_AUGH_BUTTON_TWO, time=10).click()

    def click_on_the_augh_button_pass_three(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_AUGH_BUTTON_PASS_THREE, time=10).click()

    def click_on_the_disk_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_DISK_BUTTON, time=10).click()

    def click_on_the_file_for_copy(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_FILE_FOR_COPY, time=10)

    def click_on_the_create_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_CREATE_BUTTON, time=10).click()

    def click_on_the_create_button_folder(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_CREATE_BUTTON_FOLDER, time=10).click()

    def click_on_the_save_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SAVE_BUTTON, time=10).click()

    def click_on_the_copy_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_COPY_BUTTON, time=10).click()

    def click_on_the_name_of_folder(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_CLICK_ON_THE_NAME_OF_FOLDER, time=10).click()

    def click_on_the_copy_button_two(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_COPY_BUTTON_TWO, time=10).click()

    def double_click_on_the_folder(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_DOUBLE_CLICK_ON_THE_FOLDER, time=10)

    def click_on_the_user_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_USER_BUTTON, time=10).click()

    def click_on_the_exit_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_EXIT_BUTTON, time=10).click()