from django.apps import AppConfig


class DepartmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'departments'

    def ready(self):
        import departments.management.commands.create_groups
