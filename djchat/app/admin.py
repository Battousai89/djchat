from django.contrib import admin
from app.models import User, Server, Channel, Message, Role, ServerMember

admin.site.register(User)
admin.site.register(Server)
admin.site.register(Channel)
admin.site.register(Message)
admin.site.register(Role)
admin.site.register(ServerMember)
