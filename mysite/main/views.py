from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',)


def private_leasing(request):
    return render(request=request,
                  template_name='main/private_leasing.html',)
def business_leasing(request):
    return render(request=request,
                  template_name='main/business_leasing.html',)

                  
