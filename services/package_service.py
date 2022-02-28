import datetime
from typing import Optional, List

from data.package import Package
from data.release import Release


def package_count() -> int:
    return 254_030


def release_count() -> int:
    return 254_030


def latest_packages(limit: int = 5) -> List:
    return [
               {'id': 'fastapi', 'summary': "A great web framework"},
               {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
               {'id': 'httpx', 'summary': "Requests for an async world"},
           ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name, "This is the summary", "Full details here!",
        "https://fastapi.tiangolo.com/", "MIT", "Sebastián Ramírez"
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())
