from django.db import models

# Create your models here.

# class DesriptionManager(models.Manager):
#     def validate_data(self, postData):
#         errors = {}
#         if len(postData['description_txt']) < 15:
#             errors["description"] = "Description should be at least 15 characters long"
#         return errors

class Description(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = DesriptionManager()

class CourseManager(models.Manager):
    def validate_data(self, postData):
        errors = {}
        if len(postData['name_txt']) < 5:
            errors["name"] = "Name should be at least 5 characters long."
        if len(postData['desc_txt']) < 15:
            errors["description"] = "Description should be at least 15 characters long"
        # if len(postData['comment_txt']) < 15:
        #     errors["comment"] = "Comment should be at least 15 characters long"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    #One descrption for one course
    desc = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class CommentManager(models.Manager):
    def validate_data(self, postData):
        errors = {}
        if len(postData['comment_txt']) < 15:
            errors["comment"] = "Comment should be at least 15 characters long"
        return errors

class Comment(models.Model):
    content = models.TextField()
    #Many comments for one course
    course =  models.ForeignKey(
        Course, 
        related_name="comments", 
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()