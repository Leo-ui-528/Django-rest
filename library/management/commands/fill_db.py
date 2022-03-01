from authapp.models import User

super_user = User.objects.create_superuser('django',
'django@geekshop.local', 'geekbrains', age=33)
