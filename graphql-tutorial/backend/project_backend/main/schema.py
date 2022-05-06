import graphene
from graphene_django import DjangoObjectType

from main.models import Category, Ingredient, Question

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "ingredients")

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id", "name", "notes", "category")

class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question

class QuestionMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        text = graphene.String(required=True)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, text, id):
        question = Question.objects.get(pk=id)
        question.text = text
        question.save()
        # Notice we return an instance of this mutation
        return QuestionMutation(question=question)

class QuestionCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String()

    question = graphene.Field(QuestionType)

    @classmethod
    def mutate(cls, root, info, text, title):
        question = Question.objects.create(
            text=text,
            title=title
        )
        return QuestionCreateMutation(question=question)


class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()
    create_question = QuestionCreateMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
