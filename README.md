# IST-303 Group Project

# How to run the Application:

## Requirements:
* Python 3.7.1
* pip
* Virtual Environment

## Run Application:

1. In the application root folder,

 <pre><code>
# In Windows
.\virtenv\Scripts\activate
# In Mac
source virtenv/Scripts/activate
</code></pre>
    You might have to <code>pip install -r requirements.txt</code> due to OS differences.
  </li>
  <li>Now, run the app Django server.<br>
    <code>
      python manage.py runserver
    </code>
  </li>
  <li>Something like this should show up:

<pre><code>
System check identified no issues (0 silenced).
April 03, 2019 - 14:24:08
Django version 2.1.7, using settings 'quest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
</code></pre>
</code></pre>
  </li>
  <li>Copy the http link given and paste into a web browser.</li>
  <li>To stop server: Ctrl+C</li>
  <li>Deactivate the virtual environment</li>
</ol>

<h3>Run Discord Monitor script:</h3>
(Will not work properly due to disconnected services)<br>
In the application root folder, run <code>python monitor.py</code>

<h3>Tests:</h3>
In the application root folder, run <code>pytest</code>
 
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
1) As a user, I can search for travel information\
>Priority 20 - 7 Days\
>Tasks: (Front End Interface)
>- 1.1 Select where: Basic search interface (Drop Down List of City Name) 
Database search (Back End) - 3 Days
>- 1.2 Put in date (When - Trip date entry) - 2 Days
>- 1.3 Select point of interests (What) - 2 Days

2) As a user, I can search for detailed information about my travel\
>Priority 20 - 5 Days\
>Tasks: (Front End Interface)
>- 2.1 Type out where: Intermediate search interface (Open textbox for City Name with auto-populate) - 4 Days
>- 2.2 Pop open error message if not all criteria selected - 1 Day

3)  As a user, I can view the search criterias on the search result page\
>Priority 10 - 3 Days\
>Tasks: (Front End Interface)
>- 3.1 List out where and when - 1.5 Day
>- 3.2  Add an edit / modify back button to search page - 1.5 Day

4) As a user, I can view the search results\
>Priority 10 - 15 Days\
>Tasks: (Front End Interface)
>- 4.1 List out search results of locations - 3 Day
>- 4.2 Prepare listing of restaurants - 3 Day
>- 4.3 Prepare listing of hotels - 3 Day
>- 4.4 Prepare listing of sightsee - 3 Day
>- 4.5 Structure and populate database with the listing - 4 Day

5) As a user, I can view the search results’ additional information\
>Priority 40 - 8 Days\
>Tasks:
>- 5.1 List out where and when - 1 Day
>- 5.2 Display for weather forecast - 2 Day
>- 5.3 Display for sunrise and sunset -2 Day
>- 5.4 Overlay map of potential unsafe areas - 3 Day


6) As a user, I can review and organize search results\
>Priority 30 - 15 Days\
>Tasks: (Front End Interface)
>- 6.1 Filter and sort - 5 Days
>- 6.2 Compare results for restaurants- 5 Days
>- 6.3 Compare results for hotels- 5 Days


7) As a user, I can export / share the selected search results\
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

>10/2/2019 
>- Attendee: Pranav, Ali, Yian
>- Notes: Finalize the app functionality

>10/4/2019
>- Attendee:Ali, Chuck, Yian
>- Notes:  Work on Part B and in class exercise

>10/8/2019 Meeting with Professor
>- Attendee: Pranav, Ali

>10/8/2019
>- Attendee: Pranav, Ali, Chuck, Yian
>- Notes: Finalize Part B

