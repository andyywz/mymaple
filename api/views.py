from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core import serializers

from .models import Daily

# Create your views here.
def index(req):
    data = Daily.objects.all()

    for daily in data:
        if daily.is_stale():
            daily.reset()

    res = serializers.serialize('json', data)
    return HttpResponse(res, content_type = 'application/json')

def show(req, daily_id):
    daily = get_object_or_404(Daily, pk=daily_id)

    if daily.is_stale():
        daily.reset()

    return HttpResponse("Data: %s %s" %(daily, daily.completed_at))
