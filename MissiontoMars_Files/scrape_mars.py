
# Dependencies
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import time
import re


# Mars News Scrape

#ChromeDriver Splinter Execution
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

    #Visit Mars URL
    mars_url = "https://redplanetscience.com/"
    browser.visit(mars_url)

    time.sleep(5)


    #Beautful Soup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Pull and Print Title and Article
    news_title = soup.find("div", class_="content_title").text

    news_teaser = soup.find("div", class_="article_teaser_body").text

    print(f"> Title: {news_title}\n\n> Article Teaser: {news_teaser}")


    browser.quit()


    # JPL Mars Image Scrape

    #ChromeDriver Splinter Execution
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    #Visit Mars Images URl
    images_url = "https://spaceimages-mars.com/"
    browser.visit(images_url)

    time.sleep(5)


    #BeautifulSoup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Pull and Print Image URL
    results = soup.find_all("img", class_="headerimage fade-in")

    featured_image = f"{images_url}{results[0]['src']}"
    print(featured_image)

    browser.quit()


    # Mars Facts

    #ChromeDriver Splinter Execution
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Visit Galaxy Facts URL
    galaxy_facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(galaxy_facts_url)

    time.sleep(5)

    #Beautiful Soup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Read Mars Data 
    data_table = pd.read_html(galaxy_facts_url)[1]

    browser.quit()

    #Create HTML Table 
    data_table.columns=["Category", "Data"]
    data_table.set_index("Category")

    #Save HTML Table
    data_table.to_html("mars_data.html")
    mars_data=data_table.to_html()


    # Mars Hemispheres

    #ChromeDriver Splinter Execution
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #Visit Mars Hemisphere URL
    hemispheres_url = "https://marshemispheres.com/"
    browser.visit(hemispheres_url)

    time.sleep(5)

    #Cerberus Append


    #Click Cerberus Link
    browser.click_link_by_partial_text('Cerberus')

    #Create Lists to hold data from site
    img_urls = []
    img_titles = []

    #BeautifulSoup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Append URL and Title information to lists
    cerberus_url = hemispheres_url+soup.find("img", class_='wide-image')["src"]
    img_urls.append(cerberus_url)

    cerberus_title = soup.find("h2", class_="title").text
    img_titles.append(cerberus_title)


    # Schiaparelli Append
    #Return to home page
    browser.click_link_by_partial_text('Back')

    #Click on Schiaparelli Link
    browser.click_link_by_partial_text('Schiaparelli')

    #BeautifulSoup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Append URL and Title info to lists
    schiaparelli_url = hemispheres_url+soup.find("img", class_='wide-image')["src"]
    img_urls.append(schiaparelli_url)

    syrtis_title = soup.find("h2", class_="title").text
    img_titles.append(syrtis_title)


    # Syritis Append

    #Return to Home Page
    browser.click_link_by_partial_text('Back')

    #Click on Syritis link
    browser.click_link_by_partial_text('Syrtis')

    #Beautiful Soup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Append to image and title lists
    syrtis_url = hemispheres_url+soup.find("img", class_='wide-image')["src"]
    img_urls.append(syrtis_url)

    syrtis_title = soup.find("h2", class_="title").text
    img_titles.append(syrtis_title)


    # Valles Marineris Append

    #Return Home
    browser.click_link_by_partial_text('Back')

    #Click on Valles link
    browser.click_link_by_partial_text('Valles')

    #Beautiful Soup Execution
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')

    #Append to images and titles list
    valles_url = hemispheres_url+soup.find("img", class_='wide-image')["src"]
    img_urls.append(valles_url)

    valles_title = soup.find("h2", class_="title").text
    img_titles.append(valles_title)

    browser.quit()

    #Loop and append to image urls list
    hemisphere_image_urls=[]
    for i in range(len(img_urls)):
        hemisphere_image_urls.append({"title": img_titles[i], "img_url": img_urls[i]})

    hemisphere_image_urls

    mars_info = {
          "news_title": news_title,
          "news_teaser": news_teaser, 
          "featured_image": featured_image,
          "mars_facts": mars_data,
          "hemi_titles": img_titles,
          "mars_hemispheres": img_urls
        
    }
    
    return mars_info



