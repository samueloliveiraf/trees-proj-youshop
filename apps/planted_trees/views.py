from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import JsonResponse

from apps.planted_trees.forms import PlantedTreeForm
from apps.planted_trees.models import PlantedTree

from apps.planted_trees.serializers import PlantedTreeSerializer
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_user_planted_trees(request, user_id):
    user = Account.objects.get(id=user_id)
    user = User.objects.get(user=user)
    planted_trees = PlantedTree.objects.filter(user=user)

    if not planted_trees:
        return JsonResponse({'not_found': 'Nenhuma planted_trees Encontrada.'}, status=404)

    serializer = PlantedTreeSerializer(planted_trees, many=True)
    return Response(serializer.data, status=200)
