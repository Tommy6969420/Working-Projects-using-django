from django import forms
from.models import Bill
import crispy_forms
class BillForm(forms.ModelForm):
    bill_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    vendor =  forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Vendor'}))
    bill_date =  forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Bill Date'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Due Date'}))
    reference = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Reference'}))​
    class Meta:
        model = Bill
        fields = ['vendor','bill_date','due_date','reference']  

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.layout = Layout(
            Row(
                Column('vendor', css_class='form-group col-md-2 mb-0'),
                Column('bill_title', css_class='form-group col-md-2 mb-0'),
                Column('bill_date', css_class='form-group col-md-2 mb-0'),
                Column('due_date', css_class='form-group col-md-2 mb-0'),
                Column('reference', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),Fieldset('Add lines',Formset('lines')),Row(                               
                css_class='form-row'
            ),Div(               
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

