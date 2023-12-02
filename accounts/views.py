from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             try:
#                 user_group = Group.objects.get(name="Basic")
#             except Group.DoesNotExist:
#                 user_group = Group(name="Basic")
#                 user_group.save()
#                 user_group.permissions.set([Permission.objects.get(codename=c) for c in ["add_user", "change_user", "view_user", "add_list", "change_list", "delete_list", "view_list", "view_movie", "add_review", "change_review", "delete_review", "view_review",]])
#             user.groups.add(user_group)
#             return HttpResponseRedirect(reverse('login'))
#     else:
#         form = UserCreationForm()

#     context = {'form': form}
#     return render(request, 'accounts/signup.html', context)