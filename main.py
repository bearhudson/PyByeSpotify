import requests
import rich
import json
import base64
import hashlib
import html
import os
import getpass
from environs import *
from login import LoginClass


def main():
    user = LoginClass()
    user.get_access_token()
    user.get_playlists()


if __name__ == "__main__":
    main()
