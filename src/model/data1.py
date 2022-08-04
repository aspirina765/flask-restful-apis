from marshmallow import post_load

from .data import Data, DataSchema
from .data_type import DataType


class Data1(Data):
    def __init__(self, description, amount):
        super(Data1, self).__init__(description, -abs(amount), DataType.DATA1)

    def __repr__(self):
        return '<Data1(name={self.description!r})>'.format(self=self)


class Data1Schema(DataSchema):
    @post_load
    def make_data1(self, data):
        return Data1(**data)
