from apps.api.resources import Resource
from apps.api.encoders.video import VideoEncoder
from src.hexagonal.video.application.video_searcher import VideoSearcher


class VideosGetResource(Resource):

    def get(self):
        return [VideoEncoder.encode(v) for v in VideoSearcher.all()]
