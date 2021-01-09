from apps.api.resources import Resource


class VideosGetResource(Resource):

    def __init__(self, **kwargs):
        self.videos_searcher = kwargs.get('videos_searcher')

    def get(self):
        return self.videos_searcher.all()
