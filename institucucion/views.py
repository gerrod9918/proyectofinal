from django.shortcuts import render
from institucucion.forms import FormPub
from django.shortcuts import redirect



def nueva_materia(request):
    if request.method == "POST":
        f = FormPub(request.POST)
        if f.is_valid():
            p = f.save(commit=False)
            p.save()
            return redirect('nueva_materia')
    else:
        f = FormPub()
    return render(request, 'institucucion/nueva_materia.html', {'formulario': f})
