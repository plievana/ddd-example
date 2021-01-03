import uuid
from datetime import datetime
from marshmallow import Schema, fields, validate


class Video(Schema):
    id = fields.UUID(required=True)
    video_id = fields.UUID(missing=uuid.uuid4())
    title = fields.Str(required=True, validate=validate.Length(max=255))
    duration_in_seconds = fields.Int(required=True, validate=validate.Range(min=0))
    category = fields.Str(required=True, validate=validate.Length(max=255))
    creator_id = fields.UUID(required=True)
    updated_at = fields.DateTime(missing=datetime.now())
