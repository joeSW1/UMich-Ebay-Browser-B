WHO:
Created by me, MSI student Joseph Ortigara, with help from instructor Bobby Madamanchi

SUMMARY:
This site allows the user to sort Ebay's results based on variables that are not accessible on the actual Ebay site.
For example, the user can sort based on whether the item in being sold by a top-rated seller or not.
My site offers an alternative way to search through Ebay's records.
It could be easily restructured, which isn't possible using Ebay's actual site.

DATA INFO:
1. I crawled and scraped item data from Ebay.
2. I picked the categories and options beforehand, so my app scrapes a list of
   Ebay pages that are combinations of my pre-picked variables.
3. For each listing, I scraped what I felt were the most important variables: Title, Price, Image, Link, Seller Reputation, and Hotness (How many people are interested in it)

4. For each item, I created an entry in two separate databases.
   A. One database summarizes the raw data from Ebay (variables listed above) I also give it a unique code that summarizes a lot of this information
      Example of raw data dict listing:
      {'hat;Brand New;Top;1' :
         {'name': 'Michigan Wolverines Beanie Cuffed Winter Knit Hat Cap Toque New With Tags', 'link': 'https://www.ebay.com/itm/254726335043?_trkparms=ispr%3D1&hash=item3b4edf6a43:g:KjQAAOSwb7BfacAL&amdata=enc%3AAQAGAAACoPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSg3Ye8yTWgOW7pmE1t838dv%252FVVvIyW8qnuIp%252BvXVpyeBVDW4UxJnXEgf%252FSuwmk9ZjGFgGV1k6X5LFm6%252F3OFOg8XtbQd%252B2OyJ4yqcUkoN4mY7cF1MkqNjGN7HUmuu637kqN%252FBsxLUrHDq8YxSRdkmbJsynIqv4meyyMGtpZIiNXjGSbHtfICI35029weAgktr8tQKSRmGJH4Lg7YgnhLUBTpLO%252BPuQNi1JhsPpEcVzsEiEJKiPHs%252BW69%252BNolx%252Bgs%252BvUfRMbOBGKOfPtEagvfZZy%252BmdYWHwyfyEEYPKGI824KkgCFkLRoTRDimpvq%252BCzXPhQPQbZjJXwNJs1wzxEERqahYXc4PRa8kTkRm54S7G%252Fz0WaVcVUyFj9Ka%252Fg0QuVRq4YU%252BmXKMXtL8ya2yDSCgSff8SSTomEz5T5ivPLvwapADHKiNHqyMWyEcjXQK8bqGRLlKcDixsBO1nHlo4OJPAT9%252FG414xuzvDIFou2HKWEZg0zldAJhwoeAkbD9VnBJh61TxLnCSHbrOjI%252BwtfKKPp3qt5O4ayyOjIzB5zTpOvP8XzIJvVRoirpAZlhLkKNTy1FE9zcrweIFvAdI8%252BXZZcAmcWaunewGzM165LSGYnVrnnjJ6YRCHFTAbA%252BaCd2DifMa6EereOn5xauN6MStwVxphgP%252FbMDaD5Vsinhy9QM%252FcXMx4rSJSdM1kpEHL7vfcwTrNPiBbBjCUNX9ZU8rRjMq%252BqS3Vv4cvigqwROmRxNW37yuyCoA5f4vbCoKUQCQpoxgPafa7ivFoivV4jje1N4PePSQqiA16qCR4fYLVYiEdBCaO8eeR7gD%252BTccYbpACNr6hoMRBTOu9yH2PytQA4Q%253D%253D%7Cclp%3A2334524%7Ctkp%3ABFBMrsjTj7lf', 'image': 'https://i.ebayimg.com/thumbs/images/g/KjQAAOSwb7BfacAL/s-l225.jpg', 
         'price': 13.99, 'hotness': None, 'condition': 'Brand New', 'reputation': 'Top', 'category': 'hat'}
      }

   B. The other is a network graph built using networkx. Before Ebay data is added here, I add some "category" nodes, which will be the searchable options of the database (e.g. "condition": "pre_owned", "new). For each listing, I create a new Node in this database, and then based on its data, I connect it to the category nodes that it matches. So, for example, a pre-owned hat will share edges with the "pre_owned" node and the "hat" node. I also add an attribute to each node. The category nodes are type "category" while the listing nodes are type "listing"
      Example of node in network graph:
      Node('hat;Brand New;Top;1')
         'type': 'listing',
         'neighbors': ['hat', 'top_rated', 'new']

5. When the user specifies what type of listings they want to see, a custom "common neighbors" function is run, which sees which "listing" nodes match the criteria.
6. The code of each match is searched in the raw_data dataset, and then the full info for
Each listing is sent to the View
6. These nodes are then displayed in a table

Note: I conformed to the MVC structure for this project

Thank you for your time.

Best,
Joe


