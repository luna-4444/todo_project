from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def webhook(request):
    data = request.body.decode("utf-8")
    pprint(request.body)

    # return HttpResponse("Hello, world. You're at the webhook.")
    return JsonResponse({"data": data})
