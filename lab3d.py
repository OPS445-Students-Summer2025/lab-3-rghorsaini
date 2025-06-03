#!/usr/bin/env python3
# Author Name: Ranjan Ghorsaini
# Author ID: 144843224

import subprocess

def free_space():
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    stdout, stderr = p.communicate()
    return stdout.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
