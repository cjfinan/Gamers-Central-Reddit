# Gamers Central
Gamers Central is a inclusive gaming commuinity that creates a place to talk about all things games!
It allows its members to share their ideas, talk about other peoples topics all whilst styling thier own profiles to stand out from the crowd 

[Reponsive Design](INSERT LINK)

You can view The live site [here!](https://gamers-central.herokuapp.com/)

### Table of contents


## UX

### Site Purpose:
- The intent of this site is to bring anyone who loves games together.
- Gamers Central is a online gaming commuinty where the focus is on discussion and promoting individuality.
- Anyone can access the site, view and search for the posts or topics they are interested in.

### Site Goal:
To build a commuinty and place where people can share their views and ideas through creating their own posts aswell as, commenting on other peoples posts to create discussion.
Promote individuality through creating their own custom profiles.

### Audience:
For everyone who has a love for games. For people who want to have more in depth disscussions about certain gaming topics. Also for people who might be new to games and want to either know more or be apart of a commuinty.

### Communication:
A very minimal layout allows great communication between the site and user, easy to follow and clear navigation wherever you end up.

### Current User Goals:
For Gamers to easily create their own posts to start a conversation or be apart of someone else's by commenting. But also for people new to gaming who might be looking to be in the know.

### New User Goals:
To become istantly intregued and feel the urge to click on a post and navigate around

### Future Goals:
- Add direct messages between users
- Users to recieve their own notifications for when a post or comment has been approved
- Have a most engaged with post on each users profile
- Have a search filter where you can select certain topics

## User Stories

### Admin Stories:
1. As a Site Admin I can approve or reject comments so that I can manage and maintain appropriate comments
    - Story points: 1
2. As a site admin I can approve or decline posts so that the site can be managed and have appropriate content
    - Story points: 1

### Site User Stories:
1. As a Site User I can view the number of likes on each post so that I can see which is the most popular
    - Story points: 1

2. As a site user i can like and unlike a post so that I can interact with the community
    - Story points: 3

3. As a site user I can view a list of posts so that I can select one to read at a time
    - Story points: 1

4. As a Site User I can register an account so that I can post, comment and like
    - Story points: 2

5. As a Site User I can write comments on a post so that I can feel apart of the community
    - Story points: 3

6. As a site user I can create posts so that I am creating a conversation with others
    - Story points: 3

7. As a Site User I can create my own profile so that I can feel apart of the community
    - Story points: 4

8. As a Site User I can edit my profile so that I express my individuality
    - Story points: 2

9. As a Site User I can edit my settings so that I can change all of my details
    - Story points: 2

10. As a Site User I can search for content or the title of a post so that I can filter through what i want to see
    - Story points: 2

11. As a Site User I can edit my post in case i make any mistakes or it needs updating
    - Story points: 1

12. As a Site User delete my posts in case I no longer want it for people to see
    - Story points: 1

## Design
Wireframes:

Home page:

![Homepage](/static/images/homepage-wireframe.png)

Post page:

![Postpage](/static/images/post-detail-page.png)

Profile page:

![Profilepage](/static/images/profile-page.png)

Colour Palette:

![ColourPalette](/static/images/colour-palette.png)

### Font:
All fonts were obtained by the Google fonts library and i chose the following:
Poppins

### Imagery:
All imagery for the background and placeholders were supplied by me.

## Features

#### Home Page:

![Homepage](LINK HERE)

#### Navigation Bar:

![Navbar](LINK HERE)
#### Mobile:

![NavbarMobile](LINK HERE)

#### Post Page
![PostPage](LINK)

#### Profile Page
![ProfilePage](LINK)

#### Log in, Log Out and Sign up:
![Login](LINK)
![Logout](LINK)
![SignUp](LINK)

#### Create Post

![CreatePost](LINK)

#### Edit and delete Posts

![EditPost](LINK)
![DeletePost](LINK)

#### Comment on a post:
![Comment](LINK)

## Testing

1. User profiles showing posts that were yet to be approved:
    - [Expected] - Only posts from the user that have been approved to show on profile page
    - [Testing] - Tested this feature by creating a draft post and seeing if it turns up on the page
    - [Result] - Draft post showed on profile page
    - [Fix] - Added "status=1" to line of code
    - ![Test](/static/images/draft-post-test.png)


2. Error caused when viewing a post made by a user who has not created a profile:
    - [Expected] - User can create a post to be viewed without having to create a profile
    - [Testing] - Created a new user and made a post
    - [Result] - Error caused when trying to click this post
    - [Fix] - Added if statement to html where the profile link are only visible if the user has a "userprofile"
    - ![Test](/static/images/if-statement-test.png)


3. Reponse message to user when posting a comment:
    - [Expected] - When a authenticated user submits a comment a success message shows
    - [Testing] - Submit a comment as an authenticated user
    - [Result] - No response message showing
    - [Fix] - Remove '"commented": False' from the post function of the PostDetail View
    - ![Test](/static/images/comment-mesage-test.png)


4. User can create post as any user:
    - [Expected] - Authenticated users can only create posts as themselves
    - [Testing] - Created post as a authenticated user
    - [Result] - User can select which author(user) they would like to post as
    - [Fix] - Remove "author" from CreatePostForm and create author instance within PostCreate View
    - ![Test](/static/images/author-test1.png)
    - ![Test](/static/images/author-test2.png)


5. When voting on post from homepage, redirects to post detail page
    - [Expected] - When voting on a post from the home page it should refresh the page that you are on
    - [Testing] - Sign in and vote on a post from the home page
    - [Result] - Redirects you to the post detail page of that post
    - [Fix] - Change the HttpResponseRedirect within the respective Vote views so it gets the page that you are currently on
    - ![Test](/static/images/votes-test.png)


6. Error when clicking link to authors profile through the post detail page
    - [Expected] - If the posts author has a profile you should be able to view this
    - [Testing] - Click on the posts author link on the post detail page to try and view their profile
    - [Result] - Error "Reverse for 'view_profile' with arguments '('',)' not found."
    - [Fix] - Change the view profile url instead of getting the current user logged in use "post.author"
    - ![Test](/static/images/post-author-test.png)


7. Update Profile view not working
    - [Expected] - After submitting the form to update your profile it should redirect you to the home page
    - [Testing] - Update user profile and submit form
    - [Result] - Error message and does not redirect you to the homepage
    - [Fix] - Create a success_url in the UserEdit view
    - ![Test](/static/images/update-profile.png)


### Validator Testing

- HTML files pass through the W3C Validator with no issues
- Errors listed only reference {%%} and {{}} tags
- CSS files pass through the Jigsaw Validator with no issues
- Python files pass through Validator with no issues

#### Lighthouse

![Lighthouse](LINK)

### Technologies Used

#### Main Languages:
- HTML5
- CSS3
- Python
- SQL - Postgres

#### Frameworks, Libraries and Programs:
- Django
- Boostrap - to enhance user experiance and for faster development
- Google Fonts - to style the sites font
- Balsamiq - to create wireframes for all my pages
- Am i Responsive? - to create a screen shot of all device sizes
- Procreate - to create images for the site

#### Installed Packages:
- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote
- django-allauth
- django-crispy-forms

## Deployment
The site was deployed to Heroku:

- Go to Heroku and create a new app called gamers-central.
- Add the Heroku Postgres database to the Resources tab.
- Go to Settings Tab, to add the following key/value pairs to the configvars:
  - key: SECRET_KEY | value: randomkey
  - key: PORT | value: 8000
  - key: CLOUDINARY_URL | value: API environment variable
  - key: DATABASE_URL | value: value supplied by Heroku
  
- Add the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the env.py file

- Add DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file

- Add os statement for the env.py file.

- Add Heroku to ALLOWED_HOSTS in settings.py

- Create Procfile

- Push project to Github

- Connect github account to Heroku through the Deploy tab

- Connect github project repository, click "Deploy" button




