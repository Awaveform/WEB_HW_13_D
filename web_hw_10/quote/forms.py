from django.forms import ModelForm, CharField, TextInput, DateField
from .models import Tag, Quote, Author


class TagForm(ModelForm):
    name = CharField(
        min_length=3, max_length=25, required=True, widget=TextInput()
    )

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):

    name = CharField(
        min_length=5, max_length=50, required=True, widget=TextInput()
    )
    description = CharField(
        min_length=10, max_length=150, required=True, widget=TextInput()
    )

    class Meta:
        model = Quote
        fields = ['name', 'description']
        exclude = ['tags']


class AuthorForm(ModelForm):

    fullname = CharField(
        min_length=5, max_length=50, required=True, widget=TextInput()
    )
    # born_date = DateField(
    #     # min_length=10, max_length=150,
    #     required=False, widget=DateField()
    # )
    born_date = DateField(
        required=False, widget=TextInput(attrs={'type': 'date'})
    )
    born_location = CharField(
        min_length=2, max_length=24, required=True, widget=TextInput()
    )
    author_description = CharField(
        min_length=10, max_length=1024, required=True, widget=TextInput()
    )

    class Meta:
        model = Author
        fields = [
            'fullname', 'author_description', 'born_date', 'born_location'
        ]
        # exclude = ['tags']
