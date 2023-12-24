from django.contrib import admin
from . models import Admin , Category ,User,Policy,PolicyRecord,Policyapply,Question

# Register your models here.
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Policy)

admin.site.register(Policyapply)
admin.site.register(Question)


