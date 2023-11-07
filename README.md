# [View the Live project here](https://quicknote-ci-m3-tom-ballard-28c10547420d.herokuapp.com/)

## QuickNotes

This Flask-based web application was developed to offer users a swift, simple, efficient, and secure online platform for storing notes.

!["Am I Responsive" image](docs/supp-images/amiresponsive.jpg)

## User Experience

### Key information for the site

1. __Secure Account Creation and Note Storage:__
The platform facilitates the creation of personalized and secure user accounts, offering a dedicated space for users to securely store their notes. This ensures the privacy and protection of their information.

2. __Comprehensive Note Management:__
Users have the flexibility to create, view, edit, and delete notes that are exclusively linked to their accounts. This comprehensive set of note management features allows users to tailor their notes at their convenience, enhancing their experience on the platform.

3. __Intuitive Note Organization:__
Notes are intelligently organized based on their chronological order, displaying the most recent or newly edited notes at the top of the list. This sorting mechanism, based on date and time, allows users to effortlessly track and access their latest entries with ease.

4. __Multi-Device Accessibility:__
The platform is designed for accessibility across various devices, ensuring a seamless user experience across desktops, tablets, and mobile devices. Users can access their notes conveniently while on the move, using the web browser on their device of choice, thus enabling a flexible and on-the-go approach to note management.

### User Stories

#### Client Goals

* __Efficient Note Management:__ To create, edit, view, delete, and store notes seamlessly and rapidly, seeking a user-friendly experience that ensures swift and easy note management.

* __Cross-Platform Note Access:__ The capability to view notes across multiple platforms, ensuring accessibility and convenience irrespective of the device or platform used.

#### First-Time Visitor Goals

* __Account Creation and Note Initiation:__ Visitors aim to effortlessly create an account and promptly generate their inaugural note, seeking a seamless introduction to the platform.

* __Note Management Understanding:__ Visitors aspire to comprehend how to edit and delete their notes, ensuring efficient control and customization of their entries.

* __Quick Note Access:__ Visitors desire swift and easy access to their notes, aiming to effortlessly view and engage with their created content.

* __Account Deletion Clarity:__ Visitors are interested in understanding how to delete their account if necessary, seeking clear guidance on managing their account settings.

#### Returning Visitor Goals

* __Note Access and Management:__ Returning visitors aim to revisit the site to effortlessly view, edit, and delete their existing notes, ensuring easy access to their previously created content.

* __Account and Note Deletion:__ Visitors returning to the site desire the ability to delete both their account and notes if they wish to do so, seeking a straightforward process for account and data management.

## Features

### Existing Features

* __Navigation__

  * The site's navigation intelligently adjusts based on the user's login status. For logged-out users, it provides clear pathways to sign up and log in, ensuring a seamless entry into the platform. Once logged in, the navigation dynamically adapts, offering direct access to the user's notes, account management, and other relevant sections, providing an intuitive and personalized user experience.

* __Landing/Welcome Page__

  * The Landing/Welcome Page serves as an introduction to the app, offering users a concise overview of its functionalities. It prominently features a user-friendly registration form for new users to sign up directly or provides a 'Login!' link for existing users, ensuring a seamless entry into the platform.

* __Notes Page__

  * The Notes Page is meticulously crafted to streamline note creation and easy access. It includes a visible button for creating new notes, ensuring a swift and intuitive process. Once created, notes are displayed within a collapsible element, presenting their titles and creation dates. This design optimizes screen space, allowing users to efficiently manage their notes by expanding, editing, or deleting as needed.

* __Edit Note Page__

  * Dedicated to enhancing user control, the Edit Note Page empowers users to modify specific note details, such as titles and content. Any changes made to a note update it, moving it to the top of the notes page for quick and convenient access.

* __Delete Notes__

  * The 'Delete Notes' feature strategically incorporates a modal prompt for user confirmation before deletion. This intentional design minimizes accidental deletion of notes, ensuring a deliberate action by the user.

* __Account Page__

  * The Account Page serves as a hub for account-related actions. It offers a user-friendly interface for users to manage their accounts and corresponding notes. Featuring straightforward instructions, warnings, and two prominently placed buttons: 'Back to Notes' and 'Delete Account.' The 'Delete Account' option triggers a confirmation modal, mitigating the risk of accidental account deletion. The 'Back to Notes' button seamlessly redirects users to their notes page, enhancing user navigation.

* __Modals__

  * Modal dialogs are strategically incorporated throughout the platform to confirm critical user actions. These modal prompts serve as a safeguard against accidental actions, such as note deletion, account deletion, and logging out, enhancing user confidence and preventing unintended actions.

* __Footer Section__

  * The footer section incorporates essential information or links, adding to the site's accessibility and providing additional resources or contact details for users to navigate or seek support as needed.

### Future Features

* __Search Notes__

  * Given additional time or as an update to the app, I believe a valuable addition would be to grant users the ability to search their notes using keywords. This feature would greatly assist in easily locating specific notes, especially for users managing a large volume of stored notes.

* __Set Notes to Important__

  * Given more time or as an update to the app, I believe that enabling users to mark and set notes as important, always displaying them at the top, would greatly enhance the app's value and user experience.

## Design

### Initial Concept

The primary design concept aimed to create a clear and easily readable website with high contrast. It includes a splash of colour for highlighting key points and buttons, providing users with a clean, crisp, and easy-to-navigate experience.

### Colour Scheme

The chosen neutral colour scheme of whites and blacks, along with drop shadows, and the use of Indigo for action buttons and links, was selected to improve visual clarity while maintaining a clean and modern aesthetic.
!["Colour Scheme" image](docs/supp-images/colourpalette.jpg)

### Typography

["Roboto"](https://fonts.google.com/specimen/Roboto) The font is the default font used by Materialize CSS. It is a modern, easily readable, and widely used typeface.

![Roboto Typeface](docs/supp-images/robototypeface.jpg)

### Wireframes

#### Desktop

* [Home](docs/wireframes/home.jpg)

* [Notes](docs/wireframes/notes.jpg)

* [Add/Edit Note](docs/wireframes/edit_note.jpg)

* [Login](docs/wireframes/login.jpg)

* [Account](docs/wireframes/account.jpg)

#### Mobile & Tablet

* [Home](docs/wireframes/tablet_mobile_home.jpg)

* [Notes](docs/wireframes/tablet_mobile_notes.jpg)

* [Add/Edit Note](docs/wireframes/tablet_mobile_add_edit_note.jpg)

* [Login](docs/wireframes/tablet_mobile_login.jpg)

* [Account](docs/wireframes/tablet_mobile_account.jpg)

### Finalised Design

#### Home

!["Final Home" image](docs/supp-images/home.jpg)

#### Login

!["Final Login" image](docs/supp-images/login.jpg)

#### Notes

!["Final Notes" image](docs/supp-images/notes.jpg)

#### Add Note

!["Final Add Note" image](docs/supp-images/add_note.jpg)

#### Edit Note

!["Final Edit Note" image](docs/supp-images/edit_note.jpg)

#### Account

!["Final Account" image](docs/supp-images/account.jpg)

#### Delete Note Modal

!["Final Delete Note Modal" image](docs/supp-images/delete_note_modal.jpg)

#### Delete Account Modal

!["Final Delete Modal" image](docs/supp-images/delete_account_modal.jpg)

#### Logout Modal

!["Final Logout Modal" image](docs/supp-images/logout_modal.jpg)

## Technologies Used

### Languages Used

* [HTML](https://en.wikipedia.org/wiki/HTML5)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Java Script](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Flexbox)

### Frameworks, Libraries & Programs Used

#### Frameworks

* [Materialize CSS:](https://materializecss.com/) A contemporary, responsive front-end framework founded on Material Design. It offers a comprehensive set of components and styles, enabling the creation of visually appealing and user-friendly web interfaces that seamlessly adapt to various screen sizes.

* [Flask:](https://flask.palletsprojects.com/en/3.0.x/) A lightweight and versatile web framework written in Python. Flask simplifies the process of building web applications and APIs, providing a collection of tools and libraries. Renowned for its simplicity and extensibility, Flask is a preferred choice for Python developers due to its ease of use and straightforward approach to web application development.

#### Libraries

* [Jinja:](https://jinja.palletsprojects.com/en/3.1.x/) Employed as a template engine, Jinja enables the creation of dynamic web pages by providing a seamless integration between Python and HTML, simplifying the presentation of data and content.

* [SQLAlchemy:](https://www.sqlalchemy.org/) This Python SQL toolkit and Object Relational Mapper offer developers robust SQL functionalities and an Object-Relational Mapping system. It facilitates efficient and high-performance database access, employing a simple and Pythonic domain language for enterprise-level persistence patterns.

#### Development and Deployment Platform

* [Heroku:](https://www.heroku.com) Chosen for deployment, Heroku provides a platform for hosting and managing web applications, offering scalability and reliability.

#### Database Management

* [ElephantSQL:](https://www.elephantsql.com/) Utilized for Database Management, ElephantSQL offers cloud-based PostgreSQL databases, ensuring data management and access.

#### Tools and Programs

* [Gitpod.io:](https://code.visualstudio.com/) Utilized as an online integrated development environment for writing website code, Gitpod.io streamlines coding and collaboration.

* [GitHub:](https://www.github.com/) Served as the project's code repository after being pushed from Gitpod.io, ensuring version control and collaboration among developers.

* [Adobe XD:](https://www.adobe.com/creativecloud.html) Employed during the design phase for wireframe creation, Adobe XD facilitated the visualization and prototyping of the website layout and user interface.

* [Google Dev Tools:](https://developer.chrome.com/docs/devtools/) Employed for troubleshooting, feature testing, and issue resolution related to website responsiveness and styling, Google Dev Tools assists in debugging and optimizing web content.

* [Am I Responsive?:](https://ui.dev/amiresponsive) Used to showcase the website's appearance across various devices, Am I Responsive? assists in visualizing and testing the website's responsiveness and layout on different screen sizes.

### Data Schema

#### User Table

| Field        | Type          | Description           |
|--------------|---------------|-----------------------|
| id           | Integer       | Primary Key           |
| first_name   | Text          | User's First Name     |
| last_name    | Text          | User's Last Name      |
| email        | Text          | User's Email          |
| password     | Text          | Hashed Password       |
| notes        | Relationship  | Relationship to Notes |

#### Note Table

| Field         | Type          | Description           |
|---------------|---------------|-----------------------|
| id            | Integer       | Primary Key           |
| note_title    | Text          | Title of the Note     |
| note_content  | Text          | Content of the Note   |
| note_date     | Date/Time     | Date of the Note      |
| user_id       | Integer       | Foreign Key to User   |

## Deployment & Local Development

### Deployment

This project was deployed to Heroku via Elephant SQL using the following steps:

#### ElephantSQL

1. Navigate to ElephantSQL.com and create a user account, using the login with GitHub option.
2. Click “Create New Instance”.
3. Set up your plan. (You can leave the 'tags' field blank.)
4. Select region.
5. Select a data center near you
6. Then click “Review”.
7. Check your details are correct and then click “Create instance”.
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, clicking the copy icon will copy the database URL to your clipboard
10. Leave this tab open, we will come back here later

#### Heroku

1. Log into Heroku.com and click “New” and then “Create a new app”.

2. Choose a unique name for your app, select the region closest to you and click “Create app”.

3. Go to the Settings tab of your new app.

4. Click Reveal Config Vars.

5. Return to your ElephantSQL tab and copy your database URL.

6. Back on Heroku, add a Config Var called DATABASE_URL and paste your ElephantSQL database URL in as the value. Make sure you click “Add.”

7. Add each of your other environment variables except DEVELOPMENT and DB_URL from the env.py file as a Config Var.

8. Navigate to the “Deploy” tab of your app.

9. In the Deployment method section, select “Connect to GitHub”.

10. Search for your repo and click Connect.

11. Optional: You can click Enable Automatic Deploys in case you make any further changes to the project. This will trigger any time code is pushed to your GitHub repository.

12. As we already have all our changes pushed to GitHub, we will use the Manual Deploy section and click Deploy Branch. This will start the build process.

13. Now, we have our project in place, and we have an empty database ready for use. As you may remember from our local development, we still need to add our tables to our database. To do this, we can click the “More” button and select “Run console.”

14. Type `python3` into the console and click Run.

15. In the terminal that opens, write `from quicknote import db` and then press enter.

16. In the terminal, write `db.create_all()` and then press enter.

17. Exit the Python terminal, by typing `exit()` and hitting enter, and close the console. Our Heroku database should now have the tables and columns created from our models.py file.

18. The app should be up and running now, so click the “Open app” button

### Local Deployment

#### To fork the Quick Notes repository

1. Log in (or sign up) to [GitHub](https://github.com).

2. Go to the repository for this project, at [GitHub Repository](https://github.com/ThomasBallardCI/m3-notes-app).

3. On this repository's page, click the "Fork" button located in the top right corner of the page. It's usually next to the "Star" and "Watch" buttons.

4. Clicking the "Fork" button will create a copy of the repository in your GitHub account.

5. Wait for the Fork to Complete: GitHub will redirect you to the newly forked repository in your account. It may take a few moments to complete the forking process.

    Once the forking process is complete, you'll have your own copy of the repository in your GitHub account. You can make changes, modifications, or updates to this forked repository without affecting the original repository. If you wish to contribute your changes back to the original repository, you can create a pull request from your forked repository.

#### To clone the Quick Notes repository

1. Log in (or sign up) to [GitHub](https://github.com).

2. Go to the repository for this project, at [GitHub Repository](https://github.com/ThomasBallardCI/m3-notes-app).

3. Above the list of files, click "Code".
    * Copy the URL provided (It could be a HTTPS or SSH)

4. Open Terminal(forMac/Linux) or Command Prompt/Powershell (for Windows):
    * Navigate to the directory where you want to clone the repository.

5. Clone the Repository:
    * Use the `git clone` command followed by the repository URL you copied previously.

    * To clone the repository using HTTPS:

      `git clone https://github.com/ThomasBallardCI/m3-notes-app.git`

    * To clone the repository using SSH (if you hav setup SSH keys on GitHub):

      `git clone git@github.com:ThomasBallardCI/m3-notes-app.git`

6. Once the cloning is complete, you will have a local copy of the repository in your specified directory.

    This process creates a local copy of the GitHub repository on your machine, allowing you to make changes, additions, and updates locally.

### Installations and commands in the terminal that are necessary when forking or using a different workspace

* To install required libraries and packages necessary for this project to function correctly in the terminal run the following command:

  * `pip install -r requirements.txt`
  
    This command reads the file and installs each library listed, ensuring you have the necessary dependencies to run your Python project.

* To create a working database in the workspace the following commands are required in the terminal:
  * `set_pg`

  * `psql`

  * `CREATE DATABASE quicknote;`

  * `\q`

  * `python3`

  * `from quicknote import db`

  * `db.create_all()`

  * `exit()`

* To delete the database (you must delete and recreate the database if the models are changed)
  * `set_pg`

  * `psql`

  * `DROP DATABASE quicknote;`

  * `\q`

  * Then repeat the steps above for creating a database to create a new working database with the updated models.

## Testing

Testing was an ongoing process as I built out the Quick Notes application, utilizing Chrome Developer Tools with along with console logging to ensure I was getting the required responses from the code as it was written.

### Validator Testing

#### [HTML Validator](https://validator.w3.org/)

* __Result for base.html__

  19 Errors appear due to the jinja template syntax
  ![HTML Results base.html](docs/validation-results/html_valid_base.jpg)

* __Results for home.html__

  4 Errors appear due to the jinja template syntax
  ![HTML Results home.html](docs/validation-results/html_valid_home.jpg)

* __Results for login.html__

  4 Errors appear due to the jinja template syntax
  ![HTML Results login.html](docs/validation-results/html_valid_login.jpg)

* __Results for notes.html__

  10 Errors appear due to the jinja template syntax
  ![HTML Results notes.html](docs/validation-results/html_valid_notes.jpg)

* __Results for add_note.html__

  5 Errors appear due to the jinja template syntax
  ![HTML Results add_note.html](docs/validation-results/html_valid_add_note.jpg)

* __Results for edit_note.html__

  5 Errors appear due to the jinja template syntax
  ![HTML Results edit_note.html](docs/validation-results/html_valid_edit_note.jpg)

* __Results for user_management.html__

  6 Errors appear due to the jinja template syntax
  ![HTML Results user_management.html](docs/validation-results/html_valid_account.jpg)

#### [CSS Validator](https://jigsaw.w3.org/css-validator/)

* __Results for Style.css__

  ![CSS Results style.css](docs/validation-results/css_valid.jpg)

#### [JSLint](https://jslint.com)

* __Script.js__
  ![JSLint script.js](docs/validation-results/js_valid.jpg)

#### [Python Validator](https://pep8ci.herokuapp.com/)

* __Results for init.py__

  ![Python Results init.py](docs/validation-results/python_valid_init.jpg)

* __Results for Models.py__

  ![Python Results models.py](docs/validation-results/python_valid_models.jpg)

* __Results for Routes.py__

  ![Python Results routes.py](docs/validation-results/python_valid_routes.jpg)

* __Results for Run.py__

  ![Python Results run.py](docs/validation-results/python_valid_run.jpg)

### Manual Testing

All manual testing was carried out by myself and a few friends on various devices and browsers.

#### Desktop Browsers

* Chrome Version 114.0.5735.199 (Official Build) (64-bit)
* Firefox Version 115.0.2 (64-bit)
* Microsoft Edge4 Version 114.0.1823.82 (Official Build) (64-bit)

#### Mobile Device and Browser

* Samsung Galaxy S21+
* One UI Version 5.1/Android 13
* Chrome Version 114.0.5735.196

#### Tablet Device and Browser

* Apple iPad Pro 13" 2021 - iPadOS Version 16.5.1
* Safari Version 16.0

### Test Cases and Results

* Chrome Developer tools were used to fully test the site and its functionality throughout the development process, in combination with console logs as code was written, to ensure it was functioning correctly. The Chrome Developer tools were also used to test responsiveness for mobile and tablet device-specific styling before moving on to functionality testing on those devices physically.

#### Button

* Testing of all buttons was carried out on all platforms to ensure they took you to the relevant section, opened or closed the correct modals and submitted the information correctly (user registration and note create/edit).

#### Input Field

* Testing of the input fields was done by passing them characters below and above the limits set for each input field.

#### Authentication

* Authentication was tested by creating a user account and ensuring when logged in the user can only see the relevant sections of the app.
  * Nav bar elements "Notes" "Account" "Logout"
  * Pages "Notes" "Account"
  * Actions "creating notes" "editing notes" "deleting notes" "deleting account"
  * Views Users can only view, edit and delete the notes they have created as well as only able to delete the account they have created whilst logged in
  * Returning user if logged in will be directed to their notes page

#### Database

* User Account data is added and persists over time
* User Note data is added and persists over time
* User Notes are edited correctly
* User Notes are deleted correctly
* User Account is deleted correctly

### Known Bugs

* No Known Bugs

## Credits

* [Tech With Tim](https://www.youtube.com/watch?v=dam0GPOAvVI&list=WL&index=4) For the User Authentication and Login.

* [Code Institute](https://codeinstitute.net/) Relational Database "Task Manager" walkthrough

* [StackOverflow](https://stackoverflow.com/questions/4830535/how-do-i-format-a-date-in-jinja2) Formatting Date with Jinja

* [StackOverflow](https://stackoverflow.com/questions/64158349/materialize-css-getting-a-badge-to-left-align) Help with aligning dates on the notes via Materialize

* [Materialize CSS](https://materializecss.com/) For layout and styling

Massive thanks to my tutor, Julia, for helping with suggestions for the code for note deletion to correctly delete the selected note as well as all the other support and brainstorming on ideas.

Massive thanks to my September 2022 Cohort group for helping with testing and peer reviewing my code.
