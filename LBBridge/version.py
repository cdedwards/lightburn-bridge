# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.3 (main, Jul 25 2022, 17:09:16) [Clang 13.0.0 (clang-1300.0.27.3)]
# Embedded file name: /boot/LBBridge/LBBridge/version.py
# Compiled at: 2021-09-13 10:26:38
# Size of source mod 2**32: 193 bytes
__version__ = (1, 0, 0, "RC3")


def version_str():
    v = [str(i) for i in __version__]
    res = ".".join(v[0:3])
    if len(v) > 3:
        if v[3]:
            res += f"-{v[3]}"
    return res
