from os.path import splitext
from uuid import uuid4
from time import time

from django.core.files.storage import FileSystemStorage


class UUIDFileStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        When saving changes the file name

        :param name:
        :param max_length:
        :return:
        """
        _, ext = splitext(name)
        file_name = '{}_{}{}'.format(uuid4().hex, int(time()), ext)

        return file_name
