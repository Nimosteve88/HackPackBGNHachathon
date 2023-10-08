from django.http import HttpResponse
from django.template import loader
from .models import LoginDetails
from django.shortcuts import redirect, render


def homepage(request):
  template = loader.get_template('homepage.html')
  return render(request, 'homepage.html')

def chatbot(request):
  template = loader.get_template('chatbox.html')
  return render(request, 'chatbox.html')

def login(request):
  if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('new_password')

        # Save the data to the LoginDetails model
        login_details = LoginDetails(
            FirstName=first_name,
            LastName=last_name,
            Email=email,
            Password=password  
        )
        login_details.save()
        return redirect('homepage')
  template = loader.get_template('login.html')
  return render(request, 'login.html')

def pronouncequiz(request):
  template = loader.get_template('Pronouncequiz.html')
  return render(request, 'Pronouncequiz.html')


def newsfeed(request):
    import requests
    api_key = 'b2c8adec9244439385335aee2daf292e'
    url = f'https://newsapi.org/v2/top-headlines?country=ng&apiKey={api_key}'
    
    response = requests.get(url)
    articles = []
    
    if response.status_code == 200:
        data = response.json()
        if 'articles' in data:
            articles = data['articles']
    
    context = {
        'articles': articles
    }
    
    return render(request, 'naijanews.html', context)



# {% load static %}
# href="{% static 'homepage.css' %}"
# href="{% url 'chatbot' %}"
