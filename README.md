# IST-303 Group Project

# How to run the Application:

## Requirements:
* Python 3.7.1
* pip
* Virtual Environment
* Django
* Geopy
* wkhtmltox

## Run Application:

1. Clone folder from Github

2. Create Virtual Environment
> <pre><code> pip install virtualenv</code></pre>
> <pre><code> virtualenv env</code></pre>
> Activiate the virtual envrionment in the root folder
> <pre><code>In Windows
> env\Scripts\activate</code></pre>
> <pre><code>In Mac
> source env/bin/activate
> </code></pre>

3. Install application required packages
> <pre><code>pip install -r Requirements.txt</code></pre>

4. Cd into la_travel-project

5. You may have to migrate any unapplied migrations by using: python manage.py makingmigrations, python manage.py migrate

<pre><code> Operations to perform:
  Apply all migrations: admin, auth, contenttypes, search, sessions
Running migrations:
  Applying search.0001_initial... OK
  Applying search.0002_auto_20191102_1525... OK
  Applying search.0003_place_type... OK
  Applying search.0004_auto_20191102_2101... OK</code></pre>

6. Run Virtual Server
> <pre><code>python manage.py runserver</code></pre>
> Results
> <pre><code>
> System check identified no issues (0 silenced).
> April 03, 2019 - 14:24:08
> Django version 2.1.7, using settings 'quest.settings'
> Starting development server at http://127.0.0.1:8000/
> Quit the server with CTRL-BREAK.
> </code></pre>

7. Copy http link into a web browser
> Access LA Travel Application

8. Stop server
>  <pre><code>Ctrl+C</code></pre>

9. Deactivate virtual environment
>  <pre><code>Deactivate</code></pre>

<h3>Tests:</h3>

> - Activate virtualenv, cd la-travel_project, and run <code>pytest</code>

<h3>Admin:</h3>

> - Username: cgu
> - Password: 1234

# How to use the Application:
<h3>Map:</h3>

Around me:
> - Click the button and then enter the zip code, place, or just click on the location on the map.

Directions:
> - Click on the button and enter the destination, or simply click on the map.
> - If you wan to avoid passing by specific area, click on the cone symbol and mark the areas that you want to avoid.   

Basemap background:
> - If you want to change the map background, click on the basemap and click that background of your choice.

Search:
> - You can search for places using business name, business type, zip code, or category. You can also search by areas that you want to avoid.

Avoid traffic:
> - You can see the real time traffic of the Los Angelos area. The green color means no traffic, while the red color means heavey traffic.

Crime data:
> - The black dots on the map reprensent the areas where arrest has been done by police. When you click on the black dot, you will be able to see the details of the arrest. 


# Part A

Team Members:
Ali, Chuck, Pranav, Yian

Team Name:
Fab4.Py

Product:
Los Angeles Travel Guide App

Stakeholder
* Individuals who are travel planners and travelers in Los Angeles
* LA Business agencies in the travel industry, such as Hotel, Travel Agency, Restaurants, etc.


**User Story and Estimated Time of Completion**

As a user, I would like to enter an  address through a basic search interface to find travel information
* A.1 As a user, I would like to see information about fun places to visit (Complete by Milestone 1.0)
* A.2 As a user, I would like to see information about safe travel areas (Complete by Milestone 1.0)
* A.3 As a user, I would like to see information about restaurants in the area (Complete by Milestone 1.0)
* A.4 As a user, I would like to see information about hotels in the area (Complete by Milestone 1.0)

As a user, I would like to enter the trip duration, and have the tool schedule my trip through outlook (Complete by Milestone 2.0)

Part A Requirements Completed on 9-25-2019.

# Part B
**Breakdown User Stories**
1) As a user, I can search for travel information
>Priority 20 - 7 Days\
>Tasks: (Front End Interface)
>- 1.1 Select where: Basic search interface (Drop Down List of City Name)
Database search (Back End) - 3 Days
>- 1.2 Put in date (When - Trip date entry) - 2 Days
>- 1.3 Select point of interests (What) - 2 Days

2) As a user, I can search for detailed information about my travel
>Priority 20 - 5 Days\
>Tasks: (Front End Interface)
>- 2.1 Type out where: Intermediate search interface (Open textbox for City Name with auto-populate) - 4 Days
>- 2.2 Pop open error message if not all criteria selected - 1 Day

3)  As a user, I can view the search criterias on the search result page
>Priority 10 - 3 Days\
>Tasks: (Front End Interface)
>- 3.1 List out where and when - 1.5 Day
>- 3.2  Add an edit / modify back button to search page - 1.5 Day

4) As a user, I can view the search results
>Priority 10 - 15 Days\
>Tasks: (Front End Interface)
>- 4.1 List out search results of locations - 3 Day
>- 4.2 Prepare listing of restaurants - 3 Day
>- 4.3 Prepare listing of hotels - 3 Day
>- 4.4 Prepare listing of sightsee - 3 Day
>- 4.5 Structure and populate database with the listing - 4 Day

5) As a user, I can view the search results’ additional information
>Priority 40 - 8 Days\
>Tasks:
>- 5.1 List out where and when - 1 Day
>- 5.2 Display for weather forecast - 2 Day
>- 5.3 Display for sunrise and sunset -2 Day
>- 5.4 Overlay map of potential unsafe areas - 3 Day


6) As a user, I can review and organize search results
>Priority 30 - 15 Days\
>Tasks: (Front End Interface)
>- 6.1 Filter and sort - 5 Days
>- 6.2 Compare results for restaurants- 5 Days
>- 6.3 Compare results for hotels- 5 Days


7) As a user, I can export / share the selected search results
>Priority 40 - 9 Days\
>Tasks:
>- 7.1 Export to outlook calendar - 2 Days
>- 7.2 Export to email - 2 Days
>- 7.3 Copy information - 2 Days
>- 7.4 Print formatted information - 3 Days

**Allocate Tasks**

**Milestone 1.0 - 27 Work Days**\
User Stories: Part of 1, 4, Complete 2, 3, 5\
Iteration 1 (23  days)


>Ali

>- 4.2 Prepare listing of restaurants - 3 Day
>- 4.3 Prepare listing of hotels - 3 Day


>Chuck

>- 5.3 Display for sunrise and sunset -2 Day
>- 5.4 Overlay map of potential unsafe areas - 3 Day
>- 3.2  Add an edit / modify back button to search page - 1.5 Day


>Pranav

>- 4.1 List out search results of locations - 3 Day
>- 4.5 Structure and populate database with the listing - 4 Day


>Yian

>- 5.1 List out where and when - 1 Day
>- 5.2 Display for weather forecast - 2 Day
>- 1.1 Select where: Basic search interface (Drop Down List of City Name)
Database search (Back End) - 3 Days



**Milestone 2.0 - 36 Days**\
User Stories: Complete 1, 2, 4, 6\
Iteration 1 (30  days)


>Ali

>- 6.1 Filter and sort - 5 Days
>- 4.4 Prepare listing of sightsee - 3 Day


>Chuck

>- 7.1 Export to outlook calendar - 2 Days
>- 7.2 Export to email - 2 Days
>- 7.3 Copy information - 2 Days
>- 7.4 Print formatted information - 3 Days


>Pranav

>- 2.1 Type out where: Intermediate search interface (Open textbox for City Name with auto-populate) - 4 Days
>- 2.2 Pop open error message if not all criteria selected - 1 Day
>- 6.2 Compare results for restaurants- 5 Days


>Yian

>- 1.2 Put in date (When - Trip date entry) - 2 Days
>- 1.3 Select point of interests (What) - 2 Days
>- 6.3 Compare results for hotels- 5 Days


**Velocity**

>- Starting velocity 30%
>- 4 (number of people in our team) x 23 (days for Milestone 1) x 0.3 velocity) = 27.6 amount of work for 1 Milestone
>- 4 (number of people in our team) x 30 (days for Milestone 2) x 0.3 velocity) = 36 amount of work for 2 Milestone
>- Total 63.6 amount of work days


**Burndown Chart**
>- Please view chart via google doc in Burn Down Chart section: https://docs.google.com/document/d/1h2-bK45PE2THBrbqpFhjicYiz09DstYrtsH_04xu95A/edit?usp=sharing

**Stand Up Meeting**
>- Wednesday after class
>- Friday at 11:30AM

**Team Meetings**
>- Please view photo evidence via google doc in the Team Meeting section: https://docs.google.com/document/d/1h2-bK45PE2THBrbqpFhjicYiz09DstYrtsH_04xu95A/edit?usp=sharing


# Part D
**Learned outcomes**
> From this project, we learned the following things:
>- 1- how to use git and GitHub for the collaborative work of team members. 
>- 2- how to use Zen hub to create the tasks and create the burn down chart.
>- 3- how to use python and relevant libraries to build a working program. 
>- 4- how to test a program using pytest functions.
