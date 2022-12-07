import graphene
from graphene_django import DjangoObjectType
from users.models import Book, User


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'



class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_user_by_id(self, info, id1):
        try:
            return User.objects.get(id=id)

        except User.DoesNotExist:
            return None

    books_by_user_name = graphene.List(BookType, name=graphene.String(required=False))

    def resolve_books_by_user_name(self, info, name=None):
        books = Book.objects.all()

        if name:
            books = books.filter(user__name=name)
        return books


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")
#     schema = graphene.Schema(query=Query)

class UserMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, birthday_year, id1):
        user = User.objects.get(pk=id)
        user.birthday_year = birthday_year
        user.save()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    update_user = UserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
