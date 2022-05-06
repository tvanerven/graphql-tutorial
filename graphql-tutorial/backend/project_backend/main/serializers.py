from rest_framework.serializers import ModelSerializer

from main.models import Ingredient, Category


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class IngredientSerializer(ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'
