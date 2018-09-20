
# coding: utf-8

# In[ ]:


#Recipes V2.1


# In[8]:


#import all relevant packages
import csv

#the most up-to-date, working version of all functions used are kept here

def Header(): #a function which will print a fun header at the start of the program
    print '---RECIPE FINDER V2.0---','\n','--09 19 2018--','\n','-Because not knowing what to make is a bad excuse!-','\n','\n','\n'

#a function which will enable faster creation of recipe dicts and storage of those dicts in a list
def AddRecipe(name, sweet, savory, spicy, effort, ingredients, prepTime):
    dictionary = {}
    dictionary['sweet'] = sweet #assigning each of the attributes above as a value with a corresponding key having the corresponding variable name
    dictionary['savory'] = savory
    dictionary['effort'] = effort
    dictionary['spicy'] = spicy
    dictionary['ingredients'] = ingredients
    dictionary['name'] = name
    dictionary['prep time'] = prepTime
    recipes.append(dictionary)

#a function which calculates the average of a variable number of inputs
def Avger(*args):
    argLengthList = []
    for i in args:
        argLengthList.append(i)
    return sum(args)/len(argLengthList)

#a function which returns the recipe with the highest/lowest value for a specified attribute
def FindMe(minMax, attribute):
    nameList = []
    attributeList = []
    for i in recipes:
        nameList.append(i['name'])
        attributeList.append(i[attribute])
    attributeZip = zip(nameList,attributeList)
    for i in attributeZip:
        if minMax == 'minimum':
            if i[1] == min(attributeList):
                print i 
        elif minMax == 'maximum':
            if i[1] == max(attributeList):
                print i
        else:
            print 'minMax value not allowed.  Please specify either minimum or maximum.'
            break
            
#a function which guides the user through the task of adding a recipe        
def StartRecipeAdd(time):
    firstTimeAddMessage = 'Thanks for adding to the collection.'
    secondTimeAddMessage = 'Thanks for adding another one to the collection.'
    if time == 'first':
        print firstTimeAddMessage
        RecipeQuestions(recipes)
    elif time == 'not first':
        print secondTimeAddMessage
        RecipeQuestions(recipes)
        
#a function which guides the user through the task of finding a recipe 
def StartRecipeFind(time):
    firstTimeFindMessage = 'Yum.  Time to pick a recipe out!'
    secondtimeFindMessage = 'Look at you go!  Time to pick out another recipe.' #not working for some reason, says secondtimeFindMessage is not defined
    if time == 'first':
        print firstTimeFindMessage
    elif time == 'not first':
        print secondtimeFindMessage
    AskFlavorfulness() # AskFlavorfulness to ask user what flavors they want to prioritize in the recommended recipe
   
    
#a function which begins the UI, prompting the user to choose what task they want performed
def Welcome():
    begOption1 = 'Enter a recipe.'
    begOption2 = 'Cook something!'
    print 'Welcome to the recipe finder.  What do you want to do?','\n', '-',begOption1, '\n','-',begOption2
    welcomeMessageResponse = input() #create a space for the user to choose between adding a recipe and looking one up
    welcomeMessageResponseString = str(welcomeMessageResponse) 
    print '\n', 'You entered: ', welcomeMessageResponseString
    if welcomeMessageResponse == begOption1:
        StartRecipeAdd('first')
    elif welcomeMessageResponse == begOption2:
        StartRecipeFind('first')

#a function which either ends the UI or pulls the user back in for another task
def Goodbye():
    endOption1 = 'Enter another recipe.'
    endOption2 = 'Cook something else!'
    endOption3 = 'Nope, all done!'
    while True: #initialize an endless loop, allowing the user to keep selecting options until they want to exit
        print '\n','Want to do anything else?','\n', '-',endOption1, '\n','-',endOption2, '\n','-',endOption3
        endMessageResponse = input()
        endMessageResponseString = str(endMessageResponse)
        print '\n', 'You entered: ', endMessageResponseString
        if endMessageResponse == endOption1:
            StartRecipeAdd('not first') #initialize the recipe adding procedure here
        elif endMessageResponse == endOption2:
            StartRecipeFind('not first') #initialize the recipe selection procedure here
        elif endMessageResponse == endOption3:
            print '\n','Sounds good.  Thanks for using the recipe finder!'
            break #exit the while loop

#a function which pulls the flavor values for a given (input) recipe
def FlavorFind(recipeName, flavor): #easier than calling a value of a key of a dictionary within a list...I think...
                                    #FlavorFind('chicken and rice','savory') #example of how to use FlavorFind
    for i in recipes:
        if i['name'] == recipeName:
            return i[flavor]

#a function which calculates the average of a variable number of inputs
def Avger(args):
    argLengthList = []
    for i in args:
        argLengthList.append(i)
    return sum(args)/len(argLengthList)

def FindFlavorfulness(recipeName, flavorList): #a function which searches the recipe list for a given recipe (recipeName) and the flavors specified in a list (flavorList), then calculates flavorfulness by averaging the values corresponding to those flavors
                         #designed to pair with AskFlavorfulness: Ask determines which flavors to search for, and Find measures the flavorfulness associated with those flavors for a given recipe
                         #the two functions were split up to allow a more flexible/iterative approach to finding lots of recipes' flavorfulness 
    
    #NOTE1: example of the two functions mentioned above working together
    #AskFlavorfulness()
    #FindFlavorfulness('chicken and rice', globalAskFlavorfulnessOutputList)
    
    #NOTE2: the benefit of separating these functions is that FindFlavorfulness can be used independently of AskFlavorfulness
    
    flavorValueList = [] #create a blank list, flavorValueList, into which the flavor values corresponding with each flavor in the input list, flavorList, will be appended
    for flavor in flavorList:
        flavorValueList.append(FlavorFind(recipeName,flavor)) #add each value corresponding to each flavorList flavor to flavorValueList
       
    return Avger(flavorValueList) #output the average of all flavor values to calculate a given recipe's flavorfulness 

def AskFlavorfulness(): #a function which interact with the user to determine which flavors the user wants to evaluate/prioritize flavorfulness by
       
    print 'Flavor-wise, what are you in the mood for?  Your options are...','\n', '-sweet', '\n', '-spicy', '\n', '-savory' #make the user pick from the flavor options
    userResponse = input() #store the user's response in a variable for subsequent cleaning/analysis
    print 'Your response was:', userResponse
    unwantedInputs = ['',' ']
    outputList = [] #create a blank list into which all flavors scraped from userResponse will be placed
    outputString = '' #create a blank string which will be the used to create each flavor added into outputList
    userResponse = userResponse.replace(' ','') #strip all spaces from userResponse. this way, assuming no errors, the only things in the string will be words we want, and commas
                                                #the above assumption is NOT SMART, figure out a better way to handle errors/the string...
    userResponse = userResponse + ',' #add a comma onto the end of userResponse to make the logic below work
                                      #NOTE this implementation is really sloppy and needs work...
                                      #more elegant implementation: once the loop below hits the end of userResponse, append outputString onto outputList one last time
    for character in userResponse:
        if character <> ',':
            outputString = outputString + character #add the current character onto the string which will be appended onto outputString
        else:
            outputList.append(outputString) #if the loop has reached a comma, that means it's time to append outputString (by now presumably a full word/flavor) onto outputString
            outputString = '' #once the scraped word has been appended onto outputList, clear out outputString to begin the next word
    
    tupleList =  [] #create a blank list into which we'll add tuples containing all of the relevant info for each recipe 
    
    for recipe in recipes:
        #create a tuple of recipe name, flavorfulness, effort, and cost
        infoTuple = (recipe['name'], FindFlavorfulness(recipe['name'], outputList), recipe['prep time'], recipe['effort']) 
        #add that tuple to tupleList
        tupleList.append(infoTuple)
    
    sortedTupleList = sorted(tupleList, key = lambda item:-item[1]) #sort the recipes descending by their flavorfulness value
              
    print 'Ok, you should cook...',sortedTupleList[0][0], 'or', sortedTupleList[1][0] #return the first elements (name) of the elements (tuples) of sortedTupleList with the highest and second highest flavorfulness    

    
def RecipeQuestions(recipeList): #a function which allows the user to, by answering a series of questions, add a recipe to the list of pre-done recipes
    
    leaveOption = 'All done.'
    stayOption = 'Add another!'
    
    affirmativeExportOption = 'Yes.'
    negativeExportOption = 'No.'
    
    #recipeList = [] #uncomment when debugging.  otherwise recipeList value should be set to recipes, the name of the list where the default recipes are stored
    newRecipeCounter = 0 #create a variable which counts the number of new recipes added by the user after calling this function
    
    print 'Ok, time to add some recipes!','\n','Want to use the default recipe list, or import your own?','\n','-Default.','\n','-Import.'
    response = input()
    if response == 'Import.':
        ReadorWrite('r',recipes,r'C:\Users\ckene\Desktop\test.csv') #import the list of recipes which the user would rather use than the default recipe list
        recipeList = recipes #assign the list read in by ReadorWrite above as the list of recipes used by RecipeQuestions
    elif response == 'Default.':
        print 'Sounds good.  The default list of recipes will be used.'
        
    while True:
        
        qList = ['What is the name of the recipe?', 
                'On a scale of one to ten, how sweet is the recipe?',
                'On a scale of one to ten, how savory is the recipe?',
                'On a scale of one to ten, how spicy is the recipe?',
                'On a scale of one to ten, how much effort does cooking this recipe require?',
                'List the ingredients in this recipe',
                'On a scale of one to ten, how lengthy is prep time for this recipe?'] #list of questions to ask user
        rDict = {} #blank dictionary to store responses to qList questions in
        dList = ['name', 'sweet', 'savory', 'spicy', 'effort', 'ingredients', 'prep time'] #list of rDict keys
        
        qualList = ['name', 'ingredients'] #a list of all keys which should expect non-numeric values
        
        
        for q,d in zip(qList,dList):
            print q
            if d in qualList: #if the key corresponding to the value just input by the user is non-numeric
                rDict[d] = input() #then just add it to the dictionary as-is
            else: #otherwise (aka the value corresponds to a numeric key aka the value, entered as a string, should actually be numeric)
                rDict[d] = int(input()) #recast the input as numeric before adding it to the recipe dictionary, allowing math to be performed on it elsewhere in the program...
        
        recipeList.append(rDict) #append the newly added recipe onto the list of existing recipes
        newRecipeCounter += 1 #add one to the count of newly added recipes
        
        #allow the user to determine whether to add another recipe
        print 'Add another recipe?','\n', '-',leaveOption,'\n', '-',stayOption
        addResponse = input()
        if addResponse == leaveOption:
            break #if the user is done adding recipes, break the loop
        else:
            print 'Sounds good.','\n'
            
    
    #print recipeList #uncomment when debugging
    
    #if new recipes were added, give the user the opportunity to save the new collection of recipes
    if newRecipeCounter > 0:
        print 'It looks like', newRecipeCounter, 'new recipes were added.  Want to export these?','\n', '-',affirmativeExportOption,'\n', '-',negativeExportOption
        exportResponse = input()
        if exportResponse == affirmativeExportOption:
            print 'Sounds good, time to export the recipes.'
            ReadorWrite('w',recipes,r'C:\Users\ckene\Desktop\test.csv')
        else:
            print 'Ok.  Newly added recipes will not be exported.'
    
    return 'All done adding recipes!'  

def ReadorWrite(rw,recipes,filePath): #a function which either reads a .csv in as a list of recipes, or writes a list of recipes out as a .csv
    #rw - read or write
    #recipes - the name of the data structure which stores the recipes within the program
    #filePath - the location of the file to be written to/read from
    
    #filePath = r'C:\Users\ckene\Desktop\test.csv'
    #recipes = recipes
    
    if rw == 'w':
        #confirm that the right filepath is being used
        print 'Recipes will be written to', filePath,'.  Is that correct?','\n','-Yes.','/n','-No.'
        response = input()
        if response == 'No.': #if the user wants to specify a new filepath, give them an opportunity to do it here
            print 'Please specify new filepath:'
            filePath = input()
        #export current list of recipes to a .csv
        outfile = open(filePath,'w')
        fieldnames = ['name', 'sweet', 'savory', 'spicy', 'effort', 'ingredients', 'prep time']
        writer = csv.DictWriter(outfile,fieldnames = fieldnames)
        writer.writeheader()
        for i in recipes:
            writer.writerow(i)
        print 'Done writing recipes to filepath.'

    elif rw == 'r':
        #confirm that the right filepath is being used
        print 'Recipes will be read from', filePath,'.  Is that correct?','\n','-Yes.','/n','-No.'
        response = input()
        if response == 'No.': #if the user wants to specify a new filepath, give them an opportunity to do it here
            print 'Please specify new filepath:'
            filePath = input()
        #import a .csv and use it as the list of recipes
        infile = open(filePath)
        reader = csv.DictReader(infile)

        readList = [] #list to store .csv dict elements in
        for row in reader:
            readList.append(row)
        recipes = readList #replace list of default recipes with read-in list of recipes
        print 'Done reading recipes from filepath.'


# In[10]:


#This cell runs everything

#load a handful of default recipes to get things started
recipes = [] #define an empty list, recipes, which will contain all of the recipes

#use the function to (quickly) add another recipe to recipe
ingredients = 'Teriyaki glaze, salmon, garlic, lemon juice'
AddRecipe('Teriyaki Salmon', 8, 3, 3, 1, ingredients, 4)

ingredients = 'beef, brown sugar, garlic, ginger, sriracha, soy sauce, green onion'
AddRecipe('Korean Beef', 8, 4, 8, 2, ingredients, 3)

ingredients = 'chicken, breadcrumbs, chicken bouillon, carrots, flour, egg, rice'
AddRecipe('chicken and rice', 2, 10, 0, 7, ingredients, 10)

ingredients = 'pasta, tomato sauce, beef, cumin, pepper, salt, onion'
AddRecipe('pasta with beef sauce', 1, 8, 2, 1, ingredients, 2)

ingredients = 'chicken, walnuts, spinach, apples, strawberries, raspberry vinaigrette'
AddRecipe('raspberry vinaigrette salad', 5, 1, 0, 2, ingredients, 1)

ingredients = 'sweet potato, onion (diced), bell pepper (diced), cajun seasoning, garlic, salt, pepper'
AddRecipe('sweet potato burger patty', 3, 2, 5, 8, ingredients, 9) 

ingredients = 'de-veined shrimp, red pepper flakes, garlic, cooking wine, spinach, pasta, olive oil'
AddRecipe('red pepper shrimp scampi', 5, 0, 9, 2, ingredients, 3)

#activate the functions which guide the user through the program interface
Header()
Welcome() #initialize functions and guide user through first task they want to complete
Goodbye() #upon completion of fist task, ask the user if they want to do anything else.  If so, do it.  If not, wrap up.
# quit() #exit the program #LEAVE THIS LINE OUT UNTIL PRODUCTION TO AVOID HAVING TO RESTART THE KERNEL EACH TIME 

