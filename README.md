Podcast API
This is a Flask-based RESTful API for managing podcast episodes, guests, and appearances. It provides endpoints to create, retrieve, and manage podcast-related data.

Table of Contents
Installation
Usage
API Endpoints
GET /
GET /episodes
GET /episodes/<id>
GET /guests
POST /appearances
Testing with Postman
Contributing
License
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/barangievans/phase-4-code-challenge.git
cd phase-4-code-challenge
Create a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database (SQLite is used in this project):

bash
Copy code
export FLASK_APP=app
flask run
Usage
Start the Flask server:

bash
Copy code
flask run
The API will be accessible at http://127.0.0.1:5000.

API Endpoints
GET /
Returns a welcome message and available endpoints.

Request:

http
Copy code
GET /
Response:

json
Copy code
{
  "message": "Welcome to the Podcast API!",
  "endpoints": {
    "/episodes": "Get all episodes",
    "/episodes/<int:id>": "Get a specific episode by ID",
    "/guests": "Get all guests",
    "/appearances": "Create a new appearance (POST)"
  }
}
GET /episodes
Retrieves all podcast episodes.

Request:

http
Copy code
GET /episodes
Response:

json
Copy code
[
  {
    "id": 1,
    "date": "2023-10-01",
    "number": 1
  },
  ...
]
GET /episodes/<id>
Retrieves a specific episode by its ID.

Request:

http
Copy code
GET /episodes/1
Response:

json
Copy code
{
  "id": 1,
  "date": "2023-10-01",
  "number": 1,
  "appearances": [
    {
      "id": 1,
      "guest": {
        "id": 1,
        "name": "Guest Name",
        "occupation": "Guest Occupation"
      },
      "rating": 5
    }
  ]
}
GET /guests
Retrieves all guests.

Request:

http
Copy code
GET /guests
Response:

json
Copy code
[
  {
    "id": 1,
    "name": "Guest Name",
    "occupation": "Guest Occupation"
  },
  ...
]
POST /appearances
Creates a new appearance for a guest on a specific episode.

Request:

http
Copy code
POST /appearances
Content-Type: application/json

{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 1
}
Response:

json
Copy code
{
  "id": 1,
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1,
  "episode": {
    "date": "2023-10-01",
    "id": 1,
    "number": 1
  },
  "guest": {
    "id": 1,
    "name": "Guest Name",
    "occupation": "Guest Occupation"
  }
}
Testing with Postman
To test the API using Postman:

Open Postman and create a new request.
Set the method to GET, POST, etc., based on the endpoint you want to test.
Enter the URL (e.g., http://127.0.0.1:5000/episodes).
For POST requests, select the Body tab, choose raw, and set the format to JSON.
Send the request and review the response.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to modify any sections as necessary!