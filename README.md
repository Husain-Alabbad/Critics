# Critics App

A full stack python and Django based web application where users can add and view ratings and reviews for different contents like tv shows (movies, series, anime), games and novels.
A Valid User can also create, list, update and delete contents like actors, authors, directors other than tv shows, games and novels.

# Technologies Used

**HTML**: for creating different templates that would be rendered on different pages or routes.

**CSS**: for styling the HTML templates and forms.

**PYTHON**: as backend language for writing codes and programs.

**DJANGO**: as python backend framework for application development.

**POSTGRES**: SQL database for storing and saving all the data related to our application.

**BOOTSTRAP**: for the layout and design of our application.

# General Approach

We decided to build a review and rating application for different contents like tv shows, games and novels. First of all we developed relationships between different entities
and linked them such as tv shows with actors and directors, novels with games and authors. We created our ERD on a piece of a paper and developed one to one, one to many and
many to many relationships between our app entities. For Our User model we related it to all the entities.

We divided the models upon each group members and started our app development by first creating the models followed by the definining our urls and routes in the main_app path
functions and then created views functions using the generic class based views. We created html templates for each of the models for listing, detailing, editing and deleting 
the model contents. Since we used the CBV approach, we used conventional names for our templates in order for the CBV to find the templates inside our main app folder. We created postgres database for our app using the pg-admin tool and migrated our models each time when required. All the CRUD operations were tested using Django administration
by creating a superuser and then using the main app to make sure everything works fine. 

The challenging part of the app development was to develop and implement the review and rating functionality for each of the models. For that a review model was created which includes the category id field having choices of different categories of contents from nested tuples. 

# Application Architecture

## Entity Relationship Diagram ERD

![5c04bb91-817c-40f2-8949-8f022f6ff001](https://media.git.generalassemb.ly/user/46587/files/79a2cba1-2e1a-4346-9375-dd85fdd4afea)

## User Stories

* As a user I should be able to register an account by clicking the signup button and submit my information.
* As a registered user I should be able to sign in to the app and view all the content such as TV shows, actors, directors, games, novels and authors and its rating and reviews.
* As a user I should be able to add a review and a rating to the list of available contents.
* As a user I should be able to add, edit and delete my own content such as TV shows, actors, directors, games, novels and authors.
* As a user I should be able to view and update my profile informations.

## Wireframes

![p03-wireframe-01](https://media.git.generalassemb.ly/user/46587/files/24240fd3-4acd-40f2-b413-209ce79ac536)
![p03-wireframe-02](https://media.git.generalassemb.ly/user/46587/files/cf9dcb08-76a4-4cc4-bdc4-b228734e188b)
![p03-wireframe-03](https://media.git.generalassemb.ly/user/46587/files/6917899c-a40d-4852-9004-5727de09eaa2)
![p03-wireframe-04](https://media.git.generalassemb.ly/user/46587/files/9a0b8463-0159-40cd-ab68-35e4b7e0f1d3)
![p03-wireframe-05](https://media.git.generalassemb.ly/user/46587/files/3dee8a71-b009-49c7-bd01-31c735d460e6)
![p03-wireframe-06](https://media.git.generalassemb.ly/user/46587/files/1e345070-8e7e-4c99-b156-4e19a20f6321)
![p03-wireframe-07](https://media.git.generalassemb.ly/user/46587/files/e996c05b-4c11-4817-ab47-e998c9fc866d)
![p03-wireframe-08](https://media.git.generalassemb.ly/user/46587/files/7267b166-cc31-49bb-a035-9beecd008637)
![p03-wireframe-09](https://media.git.generalassemb.ly/user/46587/files/1cb243cd-ccbf-46e0-9ea9-37b54845f645)
![p03-wireframe-10](https://media.git.generalassemb.ly/user/46587/files/c460ea74-1852-4bd9-aff4-f808b6b7f6db)









