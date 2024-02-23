from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook

from formatter import format_file

MAX_WAIT_TIME = 10

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

wb = Workbook()
ws = wb.active

ws.append(['Name', 'Tagline', 'Technology', 'Topics', 'Ideas List', 'GSoC Link', 'Comments'])

print('Loading.', end='')
with open('links.txt', 'r') as links:
    for link in links:
        driver.get(link)
        
        WebDriverWait(driver, MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization'))
        )

        name = driver.find_element(By.CSS_SELECTOR,             'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization > app-org-page-title > app-feature-banner > section > div > div > app-feature-cta > div > div:nth-child(1) > div:nth-child(1) > h2 > span').text
        tagline = driver.find_element(By.CSS_SELECTOR,          'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization > app-org-page-title > app-feature-banner > section > div > div > app-feature-cta > div > div:nth-child(1) > div:nth-child(3) > p').text
        technologies = driver.find_element(By.CSS_SELECTOR,     'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization > app-org-info > section > div.section__inner > div > div > div.grid__row__item.grid__row__item--span9\@md > div > app-org-info-details > div > div.tags > div.tag.tech > div.tech__content').text
        topics = driver.find_element(By.CSS_SELECTOR,           'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization > app-org-info > section > div.section__inner > div > div > div.grid__row__item.grid__row__item--span9\@md > div > app-org-info-details > div > div.tags > div.tag.topics > div.topics__content').text

        ideas_list_link = driver.find_element(By.CSS_SELECTOR,  'body > app-root > app-layout > mat-sidenav-container > mat-sidenav-content.mat-drawer-content.mat-sidenav-content.site__main.theme.theme--gray.ng-star-inserted > div > div > main > app-program-organization > app-org-info > section > div.section__inner > div > div > div.grid__row__item.grid__row__item--span9\@md > div > div > div > a').get_property("href")
        ideas_list_link = f'=HYPERLINK("{ideas_list_link}", "{ideas_list_link}")'

        gsoc_link = link.removesuffix('\n')
        gsoc_link = f'=HYPERLINK("{gsoc_link}", "{gsoc_link}")'

        ws.append([name, tagline, technologies, topics, ideas_list_link, gsoc_link])

        print('.', end='')

print()
driver.quit()

format_file(ws)

destination_path = 'GSoC_Shortlist.xlsx'

wb.save(destination_path)
print(f'File saved to {destination_path}')
