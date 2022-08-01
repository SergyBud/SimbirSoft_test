from selenium.webdriver import Keys
from Yandex_disk_page import SearchHelper, YandexSeacrhLocators
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_the_augh_button_one()
    yandex_main_page.enter_word("sergbadurin@yandex.ru")
    yandex_main_page.click_on_the_augh_button_two()
    yandex_main_page.enter_password("Gheui2*5")
    yandex_main_page.push_keyboard(Keys.ENTER)
    yandex_main_page.click_on_the_disk_button()
    browser.implicitly_wait(10)
    browser.switch_to.window(browser.window_handles[1])
    yandex_main_page.click_on_the_create_button()
    yandex_main_page.click_on_the_create_button_folder()
    yandex_main_page.enter_folder_name("")
    yandex_main_page.click_on_the_save_button()
    time.sleep(3)
    copied_file = yandex_main_page.click_on_the_file_for_copy()
    actionChains = ActionChains(browser)
    actionChains.context_click(copied_file).perform()
    yandex_main_page.click_on_the_copy_button()
    time.sleep(3)
    yandex_main_page.click_on_the_name_of_folder()
    yandex_main_page.click_on_the_copy_button_two()
    time.sleep(3)
    double_click = yandex_main_page.double_click_on_the_folder()
    actionChains.double_click(double_click).perform()
    time.sleep(3)
    check_file = yandex_main_page.search_element(YandexSeacrhLocators.LOCATOR_YANDEX_CHECK_FILE_IN_FOLDER)
    assert check_file, "elements not found"
    check_name_of_file = yandex_main_page.check_file_contain_word()
    assert 'Файл для\nскачи…я.docx' in check_name_of_file
    yandex_main_page.click_on_the_user_button()
    yandex_main_page.click_on_the_exit_button()
    time.sleep(3)

