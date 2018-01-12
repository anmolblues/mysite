import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_pub_date(self):
        return str(self.pub_date)
	

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14, blank=True, null=True)
    loc = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'

    def __str__(self):
        return self.dname


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    mgr = models.IntegerField(blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, models.DO_NOTHING, db_column='deptno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp'

    def __str__(self):
        return self.ename