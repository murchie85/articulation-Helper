from tools import *
quoteList = 'storage/SentenceDict.txt'
wordList  = 'storage/wordDict.txt'
print('\033c')


welcome="""
 --------------------------------------------------------
|                                                       |
|           📚 Articulation Center 📚                   |
|                                                       |
 --------------------------------------------------------


 [1] View List of Quotes
 [2] View useful words
 [3] Add to Expression Dict
 [4] Add to word bank
 [5] View a Random Quote
 [x] Exit

"""




print(welcome)
choice = ''

# -----main loop
while(choice.upper()!='X'):
    choice = str(input('Select an Option: '))
    
    if(choice=='1'):
        print('\033c')
        getQuoteList(quoteList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)
    
    if(choice=='2'):
        print('\033c')
        getWordList(wordList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)

    if(choice=='3'):
        saveQuote(quoteList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)

    if(choice=='4'):
        saveWord(wordList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)

    if(choice=='5'):
        print('\033c')
        randomQuote(quoteList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)