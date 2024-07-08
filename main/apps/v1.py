from django.urls import include, path


urlpatterns = [
    path(
        "user/",
        include(
            ("main.apps.user.urls", "main.apps.user.urls"),
            namespace="user",
        ),
    ),
    path(
        "file/",
        include(
            ("main.apps.file.urls", "main.apps.file.urls"),
            namespace="file",
        ),
    ),
]