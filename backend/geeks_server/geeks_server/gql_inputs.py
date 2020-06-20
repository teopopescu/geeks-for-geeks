from graphene import ObjectType, Schema, String, Int, NonNull, List, Field, Mutation


class InputUserTypes(ObjectType):
    user_type_id = Int(required=True)
    user_type = NonNull(String)


class InputUsers(ObjectType):
    user_id = Int(required=True)
    user_type_id = Int()
    email = String()


class InputQuestions(ObjectType):
    question_id = Int(required=True)
    topic_id = Int()
    text = String()


class InputTopics(ObjectType):
    topic_id = Int(required=True)
    name = String(required=True)
    description = String()

