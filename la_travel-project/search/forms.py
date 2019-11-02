from django import forms

class SearchForms (forms.Form):
    Where = forms.ChoiceField(label='Where: ', choices=[('Agoura Hills','Agoura Hills'), ('Alhambra', 'Alhambra'),('Arcadia', 'Arcadia'),('Artesia', 'Artesia')])
    WhenFr = forms.CharField(label='When (From): ', max_length = 200)
    WhenTo = forms.CharField(label='When (To): ', max_length = 200)
    What = forms.CharField(label='What: ', max_length = 200)
