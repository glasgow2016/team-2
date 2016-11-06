from maggies_webapp.models import StaffMember


def includeProfile(request):
    if request.user.is_authenticated():
        prof = StaffMember.objects.filter(user_mapping=request.user)
        if len(prof) == 1:
            return {"staffmember": prof[0]}
    return {}