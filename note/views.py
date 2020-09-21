from django.shortcuts import render, redirect, get_object_or_404
from core.models import Note, User
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import Http404
import datetime
from .forms import NoteForm
# Create your views here.

@login_required



def home(request):
    user_email = request.user.get_username()
    user = User.objects.get(email=user_email)
    username = user.username

    if request.method=='POST':

        if request.POST.get('important')=='Show only important':
            print('aaa')
            note = Note.objects.filter(users__id=user.id).filter(important=True).order_by('-date')
            return render(request, 'note.html', {'note': note, 'username': username, 'filtered': True})
        else:
            pass


    note = Note.objects.filter(users__id=user.id).order_by('-date')
    return render(request, 'note.html',{'note': note,'username': username})


@login_required
def post_func(request):
    user_email = request.user.get_username()
    user = User.objects.get(email = user_email)
    username = user.username
    important = request.POST.get('important')

    if request.method =='POST':
        note = Note.objects.create(
            memo = request.POST.get('memo'),
            images=request.FILES.get('images'),
            users = user,
            important = important
        )
        note.save()
        return redirect('note')

    return render(request, 'post.html',{'username': username, 'important': important})

@login_required
def deletefunc(request, id):
    user_email = request.user.get_username()
    user = User.objects.get(email = user_email)
    username = user.username

    user_memo = Note.objects.get(id = id)

    if user_memo.users!= user:
        raise Http404('this memo does not exist')

    if request.method== 'POST':
        user_memo.delete()
        return redirect('note')

    return render(request,'delete.html', {'post':user_memo,'username': username})


def edit(request, id):
    user_email = request.user.get_username()
    user = User.objects.get(email=user_email)
    user_memo = Note.objects.get(id=id)
    username = user.username

    memo = get_object_or_404(Note, id =id)

    if user_memo.users != user:
        raise Http404('this memo does not exist')

    if request.method== 'POST':
        form = NoteForm(request.POST, instance= memo)
        if form.is_valid():
            note = form.save()
            note.save()
            return redirect('note')
    else:
        form= NoteForm(instance=memo)

    return render(request,'edit.html', {'form': form, 'username': username})







