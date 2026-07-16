from django.contrib import admin
from .models import Server, Deployment


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):

    list_display = (

        "name",
        "ip_address",
        "operating_system",
        "status",
        "cpu_usage",

    )

    search_fields = (

        "name",
        "ip_address",

    )



@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):

    list_display = (

        "application",
        "version",
        "server",
        "status",
        "deployed_at",

    )

    search_fields = (

        "application",
        "version",

    )