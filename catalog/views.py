from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"{name}, ({email}) says: {subject}\n{message}")
    return render(request, 'catalog/contacts.html')
