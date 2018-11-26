# Use case diagram
![UseCase-en](UseCase-en.png)
---

## Table of Contents
  1. [Glossary](#1) <br>
  2. [Actors](#2) <br>
  3. [Use cases](#3) <br>
    3.1 [Sign up](#3.1) <br>
    3.2 [Sign in](#3.2) <br>
    3.3 [Search information](#3.3) <br>
    3.4 [Write an article](#3.4) <br>
    3.5 [Format text](#3.5) <br>
    3.6 [Add an image](#3.6) <br>
    3.7 [Rate information](#3.7) <br>
    3.8 [Leave a comment](#3.8) <br>
    3.9 [Edit personal data](#3.9) <br>
    3.10 [Delete profile](#3.10) <br>
    3.11 [Delete someone else's information](#3.11) <br>
    3.12 [Sign out](#3.12) <br>

## 1 Glossary<a name="1"></a>
<p align="justify"> List of basic definitions used in the design:</p>

| Term | Definition |
|: --- |: --- |
| Unregistered user | The person using the site without logging in |
| Registered User | Signed in user |
| Admin | A person logged in with privileged access |
| Information | All data displayed on the site. It can be divided into three categories: user profile (his personal data), article and comment |
| Profile | Section of the site that stores personal data and articles of the user |
| Article | Text posted by the user in his profile |
| Comment | Text posted by the user after the article |
| Nickname | Unique username |

## 2 Actors<a name="2"></a>
Actors are non-signed in user, signed in user and administrator. Their definitions are described in [glossary](#1).

## 3 Use cases<a name="3"></a>
### 3.1 Sign up <a name="3.1"></a>
**Description:** this use case allows a user to create his own profile on the site.<br>
**Precondition:** an unregistered user entered the registration page by clicking on the "Sign up" button.

**Main stream:**
1. The site displays a registration page that contains input fields for a nickname, email, password, and password confirmation.
2. The user enters his nickname.
3. The system will check the entered name to match nicknames of already registered users. If a match is found, the alternative stream A1 will be executed.
4. The user enters his email.
5. The user enters his password.
6. The user confirms his password.
7. The system checks the entered passwords for a match. If they differ, the alternative stream A2 will be executed.
8. The user clicks on the button "Create my account". If the user ignored events from alternate stream A1 and A2, the button will be inactive (return to step 2 and step 6).
9. The system adds the user to the database.
10. A message about successful registration appears on the page.
11. The use case ends.

**Alternative stream A1:**
1. A message appears above the input field stating that the nickname is already in use.
2. Return to step 2 of the main stream.

**Alternative stream A2:**
1. A message appears above the input field stating that the passwords do not match.
2. Return to step 6 of the main stream.
---

### 3.2 Sign in<a name="3.2"></a>
**Description:** this use case allows the user to sign in to their profile.<br>
**Precondition:** an unregistered user entered the registration page by clicking on the "Sign in" button.

**Main stream:**
1. The site displays a login page that contains input fields for an nickname and password.
2. The user enters his nickname and password.
3. The user clicks on the "Sign in" button.
4. The system checks the entered data with the data from the database. If they do not match, the alternate stream A3 will be executed.
5. The user loads the main page under his profile.
6. The use case ends.

**Alternative stream A3:**
1. A message appears on the page stating that the alias and password entered are incorrect.
2. Return to step 2 of the main stream.
---

### 3.3 Search information<a name="3.3"></a>
**Description:** this use case allows user to find other user profiles and their articles.

**Main stream:**
1. The user clicks on the search field (available on each page of the site).
2. The user enters the information of interest.
3. The user clicks on the "Search" button.
4. The system searches for the entered data in the sections of nicknames and database article titles. In case the information is not found, the alternative A4 stream will be executed.
5. The user loads the page with a list of users and articles.
6. The use case ends.

**Alternative stream A4:**
1. The user browser is loading a page with a message stating that no match was found.
2. Return to step 1 of the main stream.
---

### 3.4 Write an article<a name="3.4"></a>
**Description:** this use case allows signed in user to publish article in his profile.

**Main stream:**
1. The user clicks on the "Write" button.
2. The site loads a page with input fields for the name and text of the article.
3. The user fills in the fields.
4. The user clicks on the "Post" button. If the user has not filled in all the fields, the alternative stream A5 will be executed.
5. The system creates a file in which it writes an article, and adds it to the database.
6. The user browser loads the article page.
7. The use case ends.

**Alternative stream A5:**
1. A message appears on the page stating that not all fields are filled.
2. Return to step 3 of the main stream.
---

### 3.5 Format text<a name="3.5"></a>
**Description:** this use case allows the user to change the appearance of the text. There are 7 buttons for formatting.<br>
**Precondition:** the user clicked on the "Write" button and the "Write an article" use case began.

**Main stream:**
1. The user clicks on one (or several) text formatting buttons.
2. The system adds in accordance with the pressed button markup, text placement or its appearance changes.
3. The use case ends.
---

### 3.6 Add image<a name="3.6"></a>
**Description:** this use case allows the user to add an image to the article.<br>
**Precondition:** the user clicked on the "Write" button and the "Write an article" use case began.

**Main stream:**
1. The user clicks on the "Add image" button.
2. The file selection dialog window opens.
3. User selects an image. If the user closes the dialog box, the use case completes ahead of schedule.
4. The system loads the photo into the article.
5. The use case ends.

**Additional information:** after pressing the "Post" button, the image is assigned an identifier that is placed in the text of the article, the image file is separately added to the database.

---

### 3.7 Rate information<a name="3.7"></a>
**Description:** this use case allows the signed in user to rate the information.

**Main stream:**
1. The user clicks the "Like" or "Dislike" button in the profile under the article or near the comment.
2. The system checks which user puts the assessment and what it estimates. If the user tries to evaluate his information, the alternate stream A6 will be executed. If the user tries to re-evaluate the information, the alternative flow A7 will be executed.
3. The system sends the recalculated rating to the user.
4. The user sees a new rating.
5. The use case ends.

**Alternative stream A6:**
1. A message appears on the page stating that it is forbidden to evaluate yourself.
2. The use case ends.

**Alternative stream A7:**
1. A message appears on the page stating that re-evaluate is forbidden.
2. The use case ends.
---

### 3.8 Leave a comment<a name="3.8"></a>
**Description:** this use case allows the signed in user to write a comment to the article.

**Main stream:**
1. The user clicks enters the text in the comment field under the article.
2. The user clicks on the "Post" button.
3. The system adds the comment to the database.
4. The site loads an article page with a comment added.
5. The use case ends.
---

### 3.9 Edit personal data<a name="3.9"></a>
**Description:** this use case allows the signed in user to change his own personal data.

**Main stream:**
1. The user clicks on the "Settings" button.
2. The site loads the profile settings page.
3. The user changes the data in the input fields.
4. The user clicks on the "Save" button.
5. The system adds changes to the database.
6. The site loads the profile page.
7. The use case ends.
---

### 3.10 Delete profile<a name="3.10"></a>
**Description:** this use case allows the signed in user to delete his profile.

**Main stream:**
1. The user clicks on the "Settings" button.
2. The site loads the profile settings page.
3. The user clicks on the "Delete the account" button.
4. A window appears on the page asking for confirmation.
5. The user clicks on the "Yes" button. If the user clicks the "No" button, the use case ends early.
6. The system forces the user out of the profile and removes it from the database.
7. The site loads the main page.
8. The use case ends.
---

### 3.11 Delete someone else's information<a name="3.11"></a>
**Description:** this use case allows the administrator to delete someone else's information.

**Main stream:**
1. The administrator clicks on the "Delete" button in front of a profile, article or comment.
2. A window appears on the page asking for confirmation.
3. The administrator clicks the "Yes" button. If the administrator clicks the "No" button, the use case ends early.
4. The system deletes information from the database.
5. The site loads the updated page.
6. The use case ends.

**Additional information:** if the administrator deleted the user profile, then the user must forcibly exit his profile.

---

### 3.12 Sign out<a name="3.12"></a>
**Description:** this use case allows the signed in user to sign out of his profile.<br>
**Precondition.** the user is signed in.

**Main stream:**
1. The user clicks on the "Sign out" button.
2. The system makes the user unauthorized.
3. The site loads the main page.
4. The use case ends.
