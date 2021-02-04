from src.hexagonal.video.application.delete.video_deleter import VideoDeleter
from tests.src.hexagonal.video.domain.video_mother import VideoMother


def test_delete_video():
    video = VideoMother.create()
    # TODO 0 - inject repository and publisher

    user_deleter = VideoDeleter.delete(video.id)

    # TODO 1 - test video is not in repository

    # TODO 2 - test publisher has published video message
