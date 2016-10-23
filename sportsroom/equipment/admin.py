from django.contrib import admin
from .models import Student, Equipment, BorrowedItem, Queue



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number")

class EquipmentAdmin(admin.ModelAdmin):
    list_display= ('category', 'n_equipment')

class BorrowedItemAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'get_equipment', 'issue_date', 'due_date')

    def get_student(self, obj):
        return obj.student.user.username
    get_student.short_description = "Name"

    def get_equipment(self, obj):
        return obj.equipment.category
    get_equipment.short_description = "Category"


class QueueAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'get_equipment')

    def get_student(self, obj):
        return obj.student.user.username
    get_student.short_description = "Name"

    def get_equipment(self, obj):
        return obj.equipment.category
    get_equipment.short_description = "Category"

admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(BorrowedItem, BorrowedItemAdmin)
admin.site.register(Queue, QueueAdmin)

