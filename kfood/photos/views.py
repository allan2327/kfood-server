from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import PhotoForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer
from .classifier import classify


def index(request):
    # Photo uploading view
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # Classify image
            label = classify(request.FILES['photo'].read())
            messages.success(
                request,
                "Photo upload successful. Classified as: {}".format(label))
            return HttpResponseRedirect(reverse('photos:index'))
        else:
            messages.warning(request, "Photo upload failed")
    else:
        form = PhotoForm()
    return render(request, 'photos/index.html', {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ClassifyView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return Response({"success": True}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        photo = request.data.get('photo', None)
        if photo:
            label = classify(photo.read())
            return Response({"success": True, "class": label})
        else:
            return Response({"success": False})
