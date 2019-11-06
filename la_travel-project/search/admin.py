from django.contrib import admin

# Register your models here.
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
    #list_display = ['Company Name', 'Address', 'City', 'State', 'Zip Code', 'County', 'Neigborhood', 'Phone Number', 'Website Link', 'SIC Description', 'SIC Code', 'Cuisine Type (If Applicable)','Tuesday Open', 'Tuesday Close', 'Wednesday Open', 'Wednesday Close', 'Thursday Open', 'Thursday Close', 'Friday Open', 'Friday Close', 'Saturday Open', 'Saturday Close', 'Sunday Open', 'Sunday Ave', 'Twitter Account', 'Facebook Link' ]
