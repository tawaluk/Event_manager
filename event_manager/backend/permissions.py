from rest_framework.permissions import IsAuthenticated


class CustomPermission(IsAuthenticated):

    pass
