
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from directs.models import Message
from django.contrib.auth.models import User
from authy.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator
from . import emotion
from django.http import JsonResponse , HttpResponse

@login_required
def inbox(request):
    user = request.user
    messages = Message.get_message(user=request.user)
    active_direct = None
    directs = None
    profile = get_object_or_404(Profile, user=user)

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, reciepient=message['user'])
        directs.update(is_read=True)

        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0
    context = {
        'directs':directs,
        'messages': messages,
        'active_direct': active_direct,
        'profile': profile,
    }
    return render(request, 'directs/direct.html', context)

@login_required
def Directs(request, username):
    user  = request.user
    messages = Message.get_message(user=user)
    active_direct = username
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    directs.update(is_read=True)
    to_user = User.objects.get(username=username)
    e_directs = Message.objects.filter(user=to_user,sender__username=username).order_by('-id')[:5]
   
    if not e_directs:
        e_direct=0
    else:
        bod_string=''
        for dirt in e_directs:
            bod_string = bod_string +' '+ str(dirt.body)

        e_direct = emotion.text_to_emotion(str(bod_string))

    for message in messages:
            if message['user'].username == username:
                message['unread'] = 0
    context = {
        'user':username,
        'to_user':to_user,
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
        'e_direct':e_direct,
    }
    return render(request, 'directs/direct.html', context)

def SendDirect(request):
    from_user = request.user
    to_user_username = request.POST['to_user']
    body = request.POST['body']
    to_user = User.objects.get(username=to_user_username)
    Message.sender_message(from_user, to_user, body)
    return HttpResponse('message sent')



def UserSearch(request):
    query = request.GET.get('q')
    context = {}
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        # Paginator
        paginator = Paginator(users, 8)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)

        context = {
            'users': users_paginator,
            }

    return render(request, 'directs/search.html', context)

def NewConversation(request, username):
    from_user = request.user
    body = ''
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('search-users')
    if from_user != to_user:
        Message.sender_message(from_user, to_user, body)
    return redirect('message')

@login_required
def getMessages(request, username):
    user  = request.user
    directs = Message.objects.filter(user=user, reciepient__username=username)  
    return JsonResponse({"directs":list(directs.values())})