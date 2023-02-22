from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Novel, Director, Game, Tvshow, Stars, Author
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm
from .models import Review
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.



@login_required
def add_review(request, model_id, category_id):
    form = ReviewForm(request.POST)
    print(model_id, "model_id")
    print(category_id, "category_id")
    red_URL = ''
    if form.is_valid():
        new_review = form.save(commit=False)

        new_review.category_id = category_id
        new_review.reference_id = model_id
        new_review.save()

        if category_id == 1:

            red_URL = 'tvshows_detail'
        elif category_id == 2:
            red_URL = 'novels_detail'
        elif category_id == 3:
            red_URL = 'games_detail'
        elif category_id == 4:
            red_URL = 'stars_detail'
        elif category_id == 5:
            red_URL = 'directors_detail'
        elif category_id == 6:
            red_URL = 'authors_detail'
    return redirect(red_URL, pk=model_id)


class NovelList(LoginRequiredMixin, ListView):
    model = Novel
    paginate_by = 3


class NovelDetail(LoginRequiredMixin, DetailView):
    model = Novel

    def get_context_data(self, **kwargs):
        context = super(NovelDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=2)
        page = self.request.GET.get('page')
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context


class NovelCreate(LoginRequiredMixin, CreateView):
    model = Novel
    fields = ['title','sub_title','published_date','publisher','pages','author','image']
    success_url = '/novels/'

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        form.instance.user = self.request.user
        return super(NovelCreate, self).form_valid(form)


class NovelUpdate(LoginRequiredMixin, UpdateView):
    model = Novel
    fields = ['title','sub_title','published_date','publisher','pages','author','image']
    def get_queryset(self):
        qs = super(NovelUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class NovelDelete(LoginRequiredMixin, DeleteView):
    model = Novel
    success_url = '/novels/'
    def get_queryset(self):
        qs = super(NovelDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class AuthorList(LoginRequiredMixin, ListView):
    model = Author
    paginate_by = 3


class AuthorDetail(LoginRequiredMixin, DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=6)
        page = self.request.GET.get('page')
        # Show 3 reviews per page.
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context

    


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name','gender','nationality','dob','image']

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        form.instance.user = self.request.user
        return super(AuthorCreate, self).form_valid(form)

class AuthorUpdate(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['name','gender','nationality','dob','image']
    def get_queryset(self):
        qs = super(AuthorUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class AuthorDelete(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/authors/'
    def get_queryset(self):
        qs = super(AuthorDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    return render(request, 'contact.html')


# def signup(request):
#     error_message = ""
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = "Invalid signup - Please try again later"

#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)

# Director Views


class DirectorList(LoginRequiredMixin, ListView):
    model = Director
    paginate_by = 3


class DirectorDetail(LoginRequiredMixin, DetailView):
    model = Director
    
    def get_context_data(self, **kwargs):
        context = super(DirectorDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=5)
        page = self.request.GET.get('page')
        # Show 3 reviews per page.
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context


class DirectorCreate(LoginRequiredMixin, CreateView):
    model = Director
    fields = ['name', 'gender', 'nationality', 'dob', 'image']
    # '__all__'
    # ['name', 'gender', 'nationality', 'dob', 'image']

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        form.instance.user = self.request.user
        return super(DirectorCreate, self).form_valid(form)


class DirectorUpdate(LoginRequiredMixin, UpdateView):
    model = Director
    fields = ['name', 'gender', 'nationality', 'dob', 'image']
    def get_queryset(self):
        qs = super(DirectorUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class DirectorDelete(LoginRequiredMixin, DeleteView):
    model = Director
    success_url = '/directors/'
    def get_queryset(self):
        qs = super(DirectorDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)

# Game View......................................

class GameList(LoginRequiredMixin, ListView):
    model = Game
    paginate_by = 3


class GameDetail(LoginRequiredMixin, DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=3)
        page = self.request.GET.get('page')
        # Show 3 reviews per page.
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'subtitle', 'platform',
              'genre', 'release_date', 'image', 'novel']
    # '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(GameCreate, self).form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game

    fields = ['title', 'subtitle', 'platform',
              'genre', 'release_date', 'image']

    def get_queryset(self):
        qs = super(GameUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)



class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'

    def get_queryset(self):
        qs = super(GameDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)

# @login_required


# Tv shows CBV.........................................................

class ShowList(LoginRequiredMixin, ListView):
    model = Tvshow
    fields = ['title', 'type', 'genre', 'image']
    paginate_by = 3


class ShowDetail(LoginRequiredMixin, DetailView):
    model = Tvshow
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ShowDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=1)
        page = self.request.GET.get('page')
        # Show 3 reviews per page.
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context


class ShowCreate(LoginRequiredMixin, CreateView):
    model = Tvshow
    fields = ['title', 'type', 'genre', 'duration',
              'releaseDate', 'stars', 'image', 'director', 'novel', 'game']
    # ['title', 'type', 'genre', 'duration', 'releaseDate','stars']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ShowCreate, self).form_valid(form)


class ShowUpdate(LoginRequiredMixin, UpdateView):
    model = Tvshow
    fields = ['title', 'type', 'genre', 'duration',
              'releaseDate', 'stars', 'image', 'director']
    def get_queryset(self):
        qs = super(ShowUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class ShowDelete(LoginRequiredMixin, DeleteView):
    model = Tvshow
    success_url = '/tvshows/'
    def get_queryset(self):
        qs = super(ShowDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)

# STars CBV...........................................................

class StarList(LoginRequiredMixin, ListView):
    model = Stars
    fields = ['name', 'nationality', 'image']
    paginate_by = 3


class StarDetail(LoginRequiredMixin, DetailView):
    model = Stars
    fields = ['name', 'gender', 'nationality', 'dob', 'movies', 'image']
    # fields = ['name', 'gender', 'nationality', 'dob', 'movies', 'image']

    def get_context_data(self, **kwargs):
        context = super(StarDetail, self).get_context_data(**kwargs)
        review_form = ReviewForm()
        context['review_form'] = review_form
        all_reviews = Review.objects.filter(category_id=4)
        page = self.request.GET.get('page')
        context['all_reviews'] = Paginator(all_reviews, 5).get_page(page)
        return context


class StarCreate(LoginRequiredMixin, CreateView):
    model = Stars
    fields = ['name', 'gender', 'nationality', 'dob', 'movies', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(StarCreate, self).form_valid(form)


class StarUpdate(LoginRequiredMixin, UpdateView):
    model = Stars
    fields = ['name', 'gender', 'nationality', 'dob', 'movies', 'image']
    # ['name', 'gender', 'nationality', 'dob', 'movies', 'image']
    def get_queryset(self):
        qs = super(StarUpdate, self).get_queryset()
        return qs.filter(user_id=self.request.user)

class StarDelete(LoginRequiredMixin, DeleteView):
    model = Stars
    success_url = '/stars/'
    def get_queryset(self):
        qs = super(StarDelete, self).get_queryset()
        return qs.filter(user_id=self.request.user)


@login_required
def assoc_director(request, tvshow_id, director_id):
    # Add this director_id with the cat selected
    Tvshow.objects.get(id=tvshow_id).directors.add(director_id)
    return redirect('detail', tvshow_id=tvshow_id)

@login_required
def unassoc_director(request, tvshow_id, director_id):
    # Remove this director_id from the cat selected
    Tvshow.objects.get(id=tvshow_id).directors.remove(director_id)
    return redirect('tvshows_detail', tvshow_id=tvshow_id)