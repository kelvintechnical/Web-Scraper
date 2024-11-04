import requests
import csv
from bs4 import BeautifulSoup

books = []
url = "https://books.toscrape.com/" #target URL
response = requests.get(url) #sends HTTP GET request to fetch page's html conent

#We’ll want to ensure we’ve successfully fetched the page by checking the status_code of the response.

if response.status_code == 200:
    print("Page fetched successfully")
else:
    print(f'Failed to fatch page. Status code: {response.status_code}')
#This code will print a success message if the page loads correctly. If not, it will tell us the status code so we can troubleshoot.


soup = BeautifulSoup(response.text, 'html.parser')
# response.text gives us the HTML content of the page.
# BeautifulSoup(..., 'html.parser') creates a BeautifulSoup object, allowing us to search and navigate the HTML structure.

# What Parsing Means with BeautifulSoup ??
# When we "parse" with BeautifulSoup, we load the HTML content and get access to tools that let us search within it. This helps us identify and retrieve the specific pieces of data we're interested in, like:

# Headlines or text content within tags like <h1>, <h2>, <p>, etc.
# Links within <a> tags.
# Images within <img> tags.
# Divs or spans with certain classes that structure the page's layout.

prices = soup.find_all('p', class_='price_color')
# This line searches for every <p> tag with the class price_color and stores them in the prices list.

for price in prices:
    print(price.get_text())


titles = soup.find_all('h3')


for title in titles:
    book_title = title.a['title'] # Extract the title attribute from the <a> tag within <h3>
    print(book_title)

    for title, price in zip(titles, prices):
        book_data = {
            'title': title.a['title'],
            'price': price.get_text()
        }
        books.append(book_data) # Add the dictionary to the books list

with open("books.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price"])
    writer.writeheader() #write the header row
    writer.writerows(books) #write all book data rows


with open("books.csv", mode="r") as file:
    print(file.read())


    # URL https://public.tableau.com/authoring/tableau_practice_project/Sheet1/Sheet%202#1