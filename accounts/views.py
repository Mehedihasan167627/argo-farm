from django.shortcuts import render
from django.views import View 


class FinancialYearView(View):
    def get(self,request):
        return render(request,"accounts/financial_year.html")
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
        return render(request,"accounts/sub_account.html")
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class PredifiendAccountView(View):
    def get(self,request):
        return render(request,"accounts/predefined_account.html")
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class DebitVoucherView(View):
    def get(self,request):
        return render(request,"accounts/debit_voucher.html")
    def post(self,request):
        # get all post keys 
        # request.POST.get('')    
        pass 
class CrebitVoucherView(View):
    def get(self,request):
        return render(request,"accounts/credit_voucher.html")
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