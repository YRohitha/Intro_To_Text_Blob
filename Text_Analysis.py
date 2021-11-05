from textblob
import TextBlob

text = TextBlob(‘she is a good cook’)
print(text.sentiment)
'''
Now
let’ s write another chunk of code where we will define a
function that calculates the subjectivity and the polarity and gives an output based on the threshold that we’ ll choose.
'''

def sentiment_analysis(tweet):
 def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

 #Create a function to get the polarity
 def getPolarity(text):
   return TextBlob(text).sentiment.polarity

 #Create two new columns ‘Subjectivity’ & ‘Polarity’
 tweet[‘TextBlob_Subjectivity’] =    tweet[‘tweet’].apply(getSubjectivity)
 tweet [‘TextBlob_Polarity’] = tweet[‘tweet’].apply(getPolarity)
 def getAnalysis(score):
  if score < 0:
    return ‘Negative’
  elif score == 0:
    return ‘Neutral’
  else:
    return ‘Positive’
 tweet [‘TextBlob_Analysis’] = tweet  [‘TextBlob_Polarity’].apply(getAnalysis )
return tweet
