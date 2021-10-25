from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
# from django.db.models import F
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if single_hero is None:
        return Http404
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        single_hero.name = name
        single_hero.alter_ego = alter_ego
        single_hero.primary_ability = primary
        single_hero.secondary_ability = secondary
        single_hero.catch_phrase = catchphrase
        single_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
         context = {
             'hero_id': hero_id
         }
         return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    if single_hero is None:
        return Http404
    single_hero.delete()
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)
    

