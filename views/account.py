import fastapi
from fastapi_chameleon import template
from starlette import status
from starlette.requests import Request

from infrastructure import cookie_auth
from services import user_service
from viewmodels.account.account_viewModel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

router = fastapi.APIRouter()


@router.get('/account')
@template(template_file="account/index.pt")
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template(template_file="account/register.pt")
def register(request: Request):
    print("iamstupid")
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register')
@template(template_file="account/register.pt")
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()
    if vm.error:
        return vm.to_dict()
    # Create the account
    account = user_service.create_account(vm.name, vm.email, vm.password)
    # Login the user
    response = fastapi.responses.RedirectResponse(url="/account", status_code=status.HTTP_302_FOUND)
    # Post redirect
    cookie_auth.set_auth(response, account.id)
    print("post redirect")
    return response


@router.get('/account/login')
@template(template_file="account/login.pt")
# ################### LOGIN #################################

@router.get('/account/login')
@template(template_file='account/login.pt')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):

    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = user_service.login_user(vm.email, vm.password)
    if not user:
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get('/account/logout')
def logout():
    response = fastapi.responses.RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    # Post redirect
    cookie_auth.logout(response)
    return response
