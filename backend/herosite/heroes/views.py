from .models import Hero

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import HeroSerializer
# Create your views here.


@api_view(['GET', 'POST', 'DELETE'])
def getHeroes(request):
    if request.method == 'GET':
        heroes = Hero.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            heroes = heroes.filter(name__icontains=title)

        serializer = HeroSerializer(heroes, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        hero_data = JSONParser().parse(request)
        serializer = HeroSerializer(data=hero_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Hero.objects.all().delete()
        return JsonResponse({'message': '{} Heroes were deleted successfully!'.format(
            count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def getHero(request, pk):
    try:
        hero = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return JsonResponse({'message': 'The hero does not exist'}, 
        status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        hero_serializer = HeroSerializer(hero)
        return JsonResponse(hero_serializer.data)
    
    elif request.method == 'DELETE':
        hero.delete()
        return JsonResponse({'message': 'Hero was deleted successfully!'},
        status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        hero_serializer = HeroSerializer(hero, data=request.data)
        if hero_serializer.is_valid():
            hero_serializer.save()
            return JsonResponse(hero_serializer.data)
        return JsonResponse(hero_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
