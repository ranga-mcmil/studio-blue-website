from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            # messages.success(request, "Mail Sent")
            return redirect('portfolio:home')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'portfolio/home.html', context)
