from graphene import ObjectType, Schema, String, Int, NonNull, List, Field
from .views import get_user_types


class UserTypes(ObjectType):
    user_type_id = Int(required=True)
    user_type = NonNull(String)


class Users(ObjectType):
    user_id = Int(required=True)
    user_type_id = Int()
    email = String()


class Query(ObjectType):
    user = Field(Users, user_id=Int())
    users = List(Users)
    user_types = List(UserTypes)

    def resolve_user(root, info, user_id):
        return Users(user_id=user_id, user_type_id=1, email="asdf")

    def resolve_users(root, info):
        return [
            Users(user_id=1, user_type_id=1, email="asdf"),
            Users(user_id=2, user_type_id=1, email="asdf"),
        ]

    def resolve_user_types(root, info):
        query_results = get_user_types()
        return_results = []
        for row in query_results:
            return_results.append(UserTypes(user_type_id=row[0], user_type=row[1]))

        return return_results


schema = Schema(query=Query)
# results = schema.execute(
#     """
#         query {
#             user(userId: 1) {
#                 userId
#                 userTypeId
#                 email
#             }
#         }
#         """
# )

# print(results.data)

# results = schema.execute(
#     """
#         {
#             users {
#                 userId
#                 userTypeId
#                 email
#             }
#         }
#         """
# )

# print(results.data)
