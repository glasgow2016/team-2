from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import TempVisitNameMapping

import json


def get_suggestion(request, partial):
    temp_results = TempVisitNameMapping.filter(visitor_name__icontains=partial)
    if len(temp_results) == 0:
        temp_results = []
        for visitor in TempVisitNameMapping.objects.all():
            #if ()
            pass
    return json.dumps([{"name": obj.visitor_name, "id": obj.related_visitor}
                       for obj in temp_results])
