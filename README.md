# True Crime Story Time #

This is a blogging website for true crime lovers to unite and read about some of the most famous spine-tingling true crime cases.   It allows users to read blog posts or like posts as a member.  Non-members have the ability to browse through blog posts and can sign up as a member if they wish to interact with a post with a like.  

Admin has the ability to create, read, update and delete posts.

You can view the live site [here](https://truecrimestorytime.herokuapp.com/)

<h2 align ="center"><img src = "assets/docs/am_i_responsive.png"></h2>

# User Experience #

## User Stories ##

I used the Agile Methodology Tool on Github to plan my project and use as a to do list.  I would move the issues I was working on across from the To Do column to the In Progress column.  Completed issues would then be dragged across to the Done column.  

<h2 align ="center"><img src = "assets/docs/agilemeth.png"></h2>

## General User Goals ##
- As a user, upon landing on the website, I want to know immediately what it is about
- As a user, I want to be able to browse a selection of true crime blog posts and choose which one I want to read
- As a user, I want to be able to click on a post to access the whole blog post
- As a user/admin, I want the number of likes on each post to be visible so that I can easily see which ones are popular
- As a user/admin, I want to be able to create an account and log in to view/read/create posts

## Member User Goals ##
- As a user with an account, I want to be able to log in easily and be remembered
- As a user with an account, I want to be able to like or unlike blog posts
- As a user with an account, I want to be able to log out 

## Non Member User Goals ##
- As a user without an account, I want to be able to browse and read blog posts
- As a user without an account, I want the option to sign up and create an account

## Admin User Goals ##
- As admin, I want to create, read, update and delete posts so that I can manage my blog content
- As admin, I want the option to write draft posts that can be saved and posted later 

## Relationship Diagram ##

<h2 align ="center"><img src = "assets/docs/relationshipdiagram.png"></h2>

# Design

## Wireframes

## Landing Page (non member) 

Non members are able to browse through blog posts, view number of likes on each post and have the option to sign up and create an account 

<h2 align ="center"><img src = "assets/docs/landingpage.png"></h2>

## Landing Page (member) 

Members are able to browse through blog posts, view number of likes on each post and have the option to log out 

<h2 align ="center"><img src = "assets/docs/landing_member.png"></h2>

## Blog Post Page (member)

Members are able to like or unlike posts

<h2 align ="center"><img src = "assets/docs/blogpost_member.png"></h2>

## Blog Post Page (non member)

Non members can read blog posts without the option to like 

<h2 align ="center"><img src = "assets/docs/blogpost_nonmember.png"></h2>

## Log In Page 

<h2 align ="center"><img src = "assets/docs/login.png"></h2>

## Log Out Page 

<h2 align ="center"><img src = "assets/docs/logout.png"></h2>

# Features

## Navigation Bar
- The navigation bar is fully responsive.  It has links to log in, home, sign up and log out.  The logo to the left is also a link to the home page.

<h2 align ="center"><img src = "assets/docs/navbar.png"></h2>

## Posts 

- Blog posts feature the author, blog post title, date and time stamps, likes and like count.  This section displays 3 posts and site pagination exists if more posts are created (next/prev).  Hover feature exists on next/prev links.

<h2 align ="center"><img src = "assets/docs/blogposts.png"></h2>

## Post Detail

- When a user clicks on a blog post, they are taken to a new page to read the full blog post.  This page also contains, author, blog post title, date and time stamps, likes and like count.  Users who are members are also able to like posts by clicking on the heart icon.  

<h2 align ="center"><img src = "assets/docs/post_detail.png"></h2>


## Footer 
- The footer has social links that are working.  

<h2 align ="center"><img src = "assets/docs/footer.png"></h2>

## Sign Up 
- Non members are able to create a new account via the sign up link.  Existing members can also log in from here.

<h2 align ="center"><img src = "assets/docs/signup.png"></h2>

## Login 
- Members can log into their account to like posts.  Non members can also sign up from here.

<h2 align ="center"><img src = "assets/docs/log_in.png"></h2>

## Logout
- Members can log out of their account.

<h2 align ="center"><img src = "assets/docs/signout.png"></h2>

## Admin
- Admin is able to create, read, update and delete posts from the backend.  
- Images can be added to new or existing posts by Admin.  
- Likes can be monitored from the backend allowing Admin to see which users have liked what
- Posts can be saved as drafts and finished later 
- Admin can delete selected users if necessary 

# Technologies

## Languages
- HTML5
- CSS3
- JavaScript
- Python3

## Frameworks, Libraries & Programs
- Balsamiq
Balsamiq was used for wireframes
- Bootstrap
Bootstrap templates
- Cloudinary
Cloudinary was used to store the placeholder image
- Django
Django built the app
- Django Allauth
Django allauth for account creation and management
Font Awesome
- Font Awesome was used for the like heart icon
- Google Fonts
Imported fonts used from Google Fonts
- Heroku
Heroku was used for hosting and deploying the site
- PostgreSQL
PostgreSQL for database management
- Summernote
Summernote WYSIWYG for Bootstrap




















