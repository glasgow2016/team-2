from maggies_webapp.models import Visit
from collections import Counter


def get_visitor_stats():
    columns = ["gender", "journey_stage", "nature_of_visit", "type", "cancer_site"]
    presets = {}
    values = Visit.objects.all().values_list("gender", "journey_stage", "nature_of_visit", "type", "cancer_site")
    for num in range(0, len(values[0])):
        b = map(lambda x: x[num], values)
        if b.__sizeof__() > 0:
            c = Counter(b)
            presets[columns[num]] = c.most_common(1)[0][0]
    print(presets)
    return presets


def most_common(lst):
    return max(lst, key=lst.count)
