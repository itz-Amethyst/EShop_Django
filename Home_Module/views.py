from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'Home_Module/index.html')

def contact_page(request):
    return render(request, 'Home_Module/contact-us.html')

def site_header_component(request):
    return render(request, 'shared/components/header.html', {
        'link': 'آموزش پایتون'
    })

def site_footer_component(request):
    return render(request, 'shared/components/footer.html', {})