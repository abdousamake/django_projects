from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.
from cats.models import Cat, Comment

from django.views import View
from django.views import generic

from cats.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from cats.forms import CreateForm, CommentForm

class CatListView(OwnerListView):
    model = Cat
    template_name = "cat_list.html"

class CatDetailView(OwnerDetailView):
    model = Cat
    template_name = "cat_detail.html"
    def get(self, request, pk) :
        cat = Cat.objects.get(id=pk)
        comments = Comment.objects.filter(cat=cat).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'cat' : cat, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class CatCreateView(OwnerCreateView):
    model = Cat
    fields = ['name', 'foods', 'weight']
    template_name = "cat_form.html"

class CatUpdateView(OwnerUpdateView):
    model = Cat
    fields = ['name', 'foods', 'weight']
    template_name = "cat_form.html"

class CatDeleteView(OwnerDeleteView):
    model = Cat
    template_name = "cat_delete.html"

class CommentCreateView(OwnerCreateView):
    def post(self, request, pk) :
        f = get_object_or_404(Cat, id=pk)
        comment_form = CommentForm(request.POST)
        comment = Comment(text=request.POST['comment'], owner=request.user, cat=f)
        comment.save()
        return redirect(reverse_lazy('cat_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "cat_comment_delete.html"
