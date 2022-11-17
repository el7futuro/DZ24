from typing import Dict, Any

from marshmallow import Schema, fields, validates_schema, ValidationError

valid_cmd = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')


class RequestSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema()
    def validate_cmd(self, values: Dict[str, str], *args: Any, **kwargs: Any) -> Dict[str, str]:
        if values['cmd'] not in valid_cmd:
            raise ValidationError('cmd not valid')
        return values


class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
