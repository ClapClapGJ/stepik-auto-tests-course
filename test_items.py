
class TestLang:
    def test_button_for_item_add(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(10)
        button = len(browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"))
        assert button > 0, '!!!НЕ НАШЕЛ!!!'
