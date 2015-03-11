# CapOne
# Challenge on MindSumo about #Oscar2015
# Author: Josuel Musambaghani

In the Capital One challenge contest, three main concerns were carefully treated:

1) Popularity Rank: A list of the most tweeted about best picture nominees (ranked from 1-8)
2) Winner Announcement Prediction: Hour and minute when the winner (Birdman) was mentioned on Twitter most frequently
3) Location: A list of which states were the most active in tweeting about #Oscars2015 (rank ordered from most active to least)

I solved the challenge using the python file that can be found in this repository.

The project has mainly four main parts:

Part 1: Preamble

The goal of this part is to assemble all important modules (from outside the code) that can be helpful when solving the three challenges. The library CSV was imported to facilitate manipulations of the file od data given in the CSV format.

In addition, I created a function called 'ColCall(col)'; this function will help to get data from any entire column of the file (oscars_tweets.csv) under the form (datatype) of a list.

Part 2: Challenge 1 -- Popularity rank

This part deals with the 'Popularity rank.' I mainly used the 'Tweets' column, accessed by using the previous function 'ColCall(col)' where col=2.

Furthermore, I created another function called 'FindAppearance(Film)' that loops over the whole column of Tweets by counting the number of each film founded. Here, I had to particularly loop some strings like: 'ic' (standing for picture), 'irdman' (standing for Birdman), 'gnorance', 'ertue' (both standing for the other name of the film Birdman 'The unexpected vertue of ignorance'). This approach made the looping more accurate by avoiding some mismatch between the best picture nominations' statistics and other nominations (because there were films such as 'Selma' with diverse nominations, other than best picture nomination).

Part 3: Challenge 2 -- Winner announcement prediction

The code here is mainly about the winner of the best picture, Birdman (or The Unexpected Vertue of Ignorance).
Three main procedures were used in this part:

1. Firstly, I looped in the Tweets to find mentions about Birdman (or The unexpected virtue of ignorance).

2. Secondly, I looked for the index of each tweet containing any information about Birdman (the winner). Then using the found index (from the tweet), I associated each Birdman's tweet with the exact time the when the user tweeted. Here, I stored all the times (obtained by using indexes from 'Tweets') when Birdman was mentioned in a list called 'store1'.

3. Once the time correspondence is founded, I counted the occurrence of each value of time (reduced to hours and minutes, without seconds and fractions) in the list 'store1'. The time with most occurrences is the time with most tweets.

Part 4: Challenge 3 -- Location [States that tweeted the most]

Here, I used a dictionary (called 'states') that stores all the US States and their abbreviations as keys. Every key stores in its list possible strings that can be written in a tweet (post) that refers to a specific states; for example, for the state of California, we have the key 'CA' and the list ['California', 'cali', 'CA']. The dictionary 'states' was then used in a for loop to count how many times the name of a state was mentioned in a tweet. The looping here is done in the column of 'Users location' (see data oscars_tweets.csv), turned to a list by using the initial function ColCall(col). 
