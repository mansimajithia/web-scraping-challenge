# Web Scraping Homework - Mission to Mars
## Objective

The purpose of the Homework was to build a Full Stack Application. 
1. The first part of this homework was to use Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinters to build different dictionaries by scraping websites for Mars Data. This included Mars images and table of information.
2. The second part of this assignment was to create a MongoDB Database.
3. After creating a MongoDB, it was time to create a Flask Application. This Flask Application turned the webscraping material into dictionaries so that the HTML script could read and publish all information related to Mars.

For specific information about the assignment, please read below:


## Step 1 - Scraping

Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Create a Jupyter Notebook file called `mission_to_mars.ipynb` and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

### NASA Mars News

* [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest news and paragraph text on Mars. This was achieved through BeautifulSoup and Splinter through Pandas in Jupyter Notebook.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) to collect the feature images of Mars.

* Used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Facts

* [Mars Facts webpage] (https://space-facts.com/mars/) and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## Step 2.1 - Flask Application

* Jupyter Notebook was converted into a Python script called `scrape` that executed all of scraping code from above and returnd one Python dictionary containing all of the scraped data.

- - -

## Step 2.2 Mongo DB

* A Database was created to store all scraped data

* Next, a roote route was created that would query the Mongo Database and pass mars data into an HTML template to display the data.

- - -

## Step 3 - Submission

To submit your work to BootCampSpot, create a new GitHub repository and upload the following:

1. The Jupyter Notebook containing the scraping code used.

2. Screenshots of your final application.

3. Submit the link to your new repository to BootCampSpot.

## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for your database. For this homework, you can simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure your HTML template.

### Copyright

Trilogy Education Services © 2019. All Rights Reserved.
