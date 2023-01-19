from selenium import webdriver
import time
import data
import unittest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
driver.maximize_window()


       
driver = webdriver.Chrome()
driver.maximize_window 


class TestQa(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window 
    def test_create_text_data(self): 
        driver.maximize_window 
        browser = self.browser
        browser.get("https://demoqa.com/text-box") # buka situs
        browser.find_element(By.ID,"userName").send_keys("SectumSempra")
        time.sleep(2)
        browser.find_element(By.ID,"userEmail").send_keys("testing@test.com") 
        time.sleep(2)
        browser.find_element(By.ID,"currentAddress").send_keys("Cikarang") 
        time.sleep(2)
        browser.find_element(By.ID,"permanentAddress").send_keys("Pilar") 
        time.sleep(2)
        # browser.find_element(By.XPATH,"//*[@id='submit']").click()
        # time.sleep(2)
        checkName = browser.find_element(By.ID,"userName").text
        print(checkName)
      

    def test_check_box(self): 
        driver.maximize_window
        browser = self.browser 
        browser.get("https://demoqa.com/checkbox") # buka situs
        browser.find_element(By.XPATH,"//*[@id='tree-node']/ol/li/span/label/span[1]").click()
        time.sleep(5)
        check = browser.find_element(By.ID,"result").text
        print(check)

    def test_radio_button(self): 
        driver.maximize_window
        browser = self.browser 
        browser.get("https://demoqa.com/radio-button") # buka situs
        browser.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/div[3]/label").click()
        time.sleep(5)
        check = browser.find_element(By.XPATH,"//*[@id='app']/div/div/div[2]/div[2]/div[2]/p").text
        print(check)

       

        # dibawah ini untuk input form 
       
        
       
       
        
        #

if __name__ == "__main__": 
    unittest.main()          
          


    
       
       
        










