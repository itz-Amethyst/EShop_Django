from django.shortcuts import render , redirect
from .forms import ContactUsForm , ContactUsModelForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse

from .models import ContactUs


# Create your views here.

class ContactUsView(FormView):
    model = ContactUs
    template_name = 'contact_module/contact-us.html'
    success_url = '/contact-us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def post( self, request ):
    #     contact_form = ContactUsModelForm(request.POST)
    #     if contact_form.is_valid():
    #
    #         contact_form.save()
    #         return redirect('home_page')
    #     return render(request, 'contact_module/contact-us.html',{
    #         'contact_form': contact_form
    #     })

class CreateProfileView(View):
    def get( self, request ):
        return render(request, 'contact_module/create-profile.html')

    def post( self, request ):
        print(request.FILES)
        return redirect('create_profile')


#? Function based view
# def contact_us_page(request):
#     #? Old Way
#     if request.method == "POST":
#         contact_form = ContactUsForm(request.POST)
#         if contact_form.is_valid():
#             print(contact_form.cleaned_data)
#             contact = ContactUs(
#                 title = contact_form.cleaned_data.get('title'),
#                 full_name = contact_form.cleaned_data.get('full_name'),
#                 email = contact_form.cleaned_data.get('email'),
#                 message = contact_form.cleaned_data.get('message'),
#             )
#
#             contact.save()
#             return redirect('home_page')
#     else:
#         contact_form = ContactUsForm()
#
#     return render(request, "contact_module/contact-us.html", {
#         'contact_form': contact_form
#     })