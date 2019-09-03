from django.views.generic.edit import FormView

from restaurants.forms import UploadFileForm


class UploadFileView(FormView):
    form_class = UploadFileForm
    template_name = 'upload_form.html'
    success_url = ''
