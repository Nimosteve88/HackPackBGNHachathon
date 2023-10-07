from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('Pronouncequiz.html')
  return HttpResponse(template.render())

def homepage(request):
  template = loader.get_template('homepage.html')
  return HttpResponse(template.render())

def chatbot(request):
  template = loader.get_template('chatbox.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def pronouncequiz(request):
  template = loader.get_template('Pronouncequiz.html')
  return HttpResponse(template.render())