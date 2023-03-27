from django.conf import settings
from django.http import Http404
from django.shortcuts import render

def webclient(request):
    if not settings.WEBCLIENT_ENABLED:
        raise Http404

    pagevars = {"browser_sessid": request.session.session_key}
    return render(request, "new_webclient.html", pagevars)
