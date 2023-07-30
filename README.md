

# Discord Clone

## Project Overview

The Discord Clone project is a web application built with Django in the backend and HTML/CSS in the frontend. It aims to replicate some functionalities of the popular communication platform Discord. The application allows users to create accounts, log in, and authenticate using their credentials. It features a comprehensive RESTful API powered by Django Rest Framework (DRF) that enables full CRUD (Create, Read, Update, Delete) operations on various endpoints.

### Key Features:

- User Authentication:

Users can create accounts and log in to the application.
Authentication is done using a username/email and password combination.
Token-based authentication will be configured, providing secure access to API endpoints.
User Avatar and Profile:
Users can upload and use avatars to personalize their profiles.

- Topics and Rooms:

Users can create topics related to tech-related discussions and subjects.
Each topic can have multiple rooms for specific discussions within that topic.
- Room Participants and Messages:

Users can participate in different rooms within a topic.
Rooms host discussions where participants can exchange messages.
Participants in a room can view and interact with messages posted in that room.
RESTful API:

- The application includes a DRF-powered API that exposes various endpoints.
Endpoints allow users to perform full CRUD operations on topics, rooms, participants, messages, and user data.
Frontend and Styling:
  
- Future Plans:

Configure Token-Based Authentication: Implement token-based authentication to secure the application's API endpoints and ensure user data protection.
Enhance User Profiles: Provide users with more options to customize their profiles and add additional information, enhancing the community experience.
Real-Time Communication: Implement real-time communication features, such as live chat and notifications, using technologies like WebSockets or Django Channels.
### Endpoints:

- /api/topics/: Create, retrieve, update, and delete topics.
- /api/rooms/: Create, retrieve, update, and delete rooms within topics.
- /api/user/: Access user profiles and information, including avatars, names, and bios.
- /api/message/: Create, retrieve, update, and delete messages within rooms.


### Cloning the repository

1. Clone the repository:

        git clone <repository_url>

2. Create and activate a virtual environment (optional, but recommended):

       python3 -m venv env

       source env/bin/activate # On macOS/Linux

       .\env\Scripts\activate # On Windows

3. Install the project dependencies:

       pip install -r requirements.txt

4. Run database migrations:
    
       python manage.py migrate

5. Create a superuser (admin) for accessing the admin interface:
    
         python manage.py createsuperuser

6. Start the development server:

       python manage.py runserver
7. Access the application in your web browser at `http://localhost:8000/`.

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="projectScreenshots/home.png">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="projectScreenshots/room.png">  
</td>
<tr>
<td>
<p>User Profile</p>
<img src="projectScreenshots/user_profile.png" alt="User Profile">
</td>
<td>
<p>DRF documentation</p>
<img src="projectScreenshots/drf.png" alt="DRF documentation">
</td>
</tr>

</table>

