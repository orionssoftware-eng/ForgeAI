class SecurityFilter:

    BLOCKED = [

        "import os",
        "import shutil",
        "import subprocess",
        "import socket",
        "eval(",
        "exec(",
        "__import__"

    ]

    @staticmethod
    def check(code):

        for item in SecurityFilter.BLOCKED:

            if item in code:

                return False, item

        return True, None