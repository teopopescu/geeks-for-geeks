from .gql_queries import MyQuery
from .gql_mutations import MyMutations
from graphene import Schema

schema = Schema(query=MyQuery, mutation=MyMutations)
