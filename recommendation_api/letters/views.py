from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from .models import Student, Professor, Skill, RecommendationRequest, RecommendationLetter
from .serializers import (
    StudentSerializer,
    ProfessorSerializer,
    SkillSerializer,
    RecommendationRequestSerializer,
    RecommendationLetterSerializer
)



class StudentListCreateAPIView(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProfessorListCreateAPIView(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



class SkillViewSet(ViewSet):

    def list(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        skill = Skill.objects.get(pk=pk)
        skill.delete()
        return Response({"message": "Skill deleted"})

class RecommendationRequestListCreateAPIView(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = RecommendationRequest.objects.all()
    serializer_class = RecommendationRequestSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class RecommendationRequestDetailAPIView(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = RecommendationRequest.objects.all()
    serializer_class = RecommendationRequestSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)



class RecommendationLetterViewSet(ModelViewSet):
    queryset = RecommendationLetter.objects.all()
    serializer_class = RecommendationLetterSerializer