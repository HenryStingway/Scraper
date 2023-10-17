from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()

# Öffnen Sie die Webseite mit dem iFrame
driver.get('https://www.palmaairport.info/de/fluge/flug-ankunfte/')

# Wechseln Sie zum iFrame
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)

# Jetzt können Sie den Inhalt des iFrames parsen, z.B. mit Beautiful Soup
# Verwenden Sie driver.page_source, um den HTML-Inhalt des iFrames abzurufen
iframe_content = driver.page_source
print(iframe_content)
# Verarbeiten Sie iframe_content mit Beautiful Soup
# Führen Sie die gewünschten Operationen aus
soup = BeautifulSoup(iframe_content, 'lxml')
#html_text = requests.get('https://www.palmaairport.info/de/fluge/flug-ankunfte/').text
#soup = BeautifulSoup(html_text, 'lxml')
#jobs = soup.find('div', class_ = 'avionio-widget')
#print(jobs)