import graphene
from . import views
from .gql_inputs import InputUserTypes, InputUsers, InputQuestions, InputTopics


class CreateUser(graphene.Mutation):
    class Arguments:
        user_type_id = graphene.Int()
        email = graphene.String()

    user = graphene.Field(InputUsers)

    def mutate(root, info, user_type_id, email):
        query_results = views.create_user(user_type_id, email)
        user = InputUsers(**query_results[0])
        return CreateUser(user=user)


class CreateTopic(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()

    topic = graphene.Field(InputTopics)

    def mutate(root, info, name, description):
        query_results = views.create_topic(name, description)
        topic = InputTopics(**query_results[0])
        return CreateTopic(topic=topic)


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_topic = CreateTopic.Field()


# class CreateQueInputTopicsstion(graphene.Mutation):
#     class Arguments:
#         description = graphene.String()

#     topic = graphene.Field(Topics)

#     def mutate(root, info, description):
#         query_results = views.create_topic(description)
#         topic = Topics(**query_results[0])
#         return CreateTopic(topic=topic)
