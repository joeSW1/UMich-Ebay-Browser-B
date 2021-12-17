WHO:
Created by me, MSI student Joseph Ortigara, with help from instructor Bobby Madamanchi

WHY:
This site allows the user to sort Ebay's results based on variables that are not accessible on the actual Ebay site.
For example, the user can sort based on whether the item in being sold by a top-rated seller or not.
My site offers an alternative way to search through Ebay's records.
It could be easily restructured, which isn't possible using Ebay's actual site.

WHAT:
I crawled and scraped item data from Ebay.
Then I categorized each item and arranged them in a tree structure
The user is able to select options on the webpage in order to see the items that fit their search

HOW:
I used the MVC structure to organize my data.
    The Model is found in the python files like network_setup.py and ebay_data_object.json
    The View is found in the HTML templates like index.html
    And the Controller is found in the python files like helloflask.py
I used the anytree library to construct my data tree.
I scraped and crawled Ebay listings using BeautifulSoup4.
For each item, I created an entry in two separate databases.
   1. One database summarizes the raw data from Ebay: The item's price, image, link, condition, category, seller reputation. I also give it a unique code that summarizes a lot of this information
   2. The other is a series of nodes labeled using the code from former database (1.)  
   This way, the tree of nodes functions as a flat representation of the more complex database. The controller pulls the structure from the tree (Database 2.), and then pulls the content of each node from its respective entry in the raw database (Database 1.)
I hosted the site using Flask, and used a 'Post' Form to update the table.

FUTURE STEPS:
I think that someone could explore how to restructure the sorting function to better fit with user's needs.
Also, a future developer could find ways of combining Ebay data with related data to offer a completely new, curated experience
Lastly, someone could update the webpage to make it more responsive

Thank you for your time.

Best,
Joe


