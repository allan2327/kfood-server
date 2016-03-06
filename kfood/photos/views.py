from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import PhotoForm
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
