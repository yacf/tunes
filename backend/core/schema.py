import graphene
import videos.schema

class Query(videos.schema.Query, graphene.ObjectType):
    pass

# class Mutation(graphene.ObjectType):
#     pass

schema = graphene.Schema(query=Query) #, mutation=Mutation)