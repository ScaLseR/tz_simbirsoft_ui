from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.disk_page import DiskPage

file_name = 'Файл для копирования'
folder_name = 'Задание_2'
url = 'http://yandex.ru'
login = 'simbirsofttzskorik'
password = '123qazqwe!@#'


def test_copy_file_to_folder(browser):
    """test case"""
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorized_user(login, password)
    login_page.go_to_disk_page()
    disk_page = DiskPage(browser, browser.current_url)
    disk_page.copy_file_to_folder(file_name, folder_name)
    disk_page.open_folder_in_disk(folder_name)
    disk_page.delete_files_in_folder(file_name)
    assert disk_page.count_files_in_folder() == 1
    assert disk_page.get_file_name() == file_name
