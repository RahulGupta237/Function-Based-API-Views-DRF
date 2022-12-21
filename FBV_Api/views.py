from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

# @api_view()
# def Home_api(request):
#     return Response({'msg':"Helllow World"})

from .models import Student
from .serializer import student_serializer

@api_view(['POST','GET','PUT','DELETE'])
def Home_api(request):
    if request.method=="GET":
        id = request.data.get('id')
        if id is not None:
            st=Student.objects.get(id=id)
            serializer=student_serializer(st)
            print(type(serializer),serializer)
            return Response(serializer.data)

        st=Student.objects.all()
        serializer=student_serializer(st,many=True)
        return Response(serializer.data)

    if request.method=="POST":
        # print(type(request.data))
        # return Response({'msg':"THis is Post request",'data':request.data})
        serializer=student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data successfully created"})
        return Response(serializer.error)
        

    if request.method=="PUT":
        # print(type(request.data))
        # return Response({'msg':"THis is Put request"})
        if request.method=='PUT':
            id=request.data.get('id')
            st=Student.objects.get(pk=id)
            serializer=student_serializer(st,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Data sucessfully udated"})
            return Response(serializer.error)
    if request.method=="DELETE":
        # print(type(request.data))
        # return Response({'msg':"THis is Put request"})
        
            id=request.data.get('id')
            st=Student.objects.get(pk=id)
            st.delete()
            
            return Response({"msg":"Data Successfully deleted"})
         
