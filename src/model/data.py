import datetime as dt

from marshmallow import Schema, fields


class Data(object):
    def __init__(self, description, amount, type):
        self.description = description
        self.prediction = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Data(name={self.description!r})>'.format(self=self)


class DataSchema(Schema):
    description = fields.Str()
    prediction = fields.Number()
    created_at = fields.Date()
    type = fields.Str()
