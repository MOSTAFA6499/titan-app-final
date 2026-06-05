import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'titan_core.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# اینجا میتونی اطلاعات ادمین رو تغییر بدی
username = "titan_admin"
email = "admin@example.com"
password = "Admin12345678"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"ادمین {username} با موفقیت ساخته شد!")
else:
    print(f"ادمین {username} قبلاً وجود دارد.")
