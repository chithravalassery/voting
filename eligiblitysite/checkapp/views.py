from django.shortcuts import render
import datetime

def check(request):
    return render(request, 'index.html')

def cond(request):
    name = request.POST['name']
    dobStr = request.POST['dob']
    dob = dobStr.split('-')
    today = datetime.datetime.now().year
    age = today - int(dob[0])

    if age >= 18:
        result = "You are eligible to vote"
    else:
        result = "Sorry! You are not eligible"

    return render(request, 'index.html', {'Name': name, 'Age': age, 'Check': result})

  