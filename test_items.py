
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find__card_btn(browser):
    browser.get(link)
#    time.sleep(30)
    but = browser.find_element_by_class_name('btn-add-to-basket')
    assert but.is_displayed(), "Button: Add to basket not displayed"    
