from django.db import models


class Server(models.Model):

    STATUS_CHOICES = [

        ("Online", "Online"),
        ("Offline", "Offline"),
        ("Warning", "Warning"),

    ]

    name = models.CharField(max_length=100)

    ip_address = models.GenericIPAddressField()

    operating_system = models.CharField(max_length=100)

    cpu_usage = models.IntegerField(default=0)

    memory_usage = models.IntegerField(default=0)

    storage_usage = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Online",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


class Deployment(models.Model):

    STATUS_CHOICES = [

        ("Success", "Success"),
        ("Running", "Running"),
        ("Failed", "Failed"),

    ]

    application = models.CharField(max_length=100)

    version = models.CharField(max_length=30)

    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="deployments",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Success",
    )

    deployed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.application