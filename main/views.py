from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Record
from main.forms import RegistrationForm, RecordForm, PartialNewPostForm
from  django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from  django.contrib.auth import login

def detail(request):
    a = Record.objects.all()[::-1]
    return render(request, 'main/posts.html', {'records': a})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/qwer')
    else:
        form = RegistrationForm()
        arg = {'form' : form}
        return render(request, 'main/register.html', arg)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'main/auth.html'
    success_url = '/qwer'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class FormAddRecordView(FormView):
    form_class = PartialNewPostForm
    template_name = 'main/addpost.html'
    success_url = '/qwer'

    def form_valid(self, form):
        form = PartialNewPostForm(self.request.POST)
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super(FormAddRecordView, self).form_valid(form)


def home_page(request):
    return render(request, 'main/index.html')