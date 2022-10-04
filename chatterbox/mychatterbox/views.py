import json

from django.shortcuts import render, redirect
from .models import Friend, Profile, ChatMessage
from .forms import ChatMessageForm
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    user = request.user.profile
    friends = user.friends.all()
    lastest_msgs = ChatMessage.objects.filter(msg_receiver=user)
    lastest_msgs = lastest_msgs.values('msg_sender_id', 'body','received_at').annotate(count=Count('msg_sender_id',distinct=True)).order_by('-received_at')

    last_messages= []
    for friend in friends:
        for msg in lastest_msgs:
            if msg['msg_sender_id'] == friend.profile.id:
                last_messages.append({'friend':friend.profile.name,'body':msg['body']})
                break

    print("last_messages:"+ str(last_messages))
    context={"user":user, "friends": friends, "last_messages": last_messages}
    return render(request, "mychatterbox/index.html", context)


def detail(request, pk):
    friend =Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    received_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    received_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message= form.save(commit =False)
            chat_message.msg_sender=user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect(detail, pk= friend.profile.id)

    context={"friend":friend, "form":form, "user":user, "profile":profile, "chats":chats, "num": received_chats.count()}
    return render(request, 'mychatterbox/detail.html', context)


def sentMessages(request, pk):
    user =request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen= False)

    # print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)


def receivedMessages(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    arr=[]
    chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
        # print(arr)
    return JsonResponse(arr, safe=False)


def chatNotification(request):
    user = request.user.profile
    friends = user.friends.all()
    arr=[]
    for friend in friends:
        chat = ChatMessage.objects.filter(msg_sender__id=friend.profile.id, msg_receiver=user, seen=False)
        arr.append(chat.count())
    return JsonResponse(arr, safe=False)


def readLastMsg(request):
    user = request.user.profile
    friends = Friend.objects.all()
    lastest_msgs = ChatMessage.objects.filter(msg_receiver=user)
    lastest_msgs = lastest_msgs.values('msg_sender_id', 'body', 'received_at').annotate(count=Count('msg_sender_id', distinct=True)).order_by('-received_at')
    last_messages=[]
    # print(lastest_msgs)
    for friend in friends:
        for msg in lastest_msgs:
            if msg['msg_sender_id'] == friend.profile.id:
                last_messages.append({'friend': friend.profile.name, 'body': msg['body']})
                break
    print("last_messages:" + str(last_messages))
    return JsonResponse(last_messages, safe=False)


def login_user(request):
    if str(request.user) != 'AnonymousUser':     #request.user.username
        print("user "+ str(request.user) + " logged in.")
        return redirect(index)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username:", username)
        user = authenticate(request, username=username, password=password)
        print("user:", user)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.success(request, "Invalid login. Try again.")
            return redirect('login')
    else:
        return render(request, 'mychatterbox/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logout successfully.")
    return redirect('login')


def register_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            user = authenticate(request, username=username, password=password)
            profile= Profile.objects.create(user=user, name=firstname + " " + lastname, pic="")
            messages.success(request, "Signed Up successfully.")
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()

    return render(request, 'mychatterbox/register.html', {"form":form})


def change_pp(request):

    print("image: ", image)
    return redirect('index')