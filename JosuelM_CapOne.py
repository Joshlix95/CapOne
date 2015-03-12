################################################################################
# Author: Josuel Musambaghani                                                  #
# MindSumo challenge context -- CAPITAL ONE --                                 #
# =============================================================================#
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
################################################################################

'''
************************ OUTLINE OF THE CHALLENGE ******************************
1) Popularity Rank: A list of the most tweeted about best picture
nominees (ranked from 1-8) 
2) Winner Announcement Prediction: Hour and minute when the winner
(Birdman) was mentioned on Twitter most frequently 
3) Location: A list of which states were the most active in tweeting
about #Oscars2015 (rank ordered from most active to least)
'''

import csv

# The csv module implements classes to read and write tabular
# data in CSV format like our document oscars_tweets.csv

# ============================= OPENING DATA ==================================== 

out = open("C:/Users/felix_000/Desktop/oscar_tweets.csv","rb")
data=csv.reader(out)
data=[row for row in data]
out.close

# The function ColCall(col) returns a list of data read vertically in any
# chosen column. It will help when looping through the data.
# ------------------------------------------------------------------------------

def ColCall(col): 
    ListColumn=[]
    row = 0
    while row < len(data):
        ListColumn.append(data[row][col])
        row += 1

    return ListColumn

# CHALLENGE 1 : POPULARITY RANK -- MOST TWEETED ABOUT THE BEST PICTURES NOMINEES
# ==============================================================================

# These are global variables to be used throughout the whole code.
Tweets= ColCall(2) 
Tweets1="".join(Tweets)
Tweets2 = Tweets1.lower()
nTweets = "".join(Tweets2.split())

PicNominees = ["American Sniper", "Birdman", "Unexpected Virtue of ignorance"
               , "Boyhood", "Grand Budapest Hotel", "Imitation Game",
               "Selma", "Theory of Everything", "Whiplash"]

dico_elt = {}   # global variable to be used in FindAppearance()
                # and DisplayResults(). 

# The function FindAppearance() loops in tweets to figure out how many times
# each nominee for the best picture was tweeted.
# ------------------------------------------------------------------------------

def FindAppearance():

    for elt in PicNominees:
        elt1 = elt.lower()              # lowercase data for accurate search
        elt2 = "".join(elt1.split())    # split data for accurate search

        count = 0
        
        for item in Tweets:
            item1 = "".join(item.split())   # split data for accurate search
            item2 = item1.lower()           # lowercase data for accurate search
            
            if (elt2 in item2) and ("pic" in item2) and ("best" in item2):
                count += 1
                #print count

        dico_elt[elt] = count

    print dico_elt

# The function DisplayResults() sort and display results from the previous
# function. Sorting is made by value and not by key.
# ------------------------------------------------------------------------------

def DisplayResults():
    FindAppearance()
    dico = dico_elt
    new_list = []

    # these two next lines combine the results found for "Birdman" and for
    # "The Unexpected Virtue of ignorance" together in one key -- "Birdman"

    dico_elt['Birdman'] += dico_elt["Unexpected Virtue of ignorance"]
    del dico_elt["Unexpected Virtue of ignorance"]

    m = sorted(dico.values())           # get the values use
    n = sorted(dico, key=dico.get)      # get the matching keys
    p = sorted(dico.items(), key=lambda x:x[1]) # get a list of tuples ordered by value

    # print p
    n=0
    while n <= 7:
        print "{}. ".format(n+1), p[7-n]
        n += 1
    


# CHALLENGE 2 : WINNER ANNOUNCEMENT PREDICTION
# ============================================================================

# the two next imported modules will help to deal with the time (date)
# conversion from Excel's data to Python

from datetime import datetime 
from datetime import timedelta

# The function FindTime focuses on appearances of  Birdman in tweets, and relate
# those mentions to a specific time they were posted. After finding the specific
# time in the UTC (Universal) time, the last step of this function used datetime
# to convert the given hour to the one between 5:30 to 9:30
# ------------------------------------------------------------------------------

def FindTime():
    store1=[]
    
    for elt in Tweets:
        x=Tweets.index(elt)
        if ("Birdman" and "ic") in elt:
            y=Tweets.index(elt)
            #print y
            store1.append(ColCall(0)[y])

        elif ("Unexpected" and "ic") in elt:
            z=Tweets.index(elt)
            #print z
            store1.append(ColCall(0)[z])

    #return store1

    store2 = list(set(store1))
    store3 = []

    # This part here below cuts off the seconds and fractions as we are
    # only using hours and minutes to determine the time with most "Birdman"
    # mentions. I stored them in store3
    
    for item in store2:
        item = item[:16]
        store3.append(item)

    #return store3
    store4 = list(set(store3))
    #print store4

    # This part counts the Tweets with Birdman (Or Unexpected Vertue of ignorance)
    # mention, and associate them (tweets) with the respective time (hour, minute)
    # when these mentions occured. The Dictionary here below will store the
    # specific time and the number of mentions.

    dico = {}
    numbers=[]
    for item in store4:
        numItem = ("".join(store1)).count(item)
        dico[item] = numItem
        numbers.append(numItem) # will help me to loop over in the dictionary to
                                # find the key with the highest mentions.
        
    #return dico
    numbers = list(sorted(numbers))

    for elt in dico.keys():         # This for loop looks for the key with the
                                    # highest mentions.
        if dico[elt] == numbers[-1]:
            print elt               # This is the time with the highest mentions
             
                                    # of the winner of the best picture nominee.

    # The next step here is to convert this output "elt" from the UTC (universal)
    # time to the normal required time from 5:30 to 9:30; I will just add four
    # hours to the time finded above.

            y= "23/02/15 " +elt[11:] 
            x=datetime.strptime(y, "%d/%m/%y %H:%M")
            z= str(x+timedelta(seconds=3600*4))
            print "The time when the winner (Birdman) was tweeted the most is {}".format(z)



# CHALLENGE 3 : LOCATION [STATES THAT TWEETED THE MOST ABOUT #Oscars]
# ============================================================================

# this next line stores data from the column of locations in a list
locations = ColCall(8)

# dictionaries real_states and states will serve as important tools in
# the function FindState.

real_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

states = {
        'AK': ['Alaska'],
        'AL': ['Alabama'],
        'AR': ['Arkansas'],
        'AS': ['American Samoa'],
        'AZ': ['Arizona'],
        'CA': ['California'],
        'CO': ['Colorado'],
        'CT': ['Connecticut'],
        'DC': ['District of Columbia'],
        'DE': ['Delaware'],
        'FL': ['Florida'],
        'GA': ['Georgia', 'Atlanta'],
        'GU': ['Guam'],
        'HI': ['Hawaii'],
        'IA': ['Iowa'],
        'ID': ['Idaho'],
        'IL': ['Illinois'],
        'IN': ['Indiana'],
        'KS': ['Kansas'],
        'KY': ['Kentucky'],
        'LA': ['Louisiana'],
        'MA': ['Massachusetts'],
        'MD': ['Maryland'],
        'ME': ['Maine'],
        'MI': ['Michigan'],
        'MN': ['Minnesota'],
        'MO': ['Missouri'],
        'MP': ['Northern Mariana Islands'],
        'MS': ['Mississippi'],
        'MT': ['Montana'],
        'NA': ['National'],
        'NC': ['North Carolina'],
        'ND': ['North Dakota'],
        'NE': ['Nebraska'],
        'NH': ['New Hampshire'],
        'NJ': ['New Jersey'],
        'NM': ['New Mexico'],
        'NV': ['Nevada'],
        'NY': ['New York'],
        'OH': ['Ohio'],
        'OK': ['Oklahoma'],
        'OR': ['Oregon'],
        'PA': ['Pennsylvania'],
        'PR': ['Puerto Rico'],
        'RI': ['Rhode Island'],
        'SC': ['South Carolina'],
        'SD': ['South Dakota'],
        'TN': ['Tennessee'],
        'TX': ['Texas'],
        'UT': ['Utah'],
        'VA': ['Virginia'],
        'VI': ['Virgin Islands'],
        'VT': ['Vermont'],
        'WA': ['Washington'],
        'WI': ['Wisconsin'],
        'WV': ['West Virginia'],
        'WY': ['Wyoming']
}

# The function FindState uses keys and values from dictionaries (real_states and
# states) to loop over tweets in order to find mentions of states as
# abbreviations, or as entire name of the state, or even sometimes as a pseudo
# of a state such as Cali to mean California.
# ------------------------------------------------------------------------------

def FindState():
    state_dict = {}
    
    for key in states.keys():
        for item in states[key]:
            if (key in locations) or (item in locations):
                y = locations.count(key) + locations.count(item)

                #print real_states[key] + ": "
                #print y

                state_dict[real_states[key]] = y

    p = sorted(state_dict.items(), key=lambda x:x[1])

    n = 0
    while n <= 49:
        print "{}. ".format(n+1), p[50-n]
        n += 1


################################################################################
#========================= END OF THE CHALLENGE ===============================#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
################################################################################
