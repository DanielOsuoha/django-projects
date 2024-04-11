from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import item,todo
from .forms import CreateList
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request, id):
    show = todo.objects.get(id=id)
    if show in request.user.all():
        # show = todo.objects.all()    
        return HttpResponse("<h1>TodoLists on my DB<hr> %s </h1>" % show.title)
        # context = {}
        # return render(request, 'main/base.html',context)
    else:
        return redirect('main/view')
def home(request):
  # show = todo.objects.get(id=id)
    show = todo.objects.all()
    l = []
    for i in show:
        # ls = i.item_set.all
        l.append(i)    
    # return HttpResponse("<h1>New Tech app again<br>TodoLists on my DB<hr> %s </h1>" % show.title)
    context = {
        # 'object':show,
        'object':l
        }
    return render(request, 'main/home.html',context)

def handleitem(request):
    obj = todo.objects.all()
    if request.method == 'POST':
        if 'clear' in request.POST:
           todo.objects.all().delete()
        #for loop to loop through the objects to get the valid titles
        for i in obj:
            if request.POST.get(str(i.id)):
                title = request.POST.get(str(i.id))
                text = request.POST['text'+str(i.id)]
                do = todo.objects.get(title=title)
                if request.POST.get('add') and len(text) >= 2:
                    do.item_set.create(text=text, complete=False)
                    do.save()
                
                if request.POST.get('rot'+ str(i.id)) == 'Rotate':
                    item = do.item_set.first()
                    item.delete()
                    item.save()
               
                print('in save', do)
                for item in do.item_set.all():
                    if request.POST.get('save'):
                        print(item.id, request.POST.get('c'+str(item.id)), "**")
                        if request.POST.get('c' + str(item.id)) == 'checked':
                            item.complete = True
                        else:
                            item.complete = False 
                        item.save()
                    if request.POST.get('del'+str(item.id)) == 'Delete':
                        item.delete()

                        
                do.save()
                
    return home(request)
            
            
@login_required    
def create(request):
    # You can use response.user to get the particular user you are dealing with and check if they have been authenticated
    # For templates you can use {% if user.is_authenticated %} and wrap around the block content in the base template
    
    if request.method == 'POST':
        form = CreateList(request.POST)
        if form.is_valid():
            ti = form.cleaned_data['title']
            # t = todo(title=ti)
            # request.user.todo.add(t)
            t = todo(title=ti, user=request.user)
            t.save()
            request.user.todo.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateList()
    context = {'form':form}
    return render(request, 'main/crudops.html',context)

@login_required
def view(request):
    user = request.user
    print(user.todo.all)
    context = {
        'user':user
    }
    return render(request, 'main/view.html', context)