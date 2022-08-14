import graphene
from books.schema import Query as booksQuery
from user.schema import Query as userQery, Mutation as userMutation
from graphene_django.debug import DjangoDebug

class Query(booksQuery, userQery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    pass

class Mutation(userMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
