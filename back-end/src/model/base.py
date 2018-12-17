from sqlalchemy import Column
from sqlalchemy.dialects.mysql import INTEGER


class BaseModel():
    id = Column(INTEGER(11), primary_key=True)
    @classmethod
    def find_by_id(cls, id, session):
        obj = session.query(cls).filter(cls.id == id).one()
        return obj

    @classmethod
    def find_all(cls, session):
        obj = session.query(cls).all()
        return obj

    @staticmethod
    def register(model, session):
        session.add(model)
        session.commit()

    @staticmethod
    def to_nested_obj(data, column_keys, key="id"):
        result = []
        user_id_list = []
        for d in data:
            if getattr(d[0], key) in user_id_list:
                for x in result:
                    if getattr(x, key) == getattr(d[0], key):
                        for i, column in enumerate(column_keys):
                            if getattr(x, column) == None:
                                setattr(x, column, [d[i + 1]])
                            else:
                                getattr(x, column).append(d[i + 1])
            else:
                x = d[0]
                for i, column in enumerate(column_keys):
                    setattr(x, column, [d[i + 1]])
                result.append(x)
                user_id_list.append(getattr(x, key))

        return result
