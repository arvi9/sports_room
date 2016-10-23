from django.contrib import admin

from .models import (
    Student, Equipment, BorrowedItem, Queue
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number", "fine")
    actions = ['reset_fine', ]

    class Media:
        js = ("js/action_buttons.js",)

    def reset_fine(self, request, queryset):
        queryset.update(fine=0)
        self.message_user(request, "Fine reset successfully")
    reset_fine.short_description = "Reset fine for selected students"


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('category', 'n_equipment')

    class Media:
        js = ("js/action_buttons.js",)


@admin.register(BorrowedItem)
class BorrowedItemAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'get_equipment', 'issue_date', 'due_date')
    actions = ['fine_paid', 'fine_due']

    class Media:
        js = ("js/action_buttons.js",)

    def get_student(self, obj):
        return obj.student.user.username
    get_student.short_description = "Name"

    def get_equipment(self, obj):
        return obj.equipment.category
    get_equipment.short_description = "Category"

    def fine_paid(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Update done")
    fine_paid.short_description = "Fine paid"

    def fine_due(self, request, queryset):
        # TODO
        # fine update logic
        # for obj in queryset:
        #   do something
        queryset.delete()
        self.message_user(request, "Fine added to cumulative fine. Update done")
    fine_due.short_description = "Fine pending"


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    list_display = ('get_student', 'get_equipment')
    actions = ['approve', ]

    class Media:
        js = ("js/action_buttons.js",)

    def get_student(self, obj):
        return obj.student.user.username
    get_student.short_description = "Name"

    def get_equipment(self, obj):
        return obj.equipment.category
    get_equipment.short_description = "Category"

    def approve(self, request, queryset):
        for obj in queryset:
            b = BorrowedItem(student=obj.student, equipment=obj.equipment)
            b.save()
        queryset.delete()
        self.message_user(request, "Request approved")
    approve.short_description = "Approve"
