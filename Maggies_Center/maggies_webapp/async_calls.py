from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import TempVisitNameMapping

import difflib


def get_suggestion(request, partial):
    temp_results = TempVisitNameMapping.objects.filter(
        visitor_name__icontains=partial)
    if len(temp_results) == 0:
        temp_results = []
        for visitor in TempVisitNameMapping.objects.all():
            if difflib.SequenceMatcher(None, visitor.visitor_name.lower(),
                                             partial.lower()).ratio() >= 0.78:
                temp_results += [{"name": visitor.visitor_name,
                                 "id": visitor.related_visit.id}]
        return JsonResponse(temp_results, safe=False)
    return JsonResponse([{"name": obj.visitor_name, "id": obj.related_visit.id}
                       for obj in temp_results], safe=False)
