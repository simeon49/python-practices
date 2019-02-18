#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MEnumMeta(type):
    def __new__(cls, name, bases, attrs):
        enum_tuple_dict = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                enum_tuple_dict[k] = v
                attrs[k] = v[0]
        # for k in enum_tuple_dict.keys():
        #     attrs.pop(k)
        attrs['__enum_tuple_dict__'] = enum_tuple_dict
        return type.__new__(cls, name, bases, attrs)


class MEnum(metaclass=MEnumMeta):

    @classmethod
    def get_tuples(cls):
        return list(cls.__enum_tuple_dict__.values())

    @classmethod
    def get_values(cls):
        return [x[0] for x in cls.__enum_tuple_dict__.values()]

    @classmethod
    def value_to_name(cls, value):
        for x in cls.__enum_tuple_dict__.values():
            if x[0] == value:
                return x[1]


if __name__ == '__main__':
    class EnumReviewResult(MEnum):
        NotReview = (0, "未审核")
        Pass = (1, "审核通过")
        NotPass = (2, "审核未通过")

    assert(EnumReviewResult.NotReview == 0)
    assert(EnumReviewResult.Pass == 1)
    assert(EnumReviewResult.NotPass == 2)

    assert(EnumReviewResult.value_to_name(2) == '审核未通过')
