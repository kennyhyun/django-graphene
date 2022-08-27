import graphene
from photo.schema import Query as photoQuery, Mutation as photoMutation
from books.schema import Query as booksQuery
from user.schema import Query as userQery, Mutation as userMutation
from graphene_django.debug import DjangoDebug

class Query(booksQuery, userQery, photoQuery, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')
    pass

class Mutation(userMutation, photoMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
