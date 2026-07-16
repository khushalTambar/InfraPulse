from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Server, Deployment


def home(request):

    return render(request, "index.html")


@login_required
def dashboard(request):

    servers = Server.objects.all()

    deployments = Deployment.objects.order_by("-deployed_at")[:5]

    online_servers = Server.objects.filter(status="Online").count()

    cpu_avg = round(
        sum(server.cpu_usage for server in servers) /
        max(len(servers), 1)
    )

    memory_avg = round(
        sum(server.memory_usage for server in servers) /
        max(len(servers), 1)
    )

    storage_avg = round(
        sum(server.storage_usage for server in servers) /
        max(len(servers), 1)
    )

    context = {

        "servers": servers,

        "deployments": deployments,

        "online_servers": online_servers,

        "cpu_avg": cpu_avg,

        "memory_avg": memory_avg,

        "storage_avg": storage_avg,

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context,
    )