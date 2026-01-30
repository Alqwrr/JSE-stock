POSITIVE_WORDS = {"growth", "profit", "rise", "strong", "increase", "gain","boost","increased","confidence","more","expansion","better","gold","powerful","stronger"}
NEGATIVE_WORDS = {"loss", "decline", "fall", "weak", "drop","decrease","challenges","problem","lawsuit","closure","tariff","weaker","downsize","layoff","bankruptcy"}

def score_headlines(headlines: list[str]) -> int:
    score = 0

    for headline in headlines:
        words = headline.lower().split()
        score += sum(word in POSITIVE_WORDS for word in words)
        score -= sum(word in NEGATIVE_WORDS for word in words)

    return score
