from django.db.models.signals import post_save,pre_save,pre_init
from django.dispatch import receiver
from students.models import Students
from school_information.models import Candidate,Class
from school_manager.models import UserProfileInfo




@receiver(pre_save,sender = Students)
def self_student_candidate(sender,instance,**kwargs):
    exam_primary = Candidate.objects.get(name__icontains="Primary School Certificate")
    exam_primary_id = str(exam_primary.id)

    exam_junior = Candidate.objects.get(name__icontains="Junior School Certificate")
    exam_junior_id = str(exam_junior.id)

    exam_secondary = Candidate.objects.get(name__icontains="Secondary School Certificate")
    exam_secondary_id = str(exam_secondary.id)

    """to get all objects pk 
    all_class = Class.objects.all()
    all_class_id = all_class.values_list('id',flat=True)
    sot_class =sorted(all_class_id)
    """

    five = Class.objects.get(name__icontains='five')
    five_id = five.id
    eight = Class.objects.get(name__icontains='eight')
    eight_id = eight.id
    nine = Class.objects.get(name__icontains='nine')
    nive_id = nine.id
    ten = Class.objects.get(name__icontains='ten')
    ten_id = ten.id


    if instance.Class_id == five_id:
        instance.candidate_id = exam_primary_id

    elif instance.Class_id == eight_id:
        instance.candidate_id = exam_junior_id

    elif instance.Class_id == nive_id:
        instance.candidate_id = exam_secondary_id

    elif instance.Class_id == ten_id:
        instance.candidate_id = exam_secondary_id

    else:
        instance.candidate_id = None


        """post save
        # if instance.Sd_Candidate_id_id is None:
        #     instance.Sd_Candidate_id = exam_primary_id
        #     instance.save()
        """