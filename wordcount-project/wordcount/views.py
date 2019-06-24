from django.http import HttpResponse
from django.shortcuts import render

# function for the home page, to be used in the url path for the home page when
# the user requests the home page:
def homepage(request):
    # what is sent back to the user: the html for the homepage
    return render(request, 'home.html')

def count(request):
    # this gets the text that is entered by the user:
    fulltext = request.GET.get('fulltext')

    wordlist = fulltext.split()
    # count the number of times a word appears in the text:
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # count and increase:
            worddictionary[word] += 1
        else:
            # if not yet in dictionary, then add word to dictionary:
            worddictionary[word] = 1

        sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    # this sends the text to the count page to be shown
    # this also includes the counter of the separate words
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':sortedwords})
