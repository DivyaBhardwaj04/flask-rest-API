from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"

# if __name__ == "__main__":
#     with app.app_context():
#         # Create the database tables within the app context
#         db.create_all()
#     app.run(debug=True)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help = "Name of the video", required = True)
video_put_args.add_argument("views", type=int, help = "Views of the video", required = True)
video_put_args.add_argument("likes", type=int, help = "Likes the video", required = True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help = "Name of the video")
video_update_args.add_argument("views", type=int, help = "Views of the video")
video_update_args.add_argument("likes", type=int, help = "Likes the video")

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'views' : fields.Integer,
    'likes' : fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModle.query.filter_by(id = video_id).first()
        if not result:
            abort(409, message = "Error! Not Found.")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModle.query.filter_by(id = video_id).first()
        if result:
            abort(409, message = "Video Id Taken...")
        video = VideoModle(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModle.query.filter_by(id = video_id).first()
        if not result:
            abort(409, message = "Error! Not Found, Cannot Update")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']


        db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, video_id):
        video = VideoModle.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message="Video not found.")
        db.session.delete(video)
        db.session.commit()
        return '',204

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug = True)
