import random 

def openFile(path):
    import ast

    # file check
    c = open(path)
    size = len(c.read())
    
    if(size>0):

        with open(path) as f:
            data = ast.literal_eval(f.read())
    else:
        print('**File empty** returning array')
        data = []
        

    return(data)

def saveData(data,dataPath):
    try:
        f = open(dataPath,'w')
        f.write(str(data))
        f.close()
    except:
        print('***Error** problem writing data')
        print(str(data))


def randomQuote(quoteList):
    data = openFile(quoteList)
    rq = random.choice(data)
    print(' ')
    print(' ')
    print('Type: ' + str(rq['type']))
    print('------------------------------------------')
    print(' ')
    print(' ')
    print('\n\n\n\n\n\n')
    print(rq['text'].upper())
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('------------------------------------------')



def getWordList(wordList):
    data = openFile(wordList)
    spaceMax = 20
    for item in data:
        # add dynamic space
        tags = str(item['tags'])
        diff = spaceMax-len(tags)
        for x in range(diff):
            tags += ' '
        print(tags + ': ' + str(item['text']))
    print('\n\n')

def getQuoteList(quoteList):
    data = openFile(quoteList)
    spaceMax = 20
    for item in data:
        # add dynamic space
        tags = str(item['tags'])
        diff = spaceMax-len(tags)
        for x in range(diff):
            tags += ' '

        print(tags + ': ' + str(item['text']))
    print('\n\n')



def saveQuote(quoteList):
    data = openFile(quoteList)

    tags  = str(input('What tags are there?: '))
    if(len(tags)==0): tags = 'general'
    text  = input('What is the text passage?: \n')

    quote = {'text': text,'tags':tags}
    data.append(quote)

    saveData(data,quoteList)

    print('Data saved')



def saveWord(wordList):
    data = openFile(wordList)

    tags  = str(input('What tags are there? \n(seperate with comma): '))
    if(len(tags)==0): tags = 'general'
    text  = input('What is the word(s)?: \n')

    word = {'text': text,'tags':tags}
    data.append(word)

    saveData(data,wordList)

    print('Data saved')

