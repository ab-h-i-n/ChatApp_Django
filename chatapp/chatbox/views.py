# views.py
from django.shortcuts import render, redirect
from .models import ChatInfo
from .forms import ChatForm
from django.utils import timezone

def HomePage(request):
    form = ChatForm()  # Initialize form here

    if not request.user.is_authenticated:
        return redirect("login-user")

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            username = request.user.username
            message = form.cleaned_data['message']
            current_time = timezone.now()
            ChatInfo.objects.create(username=username, message=message, timestamp=current_time)

    chat_messages = ChatInfo.objects.all()
    return render(request, "HomePage.html", {'form': form, 'chat_messages': chat_messages})
