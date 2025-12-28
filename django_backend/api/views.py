from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def about(request):
    data={'message':'This is from DRF Api for the about section',
            'status':'Success'}
    return Response(data)

@api_view(['GET'])
def contact(request):
        data={'message':'This is from DRF Api for the contact section',
                'status':'Success'}
        return Response(data)