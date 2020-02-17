from django.shortcuts import render , redirect
from .models import PetShop
from .forms import PetForm
# Create your views here.
def pets_list(request):
    list = PetShop.objects.all()
    list = [x for x in list if x.available]
    context = {
        "pet":list
    }
    return render(request, 'list.html', context)


def pets_detail(request, pet_id):
    context = {
        "pet": PetShop.objects.get(id=pet_id)
    }
    return render(request, 'detail.html', context)


def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request, pet_id):
        pet = PetShop.objects.get(id = pet_id)
        form = PetForm(instance=pet)
        if request.method == "POST":
            form = PetForm(request.POST,request.FILES,instance=pet)
            if form.is_valid:
                form.save()
                return redirect('pet-list')
        context = {
            "pet" : pet,
            "form":form,
        }
        return render(request,'update.html',context)

def pet_delete(request, pet_id):
        PetShop.objects.get(id =pet_id).delete()
        return redirect('pet-list')
