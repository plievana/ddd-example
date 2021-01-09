from datetime import datetime
import uuid
from marshmallow import Schema, fields, validate


class User(Schema):
    id = fields.UUID(required=True)
    user_id = fields.UUID(missing=uuid.uuid4())
    name = fields.Str(validate=validate.Length(max=255))
    updated_at = fields.DateTime(missing=datetime.now())