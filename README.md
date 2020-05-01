[![HitCount](http://hits.dwyl.com/swapnanildutta/instagram-search.svg)](http://hits.dwyl.com/swapnanildutta/instagram-search)
# Instagram Account Details Extraction
I have used a python code to extract the details of a given username, the searchDisplay() searches for the given username and prints the extracted data and the getDetails() searches for the given username and returns the extracted data in form of a dictionary.
## How to Use
Clone the repository and run the main.py file and enter a valid username as input.
## Requirements
For running this you need to have Python3 installed.

Then, run the command 

>***pip install -r requirements.txt***


This will instantly install all the libraies needed.
## Example
To install the package

>pip install ig-data==0.0.2

To initialize an object of the package, type within the python terminal

>import ig_data.InstaSearch as ig       ***or***      import ig_data.InstaSearch

Then using the object, call the function searchDisplay()

>ig.searchDisplay(***USERNAME***)       ***or***      ig_data.InstaSearch.searchDisplay(***USERNAME***)

And the output would be

'''
Name :  *NAME*          Username :  @*USERNAME*     Followers :  *FOLLOWER COUNT*
 Bio :  *ACCOUNT DESCRIPTION*
'''

Also using the object, call the function getDetails() and store the data in a dictionary

>dictionary=dict()

>dictionary=ig.getDetails(***USERNAME***)       ***or***      dictionary=ig_data.InstaSearch.getDetails(***USERNAME***)

And the content of **d** would be

'''
{'@context': 'http://schema.org', '@type': 'Person', 'name': *NAME*, 'alternateName': '@*USERNAME*', 'description': '*ACCOUNT DESCRIPTION*', 'url': '*PERSONAL URL IF ANY*', 'mainEntityofPage': {'@type': 'ProfilePage', '@id': 'https://www.instagram.com/*USERNAME*/', 'interactionStatistic': {'@type': 'InteractionCounter', 'interactionType': 'http://schema.org/FollowAction', 'userInteractionCount': '*FOLLOWER COUNT*'}}, 'image': 'https://www.instagram.com/static/images/ico/favicon-200.png/ab6eff595bb1.png'}
'''
