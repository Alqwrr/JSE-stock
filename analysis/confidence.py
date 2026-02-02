import time

def sentiment_scorer(Sentiment):
    accumulator = 0
    if Sentiment < 0:
        if Sentiment < -2:
            accumulator += -10
        accumulator += -10
    elif Sentiment > 0:
        if Sentiment > 2:
            accumulator += 10
        accumulator += 10
    else:
        accumulator = 0
    return accumulator

def PCT_Scorer(weekly):
    accumulator = 0
    if weekly < -100:
        accumulator += -40
    elif weekly < -50:
        accumulator += -20
    elif weekly < 0:
        accumulator += -10
    if weekly > 100:
        accumulator += 40
    elif weekly > 50:
        accumulator += 20
    elif weekly > 0:
        accumulator += 10
    return accumulator 

def calculate_confidence_score(Sentiment1=0,sentiment2=0,weeklyPCT=0.00,cumuPCT=0.00):
    confidence_score = 0
    confidence_score += sentiment_scorer(Sentiment1)
    confidence_score += sentiment_scorer(sentiment2)
    confidence_score += 2 * PCT_Scorer(weeklyPCT)
    confidence_score += 0.5 * PCT_Scorer(cumuPCT)
    
    return confidence_score