import time
from selenium import webdriver
import selenium.common.exceptions

class Screenshotter:
  def __init__( self ):
    self.driver = webdriver.Firefox()
    self.driver.set_window_size(1920,1200)


  def get_url( self, url ):
    self.driver.get(url)
    time.sleep(2)


  def click_selector( self, selector ):
    try:
      element = self.driver.find_element_by_css_selector(selector)
      element.click()
      time.sleep(2)
      return True
    except selenium.common.exceptions.NoSuchElementException as e:
      print "** WARNING: couldn't find selector '" + selector + "' to click on page."
      return False


  def take_screenshot( self, dest_path ):
    self.driver.save_screenshot(dest_path)


  def close( self ):
    self.driver.quit()
