from django import forms


class InvoiceForm(forms):
    invoice_no = forms.CharField(max_length=5)
    created = forms.DateField()
    due = forms.DateField()

    from_company_name = forms.CharField(max_length=50)
    address_1 = forms.CharField(max_length=50)
    address_2 = forms.CharField(max_length=50)

    to_company_name = forms.CharField(max_length=50)
    address_1 = forms.CharField(max_length=50)
    address_2 = forms.CharField(max_length=50)
