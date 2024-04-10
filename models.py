import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q

# Create your models here.
class Guidance_Counselor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    high_school = models.CharField(max_length=200)
    parent_income = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.00)])
    GPA = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(4.0)]) # assuming 0 to 4 scale)
    ACT = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    math_SAT = models.IntegerField(validators=[MinValueValidator(200), MaxValueValidator(800)])
    eng_SAT = models.IntegerField(validators=[MinValueValidator(200), MaxValueValidator(800)])
    guidance_ID = models.ForeignKey(Guidance_Counselor, null=False, on_delete=models.CASCADE)
    
class Extracurriculars(models.Model):
    ExtracurricularType = [
        ('sport', 'Sport'),
        ('art', 'Art'),
        ('community_service', 'Community Service'),
        ('career_development', 'Career_Development'),
        ('work', 'Work'),
        ('other', 'Other')
    ]
 
    name = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    extracurricular_type = models.CharField(choices=ExtracurricularType)

class Participates_In(models.Model):
    extracurricular_name = models.ForeignKey(Extracurriculars, null=False, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    hours =  models.IntegerField(validators=[MinValueValidator(1)])

class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    grad_rate = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)])
    tuition = models.FloatField()
    
    CollegeType = [
        ('community_college', 'Community College'),
        ('technical_college', 'Technical College'),
        ('vocational_college', 'Vocational College'),
        ('public_university', 'Public University'),
        ('private_university', 'Private University')
    ]
    
    c_type = models.CharField(choices=CollegeType, max_length=100)
    num_of_students = models.IntegerField(validators=[MinValueValidator(1)])
    room_and_board = models.FloatField()
    email_of_contact = models.EmailField(unique=True)
    
    Answer = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
        
    test_optional = models.CharField(choices=Answer, max_length=20)
    cost_after_aid = models.FloatField()
    GPA_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(4.0)])
    ACT_avg = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(36)])
    math_SAT_avg = models.IntegerField(validators=[MinValueValidator(200), MaxValueValidator(800)])
    eng_SAT_avg = models.IntegerField(validators=[MinValueValidator(200), MaxValueValidator(800)])

    class Meta:
        # Checks that the validator ranges are held within database
        constraints = [
            CheckConstraint(
                check=Q(grad_rate__gte=0.00) & Q(grad_rate__lte=100.00),
                name='grad_rate_check'
            ),
            CheckConstraint(
                check=Q(GPA_avg__gte=0.0) & Q(GPA_avg__lte=4.0),
                name='college_GPA_avg_range'
            ),
            CheckConstraint(
                check=Q(ACT_avg__gte=1) & Q(ACT_avg_lte=36),
                name='college_ACT_avg_range'
            ),
            CheckConstraint(
                check=Q(math_SAT_avg__gte=200) & Q(math_SAT_avg__lte=800),
                name='math_SAT_avg_range'
            ),
            CheckConstraint(
                check=Q(eng_SAT_avg__gte=200) & Q(eng_SAT_avg__lte=800),
                name='eng_SAT_avg_range'
                
            )
        ]
        
class Application(models.Model):
    student_id = models.ForeignKey(Student, null=False, on_delete=models.CASCADE)
    college_id = models.ForeignKey(College, null=False, on_delete=models.CASCADE)
    date_applied = models.DateField()
    date_received = models.DateField()
    
    AppType = [
        ('early_decision1', 'Early Decision I'),
        ('early_decision2', 'Early Decision II'),
        ('early_action', 'Early Action'),
        ('regular_decision', 'Regular Decision')
    ]
        
    app_type = models.CharField(choices=AppType, max_length=100)
    
    AppStatus = [
        ('submitted', 'Submitted'),
        ('admitted', 'Admitted'),
        ('denied', 'Denied'),
        ('deferred', 'Deferred'),
        ('waitlisted', 'Waitlisted')
    ]
        
    app_status = models.CharField(choices=AppStatus, max_length=100)
    essay = models.TextField(max_length=1000)
    scholarship = models.IntegerField()
    
    Answer = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
        
    visited = models.CharField(choices=Answer, max_length=20)
    interview = models.CharField(choices=Answer, max_length=20)
    
class SupplementaryQuestion(models.Model):  # Class names should be CamelCase without underscores
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)  # Use the model name directly
    question = models.TextField()

    class Meta:
        unique_together = ('college', 'question')  # This ensures uniqueness of the combination
        verbose_name_plural = "Supplementary Questions"
        
class SupplementaryQuestionAnswer(models.Model):  # CamelCase naming convention
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    question = models.ForeignKey(SupplementaryQuestion, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()

    def clean(self):
        # Ensure the question is linked to the specified college
        if not SupplementaryQuestion.objects.filter(pk=self.question.question_id, college=self.question.college).exists():
            raise ValidationError({'question': 'This question does not exist for the specified college.'})

    def __str__(self):
        return self.answer