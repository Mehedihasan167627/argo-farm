from django.shortcuts import render
from django.views import View 
from .models import*

class FinancialYearView(View):
    def get(self,request):
        queryset=Financial_year.objects.all()
        context={
            "obj_list":queryset
        }
        return render(request,"accounts/financial_year.html",context)
    
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
  
class ChartOfAccountView(View):
    def get(self,request):
        return render(request,"accounts/chart_of_account.html")

    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
    
class SubAccountView(View):
    def get(self,request):
        queryset=Account_subtype.objects.all()
        context={
            "obj_list":queryset
        }
        return render(request,"accounts/sub_account.html",context)
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class PredifiendAccountView(View):
    def get(self,request):
        queryset=predefine_account.objects.all()
        context={
            "obj_list":queryset
        }
        return render(request,"accounts/predefined_account.html",context)

    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class DebitVoucherView(View):
    def get(self,request):
        queryset=Account_voucher.objects.filter(voucher_type="Debit")
        context={
            "obj_list":queryset
        }
        return render(request,"accounts/debit_voucher.html",context)

    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class CrebitVoucherView(View):
    def get(self,request):
        queryset=Account_voucher.objects.filter(voucher_type="Credit")
        context={
            "obj_list":queryset
        }
        return render(request,"accounts/credit_voucher.html",context)
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class ContraView(View):
    def get(self,request):
      
        return render(request,"accounts/contra_voucher.html")
    def post(self,request):
        pass 


        
class JournalVoucherView(View):
    def get(self,request):
        return render(request,"accounts/journal_voucher.html")
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class BankReconcilationView(View):
    def get(self,request):
        return render(request,"accounts/bank_reconcilation.html")
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class OpeningBalanceView(View):
    def get(self,request):
        return render(request,"accounts/opening_balance.html")

    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 