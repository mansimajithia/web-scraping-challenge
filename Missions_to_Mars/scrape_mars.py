import requests
import os
from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():

    # Initialize browser
    browser = init_browser()

    time.sleep(3)

    # NASA MARS NEWS
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  

    # results are returned as an iterable list
    results = soup.find_all('div', class_="slide")

    # Get News Title and Paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_title.replace("\n","")

    news_p = soup.find('div', attrs = {'class':'rollover_description_inner'}).text
    
    # broswer.quit()

    # JPL MARS SPACE IMAGES - FEATURED IMAGE

    # Initialize browser
    browser = init_browser()

    time.sleep(10)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html   
    soup = BeautifulSoup(html,'html.parser')

    # Click on Full Image
    browser.click_link_by_partial_text('FULL IMAGE')
    # # button = browser.find_element_by_xpath('more info')
    # # button.click()
    # # browser.click_link_by_partial_text('more info')
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')
    # result = soup.find('div', id='fancybox-lock')
    # # print(result)
    # div = result.find('div', class_='buttons')
    # # link = div.find('a', class_='addthis_button_compact')
    # more_info = div.find('a', class_='button')['href']
    # # print(link)
    # # print(more_info)
    # # print(div)
    # link = ('https://www.jpl.nasa.gov'+ more_info)
    # browser.visit(link)
    # html = browser.html
    # soup = BeautifulSoup(html, 'html.parser')

    browser.click_link_by_partial_text('more info')

    # driver = webdriver.Ie()
    # driver.get(url)

    # driver.find_elements_by_link_text("more info").click()


    html = browser.html   
    soup = BeautifulSoup(html, 'html.parser')

    image_source = soup.find("figure", class_="lede")

    link = image_source.find('a')

    href = link['href']
    # print(image_source)
    print(href)

    featured_image_url = ('https://www.jpl.nasa.gov' + href)

    browser.quit()

    # MARS FACTS
    broswer = init_browser
    time.sleep(3)

    url ="https://space-facts.com/mars/"

    table = pd.read_html(url)
    df = table[0]

    df.columns = ["Description", "Values"]

    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')

    browser.quit()

    # MARS HEMISPHERES
    browser = init_browser()
    time.sleep(3)

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html

    soup = BeautifulSoup(html, 'html.parser')

    html = browser.html   
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='item')
    # results = soup.find('div', attrs={'class':'description'}).text

    html = browser.html   
    soup = BeautifulSoup(html,'html.parser')

    # Create a dictionary to later append to
    mars_dictionary = []

# Iterate through each page
    for result in results:
#     Get the title
        title = result.h3.text
        title = title.replace ("Enhanced","")
    
#     Find the link & create the link
        href = result.find('a')['href']
        base_url = "https://astrogeology.usgs.gov"
        image_link = base_url + href
    
#     Click on each link
        browser.visit(image_link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
    
#     Get the image_url
        downloads = soup.find('div', class_ = "downloads")
        image_url = downloads.find('a')['href'] 

#     Append to dictionary
        mars_dictionary.append({"title": title, "img_url": image_url})
    
    # store everything in mars_data dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table":html_table,
        "mars_dictionary": mars_dictionary
    }
    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if  __name__ == "__main__":
    print(scrape())
     