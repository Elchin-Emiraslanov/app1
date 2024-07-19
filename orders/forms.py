import re
from django import forms

class CreatedOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address =forms.ChoiceField(required=False)
    
    payment_on_get = forms.ChoiceField(
        choices=[
         ("0", "False"),
         ("1", "True"),
         ],
         )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError("Telefon nömrəsi yalnız rəqəm qəbul etməlidir ")
        
        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Nomre formati duzgun deyil")
        
        return data

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Enter your name"
    #         }
    #     )
    # )
    
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Enter your surname"
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Enter your phone number"
    #         }
    #     )
    # )

    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
        # choices=[
        #     ("0", False),
        #     ("1", True),
        # ],
    #     initial=0,
    # )

    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "forms-control",
    #             "id": "delivery-address",
    #             "rows": 2,
    #             "placeholder": "Enter delivery adress"
    #         }
    #     ),
    #     required=False
    # )

    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", "False"),
    #         ("1", "True"),
    #     ],
    #     initial="card"
    # )

