from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your views here.
from stars.models import Star, Comment

from django.views import View
from django.views import generic

from stars.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from stars.forms import CreateForm, CommentForm

class StarListView(OwnerListView):
    model = Star
    template_name = "star_list.html"

class StarDetailView(OwnerDetailView):
    model = Star
    template_name = "star_detail.html"
    def get(self, request, pk) :
        star = Star.objects.get(id=pk)
        comments = Comment.objects.filter(star=star).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'star' : star, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class StarCreateView(OwnerCreateView):
    model = Star
    fields = ['name', 'distance', 'diameter']
    template_name = "star_form.html"

class StarUpdateView(OwnerUpdateView):
    model = Star
    fields = ['name', 'distance', 'diameter']
    template_name = "star_form.html"

class StarDeleteView(OwnerDeleteView):
    model = Star
    template_name = "star_delete.html"

class CommentCreateView(OwnerCreateView):
    def post(self, request, pk) :
        f = get_object_or_404(Star, id=pk)
        comment_form = CommentForm(request.POST)
        comment = Comment(text=request.POST['comment'], owner=request.user, star=f)
        comment.save()
        return redirect(reverse_lazy('star_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "star_comment_delete.html"
