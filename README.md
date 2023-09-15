# Flask RESTful Video API

This is a simple Flask RESTful API for managing video data, including information about video names, views, and likes. You can use this API to create, read, update, and delete video records.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- Required Python libraries can be installed using the `requirements.txt` file provided in this repository. You can install them using `pip`:

  ```bash
  pip install -r requirements.txt
  
SQLite database is used by default. You can change the database configuration in the Flask app settings if needed.

Getting Started
1. Clone the repository:
   - git clone https://github.com/DivyaBhardwaj04/flask-restful-video-api.git

2. Navigate to the project directory
   - cd flask-restful-video-api

3. Run the Flask application:
   - python app.py

The API will be available at `http://localhost:5000`.

API Endpoints
`GET /video/<int:video_id>`: Retrieve information about a specific video by its ID.
`PUT /video/<int:video_id>`: Create a new video record.
`PATCH /video/<int:video_id>`: Update an existing video record.
`DELETE /video/<int:video_id>`: Delete a video record.
Request and Response Formats
To create or update a video record, send a JSON payload with the required fields (`name`, `views`, `likes`).

Responses will be in JSON format, containing the video's ID, name, views, and likes.

Usage Examples
Create a new video record:
- curl -X PUT -H "Content-Type: application/json" -d '{"name": "Sample Video", "views": 100, "likes": 10}' http://localhost:5000/video/1

Retrieve video information:
- curl http://localhost:5000/video/1

Update video information:
- curl -X PATCH -H "Content-Type: application/json" -d '{"views": 150}' http://localhost:5000/video/1

Delete a video record:
- curl -X DELETE http://localhost:5000/video/1
