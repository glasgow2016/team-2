from maggies_webapp.models import Visit

def get_visitor_stats():
    presets = {}
    values = Visit.objects.all().values_list("gender", "journey_stage", "visit_site", "nature_of_visit",
                  "cancer_site", "seen_by", "type", "activities")
    #for visitor in values:
    b = map(lambda x: x[0], values)
    for i in b:
        print(i)
    most_common(b)



def most_common(lst):
    return max(lst, key=lst.count)
