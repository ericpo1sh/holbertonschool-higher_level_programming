def multiple_returns(sentence):
    if sentence:
        newtuple = (len(sentence), sentence[0])
    else:
        newtuple = (0, None)
    return newtuple
