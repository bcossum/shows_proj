from django.shortcuts import render, redirect
from .models import show, network
import datetime

def home(request):
  return redirect('/shows')

def index(request):
  context = {
    'all_shows': show.objects.all(),
    'all_networks': network.objects.all()
  }
  return render(request, 'shows.html', context)

def add_show(request):
  return render(request, 'add_show.html')

def create_show(request):
  count = 0
  if request.method == 'POST':
    for networks in network.objects.all():
      if request.POST['network'] == networks.name:
        network_id = network.objects.get(name=request.POST['network'])
        count += 1
        break
    if count == 0:
      network.objects.create(name=request.POST['network'])
      network_id = network.objects.get(name=request.POST['network'])
    show.objects.create(
      title = request.POST['title'],
      release_date = request.POST['release_date'],
      desc = request.POST['desc'],
      networks = network_id,
      )
    show_redirect=show.objects.last()
    show_id=show_redirect.id  
  return redirect(f'/shows/{show_id}')
    
def view_show(request, show_id):
  context = {
    'show': show.objects.get(id=show_id)
  }
  return render(request, 'view_show.html', context)

def edit_show(request, show_id):
  count = 0
  if request.method == 'POST':
    show_edit = show.objects.get(id=show_id)
    for networks in network.objects.all():
      if request.POST['network'] == networks.name:
        network_id = network.objects.get(name=request.POST['network'])
        count += 1
        break
    if count == 0:
      network.objects.create(name=request.POST['network'])
      network_id = network.objects.get(name=request.POST['network'])
    show_edit.title = request.POST['title']
    show_edit.networks = network_id
    show_edit.release_date = request.POST['release_date']
    show_edit.desc = request.POST['desc']
    show_edit.save()
    return redirect(f'/shows/{show_id}')

  else:
    context = {
      'show': show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)
  
def delete(request, show_id):
  c = show.objects.get(id=show_id)
  c.delete()
  return redirect('/')
