from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics, status
from.models import Students, Teachers, Course
from.serializer import StudentSerializer, TeacherSerializer, CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



'''example'''

""" @APIView['GET','POST','DELETE'] """
class CourseView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer =CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        courseSerializer =CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data,status=status.HTTP_201_CREATED)

        return Response(courseSerializer.error)
 

class CourseListView(APIView):
    def delete(self, request, pk):
        queryset = get_object_or_404(Course, id=pk)
        queryset.delete()
        return Response({"status":"success", "data":"deteted"})

    def get(self,request,pk):
         course = Course.objects.get(id=pk)
         serializer =CourseSerializer(course)
         return Response(serializer.data)
''' using mixins'''


class TeacherListView(mixins.ListModelMixin, mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request):
        return self.list(request)

    def put(self, request):
        return self.create(request)
        


class TeacherDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)


'''Using GenericAPI View'''

 
class StndList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class StudentDetailapiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer 


