from django.http import HttpResponse, HttpResponseRedirect


def profile(request):
    return HttpResponseRedirect('/vehicles/')