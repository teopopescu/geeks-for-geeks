import graphene
from .gql_types import UserTypes, Users, Questions, Topics
from . import views


class MyQuery(graphene.ObjectType):

    user_by_id = graphene.Field(Users, user_id=graphene.Int())
    user_by_email = graphene.Field(Users, email=graphene.String())
    users = graphene.List(Users)
    user_types = graphene.List(UserTypes)
    questions = graphene.List(Questions)
    topics = graphene.List(Topics)

    def resolve_user_by_id(root, info, user_id):
        query_results = views.get_user_by_id(user_id)
        if len(query_results) == 1:
            return Users(**query_results[0])
        else:
            return {}

    def resolve_user_by_email(root, info, email):
        query_results = views.get_user_by_email(email)
        if len(query_results) == 1:
            return Users(**query_results[0])
        else:
            return {}

    def resolve_users(root, info):
        query_results = views.get_users()
        return_results = [Users(**row) for row in query_results]
        return return_results

    def resolve_user_types(root, info):
        query_results = views.get_user_types()
        return_results = [UserTypes(**row) for row in query_results]

        return return_results

    def resolve_questions(root, info):
        query_results = views.get_questions()
        return_results = [Questions(**row) for row in query_results]
        return return_results

    def resolve_topics(root, info):
        query_results = views.get_topics()
        return_results = [Topics(**row) for row in query_results]
        return return_results
