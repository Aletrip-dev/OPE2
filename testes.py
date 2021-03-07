from django.contrib.auth.models import User
userList = User.objects.values()

print(userList)