from __future__ import annotations

import re
import subprocess
import unicodedata
import sys


from jinja2.ext import Extension # type: ignore[import-untyped]


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default

def python_version() -> str:
    return f"{sys.version_info.major}.{sys.version_info.minor}"

def slugify(value, separator="-"):
    value = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^\w\s-]", "", value.lower())
    return re.sub(r"[-_\s]+", separator, value).strip("-_")


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email


class SlugifyExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["slugify"] = slugify

class PythonExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["python_version"] = python_version