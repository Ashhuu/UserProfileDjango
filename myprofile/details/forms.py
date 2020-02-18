from django import forms


class CardForm(forms.Form):
    cardNumber = forms.CharField(label="Card Number",max_length=16,
                                 widget=forms.TextInput(attrs={'placeholder': 'Card Number', 'id':'cc-number', 'class':'form-control cc-number identified visa'}), required=True)
    month = forms.CharField(label="Month", max_length=2,
                             widget=forms.TextInput(attrs={'placeholder': 'Month', 'id':'cc-exp', 'class':'form-control cc-exp'}), required=True)
    year = forms.CharField(label="Year", max_length=4,
                     widget=forms.TextInput(attrs={'placeholder': 'Year', 'id':'cc-exp', 'class':'form-control cc-exp'}), required=True)
    cvv = forms.CharField(label="CVV", max_length=3,
                          widget=forms.PasswordInput(attrs={'placeholder': 'CVV', 'class': 'form-control cc-cvc', 'id': 'x_card_code'}),
                          required=True)
    name = forms.CharField(label="Card Holder Name", widget=forms.TextInput(attrs={'placeholder': 'Card Holder Name', 'id':'cc-number', 'class':'form-control cc-number identified visa'}))