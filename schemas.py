from marshmallow import Schema, fields


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    # price = fields.Float(required=True)
    email = fields.Str(required=True)
    # no = fields.Str()


