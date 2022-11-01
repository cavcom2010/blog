from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    # We just imported this UserCreationForm.
    form_class = UserCreationForm
    """Usercreation form is built in for us."""
    success_url = reverse_lazy("login")
    """reverse_lazy function will load the url later when available."""
    template_name = "registration/signup.html"
    """template to be rendered."""