from django.contrib import admin
from .models import Producer, Datas, Sensor

# Register your models here.
admin.site.register(Sensor)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_per_page = 200
    readonly_fields = ["user"]

    list_display = [
        "id",
        "user",
        "first_name",
        "last_name",
        "email",
        "region",
        "prefecture",
        "location",
        "greenhouse_number",
        "cultivation",
        "description",
    ]
    # list_filter = ("location", "cultivation")


@admin.register(Datas)
class dataAdmin(admin.ModelAdmin):
    list_display = ["id", "datetime", "sensor", "value", "gh_name", "user"]
    # readonly_fields = [
    #     "datetime",
    #     "sensor",
    #     "value",
    # ]
    # list_max_show_all = 500

    list_per_page = 50
