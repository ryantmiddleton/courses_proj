from django.shortcuts import render, redirect
from course_app.models import Course, Description, Comment 
from django.contrib import messages

# Create your views here.
def addCourse(request):
    if request.method == "POST":
        errors = Course.objects.validate_data(request.POST)
        if len(errors) > 0:
            for key, errormsg in errors.items():
                messages.error(request, errormsg)
            return redirect("/")

        else:
            Course.objects.create(
            name=request.POST['name_txt'],
            desc=Description.objects.create(content = request.POST['desc_txt'])
        )
        return redirect("/")
    else:
        try:
            context = {
                'all_courses':Course.objects.all()
            }
        except:
            context = None
        return render(request, "addCourse.html", context)

    return redirect("/")

def addComment(request, course_id):
    if request.method == "POST":
        errors = Comment.objects.validate_data(request.POST)
        if len(errors) > 0:
            for key, errormsg in errors.items():
                messages.error(request, errormsg)
            return redirect("/")

        else:
            new_comment = Comment.objects.create(
                content=request.POST['comment_txt'],
                course = Course.objects.get(id=course_id)
        )
        return redirect("/courses/comment/"+ str(new_comment.course.id))
    else:
        context = {
            'sel_course':Course.objects.get(id=course_id)
        }
        return render (request, "addComment.html", context)
    return redirect("/")

def deleteCourse(request, course_id):
    if request.method =="POST":
        Course.objects.get(id=course_id).delete()
        return redirect('/')
    else:
        context = {
            'sel_course':Course.objects.get(id=course_id)
        }
        return render(request, "deleteCourse.html", context)
    return redirect('/')