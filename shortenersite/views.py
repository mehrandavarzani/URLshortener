from django.shortcuts import render, get_object_or_404
import random, string, json
from shortenersite.models import Url
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.checks.security import csrf

def index(request):
    return render(request,'shortenersite/index.html',{})


def redirect_original(request, short_id):
    url = get_object_or_404(Url, pk=short_id)  # get object, if not        found return 404 error
    return HttpResponseRedirect(url.orginalurl)

def shorten_url(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        short_id = get_short_code()
        b = Url(orginalurl=url, shortid=short_id)
        b.save()
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + short_id
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    # if the randomly generated short_id is used then generate next
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            temp = Url.objects.get(pk=short_id)
        except:
            return short_id
