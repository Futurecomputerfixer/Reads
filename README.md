# Reads 
# Distinctiveness and Complexity
This web application is used to help people with library book checkouts. 
At first the libararian needs to store the book information in the database with columns:title, author, how many people have checkouted this book(default to be 0 when the book data is just inserted to the database, and a link to an image )
When a user(likely a student) log in, two pages will be display: 
one is the library page, providing book recommendations for the user. All books from the library will be pulled out(minus the books that the user checked out before) ranked by the number of checkouts by other users. The user can directly checkout a book from this library page and a reminder for the date to return the book(7 days after the checkout date) will be showen. Each book displayed has its title, author, and a image. All book div have flex display wrap so when using it on a mobile device with smaller screen, the web page will display as usual.
The other one, also the index page, displays all the books the user checked out.Each Book box shows returned if the user has returned the book, or shows the deadline to return the book. The user can return books by clicking the button "return". 

# File 
the Reads folder(the same name as the parent folder) contains the setting files for the django program. The checkin folder contains the files for the web application.  
Static folder has two files: styles.css to style the html pages, and checkin.js to capture the action of clicking a button and manage the logic of checking out and returning a book using the fetch api and the urls. 
The templates folder contains the htmls rendered for the web application. login.html and register.html are for the user login/in page. layout.html provides a template for all othe htmls to reduce code.  library.html is to render the library page and index.html is to render the user checkouts page. 

# How to run the program
First, data of the books need to be input to the database(the web application is to help deal with library and library has lots of books). Next run command python3 manage.py runserver. The website will be served at 
"http://127.0.0.1:8000/checkin/"

# Additional Info
Every time a book is checked out, an Record object will be inserted to the Records database to keep track of the information of the checkout, including: which book is checkout, who (user) checks out the book, what time is the book checked out, and whether this book has been returned. A variable called checkin(default=false) will be false when the book has just been checked out and true when the book is returned