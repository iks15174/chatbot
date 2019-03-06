from django.shortcuts import render
from django.http import JsonResponse
import os
import sys
sys.path.insert(0, 'C:/Users/iks15/PycharmProjects/chatbot/crawl')
#import crawl1

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

# Create your views here.
