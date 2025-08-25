from django.shortcuts import render,redirect
from django.views import View
from .models import Emp
from .forms import addempForm
 



class home(View):
  def get(self,request):
    emp_data = Emp.objects.all()
    return render(request, 'core/home.html',{'empdata': emp_data})

class add_emp(View):
    def get(self, request):
        fm = addempForm()   
        return render(request, 'core/add_emp.html', {'form': fm})

    def post(self, request):   
        fm = addempForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add_emp.html', {'form': fm})


