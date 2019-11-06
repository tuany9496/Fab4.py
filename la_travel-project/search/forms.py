from django import forms
What_CHOICES= [
    ('Restaurants', 'Restaurants'),
    ('Hotels & Motels', 'Hotels & Motels'),
    ('Sightseeing', 'Sightseeing'),

    ]

class SearchForms (forms.Form):
    Where = forms.ChoiceField(label='Where  ', choices=[('Agoura Hills','Agoura Hills'), ('Alhambra', 'Alhambra'),('Arcadia', 'Arcadia'),('Artesia', 'Artesia'), ('Los Angeles', 'Los Angeles')])
    WhenFr = forms.CharField(label='When (From)  ', max_length = 200)
    WhenTo = forms.CharField(label='When (To)  ', max_length = 200)
    What = forms.CharField(label='What  ', widget=forms.Select(choices=What_CHOICES))
