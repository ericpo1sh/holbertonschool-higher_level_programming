def multiple_returns(sentence):
    if sentence:
        return len(sentence), sentence[0]
    else:
        first = None
        return len(sentence), first
