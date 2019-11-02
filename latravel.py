import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import *
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class MainPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       # label = tk.Label(self, text="This is page 1")
       # label.pack(side="top", fill="both", expand=True)

       # Title
       lb1 = Label(self, text="LA | Travel like a local", font= (50))
       lb1.grid(column=0, row=0)

       # Where
       lb2 = Label(self, text="WHERE :")
       lb2.grid(column=0, row=1)
       #self.txt_where = Entry(self,width=10)
       #self.txt_where.grid(column=1, row=1)

       self.combo_where = ttk.Combobox(self, width=10)
       self.combo_where['values'] = ('Agoura Hills','Alhambra','Arcadia','Artesia','Avalon','Azusa','Baldwin Park','Bell','Bell Gardens','Bellflower','Beverly Hills','Bradbury','Burbank','Calabasas','Carson','Cerritos','Claremont','Commerce','Compton','Covina','Cudahy','Culver City','Diamond Bar','Downey','Duarte','El Monte','El Segundo','Gardena','Glendale','Glendora','Hawaiian Gardens','Hawthorne','Hermosa Beach','Hidden Hills','Huntington Park','Industry','Inglewood','Irwindale','La Cañada Flintridge','La Habra Heights','La Mirada','La Puente','La Verne','Lakewood','Lancaster','Lawndale','Lomita','Long Beach','Los Angeles','Lynwood','Malibu','Manhattan Beach','Maywood','Monrovia','Montebello','Monterey Park','Norwalk','Palmdale','Palos Verdes Estates','Paramount','Pasadena','Pico Rivera','Pomona','Rancho Palos Verdes','Redondo Beach','Rolling Hills','Rolling Hills Estates','Rosemead','San Dimas','San Fernando','San Gabriel','San Marino','Santa Clarita','Santa Fe Springs','Santa Monica','Sierra Madre','Signal Hill','South El Monte','South Gate','South Pasadena','Temple City','Torrance','Vernon','Walnut','West Covina','West Hollywood','Westlake Village','Whittier')
       self.combo_where.grid(column=1 ,row=1)

       # When
       lb3 = Label(self, text="WHEN :")
       lb3.grid(column=0, row=2)
       self.txt_when_from = Entry(self,width=10)
       self.txt_when_from.grid(column=1, row=2)
       lb6 = Label(self, text=" to ")
       lb6.grid(column=2, row=2)
       self.txt_when_to = Entry(self,width=10)
       self.txt_when_to.grid(column=3, row=2)

       # How
       lb4 = Label(self, text="HOW :")
       lb4.grid(column=0, row=3)
       self.txt_how = Entry(self,width=10)
       self.txt_how.grid(column=1, row=3)


       # What
       lb5 = Label(self, text="WHAT :")
       lb5.grid(column=0, row=4)
       #txt4.grid(column=1, row=4)

       # What Checkbuttons
       self.checkbutton_eat = Checkbutton(self, text = 'Restaurants')
       self.checkbutton_eat.grid(column=1, row= 4)
       self.checkbutton_eat.deselect()
       # Set Checkbutton_eat value
       self.eat = StringVar()
       self.eat.set ('Dont Display')
       self.checkbutton_eat.config (variable = self.eat, onvalue = 'Display', offvalue = 'Dont Display' )

       self.checkbutton_hotel = Checkbutton(self, text = 'Hotels')
       self.checkbutton_hotel.grid(column=2, row= 4)
       self.checkbutton_hotel.deselect()

       self.checkbutton_see = Checkbutton(self, text = 'Sightseeing')
       self.checkbutton_see.grid(column=1, row= 5)
       self.checkbutton_see.deselect()
class SearchResultPage(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Seach Results")
       label.pack()


       # Search Terms
       search_terms_frame = ttk.Label(self,text = "Weather Forecast")
       search_terms_frame.pack()
       #Where Box
       # lb2 = Label(search_terms_frame, text="WHERE :").grid(column=0, row=0, sticky='E')
       # #lb2.pack()
       # city = tk.StringVar()
       # self.citySelected = ttk.Combobox (search_terms_frame, width = 12, textvariable = city)
       # self.citySelected['values']= ('Bellflower', 'Covina', 'Los Angeles')
       # self.citySelected.grid(column=1, row= 0)
       # #self.citySelected = ttk.Combobox(search_terms_frame, values =('Los Angeles', 'Bellflower', 'Cerritos', 'Covina') ).grid(column=1, row=0, sticky='W')#.pack()
       # #citySelected.current(#selected!)
       #self.txt_where = Entry(self,width=10)
       #self.txt_where.pack()

       # ---------------------------------------------------------------
       # max_width = max(len(x) for x in self.citySelected['values'])
       # new_width = max_width
       # self.citySelected.config (width= new_width)
       #==========================
       entry_width = 10#max_width + 3             # adjust per taste of alignment
       #==========================
       # Adding Label & Textbox Entry widgets
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Last Updated:").grid(column=0, row=1, sticky='E')         # <== right-align
       updated = tk.StringVar()
       updatedEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=updated, state='readonly')
       updatedEntry.grid(column=1, row=1, sticky='W')
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Weather:").grid(column=0, row=2, sticky='E')               # <== increment row for each
       weather = tk.StringVar()
       weatherEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=weather, state='readonly')
       weatherEntry.grid(column=1, row=2, sticky='W')                                  # <== increment row for each
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Temperature:").grid(column=0, row=3, sticky='E')
       temp = tk.StringVar()
       tempEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=temp, state='readonly')
       tempEntry.grid(column=1, row=3, sticky='W')
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Dewpoint:").grid(column=0, row=4, sticky='E')
       dew = tk.StringVar()
       dewEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=dew, state='readonly')
       dewEntry.grid(column=1, row=4, sticky='W')
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Relative Humidity:").grid(column=0, row=5, sticky='E')
       rel_humi = tk.StringVar()
       rel_humiEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=rel_humi, state='readonly')
       rel_humiEntry.grid(column=1, row=5, sticky='W')
       #---------------------------------------------
       ttk.Label(search_terms_frame, text="Wind:").grid(column=0, row=6, sticky='E')
       wind = tk.StringVar()
       windEntry = ttk.Entry(search_terms_frame, width=entry_width, textvariable=wind, state='readonly')
       windEntry.grid(column=1, row=6, sticky='W')

       # Add some space around each label
       for child in search_terms_frame.winfo_children():
           child.grid_configure(padx=4, pady=2)    # adjust per visual taste of spacing around widgets


       #########################################################################################
       # NOAA (National Oceanic and Atmospheric Administration) section starts here

       # We are creating a container frame to hold other widgets
       weather_cities_frame = ttk.LabelFrame(search_terms_frame, text=' Search Terms: ')
       weather_cities_frame.grid(column=0, row=0, padx=8, pady=4)

       # ---------------------------------------------------------------
       # Adding a Label
       ttk.Label(weather_cities_frame, text="Selected City / Weather Station ID: ").grid(column=0, row=0) # empty space for alignment

       # ---------------------------------------------------------------
       station_id = tk.StringVar()
       station_id_combo = ttk.Combobox(weather_cities_frame, width=6, textvariable=station_id)
                               # Los Angeles, Denver, New York City
       station_id_combo['values'] = ('KLAX', 'KDEN', 'KNYC')
       station_id_combo.grid(column=1, row=0)
       station_id_combo.current(0)                 # highlight first city station id

       # ---------------------------------------------------------------
       # callback function
       def _get_station():
           station = station_id_combo.get()
           get_weather_data(station)
           populate_gui_from_dict()

       get_weather_btn = ttk.Button(weather_cities_frame,text='Search', command=_get_station).grid(column=2, row=0)

       # Station City label
       location = tk.StringVar()
       ttk.Label(weather_cities_frame, textvariable=location).grid(column=0, row=1, columnspan=3)
       # ---------------------------------------------------------------
       for child in weather_cities_frame.winfo_children():
               child.grid_configure(padx=5, pady=4)

       #########################################################################################
       # NOAA DATA directly from live web search

       #Retrieve the tags we are interested in
       weather_data_tags_dict = {
           'observation_time': '',
           'weather': '',
           'temp_f':  '',
           'temp_c':  '',
           'dewpoint_f': '',
           'dewpoint_c': '',
           'relative_humidity': '',
           'wind_string':   '',
          # 'visibility_mi': '',
           'pressure_string': '',
           'pressure_in': '',
           'location': ''
           }

       # ---------------------------------------------------------------
       import urllib.request

       def get_weather_data(station_id='KLAX'):
           url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
           url = url_general.format(station_id)
           print(url)
           request = urllib.request.urlopen( url )
           content = request.read().decode()
       #     print(content)

           # Using ElementTree to retrieve specific tags from the xml
           import xml.etree.ElementTree as ET
           xml_root = ET.fromstring(content)
           print('xml_root: {}\n'.format(xml_root.tag))

           for data_point in weather_data_tags_dict.keys():
               weather_data_tags_dict[data_point] = xml_root.find(data_point).text

       #     for key, value in weather_data_tags_dict.items():
       #         print(key, value)

       # ---------------------------------------------------------------
       def populate_gui_from_dict():
           location.set(weather_data_tags_dict['location'])
           updated.set(weather_data_tags_dict['observation_time'].replace('Last Updated on ', ''))
           weather.set(weather_data_tags_dict['weather'])
           temp.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['temp_f'], weather_data_tags_dict['temp_c']))
           dew.set('{} \xb0F  ({} \xb0C)'.format(weather_data_tags_dict['dewpoint_f'], weather_data_tags_dict['dewpoint_c']))
           rel_humi.set(weather_data_tags_dict['relative_humidity'] + ' %')
           wind.set(weather_data_tags_dict['wind_string'])
          # visi.set(weather_data_tags_dict['visibility_mi'] + ' miles')
           msl.set(weather_data_tags_dict['pressure_string'])
           alti.set(weather_data_tags_dict['pressure_in'] + ' in Hg')


       #########################################################################################





       # Eat Tab
       tabControl = ttk.Notebook(self)
       eat_tab = ttk.Frame(tabControl)
       tabControl.add(eat_tab, text = 'Restaurants')
       # Rest Tab
       rest_tab = ttk.Frame(tabControl)
       tabControl.add(rest_tab, text = 'Hotels')
       # See Tab
       see_tab = ttk.Frame(tabControl)
       tabControl.add(see_tab, text = 'Sightseeing')
       tabControl.pack(expand=1, fill="both")

       self.eat_results_frame = ttk.LabelFrame(eat_tab, text=' Resturants Results ')
       self.eat_results_frame.grid(column=0, row=0, padx=8, pady=4)
       ttk.Label(self.eat_results_frame, text="Put Table Here").grid(column=0, row=0, sticky='W')



class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = MainPage(self)
        p2 = SearchResultPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main Page", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Search", command=p2.lift)


        b1.pack(side="left")
        b2.pack(side="left")


        p1.show()

if __name__ == "__main__":
    self = tk.Tk()
    main = MainView(self)
    main.pack(side="top", fill="both", expand=True)
    self.wm_geometry("600x400")
    self.mainloop()
