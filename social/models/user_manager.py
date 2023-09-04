from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from ..constants import *
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_reader_user(self, username, password, **extra_fields):
        return self._create_custom_user(
            username=username,
            password=password,
            group_names=READER_GROUP,
            permissions=[
                CAN_NOTE_PERMISSION,
                CAN_READ_PERMISSION,
                CAN_CREATE_COLLECTION_PERMISSION
            ],
            **extra_fields
        )

    def create_professor_user(self, username, password, **extra_fields):
        return self._create_custom_user(
            username=username,
            password=password,
            group_names=PROFESSOR_GROUP,
            permissions=[
                CAN_NOTE_PERMISSION,
                CAN_READ_PERMISSION,
                CAN_CREATE_COLLECTION_PERMISSION,
                CAN_PUBLISH_PERMISSION
            ],
            **extra_fields
        )

    def _create_custom_user(self, username, password, group_names, permissions, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            **extra_fields
        )

        if isinstance(group_names, str):
            group_names = (group_names,)

        for group_name in group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

        from social.models.user import User
        content_type = ContentType.objects.get_for_model(User)

        for permission in permissions:
            permission, _ = Permission.objects.get_or_create(
                codename=permission,
                content_type=content_type
            )
            user.user_permissions.add(permission)

        return user
