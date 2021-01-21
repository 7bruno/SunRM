from ..models import Message
from . import ma


class MessageSchema(ma.SQLAlchemySchema):
    class Meta:

        model = Message

    id = ma.auto_field()
    classification = ma.auto_field()
    message = ma.auto_field()
    lead_id = ma.auto_field()
    seller_id = ma.auto_field()


message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)
