from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView

# Create your views here.

from django.http import HttpResponse
from .forms import RegisterForm, AuthorForm, ContactForm
from .models import Publisher, Author, Articles


# Create your views here.
import os
import logging
from django.contrib.auth import authenticate
import json
import sys, os, time
from .forms import NameForm



logger = logging.getLogger('bread_logger')


def index(request):
    questions = models.Question.objects.all()
    context = {
        'question': questions,
    }
    return render(request, 'index.html', context)


@csrf_exempt
def contact(request):
    # message = ""
    # context = {
    #     '1':1212,
    # }
    #
    # objs = models.Question.objects.all()
    # for i in objs:
    #     logger.info('QUESTION:' + i.question_text)
    # if request.method == 'POST':
    #
    #     context = 'OK'
    #     # username = request.POST.get('username', '')
    #     # subject = request.POST.get('subject', '')
    #     # logger.info('USERNAME:' + username)
    #     # logger.info('SUBJECT:' + subject)
    #
    #     user = authenticate(username='bichkhe', password='Nguyenbinh1')
    #     if user is not None:
    #         data = {}
    #         data['result'] = 'you made a request1'
    #     # A backend authenticated the credentials
    #         logger.debug('Authenticate successfully!')
    #         # return render(request, 'sigup.html', context)
    #         return HttpResponse(json.dumps(data), content_type="application/json")
    #     else:
    #         context = 'NOK'
    #     # No backend authenticated the credentials
    #         return HttpResponse(content=context)

    context = {
        'song_name': 'Hello',
        'message': '1234',
    }

    return render(request, 'contact.html', context)


def register(request):
    if request.method == 'POST':
        response = {
            'username': request.POST['username'],
            'password': request.POST['password'],
            'email':    request.POST['email'],
        }
        return render(request, 'register_success.html', response)

    comment = AuthorForm()
    return render(request, 'register.html', {'form': comment})

class PublisherList(ListView):
    model = Publisher
    fields = ['name', 'address']
    template_name = 'sigin.html'
    context_object_name = 'my_favorite_publishers'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(PublisherList, self).form_valid(form)

class ContactView(FormView):
    template_name = 'sigin.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        logger.info("form_valid()")
        return super(ContactView, self).form_valid(form)

class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'age']
    template_name = 'sigin.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AuthorCreate, self).form_valid(form)


def news(request):
    articles = Articles.objects.all()
    tvars ={
        'articles': articles,
    }
    return render(request,'news.html', tvars)