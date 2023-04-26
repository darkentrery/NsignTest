from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from nsign.documents.forms import DocumentForm, DocumentUpdateForm
from nsign.documents.models import Document, Version


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        documents = Document.objects.all()
        update_forms = [{
            "form": DocumentUpdateForm(instance=obj),
            "obj": obj,
        } for obj in documents]
        context |= {
            "documents": documents,
            "form": DocumentForm,
            "update_forms": update_forms,
        }
        return context


class CreateDocumentView(CreateView):
    template_name = "index.html"
    success_url = reverse_lazy("index")
    form_class = DocumentForm
    model = Document

    def form_valid(self, form):
        self.object = form.save()
        Version.objects.create(document=self.object, name=self.object.name, description=self.object.description)
        return super().form_valid(form)


class UpdateDocumentView(UpdateView):
    template_name = "index.html"
    success_url = reverse_lazy("index")
    form_class = DocumentUpdateForm
    model = Document

    def form_valid(self, form):
        self.object = form.save()
        Version.objects.create(document=self.object, name=self.object.name, description=self.object.description,
                               version=self.object.last_version + 1)
        return super().form_valid(form)


class DeleteDocumentView(DeleteView):
    template_name = "index.html"
    success_url = reverse_lazy("index")
    form_class = DocumentUpdateForm
    model = Document
