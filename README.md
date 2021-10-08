# Capstone Proposal 

## This is a social media site for book lovers! Here, you’ll be able to easily keep track of what you’re currently reading, what you’ve read in the past, and what you’d like to read! You’ll also be able to update your progress as many times as you’d like and attach a comment. Finally, you’ll find multiple ways to connect with other book lovers! 


### Along with Django, Python, HTML, and CSS, this app will use:

- Materialize for the design
- The Google Books API to gather and present information about the books a user searches for 
- Vue to make axios calls and interact with the API



### Features


#### "As someone whose memory isn't amazing, I would like the ability to keep track of things I've read so I don't forget somewhere down the line"

- Allows a user to create an account, a personal profile and keep track of what they're reading at the moment, what they've read in the past, and what they'd like to read in the future

#### "As an avid reader, I would like the ability to chat with other readers because I like sharing my love for books with other people" 

- Through comments on a user's reading updates and a forum/chat room, users will be able to interact with other readers

#### "As someone who doesn't alwayas know what to read and/or doesn't always remember titles/authors, I want to be able to easily access a large collection of books to find what I'm looking for"

- Users can access Google Book's entire library through a quick and easy title, author, or keyword search



### Pages 

1. Main page: When the user first visits the website, they will be greeted by a main page that gives them an idea of what the app is all about and the ability to either login or sign up for an account

2. Timeline: Once they are logged in, they will be redirected to a twitter timeline like page. At the top of the page, there will be a place to compose a new reading update, which will be printed to the top of the timeline (updates from the people they follow will be printed below ((if the ability to follow other users does not get added, the timeline will just feature everybody in the system)))

3. Profile: At the top of each page, there will be a link to their personal profile. This will have an about the user section (a bio, photo, etc) and a section for all the books they’ve shelved (currently reading, read, want to read, and possibly other custom shelves like favorites) 

4. Browse: A page to look up books, which uses the Google Books API. Users will have the option to search by book title, author, or genre. They will search and it will print out basic information about the book, a link to buy/download the book, and the option to shelve it.

5. Chat room: This page will give the users the ability to chat with other users. Ideally, it will be sorted by genre. 



### Week by week schedule


#### Week One: 

- create bare bones of the main page, profile (with user info and shelves), book browsing page, and timeline
- set up user system with django (at least the functionality of the signup and login)
- some basic styling  
- set up models
- continue editing the content/styling of existing pages as time permits 

#### Week Two: 

- finish user system if not done already 
- set up page where users can search for books (using the Google Books API and Vue)  
- create django form for users to update their reading progress on timeline page
- add ability to like (and respond to if there's time) another user's update

#### Week Three: 

- add ability to respond to user's update if not done
- start working on chat feature 
- set up ability to follow other users
- more styling as time permits

#### Week Four: 
 
- finalize content and styling on all pages
- continue working on chat/following features if necessary 
- set up custom shelves on user profile if time permits



### Milestones

1. An app that has:

	- A main page that features a place for users to login or signup (redirecting to a new page)
	- A timeline that has updates from logged in user, as well as every authorized user
	- A profile for each user that has some basic info about them and stores what books they’ve read/are currently reading 
	- A page where users can search for books and get the book's basic information and where to buy or download it. They will also be given the option to add it to one of their shelves

2. In addition to the app in 1, this also features the ability to chat with and follow other users

3. The chat room is divided into genre (ie horror fans discuss only horror books) and the user is able to create custom shelves for their profile (favorites, read in 2021, etc)



### Data Model

- Book: title, author, image, boolean fields (currently reading/read/want to read)
- Shelves: currently reading, read, want to read (boolean fields)

    - ex: if book.currently_reading == 'true':
                {{ book.title }}

- User: name, image, bio, books (plus username and password from user app)
- readingUpdate: username, Book (title/author or image), update (text area), current page # (integer field)