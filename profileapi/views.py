from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile, Project
from .serializers import ProfileSerializer

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})


@api_view(['GET', 'POST'])
def profile_api(request):
    if request.method == "POST":
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    profile = Profile.objects.first()
    return Response(ProfileSerializer(profile).data)


@api_view(['GET'])
def projects_by_skill(request):
    skill = request.GET.get("skill")

    if not skill:
        return Response({"error": "skill query param required"}, status=400)

    projects = []
    for project in Project.objects.all():
        if skill in project.profile.skills:
            projects.append(project.title)

    return Response(projects)
