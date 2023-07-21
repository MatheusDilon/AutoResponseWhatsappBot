import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Opens the browser and the WhatsApp web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
time.sleep(10)

group_name = "degrade"
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='side']/div[1]/div/div/div[2]/div/div[1]/p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")))

# Goes to the search box and enters the group name
search_box = driver.find_element("xpath", "//*[@id='side']/div[1]/div/div/div[2]/div/div[1]/p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")  # Find the search box
search_box.send_keys(group_name)
search_box.send_keys(Keys.ENTER)
time.sleep(2)  # Waits for the page to load

last_message_text = "" # Defines the last message as null

# Checking Loop
while True:
    # List of possibles answers
    lista_resposta = ["Favor permanecer calado", 
                "O RP MENO, *CALA A BOCA!!*", 
                "Mantenha o silencio", 
                "Vc calado eh um poeta",
                "Seu silencio vale mais doq 1000 palavras",
                "Cala a boca Ryan",
                "Ryaaan... Um momentinho por favor"]
    # Chooses one randomly
    resposta = random.choice(lista_resposta)
    # Find the last message element
    last_message_element = driver.find_elements(By.XPATH, "//div[@class='message-in focusable-list-item _1AOLJ _1jHIY']")
    if last_message_element:
        new_last_message_text = last_message_element[-1].text
        sender_name = driver.find_elements(By.XPATH, "//span[@class='_3FuDI ajgl1lbb edeob0r2 _11JPr']")[-1]
        if sender_name.text == "Ryan Sub12" and new_last_message_text != last_message_text:
            response_box = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[1]/div[1]/p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
            response_box.send_keys(resposta)
            response_box.send_keys(Keys.ENTER)
            last_message_text = new_last_message_text
    
    # Cheking delay
    time.sleep(0.5)
