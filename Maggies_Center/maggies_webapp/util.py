
class Util(object):
    @staticmethod
    def generate_dict_from_instance(visitor):
         return {
                'name': visitor.visitor_name,
                'gender': visitor.related_visit.get_gender_display(),
                'cancer_type': visitor.related_visit.get_cancer_site_display(),
                'id': visitor.id
            }
