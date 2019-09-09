import requests
import json
import random
import time
foodListOne=[]
foodListTwo=[]
foodListThree=[]
foodListFour=[]
count = 0
def searchBusinesses(foodList,typeOfFood,sortBy):
    api_key = ''
    headers = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/search'
    params = {'term':typeOfFood,'latitude':'','longitude':'','radius':'10000','limit':'50','sort_by':sortBy}
    req=requests.get(url, params=params, headers=headers)
    #print('The status code is {}'.format(req.status_code))
    j = json.loads(req.text)
    businesses = j["businesses"]
    for business in businesses:
        strRating = str(business["rating"])
        strAddress = str(" ".join(business["location"]["display_address"]))
        strDistance = str(business["distance"])
        strCategories = str(business["categories"])
        foodList.append("Name: " + business["name"] +
                           "\nRating: " + strRating +
                           "\nAddress: " + strAddress +
                           "\nDistance: " + strDistance +
                           "\nCategories: " + strCategories +
                           "\n")
def pickRandomTwo(foodList):
    randomChoiceOne = random.choice(foodList)
    foodList.remove(randomChoiceOne)
    randomChoiceTwo = random.choice(foodList)
    foodList.remove(randomChoiceTwo)
    print("\n-------these are random choices------\n")
    print(randomChoiceOne)
    print(randomChoiceTwo)

def printFullResList(foodList,count):
    for res in foodList:
        count=count+1
        print(res)
    print('\n\n')
    print(count)
    print('\n\n')

searchBusinesses(foodListOne,"Burgers","rating")
pickRandomTwo(foodListOne)
input("press any button to continue")
