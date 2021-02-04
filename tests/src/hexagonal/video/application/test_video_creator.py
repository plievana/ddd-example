from src.hexagonal.video.application.video_creator import VideoCreator
from tests.src.hexagonal.video.domain.video_mother import VideoMother


def test_create_video():
    video = VideoMother.create()
    # TODO 0 - inject repository and publisher

    video_creator = VideoCreator.create(video.id, video.title, video.duration_in_seconds, video.category)

    # TODO 1 - test video is in repository

    # TODO 2 - test publisher has published video message
