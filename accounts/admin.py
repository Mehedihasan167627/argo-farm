from django.contrib import admin
from .models import* 
admin.site.register(Account_subtype)
admin.site.register(Account_subcode)
admin.site.register(Opening_balance)
admin.site.register(Account_transaction)
admin.site.register(Account_voucher)
admin.site.register(Voucher_type)
admin.site.register(Financial_year)
admin.site.register(Account_type)


@admin.register(Chart_Of_Account)
class AdminChartOfAccount(admin.ModelAdmin):
    list_display=["account_name","account_types","head_level","parent_id","id"]