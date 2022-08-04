from marshmallow import post_load

from .data import Data, DataSchema
from .data_type import DataType


class Data2(Data):
    def __init__(self, description, amount):
        super(Data2, self).__init__(description, amount, DataType.DATA2)

    def __repr__(self):
        return '<Data2(name={self.description!r})>'.format(self=self)


class Data2Schema(DataSchema):
    @post_load
    def make_data2(self, data):
        return Data2(**data)
