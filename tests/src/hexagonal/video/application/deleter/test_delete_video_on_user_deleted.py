from src.hexagonal.video.application.delete.delete_videos_on_user_deleted import DeleteVideoOnUserDeleted
from tests.src.hexagonal.user.domain.user_created_domain_event import UserDeletedDomainEventMother


def test_delete_video_on_user_deleted():
    event = UserDeletedDomainEventMother.create()

    # Option 1: invoke use case and check result
    # TODO create video with user_id
    # When event is pushed into bus
    DeleteVideoOnUserDeleted.invoke(event)

    # TODO ensure video does not exist
