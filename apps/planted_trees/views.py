from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.planted_trees.forms import MultiplePlantedTreeForm, PlantedTreeForm
from apps.planted_trees.models import PlantedTree
from apps.trees.models import Tree

from apps.accounts.models import User, Account


@login_required
def plant_tree(request):
    user = Account.objects.get(id=request.user.id)
    user = User.objects.get(user=user)

    if request.method == 'POST':
        form = PlantedTreeForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            print(form.errors)
    else:
        form = PlantedTreeForm(user=user)

    return render(request, 'plant_tree.html', {'form': form})


@login_required
def plant_trees(request):
    if request.method == 'POST':
        form = MultiplePlantedTreeForm(request.POST)
        if form.is_valid():
            trees = form.cleaned_data['trees']
            for tree_id, age, latitude, longitude in trees:
                user = Account.objects.get(id=request.user.id)
                user = User.objects.get(user=user)
                tree = Tree.objects.get(id=tree_id)
                PlantedTree.objects.create(
                    tree=tree,
                    user=user,
                    age=age,
                    latitude=latitude,
                    longitude=longitude
                )
            return redirect('success_page')
    else:
        form = MultiplePlantedTreeForm()
    return render(request, 'plant_trees.html', {'form': form})


def user_planted_trees(request):
    user = Account.objects.get(id=request.user.id)
    user = User.objects.get(user=user)
    planted_trees = PlantedTree.objects.filter(user=user)
    return render(request, 'user_planted_trees.html', {'planted_trees': planted_trees})


def user_planted_trees_admin(request):
    user = Account.objects.get(id=request.user.id)
    users = User.objects.filter(account=user)

    planted_trees = list()

    for user_actual in users:
        planted_trees.extend(PlantedTree.objects.filter(user=user_actual))

    return render(request, 'user_planted_trees.html', {'planted_trees': planted_trees})


def success_page(request):
    return render(request, 'success.html')
