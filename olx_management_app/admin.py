from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Signup)
admin.site.register(Addproduct)
admin.site.register(ProductRequest)
admin.site.register(LoginRequest)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Notification)
admin.site.register(SignupRequest)
admin.site.register(SignupRequestNotification)
admin.site.register(UserNotification)
admin.site.register(ProblemReport)
admin.site.register(AdminNotification)
admin.site.register(OverdueProductNotification)
admin.site.register(ChatMessage)
admin.site.register(PaymentHistory)
admin.site.register(Feedback)
admin.site.register(ChatMessageData)
admin.site.register(SubCategory)

