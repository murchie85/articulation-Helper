import random 

def openFile(path):
    import ast 
    with open(path) as f:
        data = ast.literal_eval(f.read())
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
    print('Tags: ' + str(rq['tags']))
    print(' ')
    print(' ')
    print(rq['text'])

def saveQuote(quoteList):
    data = openFile(quoteList)

    qtype = str(input('What type is it?: '))
    if(len(qtype)==0): qtype = 'general'
    tags  = str(input('What tags are there?: '))
    if(len(tags)==0): tags = 'general'
    text  = input('What is the text passage?')

    quote = {'type': qtype, 'text': text,'tags':tags}
    data.append(quote)

    saveData(data,quoteList)

    print('Data saved')

