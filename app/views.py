from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import random as r
import json
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'app/index.html')

def dados_graficos(request):
    if request.method == 'GET':
        list_time = []
        for i in range(21):
            list_time.append(i)
        head = request.headers.get('head')

        head = int(head)
        move_position = []
        typeprocesss = request.headers.get('type')
        typeprocesss = int(typeprocesss)
        list_position = [r.randint(1,200) for i in range(20)]
        if typeprocesss == 1: 
            list_position.insert(0,head)
            for i in list_position:
                value = i - head
                if value < -1: value = value * (-1)
                move_position.append(value)
                head = i
        if typeprocesss == 2:
            list_min = []
            list_max = []
            for i in list_position:
                if i < head:
                    list_min.append(i)

            for i in list_position:
                if i > head:
                    list_max.append(i)

            list_min = sorted(list_min, key=int, reverse=True)
            list_max = sorted(list_max)
            result = list_min + list_max
            result.insert(0,head)
            move_position = []
            for i in result:
                value = i - head
                if value < -1: value = value * (-1)
                move_position.append(value)
                head = i
            list_position = result
        if typeprocesss == 3:
            list_max = []
            list_min = []

            for i in list_position: 
                if i > head:
                    list_max.append(i)
                else:
                    list_min.append(i)

            list_max = sorted(list_max, key= int, reverse = True)
            list_min = sorted(list_min, key= int, reverse = True)
            result = list_max + list_min
            result.insert(0, head)
            for i in result:
                value = i - head
                if value < -1: value = value * (-1)
                move_position.append(value)
                head = i
            list_position = result
        return JsonResponse({'position': list_position,'time': list_time,'sum':sum(move_position)})
        
            
