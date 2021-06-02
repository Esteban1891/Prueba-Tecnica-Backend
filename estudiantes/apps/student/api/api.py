from apps.student.models import Student
from apps.student.api.serializers import StudentSerializer, StudentDetailSerializer, AdminDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Sum


@api_view(['GET','POST'])
def admin_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        try:
            if request.headers['auth'] == 'admin':
                users = Student.objects.all().values()
                users_serializer = StudentSerializer(users,many = True)
                return Response(users_serializer.data,status = status.HTTP_200_OK)
            else:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

        except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

    # create
    elif request.method == 'POST':
        try:
            user_serializer = StudentSerializer(data = request.data)
            if request.headers['auth'] == 'admin':

                # validation
                if user_serializer.is_valid():
                    user_serializer.save()            
                    return Response({'message':'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
                else:
                    return Response({'errors': 'solo se permite de 0 a 5'},status = status.HTTP_403_FORBIDDEN)
                
            else:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)
        except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)



@api_view(['GET','PUT'])
def student_detail_api_view(request,pk=None):
    # queryset
    user = Student.objects.filter(id = pk).first()

    # validation
    if user:

        # retrieve
        if request.method == 'GET': 
            try:
                if request.headers['auth'] == 'student':
                    user_serializer = StudentSerializer(user)
                    return Response(user_serializer.data,status = status.HTTP_200_OK)
                else:
                    return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

            except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)
        # update
        elif request.method == 'PUT':
            user_serializer = StudentDetailSerializer(user,data = request.data)
            try:
                if request.headers['auth'] == 'student':
                    if user_serializer.is_valid():
                        user_serializer.save()
                    else:
                        return Response({'errors': 'solo se permite de 0 a 5'},status = status.HTTP_403_FORBIDDEN)

                    return Response(user_serializer.data,status = status.HTTP_200_OK)
                else:
                    return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

            except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)
            

@api_view(['PUT'])
def admin_detail_api_view(request,pk=None):
    # queryset
    user = Student.objects.filter(id = pk).first()

    # validation
    if user:

        if request.method == 'PUT':
            user_serializer = AdminDetailSerializer(user,data = request.data)
            try:
                if request.headers['auth'] == 'admin':
                    if user_serializer.is_valid():
                        user_serializer.save()
                    else:
                        return Response({'errors': 'solo se permite de 0 a 5'},status = status.HTTP_403_FORBIDDEN)

                    return Response(user_serializer.data,status = status.HTTP_200_OK)
                    
                else:
                    return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

            except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)
                   


@api_view(['GET'])
def admin_list_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        try:
            if request.headers['auth'] == 'admin':
                s1 = Student.objects.aggregate(Sum('note'))["note__sum"]
                avg = s1/Student.objects.all().count()
                avg = round(avg, 2)
                return Response({'promedio de nota de todos los estudiantes':avg},status = status.HTTP_200_OK)
            else:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)

        except:
                return Response({'errors': 'usted no esta autorizado'},status = status.HTTP_403_FORBIDDEN)
