from maggies_webapp.models import StaffMember


def includeProfile(request):
    if request.user.is_authenticated():
        prof = StaffMember.objects.get(user_mapping=request.user)
        return {"staffmember": prof}
    return {}