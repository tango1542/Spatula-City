from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 12)]      #This form will allow the user to select up to quantity 12


class CartAddProductForm(forms.Form):           #This form will be used to add items to the cart
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)