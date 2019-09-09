import requests
import json
import random
import time
import argparse
foodListOne=[]
foodListTwo=[]
foodListThree=[]
foodListFour=[]
count = 0
argList =[]
def printArgsHelp():
    parser = argparse.ArgumentParser(description='example "py mcFood.py -c Mexican -s rating"')
    parser.add_argument('-c','--cuisine',help='please select cuisine: Mexican, Italian, American, Asian...etc')
    parser.add_argument('-s','--sort',help='Please select a sorting algorith: rating, distance, best_match')
    parser.print_help()
def argParseFunc(argumentList):
    parser = argparse.ArgumentParser(description='pick random food!')
    parser.add_argument('-c','--cuisine',help='please select cuisine: Mexican, Italian, American, Asian...etc')
    parser.add_argument('-s','--sort',help='Please select a sorting algorith: rating, distance, best_match')
    args = parser.parse_args()
    argumentList.append(str(args.cuisine))
    argumentList.append(str(args.sort))
def searchBusinesses(foodList,typeOfFood,sortBy):
    api_key = ''
    headers = {'Authorization': 'Bearer %s' % api_key}
    url='https://api.yelp.com/v3/businesses/search'
    params = {'term':typeOfFood,'location':'','radius':'40000','limit':'50','sort_by':sortBy}
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

try:
    argParseFunc(argList)
    searchBusinesses(foodListOne,argList[0],argList[1])
    pickRandomTwo(foodListOne)
except:
    printArgsHelp()
