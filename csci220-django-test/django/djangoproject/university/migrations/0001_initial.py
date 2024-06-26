# Generated by Django 4.2.11 on 2024-04-11 23:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateField()),
                ('date_received', models.DateField()),
                ('app_type', models.CharField(choices=[('early_decision1', 'Early Decision I'), ('early_decision2', 'Early Decision II'), ('early_action', 'Early Action'), ('regular_decision', 'Regular Decision')], max_length=100)),
                ('app_status', models.CharField(choices=[('submitted', 'Submitted'), ('admitted', 'Admitted'), ('denied', 'Denied'), ('deferred', 'Deferred'), ('waitlisted', 'Waitlisted')], max_length=100)),
                ('essay', models.TextField(max_length=1000)),
                ('scholarship', models.IntegerField()),
                ('visited', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=20)),
                ('interview', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('grad_rate', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('tuition', models.FloatField()),
                ('c_type', models.CharField(choices=[('community_college', 'Community College'), ('technical_college', 'Technical College'), ('vocational_college', 'Vocational College'), ('public_university', 'Public University'), ('private_university', 'Private University')], default='Community College', max_length=100)),
                ('num_of_students', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('room_and_board', models.FloatField()),
                ('email_of_contact', models.EmailField(max_length=254, unique=True)),
                ('test_optional', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=20)),
                ('cost_after_aid', models.FloatField()),
                ('gpa_avg', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('act_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(36)])),
                ('math_SAT_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)])),
                ('eng_SAT_avg', models.IntegerField(validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)])),
            ],
        ),
        migrations.CreateModel(
            name='Extracurriculars',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('extracurricular_type', models.CharField(choices=[('sport', 'Sport'), ('art', 'Art'), ('community_service', 'Community Service'), ('career_development', 'Career_Development'), ('work', 'Work'), ('other', 'Other')], default='Sport')),
            ],
        ),
        migrations.CreateModel(
            name='Guidance_Counselor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SupplementaryQuestion',
            fields=[
                ('question_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.college')),
            ],
            options={
                'verbose_name_plural': 'Supplementary Questions',
            },
        ),
        migrations.CreateModel(
            name='SupplementaryQuestionAnswer',
            fields=[
                ('answer_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='university.supplementaryquestion')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('high_school', models.CharField(max_length=200)),
                ('parent_income', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('GPA', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(4.0)])),
                ('ACT', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(36)])),
                ('math_SAT', models.IntegerField(validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)])),
                ('eng_SAT', models.IntegerField(validators=[django.core.validators.MinValueValidator(200), django.core.validators.MaxValueValidator(800)])),
                ('guidance_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.guidance_counselor')),
            ],
        ),
        migrations.CreateModel(
            name='Participates_In',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('extracurricular_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.extracurriculars')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='college',
            constraint=models.CheckConstraint(check=models.Q(('grad_rate__gte', 0.0), ('grad_rate__lte', 100.0)), name='grad_rate_check'),
        ),
        migrations.AddConstraint(
            model_name='college',
            constraint=models.CheckConstraint(check=models.Q(('gpa_avg__gte', 0.0), ('gpa_avg__lte', 4.0)), name='college_GPA_avg_range'),
        ),
        migrations.AddConstraint(
            model_name='college',
            constraint=models.CheckConstraint(check=models.Q(('act_avg__gte', 1), ('act_avg__lte', 36)), name='college_ACT_avg_range'),
        ),
        migrations.AddConstraint(
            model_name='college',
            constraint=models.CheckConstraint(check=models.Q(('math_SAT_avg__gte', 200), ('math_SAT_avg__lte', 800)), name='math_SAT_avg_range'),
        ),
        migrations.AddConstraint(
            model_name='college',
            constraint=models.CheckConstraint(check=models.Q(('eng_SAT_avg__gte', 200), ('eng_SAT_avg__lte', 800)), name='eng_SAT_avg_range'),
        ),
        migrations.AddField(
            model_name='application',
            name='college_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.college'),
        ),
        migrations.AddField(
            model_name='application',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student'),
        ),
        migrations.AlterUniqueTogether(
            name='supplementaryquestion',
            unique_together={('college', 'question')},
        ),
    ]
