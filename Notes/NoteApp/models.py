from django.db import models





# Create your models here.

class NoteAPP(models.Model):
    class Meta:
        db_table = 'notes'
        managed = True
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    Note_title = models.CharField(max_length=255)
    notes_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


