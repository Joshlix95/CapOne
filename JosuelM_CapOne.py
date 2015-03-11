import csv
# The csv module implements classes to read and write tabular
# data in CSV format like our document oscars_tweets.csv

# ============================= OPENING DATA ==================================== 

out = open("C:/Users/felix_000/Desktop/data_CapOne.csv","rb")
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

Tweets= ColCall(2) 
Tweets="".join(Tweets)
Tweets = Tweets.lower()
nTweets = "".join(Tweets.split())

Films = {
        "American Sniper":["American sniper"] ,
        "Birdman": ["Birdman", "Unexpected virtue of ignorance"],
        #"Boyhood": ["Boyhood"],
        "The Grand Budapest Hotel" : ["The Grand Budapest Hotel"],
        "The Imitation Game" : ["Imitation game"],
        "Selma" :["Selma"],
        "The Theory of Everything": ["The Theory of everything"],
        "Whiplash": ["Whiplash"]
        }

def FindAppearance():
    
    dico_films = {}
    
    NumAppear = 0
    for item in Films.keys():
        for stuff in Films[item]:
            stuff = stuff.lower()
            stuff = "".join(stuff.split())
            if nTweets.count(stuff) != 0:
                NumAppear += nTweets.count(stuff)

        dico_films[item] = NumAppear
                
    #print NumAppear
    print dico_films
