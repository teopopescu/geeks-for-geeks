import graphene


class UserTypes(graphene.ObjectType):
    user_type_id = graphene.Int(required=True)
    user_type = graphene.NonNull(graphene.String)


class Users(graphene.ObjectType):
    user_id = graphene.Int(required=True)
    user_type_id = graphene.Int()
    email = graphene.String()


class Questions(graphene.ObjectType):
    question_id = graphene.Int(required=True)
    topic_id = graphene.Int()
    text = graphene.String()


class Topics(graphene.ObjectType):
    topic_id = graphene.Int(required=True)
    name = graphene.String(required=True)
    description = graphene.String()
