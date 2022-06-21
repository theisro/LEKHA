

# Lekha project file struture

The Lekha file is the main file for the django implementation of Lekha. It's contents include the various apps and files that pertain to Lekha's functioning. For the uninitiated to Django, well go over the file structure here and explain a few django concepts.

## Files:

### Lekha

Every django project starts with a file within it that has the same name as the project (a file called Lekha within Lekha) and a manage.py file. The manage.py file is the intereface to django through which you do everything including running the server, creating new apps, and managing the database. The Lekha file contains all the core code of the project, such as the settings.py and urls.py file. 

The settings.py file is the manifest that keeps track of your project: what apps are you using? Where are your static/template files located, etc. 

The urls.py file controls the routing behaviour of your website: what url's does your website contain and what happens when you visit those urls. Typically, you connect urls to views, which represent what the user sees when they go to a url. These views are located in apps.

### main (app):

The main file is the main app in Lekha. Django has a different strategy for website building than other frameworks, wherein each functionality is bundled into an "app" that does a specific thing. These apps can be bundled into packages and reused in other projects. A django project always has one or more apps that control's it's functionality. You cannot have a django project without an app, as views are defined in apps. Views control the behaviour of specific pages: what html is shown, what happens in the backend?

The main app as the name suggests is the main app of Lekha. It controls the general behaviour of several core pages of the Lekha app. The main app serves the landing page, about us, contact us, and bug report pages among others. It also contains some of the core models within lekha.

Models are django's way of defining database structures. Through django, we dont have to learn SQL and define database tables ourselves. Instead, you can define a python class in django within the models.py file, and django automatically creates a database structure within your database of choice according to the variables in your class definition. These python classes are called models.


### Accounts (app):

The accounts file is an application in Lekha that controls all of the account related things of Lekha, such as registering new users, and logging old ones back in. 

The views.py file within it serves the html for the register and login pages among others, and retrieves data from the forms on these pages in order to use them for authentication. 

The forms.py file in this app defines the forms used in the html pages, as django has a way to automatically generate html code for forms. 

### static:

The static folder contains all the static files in Lekha (images etc).
