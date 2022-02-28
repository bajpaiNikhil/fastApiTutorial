from typing import Optional

from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None

    async def load(self):
        form = await self.request.form()  # co routine
        self.name = form.get("name")
        self.password = form.get("password")
        self.email = form.get("email")

        if not self.name:
            self.error = "Name is required"
        elif not self.email:
            self.error = "email is required"
        elif len(self.password) < 4:
            self.error = "password is weak"
