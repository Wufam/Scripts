#!/usr/bin/python3
import subprocess
#подготовить файл passwd (vnc4passwd (выбрать файл) и внести пароль)
vnc = subprocess.run(["vncviewer", "-PasswordFile", "/home/user/.vnc/passwd"])
