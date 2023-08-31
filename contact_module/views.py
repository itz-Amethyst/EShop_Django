from django.shortcuts import render , redirect
from .forms import ContactUsForm , ContactUsModelForm
from django.urls import reverse

from .models import ContactUs


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
        # contact_form = ContactUsModelForm(request.POST)

        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact = ContactUs(
                title = contact_form.cleaned_data.get('title'),
                full_name = contact_form.cleaned_data.get('full_name'),
                email = contact_form.cleaned_data.get('email'),
                message = contact_form.cleaned_data.get('message'),
            )

            contact.save()
            return redirect('home_page')
    else:
        contact_form = ContactUsForm()
        # contact_form = ContactUsModelForm()

    return render(request, "contact_module/contact-us.html", {
        'contact_form': contact_form
    })