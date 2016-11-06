from maggies_webapp.models import Centre, StaffMember


class Util(object):
    @staticmethod
    def generate_dict_from_instance(visitor):
         return {
                'name': visitor.visitor_name,
                'gender': visitor.related_visit.get_gender_display(),
                'cancer_type': visitor.related_visit.get_cancer_site_display(),
                'id': visitor.pk
         }

    @staticmethod
    def check_user_can_access(staffmember, visit):
        if staffmember.staff_type == "AD":
            return True
        centers = Centre.objects.filter(staffmember=staffmember)
        return visit.visit_site in centers

    @staticmethod
    def check_user_obj_can_access(user, visit):
        userprofile = StaffMember.objects.get(user_mapping=user)
        return Util.check_user_can_access(userprofile, visit)