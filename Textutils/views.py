from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index2.html")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    capitalize= request.POST.get('capitalize', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')




    operations = []

    if removepunc == "on":
        operations.append('removepunc')

    if capitalize == "on":
        operations.append('capitalize')

    if newlineremover == "on":
        operations.append('newlineremover')

    if extraspaceremover == "on":
        operations.append('extraspaceremover')

    if charcount == "on":
        operations.append('charcount')
    analyzed = djtext

    if removepunc!="on" and capitalize!="on" and newlineremover != "on"and extraspaceremover != "on" and charcount != "on":
        return render(request,"index3.html")

    for op in operations:
        if op == 'removepunc':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = "".join(char for char in analyzed if char not in punctuations)

        elif op == 'capitalize':
            analyzed = analyzed.upper()

        elif op == 'newlineremover':
            analyzed = analyzed.replace("\n", "")

        elif op == 'extraspaceremover':
            analyzed = " ".join(analyzed.split())

        elif op == 'charcount':
            length = len(analyzed)
            analyzed += f'\nThe number of characters in the text is {length}'

    # Prepare the parameters for rendering
    params = {'purpose': 'Operations Applied', 'analyzed_text': analyzed}
    return render(request, "analyze.html", params)



def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")


