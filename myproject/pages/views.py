from django.shortcuts import render, redirect
from .models import FormModel
from .forms import SimpleForm, ModelBasedForm   

def form_view(request):
    # -------- Way1---------
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        FormModel.objects.create(name=name, email=email, password=password)
        return redirect('form')
    return render(request, 'pages/form.html')
    """

    # -------- Way2--------
    """
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            FormModel.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            return redirect('form')
    else:
        form = SimpleForm()
    return render(request, 'pages/form.html', {'form': form})
    """

    # -------- Way3 --------
    if request.method == "POST":
        form = ModelBasedForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('form')
    else:
        form = ModelBasedForm()
    return render(request, 'pages/form.html', {'form': form})