from django import forms
from .models import District, Branch

class AccountOpeningForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    dob = forms.DateField(required=True)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)
    number = forms.IntegerField(required=True, min_value=1000000000, max_value=9999999999)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=200, required=True)
    district = forms.ModelChoiceField(queryset=District.objects.all(), required=True)
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), required=True)
    acc = forms.ChoiceField(choices=[('Savings', 'Savings'), ('Current', 'Current'), ('Joint', 'Joint')], required=True)
    materials = forms.MultipleChoiceField(choices=[('Creditcard', 'Credit card'), ('Debitcard', 'Debit card'), ('Chequebook', 'Cheque book')], widget=forms.CheckboxSelectMultiple, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        # elif self.instance.pk:
        #     self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
