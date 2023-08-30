from django.shortcuts import render , redirect
from .forms import ContactUsForm
from django.urls import reverse
# Create your views here.

def contact_us_page(request):
    # if request.method == 'POST':
    #     entered_email = request.POST['email']
    #     if entered_email == '':
    #         return render(request, 'contact_module/contact-us.html',{
    #             'has_error': True
    #         })
    #     print(request.POST)
    #     return redirect(reverse('home_page'))

    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            return redirect('home_page')
    else:
        contact_form = ContactUsForm()

    return render(request, "contact_module/contact-us.html", {
        'contact_form': contact_form
    })