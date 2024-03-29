from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import TempVisitNameMapping
from .util import Util

import difflib


@login_required
def get_suggestion(request, partial, centre_id):
    temp_results = TempVisitNameMapping.objects.filter(
        visitor_name__icontains=partial, centre__pk=centre_id)
    if len(temp_results) == 0:
        temp_results = []
        for visitor in TempVisitNameMapping.objects.filter(
                centre__pk=centre_id):
            if difflib.SequenceMatcher(None, visitor.visitor_name.lower(),
                                             partial.lower()).ratio() >= 0.78:
                temp_results += [Util.generate_dict_from_instance(visitor)]
    else:
        temp_results = [Util.generate_dict_from_instance(x) for x in
                        temp_results]
    return JsonResponse(temp_results, safe=False)

@login_required
def visitor_left(request, person_id):
    print("Visitor with mapping id" + person_id + " left...")
    visitor_status = TempVisitNameMapping.objects.filter(pk=person_id)
    visitor_status.is_in_Building = False
    visitor_status.save()
