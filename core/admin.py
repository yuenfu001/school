from django.contrib import admin
from django.db.models import Avg
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from core.models import Person, Course, Grade

# Register your models here.
class GradeAdmin(admin.ModelAdmin):
    list_display = ("person","course","grade")

class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "view_students_link")
    list_filter = ('year',)
    def view_students_link(self, obj):
        count = obj.person_set.count()
        url = (
            reverse("admin:core_person_changelist")
            #reverse(admin:%(app)s_%(model)s_%(page)) = used to lookup a URL in the Django admin
            + "?"
            + urlencode({"courses__id" :f"{obj.id}"})
        )
        return format_html('<a href= "{}">{} Students</a>', url, count)
    view_students_link.short_description = "Students"

class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "show_average")

    def show_average(self, obj):

        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        return format_html("<b><i>{}</i></b>", result["grade__avg"])
    show_average.short_description = "Average Grade"

admin.site.register(Person, PersonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Grade, GradeAdmin)