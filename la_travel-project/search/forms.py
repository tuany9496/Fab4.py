from django import forms



What_CHOICES= [
    ('Restaurants', 'Restaurants'),
    ('Hotels & Motels', 'Hotels & Motels'),
    ('Sightseeing', 'Sightseeing'),

    ]
class DateInput (forms.DateInput):
    input_type = 'date'
class DateInput2 (forms.DateInput):
    input_type = 'date'


class SearchForms (forms.Form):
    Where = forms.ChoiceField(label='Where  ', choices=[('Agoura Hills','Agoura Hills'), ('Alhambra', 'Alhambra'),('Arcadia', 'Arcadia'),('Artesia', 'Artesia'),('Avalon', 'Avalon'),('Azusa', 'Azusa'), ('Baldwin Park', 'Baldwin Park'),('Bell', 'Bell'),('Bell Gardens', 'Bell Gardens'),('Bellflower', 'Bellfower'),('Beverly Hills', 'Beverly Hills'),('Bradbury', 'Bradbury'),('Burbank', 'Burbank'),('Calabasas', 'Calabasas'),('Carson', 'Carson'),('Cerritos', 'Cerritos'),('Claremont', 'Claremont'),('Commerce', 'Commerce'),('Compton', 'Compton'),('Covina', 'Covina'),('Cudahy', 'Cudahy'),('Culver City', 'Culver City'),('Diamond Bar', 'Diamond Bar'),('Downey', 'Downey'),('Duarte', 'Duarte'),('El Monte', 'El Monte'),('El Segundo', 'El Segundo'),('Gardena', 'Gardena'),('Glendale', 'Glendale'),('Glendora', 'Glendora'),('Hawaiian Gardens', 'Hawaiian Gardens'),('Hawthorne', 'Hawthorne'),('Hermosa Beach', 'Hermosa Beach'),('Hidden Hills', 'Hidden Hills'),('Huntington Park', 'Huntington Park'),('Industry', 'Industry'),('Inglewood', 'Inglewood'),('Irwindale', 'Irwindale'),('La Cañada Flintridge', 'La Cañada Flintridge'),('La Habra Heights', 'La Habra Heights'),('La Mirada', 'La Mirada'),('La Puente', 'La Puente'),('La Verne', 'La Verne'),('Lakewood', 'Lakewood'),('Lancaster', 'Lancaster'),('Lawndale', 'Lawndale'),('Lomita', 'Lomita'),('Long Beach', 'Long Beach'),('Los Angeles', 'Los Angeles'),('Lynwood', 'Lynwood'),('Malibu', 'Malibu'),('Manhattan Beach', 'Manhattan Beach'),('Maywood', 'Maywood'),('Monrovia', 'Monrovia'),('Montebello', 'Montebello'),('Monterey Park', 'Monterey Park'),('Norwalk', 'Norwalk'),('Palmdale', 'Palmdale'),('Palos Verde Estates', 'Palos Verde Estates'),('Paramount', 'Paramount'),('Pasadena', 'Pasadena'),('Pico Rivera', 'Pico Rivera'),('Pomona', 'Pomona'),('Rancho Palos Verdes', 'Rancho Palos Verdes'),('Redondo Beach', 'Redondo Beach'),('Rolling Hills', 'Rolling Hills'),('Rolling Hills Estates', 'Rolling Hills Estates'),('Rosemead', 'Rosemead'),('San Dimas', 'San Dimas'),('San Fernando', 'San Fernando'),('San Gabriel', 'San Gabriel'),('San Marino', 'San Marino'),('i', 'Santa Clarita'),('Santa Fe Springs', 'Santa Fe Springs'),('Santa Monica', 'Santa Monica'),('Sierra Madre', 'Sierra Madre'),('Signal Hills', 'Signal Hills'),('South El Monte', 'South El Monte'),('South Gate', 'South Gate'),('South Pasadena', 'South Pasadena'),('Temple City', 'Temple City'),('Torrance', 'Torrance'),('Vernon', 'Vernon'),('Walnut', 'Walnut'),('West Covina', 'West Covina'),('West Hollywood', 'West Hollywood'),('Westlake Village', 'Westlake Village'),('Whittier', 'Whittier')])
    From = forms.DateField(widget=DateInput)
    To = forms.DateField(widget=DateInput2)
    What = forms.CharField(label='What  ', widget=forms.Select(choices=What_CHOICES))
