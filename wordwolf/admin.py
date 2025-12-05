from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, WordSet, Question, Room, RoomQuestion, Member

admin.site.register(User, UserAdmin)
admin.site.register(WordSet)
admin.site.register(Question)
admin.site.register(Room)
admin.site.register(RoomQuestion)
admin.site.register(Member)
