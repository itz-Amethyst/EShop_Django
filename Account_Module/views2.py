# from django.shortcuts import render , redirect
# from django.views import View
# from django.views.generic import CreateView
#
# from Account_Module.forms import RegisterModelForm
# from Account_Module.models import User
#
#
# # Create your views here.
#
# class RegisterView(CreateView):
#    template_name = 'Account_Module/Register.html'
#    model = User
#    form_class = RegisterModelForm
#    success_url = '/'
#
#    def post(self, request, *args, **kwargs):
#       register_form = RegisterModelForm(request.POST)
#       if register_form.is_valid():
#          print(register_form.cleaned_data)
#
#       return render(request, 'Account_Module/Register.html', context = {
#          register_form
#       })
#
#    # def post(self, request, *args, **kwargs):
#    #
#    #      pass
#    # def get( self, request, *args, **kwargs ):
#    #     register_form = RegisterModelForm()
#    #     context = {
#    #         'register_form': register_form
#    #     }
#    #
#    #     return render(request,'Account_Module/Register.html',context)