
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser, Department, Equipment, MaintenanceRecord,
    ActivityLog, AdminRegistration, Inventory
)

# ----------------------------
# Custom User Admin
# ----------------------------
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)


# ----------------------------
# Department Admin
# ----------------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# ----------------------------
# Equipment Admin
# ----------------------------
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'department', 'status', 'purchase_date')
    list_filter = ('status', 'department')
    search_fields = ('name', 'serial_number')


# ----------------------------
# Maintenance Record Admin
# ----------------------------
@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'performed_by', 'date', 'cost')
    list_filter = ('date', 'performed_by')
    search_fields = ('equipment__name', 'performed_by__username')


# ----------------------------
# Activity Log Admin
# ----------------------------
@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'action')


# ----------------------------
# Admin Registration Admin
# ----------------------------
@admin.register(AdminRegistration)
class AdminRegistrationAdmin(admin.ModelAdmin):
    list_display = ('admin_user', 'registration_date', 'verified')
    list_filter = ('verified', 'registration_date')
    search_fields = ('admin_user__username',)


# ----------------------------
# Inventory Admin
# ----------------------------
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'quantity', 'location', 'last_updated')
    list_filter = ('location',)
    search_fields = ('equipment__name', 'location')
