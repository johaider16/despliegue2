from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProfesorForm
from .models import Profesor
from django.http import HttpResponse
# Create your views here.

def base (request):
    return render(request,'base.html')
def index (request):
    return render(request,'paginas/index.html')
def estudiante(request):
    return render(request, 'paginas/estudiantes.html')

def gestionar(request):
    lista = Profesor.objects.all()

    return render(request,'paginas/gestionar.html', {'lista': lista})

def horarios (request):
    return render(request,'paginas/horarios.html')
def portafolio (request):
    return render(request,'paginas/portafolio.html')

def form_pro(request):
    data= {
        'form': ProfesorForm()
    }
    if request.method == 'POST':
        form_pro = ProfesorForm(data=request.POST)
        if form_pro.is_valid():
            form_pro.save()
            return redirect('gestionar')
    return render(request, 'form_pro.html', data)

def modificar(request, id_profe):
    profe= get_object_or_404(Profesor, id_profe=id_profe)
    data= {
        'form': ProfesorForm(instance=profe) 
    }
    if request.method =='POST':
        formu= ProfesorForm(data=request.POST, instance=profe)
        if formu.is_valid():
            formu.save()
            return redirect('gestionar')
    return render(request, 'modificar.html', data)

def eliminar(request,id_profe):
    elim=get_object_or_404(Profesor,id_profe=id_profe)
    elim.delete()
    return redirect(to='gestionar')