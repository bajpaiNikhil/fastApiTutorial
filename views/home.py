import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get('/')
@template()
def index():
    return {
        "package_count" : 254_030 ,
        "release_count": 254_030,
        "user_count": 254_030,
        "packages":[
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ]
    }


@router.get('/about')
@template()
def about():
    return {}
