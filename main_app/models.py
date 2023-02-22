from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.forms import ModelForm



# Create your models here.


GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)

NATIONALITY = (
    ('BHD', 'Bahrain'),
    ('KSA', 'Saudi Arabia'),
    ('USA', 'United States of America'),
    ('UAE', 'United Arab Emirates'),
    ('BRZ', 'Brazil'),
    ('AUS', 'Australia'),
)

CATEGORY = (
    ('1', 'TV Show'),
    ('2', 'Novel'),
    ('3', 'Game'),
    ('4', 'Star'),
    ('5', 'Director'),
    ('6', 'Author'),

)

RATING = (
    ('1', 'Really Bad'),
    ('2', 'Bad'),
    ('3', 'Average'),
    ('4', 'Above Average'),
    ('5', 'Extraordinary'),

)

GENRE = (
    ('Fight', 'Fight'),
    ('Sports', 'Sports'),
    ('Action', 'Action'),
    ('Puzzle', 'Puzzle'),
    ('Horror', 'Horror'),
    ('Comedy', 'Comedy'),
    ('Advernture', 'Adventure'),
    ('Sci-Fiction', 'Sci-Fiction')
)

SHOW = (
    ('Movies', 'Movies'),
    ('Series', 'Series'),
    ('Anime', 'Anime')
)



# Stars model..................................................................................................


class Stars(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=50, choices=GENDER, default=GENDER[0][0])
    nationality = models.CharField(
        max_length=50, choices=NATIONALITY, default=NATIONALITY[0][0])
    dob = models.DateField()
    movies = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    # Overridding
    def __str__(self):
        return self.name

    # Overridding
    def get_absolute_url(self):
        return reverse('stars_detail', kwargs={'pk': self.id})



# Director model...............................................................................
class Director(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=100, choices=GENDER, default=GENDER[0][0])
    nationality = models.CharField(
        max_length=25, choices=NATIONALITY, default=NATIONALITY[0][0])
    dob = models.DateField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('directors_detail', kwargs={'pk': self.id})


# Author model...............................................................................
class Author(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER, default=GENDER[0][0])
    nationality = models.CharField(max_length=25, choices=NATIONALITY, default=NATIONALITY[0][0])
    dob = models.DateField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('authors_detail', kwargs={'pk': self.id})

        
# Novel model...............................................................................
class Novel(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)
    published_date = models.DateField()
    publisher = models.CharField(max_length=50)
    pages = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('novels_detail', kwargs={'pk': self.id})


# Review model...............................................................................
class Review(models.Model):
    category_id = models.CharField(
        max_length=1, choices=CATEGORY, default=CATEGORY[0][0])
    reference_id = models.IntegerField()
    review = models.TextField()
    rating = models.CharField(
        max_length=1, choices=RATING, default=RATING[2][0])

    def __str__(self):
        return self.review
        
    # def reviews(self):
    #     return self.review_set.all()

    # def __str__(self):
    #     return f"{self.game.title} {self.get_review_display()}"
        # on {self.date}

    # class Meta:
    #     ordering = ['-date']

#  Game Model ........................................................
class Game(models.Model):

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="")
    platform = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE, default=GENRE[0][0])
    release_date = models.DateField()
    image = models.ImageField(upload_to='main_app/static/uploads', default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={'pk': self.id})

# TV shows model..................................................................................................
class Tvshow(models.Model):
    type = models.CharField(max_length=50, choices=SHOW, default=SHOW[0][0])
    title = models.CharField(max_length=50)
    duration = models.DurationField()
    genre = models.CharField(max_length=50, choices=GENRE, default=GENRE[0][0])
    releaseDate = models.DateField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default="")
    stars = models.ManyToManyField(Stars)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,blank=True, null=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE,blank=True, null=True)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    # Overridding
    def get_absolute_url(self):
        return reverse('tvshows_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


