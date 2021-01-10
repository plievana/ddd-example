from apps.api.resources import Resource
from apps.api.encoders.video import VideoEncoder


class VideosGetResource(Resource):

    def __init__(self, **kwargs):
        self.videos_searcher = kwargs.get('videos_searcher')

    def get(self):
        return [VideoEncoder.encode(v) for v in self.videos_searcher.all()]
