from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from destinations.serializer import LoginSerializer,RegisterSerializer,DestinationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated



class LoginAPI(APIView):
    permission_classes = [AllowAny] 
    def post(self,request):
        token=0
        data=request.data
        serilizer=LoginSerializer(data=data)
        if not serilizer.is_valid():
            return Response({'status':False,'message':serilizer.errors},status.HTTP_400_BAD_REQUEST)
        
        user=authenticate(username=serilizer.data['username'],password=serilizer.data['password'])
        if not user:
            return Response({'status':True,'message':'invaild credinital','token':str(token)},status.HTTP_201_CREATED)
        token=Token.objects.get_or_create(user=user)
        return Response({'status':True,'message':'user login','token':str(token)},status.HTTP_201_CREATED)


        
class RegisterAPI(APIView):
    permission_classes = [AllowAny] 
    def post(self,request):
        data=request.data
        serilizer=RegisterSerializer(data=data)
        if not serilizer.is_valid():
            return Response({'status':False,'message':serilizer.errors},status.HTTP_400_BAD_REQUEST)
        serilizer.save()
        return Response({'status':True,'message':'user created'},status.HTTP_201_CREATED)


    
class DestinationListCreate(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DestinationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
# @api_view(['GET','POST','PUT'])
# def index(request):
#     courses={'course-name':'python','learn':['django','Tornado','FastApi'],'course-provider':'scaler'}
#     if request.method=='GET':
#        print(request.GET.get('search'))
#        print('you hit get')
#        return Response(courses)
#     elif request.method=='POST':
#        data=request.data
#        print(data)
#        print('you hit post')
#        return Response(courses)
#     elif request.method=='PUT':
#        print('you hit put')
#        return Response(courses)
#     return Response(courses)

# class peopleAPI(APIView):
#     def get(self,request):
#         objct = person.objects.all()
#         serializer = peopleSerializer(objct, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def post(self,request):
#         data = request.data
#         serializer = peopleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # def put(self,request):
    #     data = request.data
    #     try:
    #         if 'id' not in data:
    #            return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
    #         obj = person.objects.get(id=data['id'])
    #     except person.DoesNotExist:
    #         return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = peopleSerializer(obj, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    # def patch(self,request):
    #     data = request.data
    #     try:
    #         obj = person.objects.get(id=data['id'])
    #     except person.DoesNotExist:
    #         return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = peopleSerializer(obj, data=data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    # def delete(self,request):
    #     data = request.data
    #     print(f"Received data: {data}")  # Debugging line to print received data
    #     if 'id' not in data:
    #         return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         obj = person.objects.get(id=data['id'])
    #         obj.delete()
    #         return Response({'message': 'Person deleted'}, status=status.HTTP_200_OK)
    #     except person.DoesNotExist:
    #         return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @api_view(['GET', 'POST', 'PUT', 'PATCH','DELETE'])
# def people(request):
#     if request.method == 'GET':
#         objct = person.objects.all()
#         serializer = peopleSerializer(objct, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         data = request.data
#         serializer = peopleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'PUT':
#         data = request.data
#         try:
#             obj = person.objects.get(id=data['id'])
#         except person.DoesNotExist:
#             return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = peopleSerializer(obj, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     elif request.method == 'PATCH':
#         data = request.data
#         try:
#             obj = person.objects.get(id=data['id'])
#         except person.DoesNotExist:
#             return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = peopleSerializer(obj, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         data = request.data
#         print(f"Received data: {data}")  # Debugging line to print received data
#         if 'id' not in data:
#             return Response({'error': 'ID not provided'}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             obj = person.objects.get(id=data['id'])
#             obj.delete()
#             return Response({'message': 'Person deleted'}, status=status.HTTP_200_OK)
#         except person.DoesNotExist:
#             return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({'message': 'success'})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PeopleViewset(viewsets.ModelViewSet):
#     serializer_class = peopleSerializer
#     queryset = person.objects.all()
    
#     def list(self, request):
#         search = request.GET.get('search', None)
#         print(f"Search parameter: {search}")
#         queryset = self.queryset
#         if search:
#             queryset = queryset.filter(name__istartswith=search)
#         print(f"Filtered queryset: {queryset}")
#         serializer = peopleSerializer(queryset, many=True)
#         return Response({'status': status.HTTP_200_OK, 'data': serializer.data})


