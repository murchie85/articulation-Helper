from tools import *
quoteList = 'SentenceDict.txt'
print('\033c')


welcome="""
 --------------------------------------------------------
|                                                       |
|           📚 Articulation Center 📚                   |
|                                                       |
 --------------------------------------------------------


 [1] View Random Sentence
 [2] Add to Expression Dict
 [3] View useful words
 [x] Exit

"""




print(welcome)
choice = ''

# -----main loop
while(choice.upper()!='X'):
    choice = str(input('Select an Option: '))
    
    if(choice=='1'):
        print('\033c')
        print('Getting random quote: ')
        randomQuote(quoteList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)

    if(choice=='2'):
        saveQuote(quoteList)
        input('\n\n Press any key to continue...')
        print('\033c')
        print(welcome)