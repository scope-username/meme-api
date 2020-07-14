from selenium import webdriver
from pyvirtualdisplay import Display
import ast
import html

from Blueprint.v1.models.models import origin_error_response


def search(query, cursor):
    try:
        url = 'https://9gag.com/v1/search-posts?query=' + query + "&c=" + cursor
        display = Display(visible=0, size=(800, 600))
        display.start()
        browser = webdriver.Firefox()
        browser.get(url)
        html_text = (browser.find_element_by_id('json').get_attribute('innerText')).replace("\/", "/")
        new_json = ast.literal_eval(html.unescape(html_text))
        browser.quit()
        display.stop()
        return new_json
    except:
        return origin_error_response
