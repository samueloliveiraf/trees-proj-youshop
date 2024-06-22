from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import AccountCreationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Account, User


def register_account(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AccountCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def users_list(request):
    user = Account.objects.get(id=request.user.id)
    users = User.objects.filter(account=user)

    users_all = list()

    for user_actual in users:
        user = Account.objects.get(id=user_actual.user.id)
        users_all.append(user)

    return render(request, 'users_list.html', {'users': users_all})


@login_required
def toggle_user_status(request, user_id):
    user = Account.objects.get(id=user_id)

    if request.method == "POST":
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({'status': 'success', 'is_active': user.is_active})

    return JsonResponse({'status': 'failed'})
