from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from main.models import Category, Ingredient
from main import serializers


class Home(APIView):
    def get(self, request):
        return Response('HELLO WORLD! from Django.')

class CategoryViewSet(ModelViewSet):


    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class IngredientViewSet(ModelViewSet):

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
