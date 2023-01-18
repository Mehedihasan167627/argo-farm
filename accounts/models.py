from django.db import models


class Account_type(models.Model):
    uuid                = models.CharField(max_length=50, null = True, blank = True, default='0')
    account_type_name = models.CharField(max_length=50, null = True, blank = True, default='0')

    def __str__(self):
        return self.account_type_name 
    class Meta:
        db_table = 'account_type'


class Chart_Of_Account(models.Model):
    reverse_code            = models.BigIntegerField( null = True, blank = True, default='0')
    uuid                    = models.CharField(max_length=50, null = True, blank = True, default='0')
    account_code            = models.TextField(max_length=50,  null = True, blank = True, default='0')
    account_name            = models.CharField(max_length=50, null = True, blank = True, default='0')
    
    head_level              = models.IntegerField(null = True, blank = True, default='0')
    parent_id               = models.IntegerField(null = True, blank = True, default='0')
    account_types           = models.ForeignKey(Account_type, on_delete=models.CASCADE)
    is_active               = models.SmallIntegerField(null = True, blank = True, default='1')
    is_cash_nature          = models.IntegerField(null = True, blank = True, default='0')
    is_bank_nature          = models.IntegerField(null = True, blank = True, default='0')
   
    is_budget               = models.SmallIntegerField(null = True, blank = True, default='0')
    is_depreciation         = models.SmallIntegerField(null = True, blank = True, default='0')
    depreciation_rate       = models.IntegerField( null = True, blank = True, default='0')
    is_subtype              = models.IntegerField( null = True, blank = True, default='0')
    subtype_id              = models.IntegerField( null = True, blank = True, default='0')
    is_stock                = models.IntegerField( null = True, blank = True, default='0')
    is_fixed_asset_schedule =  models.IntegerField(null = True, blank = True, default='0')
    note_no                 = models.TextField(max_length=50,null = True, blank = True, default='0')
    asset_code              = models.TextField(max_length=50, null = True, blank = True, default='0')
    dep_code                = models.TextField(max_length=50, null = True, blank = True, default='0')
    created_by              = models.SmallIntegerField( null = True, blank = True, default='39')
    created_date            = models.DateTimeField( null = True, blank = True)
    updated_by              = models.SmallIntegerField( null = True, blank = True, default='39')
    updated_date            = models.DateTimeField( null = True, blank = True)
    

    def __str__(self):
        return self.account_name

    class Meta:
        db_table = 'chart_of_account'



class Financial_year(models.Model):
    uuid                = models.CharField(max_length=50, null = True, blank = True, default='0')
    financial_year      = models.TextField(max_length=50, null = True, blank = True, default='0')
    start_date          = models.DateField(max_length=50)
    end_date            = models.DateField()
    status              = models.SmallIntegerField( null = True, blank = True, default='1')
    is_close            = models.SmallIntegerField(null = True, blank = True, default='0')

    def __str__(self):
        return self.financial_year

    class Meta:
        db_table = 'financial year'

class Account_subcode(models.Model):
    account_subtype         = models.TextField(null = True, blank = True, default='0')
    account_subtype_name    = models.TextField(null = True, blank = True, default='0')
    name                    = models.CharField(max_length=50,  null = True, blank = True, default='null')
    reference_no            = models.IntegerField(null = True, blank = True, default='0')
    status                  = models.SmallIntegerField(null = True, blank = True, default='0')
    created_by              = models.SmallIntegerField(null = True,  blank = True, default='0')
    created_date            = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_by              = models.SmallIntegerField(null = True,  blank = True, default='0')
    updated_date            = models.DateTimeField(auto_now_add=True, null = True, blank = True)

 

    def __str__(self):
        return self.account_subtype

    class Meta:
        db_table = 'account subcode'


class Account_subtype(models.Model):
    subtype_name        = models.CharField(max_length=50, null = True, blank = True, default='null')
    name                = models.TextField(max_length=50, null = True, blank = True, default='null')
    status              = models.SmallIntegerField(null = True, blank = True, default='0')
    created_by          = models.SmallIntegerField(null = True, blank = True, default='0')
    created_date        = models.DateField(null = True, blank = True)
    # sub_codes_name      = models.ForeignKey(Account_subcode, on_delete=models.CASCADE, related_name="subcode", null = True, blank = True, default='0')

    def __str__(self):
        return self.subtype_name

    class Meta:
        db_table = 'account subtype'



class Account_transaction(models.Model):
    financial_year_id   = models.TextField(max_length=20, null = True, blank = True, default='0')
    # voucher_no          = models.CharField(max_length=30, default=generate_transaction_code)
    voucher_type        = models.TextField(max_length=20, null = True, blank = True, default='AV')
    reference_no        = models.TextField( max_length=20, null = True, blank = True, default='0')
    voucher_date        = models.TextField( max_length=20, null = True, blank = True, default='0')
    Chart_of            = models.ForeignKey(Chart_Of_Account, related_name="ch_id", on_delete=models.CASCADE, blank=True, null=True)
    narration           = models.TextField(max_length=20, null = True, blank = True, default='0')
    cheque_no           = models.TextField(max_length=20, null = True, blank = True, default='0')
    cheque_date         = models.DateField( null = True, blank = True, default='2000-01-02')
    is_honor            = models.IntegerField( null = True, blank = True, default='0')
    debit               = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    credit              = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    reverse_code        = models.TextField( max_length=20, null = True, blank = True, default='0')
    subtype_id          = models.TextField( max_length=20, null = True, blank = True, default='0')
    subcode_id          = models.TextField( max_length=20, null = True, blank = True, default='0')
    is_approve          = models.TextField(max_length=20, null = True, blank = True, default='0')
    created_by          = models.SmallIntegerField( null = True, blank = True, default='0')
    created_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_by          = models.SmallIntegerField(null = True, blank = True, default='0')
    updated_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    approved_by         = models.IntegerField(null = True, blank = True, default='0')
    approved_date       = models.DateField(null = True, blank = True, default='2000-01-02')
    is_year_closed      = models.SmallIntegerField( null = True, blank = True, default='0')
    status              = models.SmallIntegerField(null = True, blank = True, default='0')
    account_name        = models.TextField(null = True, blank = True, default='0')
    date                = models.DateField(null = True, blank = True)
    remark              = models.TextField(null = True, blank = True, default='0')
    name_account        = models.TextField(null = True, blank = True, default='0')
    ledger_coments      = models.TextField(null = True, blank = True, default='0')
    TotalInWords        = models.TextField(null = True, blank = True, default='0')
    str_id              = models.CharField(max_length=25,blank=True,null=True, default='AV-0000')
    subtype             = models.CharField(max_length=100,null=True,blank=True,  default='account_voucher')
    acc_coa_id          =models.IntegerField( null = True, blank = True, default='0')
    def __str__(self):
        return str(self.name_account)

    class Meta:
        db_table = 'account_transaction'



class Account_voucher(models.Model):
    financial_year_id   = models.TextField(max_length=20, null = True, blank = True, default='0')
    # voucher_no          = models.CharField(max_length=30, default=generate_transaction_code)
    voucher_type        = models.TextField(max_length=20, null = True, blank = True, default='0')
    reference_no        = models.TextField( max_length=20, null = True, blank = True, default='0')
    voucher_date        = models.TextField( max_length=20, null = True, blank = True, default='0')
    Chart_of            = models.ForeignKey(Chart_Of_Account, related_name="chart_id", on_delete=models.CASCADE, blank=True, null=True)
    acc_coa_id          = models.IntegerField( null = True, blank = True, default='0')
    narration           = models.TextField(max_length=20, null = True, blank = True, default='0')
    cheque_no           = models.TextField(max_length=20, null = True, blank = True, default='0')
    cheque_date         = models.DateField( null = True, blank = True, default='2000-01-02')
    is_honor            = models.IntegerField( null = True, blank = True, default='0')
    debit               = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    credit              = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    reverse_code        = models.TextField( max_length=20, null = True, blank = True, default='0')
    subtype_id          = models.TextField( max_length=20, null = True, blank = True, default='0')
    subcode_id          = models.TextField( max_length=20, null = True, blank = True, default='0')
    is_approve          = models.TextField(max_length=20, null = True, blank = True, default='0')
    created_by          = models.SmallIntegerField( null = True, blank = True, default='0')
    created_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_by          = models.SmallIntegerField(null = True, blank = True, default='0')
    updated_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    approved_by         = models.IntegerField(null = True, blank = True, default='0')
    approved_date       = models.DateField(null = True, blank = True, default='2000-01-02')
    is_year_closed      = models.SmallIntegerField( null = True, blank = True, default='0')
    status              = models.SmallIntegerField(null = True, blank = True, default='0')
    account_name        = models.TextField(null = True, blank = True, default='0')
    date                = models.DateField(null = True, blank = True)     
    remark              = models.TextField(null = True, blank = True, default='0')
    name_account        = models.TextField(null = True, blank = True, default='0')
    ledger_coments      = models.TextField(null = True, blank = True, default='0')
    TotalInWords        = models.TextField(null = True, blank = True, default='0')
    str_id              = models.CharField(max_length=25,blank=True,null=True, default='AV-0000')
    subtype             = models.CharField(max_length=100,null=True,blank=True,  default='account_voucher')
    

    def __str__(self):
        return self.name_account

    class Meta:
        db_table = 'account_voucher'




class Voucher_type(models.Model):
    name        = models.CharField(max_length=50, null = True, blank = True, default='0')
    short_code  = models.TextField(max_length=20, null = True, blank = True, default='0')
    is_active   = models.SmallIntegerField(null = True, blank = True, default='0')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'voucher type'


class Opening_balance(models.Model):
    uuid                = models.CharField(max_length=50, null = True, blank = True, default='0')
    financial_year_date = models.IntegerField(null = True, blank = True, default='0')
    # voucher_no          = models.CharField(max_length=30, default=generate_transaction_code_for_OpeningBalance)
    account_name        = models.TextField(null = True, blank = True, default='0')
    Chart_of_account_id = models.IntegerField(null = True, blank = True, default='0')
    subtype             = models.CharField(max_length=50, null = True, blank = True, default='0')
    debit               = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    credit              = models.PositiveBigIntegerField( null = True, blank = True, default='0')
    date                = models.DateField(null = True, blank = True)
    open_date           = models.DateField( null = True, blank = True)
    created_by          = models.SmallIntegerField(null = True, blank = True, default='0')
    created_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_by          = models.SmallIntegerField(null = True, blank = True, default='0')
    updated_date        = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    str_id              = models.CharField(max_length=25, blank=True, null=True) 
    
    def __str__(self):
        return self.account_name

    class Meta:
        db_table = 'opening_balance'
    

class predefine_account(models.Model):
    uuid                          = models.CharField(max_length=50, null = True, blank = True, default='0')
    cash_code                     = models.IntegerField(null = True, blank = True, default='0')
    bank_code                     = models.IntegerField(null = True, blank = True, default='0')
    advance                       = models.IntegerField(null = True, blank = True, default='0')
    fixed_asset                   = models.IntegerField(null = True, blank = True, default='0')
    purchase_code                 = models.IntegerField(null = True, blank = True, default='0')
    sales_code                    = models.IntegerField(null = True, blank = True, default='0')
    customer_code                 = models.IntegerField(null = True, blank = True, default='0')
    supplier_code                 = models.IntegerField(null = True, blank = True, default='0')
    costs_of_good_solds           = models.IntegerField(null = True, blank = True, default='0')
    vat                           = models.IntegerField(null = True, blank = True, default='0')
    tax                           = models.IntegerField(null = True, blank = True, default='0')
    inventory_code                = models.IntegerField(null = True, blank = True, default='0')
    current_year_profit_loss_code = models.IntegerField(null = True, blank = True, default='0')
    last_year_profit_loss_code    = models.IntegerField(null = True, blank = True, default='0')
    salary_code                   = models.IntegerField(null = True, blank = True, default='0')
    prov_state_tax                = models.IntegerField(null = True, blank = True, default='0')
    state_tax                     = models.IntegerField(null = True, blank = True, default='0')
    CPLCode                       = models.IntegerField(null = True, blank = True, default='0')
    LPLCode                       = models.IntegerField(null = True, blank = True, default='0')
    emp_npf_contribution          = models.IntegerField(null = True, blank = True, default='0')
    empr_npf_contribution         = models.IntegerField(null = True, blank = True, default='0')
    emp_icf_contribution          = models.IntegerField(null = True, blank = True, default='0')
    empr_icf_contribution         = models.IntegerField(null = True, blank = True, default='0')
    prov_npfcode                  = models.IntegerField(null = True, blank = True, default='0')
    created_by                    = models.SmallIntegerField(null = True, blank = True, default='0')
    created_date                  = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_by                    = models.SmallIntegerField(null = True, blank = True, default='0')
    updated_date                  = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    
    def __str__(self):
        return self.customer_code

    class Meta:
        db_table = 'predefine_account'
    
