import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request > is Httprequest > Django
    #  request.body
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)