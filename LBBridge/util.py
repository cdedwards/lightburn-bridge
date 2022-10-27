# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/LBBridge/util.py
# Compiled at: 2021-09-14 07:18:28
# Size of source mod 2**32: 1304 bytes
import subprocess
from pathlib import Path
from subprocess import Popen
import shlex, os
from . import log

def shell_split(cmd, args, cwd=None, show_output=False):
    if cwd is None:
        cwd = os.getcwd()
    if show_output:
        log.info(f"Running: {cmd} {' '.join(args)}")
    process = Popen(([cmd] + args), shell=False,
      stdout=(subprocess.PIPE),
      stderr=(subprocess.STDOUT),
      cwd=cwd)
    output = ''
    while process.poll() is None:
        line = ''
        try:
            line = process.stdout.readline().decode('ascii')
        except:
            pass

        output += line
        line = line.rstrip()
        if line:
            if show_output:
                log.info(f"$> {line}")

    stdout, _ = process.communicate()
    line = ''
    try:
        line = stdout.decode('ascii')
    except:
        pass

    if line != '':
        output += line
        if show_output:
            line = line.rstrip()
            log.info(f"$> {line}")
    return (process.returncode, output)


def shell(cmd, cwd=None, show_output=True):
    split = shlex.split(cmd)
    cmd = split[0]
    args = []
    if len(split) > 1:
        args = split[1:]
    return shell_split(cmd, args, cwd, show_output)