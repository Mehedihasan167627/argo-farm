from django.shortcuts import render
from django.views import View 


class LoginView(View):
    def get(self,request):
        return render(request,"accounts/login.html")
    
    
class RegisterView(View):
    def get(self,request):
        return render(request,"accounts/register.html")
    
    

class OpeningbalanceView(View):
    def get(self,request):
        return render(request,"accounts/openingbalance.html")

class FinancialYearView(View):
    def get(self,request):
        return render(request,"accounts/financialyear.html")        