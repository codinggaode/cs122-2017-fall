def countWords(document):
    #-- start code here ---
    rawCharList = list(document)
    CharList = []
    wordList = []
    for char in rawCharList:
        if char.isalpha():
            CharList.append(char.lower())
        elif char == ' ' or char == '\n':
            if (len(CharList) > 0 and CharList[-1] != ' '):
                CharList.append(' ')

    wordList = ''.join(CharList).split(' ')
    wordCountDic = {}
    for word in wordList:
        if word in wordCountDic.keys():
            wordCountDic[word] += 1
        else:
            if word != '':
                wordCountDic[word] = 1
    
    return wordCountDic



document = '''
He will be the president of the company; right now
he is a vice president. 
But he ..... himself,  is no sure of it...
(Later he will see the imporance of these.)
'''
print(countWords(document))
#{'he': 4, 'will': 2, 'be': 1, 'the': 3, 'president': 2,
#'of': 3, 'company': 1, 'right': 1, 'now': 1, 'is': 2, 'a': 1,
#'vice': 1, 'but': 1, 'himself': 1, 'no': 1, 'sure': 1, 'it': 1, 'later': 1,
#'see': 1, 'imporance': 1, 'these': 1}






