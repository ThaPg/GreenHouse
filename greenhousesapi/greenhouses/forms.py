# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import Producer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Producer(forms.ModelForm):
    CULTIVARS_CHOICES = [
        ("Τριαντάφυλλο", "Τριαντάφυλλο"),
        ("Μαργαρίτα", "Μαργαρίτα"),
        ("Αγγούρι", "Αγγούρι"),
        ("Ντομάτα", "Ντομάτα"),
        ("Πιπεριά", "Πιπεριά"),
        ("Μαρούλι", "Μαρούλι"),
    ]

    INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 11)]

    region = forms.CharField(
        label="Περιφέρεια",
    )
    prefecture = forms.CharField(
        label="Νομός",
    )

    location = forms.CharField(label="Τοποθεσία")
    first_name = forms.CharField(label="Όνομα")
    last_name = forms.CharField(label="Επώνυμο")
    email = forms.EmailField(label="Email")
    greenhouse_number = forms.ChoiceField(
        choices=INTEGER_CHOICES, label="Αριθμός Θερμοκηπίων"
    )
    cultivation = forms.ChoiceField(choices=CULTIVARS_CHOICES, label="Καλλιέργεια")
    description = forms.TextInput()

    # specify the name of model to use
    class Meta:
        model = Producer
        # fields = "__all__"

        exclude = ["user"]


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
