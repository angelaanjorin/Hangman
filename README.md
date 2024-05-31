# Hangman Game

# Introduction

Project 3 for Code Institute Full-stack development program: Python Essentials

The Hangmann is believed to have originated in England during the 17th century. Criminals who were sentenced to death by hanging could demand the "Rite of Words and Life."

In the "Rite of Words and Life" a criminal to be hanged was strung up over a 5 legged stand, and a board with a series of short ropes representing a word was displayed. The Executioner would pick the word, and would use charcoal to mark correctly guessed letters on the dashes of the board, and incorrect letters to the side. At every incorrect guess the executioner would use a sledge hammer or axe to knock away a single leg of the stand. 5 wrong guesses, and the criminal was hanged. If the entire word was filled in correctly or guessed, the condemned would be set free from that sentence and not tried again on that crime.

View the Hangman live game [HERE](https://hangmann-game-051c0aa67667.herokuapp.com/)

![INTRO](./assets/images/readme/mainpicture.png)

# Site Goals:

The goals for this site are as follows:
* To provide the player a fun, interlectual and engaging game.
* Provide the player the ability to see the top player´s scores and compete against them.

# User Experience - UX

## User Stories

#### New User:  
* As a new user, I am looking to find information on how to play the game.  
* As a new user, I am looking to enjoy playing the game.   
* As a new user, I would like to see my scores and the scores of the top players.  

#### Returning User:
* As a returning user, I would like to continue to increase my score by playing many games to compete with the top players.


# Development Planes:
To create a game that is comprehensive and engaging for a user, as a developer you need to look at all aspects of the game and how someone who visits your app will use it. You have to consider all the user stories that have been outlined in the above sections.  

## Strategy
The strategy principal looks at user needs, as well as product/service objectives. This websites target audience was broken down into three categories:

### Roles: 
* New User
* Existing User  

### Demographic:
* People aged between 16 and 65 years

### Psychographic:

#### Lifestyle:
* People interested in online games.
* Peolpe interested in online interlectual games.   

#### The website needs to allow users to:  
* Easily enter a username and city
* Easily enter letters to play the game
* Get live feedback on if the answer is correct or incorrect
* See the correct answer if they loose the game.
* See thier scores and cumulative scores if they play many games.
* See the scores of the top 5 players.
* Exit the game after at least playing once.

#### The website needs to allow the developer to:  
* Keep track of the user's name, user´s city, date and scores using google worksheets.
* Keep track of all letters and words guessed and add them to respective lists, alerting the user if they have already guessed this letter or word and if it was correct or wrong.
* Calculate scores for guessing the letters of the word or for guessing the whole word.
* Cumulatively record the scores of the user from all the games they play.

## Scope:  

With the structure in place, it was then time to move onto the scope plane. This was all about developing website requirements based on the goals set out in the strategy plane. These requirements are broken down into two categories.

### Content Requirements:
The user will be looking for:
    * Information on how to play the game and the scoring system.
    * Feedback during the game about the letters or words they input.
    * Information about the attempts left during the game.
    * The right word to be displayed if they lose.
    * Information about the top player´s scores.
    * The ability to play again to improve thier score or exit the game.

### Functionality Requirements:
The user will be able to:
    * Give thier name and city.
    * Decide if they want to play again, see the leaderboard or exit the game at the end of playing a game.

## Skeleton
The flowchart for this project was created using[draw.io] and was a guide for the whole project.
dropdownmenu with flowchart.

## Surface
To make this game a bit more user friendly, I used color and a typewriting technique to make the game more interesting with a background story.
* The game begins with a green logo.
* With the typewriter the beginnig of the story preceding the game is told.
* Invalid inputs and wrong answwers are highlighted in red.
* The leaderboard is displayed in green and in a clear table form.

# How to play
The traditional way to play the Hangman games were played with pen and paper. It typically involved two players, one would come up with a word and write the amount of dashes on the piece of paper representing the amount of letters in the word. The other player would guess the letters of the word and for each correct letter get it filled in the blank spaces. For wrong letters the image of the hangman will be drawn, starting with the head of the man, the body, both arms and then the legs. 

In this version of the game, a background story is told about a person (the player), who is lost in a deserted train station in Europe and is met by 3 bandits who ask the lost traveller for thier name and the city they come from. Then the rules of the game are laid out and the game starts. The computer generates a random word from the word list of cities in Europe. It gives a hint to the player by informing them of how many letters the word has.

The user then can guess the word by either typing a letter or a word and they get feedback telling them if the input was correct or wrong. For every initial wrong input, they lose an attempt from the 6 original attempts and the image of the hangman starts to be built. Alist of the wrongly guessed inputs are shown to the user. They lose the game when all attempts have been used up. 

Scores are added up for the correct inputs according to the illustrated scoring system. For very correct letter they gain 10 points, for guessing the whole word letter for letter an extra bonus of 100 points are added. If they guess the whole word, they get a total score of 500.

At the end of the game, the player gets to choose from 3 options: to either play again, see the leaderboard or exit the game. If the chose to playagain, the game repeats, with the exception of showing them thereafter a cumulative total score result at the end of every game played. If they choose to see the leaderboard, they are shown the scores of the top five players. If they chose to exit, the program ends.

# Features

## Logo and Welcome Information for Users

![Logo](./assets/images/Features of Hangmann/logo and intro.png)

* The logo is the first thing that the user sees. Then a story is told with a typewriteer to capture the interest and curiosity of the user. It tells them that it is 3 am and they are lost in a deserted train station when 3 bandits appear.
[Live](https://hangmann-game-051c0aa67667.herokuapp.com/)

## User Input
![User inputs](./assets/images/Features%20of%20Hangmann/playernameandcity.png)

* Continuing the narrative, the bandits ask the user for thier name and for the city they are from.

### Invalid Name Input Error
![No name input](./assets/images/Features%20of%20Hangmann/noentryfornameinput.png)

* If the user presses enter without entering a name, an error message informs the user of the invalid input and they are prompted again to input thier name.

### Invalid City Input Error
![No city input](./assets/images/Features%20of%20Hangmann/)

* If the user presses enter without entering a city, an error message informs the user of the invalid input and they are prompted again to input thier city.

## Rules of the Game and the Scoring System

![Rules of the Game and the Scoring System](./assets/images/Features%20of%20Hangmann/gamerules.png)

* The user is then shown the game rules and how the scoring works. At the end of this display they are prompted to press the enter key to start the game. Any other input + enter would start the game too.

## Masked Random Word Display

![Random Word](./assets/images/Features%20of%20Hangmann/numberoflettersofchosenword.png)

* The user is then informed about how many letters the random word has and shown empty dashes to represent the unknown letters of the word. They are then prompted to guess a letter or word and to type in thier input.

## Game
## Playing the game
### First Correct Letter
![first correct letter](./assets/images/Features%20of%20Hangmann/firstletter.png)

### During the game
![During the game](./assets/images/Features%20of%20Hangmann/playagain4thletter.png)

* If the player guesses a word wrong for the first time during the game, the wrong letter list first appears in red with the wrongly guessed letter. And they loose 1 attempt.
### Same correct letter
![Same correct letter](./assets/images/Features of Hangmann/letteralreadycorrect.png)

### Correct Word Input
![Correct Word](./assets/images/Features%20of%20Hangmann/correctword.png)

* If the player guesses the right word in the first game, they are told the correct word and that they have won. Thier total score is automatically the maximum of 500. The Leaderboard is updated with this information. 
### End of second game:
![End of game after first game](./assets/images/Features%20of%20Hangmann/playagainwordcorrect.png)

* If the player guesses the whole word correctly in the second game and thereafter, they are presented additionaly with thier cumulative scores. 
### Wrong word input
![Wrong Word input](./assets/images/Features%20of%20Hangmann/wordwrongfirsttime.png)

* If a player inputs a wrong word for the first time, they are informed the word is wrong and they loose an attempt. The word is stored in a wrong word list but not displayed to the player.
![Same wrong word input](./assets/images/Features%20of%20Hangmann/wrongwordrepeat.png)

* If the player puts in the same wrong word, they get told this but thier attempts do not reduce by one.

## Hangman Stages
### Hangman Stage 1
![Stage 1](./assets/images/hangmanstages/stage1.png)

* If the player guesses the letter wrong for the first time the hangman starts and the head is shown.
### Hangman Stage 2
![Stage 2](./assets/images/hangmanstages/stage2.png)

* The body is shown at this second stage of the hangman.
### Hangman Stage 3
![Stage 3](./assets/images/hangmanstages/stage3.png)

* At this stage the right arm is shown of the hangman.
### Hangman Stage 4
![Stage 4](./assets/images/hangmanstages/stage4.png)

* At this stage the left arm is shown of the hangman.
### Hangman Stage 5
![Stage 5](./assets/images/hangmanstages/stage5.png)

* At this stage the right leg is shown of the hangman.
### Hangman Stage 6
![Stage 6](./assets/images/hangmanstages/stage6.png)

* At this stage the right leg is shown of the hangman.

## End Choices
![End of game choices](./assets/images/Features%20of%20Hangmann/optiona.png)

* At the end of playing a game, the player is given three choices of playing again, seeing the leaderboard or exiting the game.
### Play again
![playagain](./assets/images/Features%20of%20Hangmann/playagain.png)

* If the player chooses this option, the game restarts with a new unknown word for the player to guess. At the end of playing this second game, the player is presented with thier cumulative scores. 

![Cumulative scores](./assets/images/Features%20of%20Hangmann/playagainwordcorrect.png)

### Leaderboard
![leaderboard](./assets/images/Features%20of%20Hangmann/leaderboard.png)

* If the player chooses option "b", they get shown the scores of the top five players.
### Exit Game
![End of game](./assets/images/Features%20of%20Hangmann/exit.png)

* At the end of the game the player can choose to exit the game and that ends the programm.

## Future Features
### Multiple player option
### Different word categories
* To make the game more interesting especially for returning players, they could be asked at the beginning of the game to choose which country or nation they are lost in with a different word list partaining to cities in that country or nation. 
### Wider range of words
### More advanced graphics
### Updated Scoring System
* If a letter in the word appears more than once, the score of 10 for each correct letter should be multiplied by how many times that letter appears in the word.
* To prevent players from inputting the whole word to get the maximum score of 500 after guessing the word and only one letter is left to guess. If there are only 2 letters left to guess of the word, the user should be prevented from guessing the whole word. 

### Feedback section

* The player could be asked before exiting the game if they want to leave a feedback or not. This feedback could be stored in the google worksheet.

### Correction section
* If a player has misspelt thier name or city, they should be able to have a choice to change this, so that thier cumulative scores are stored under the rigth input.

# Storage Data
Google sheets was used to store player names, cities, date and scores. This worksheet is connected to the python code through the Google Drive and Google Sheet API from the Google Cloud Platform. With the Google Sheet API Credentials i was able to send data collected from the app and store it in the google sheet and display the stored data as output information for the player. The sensitive credentials were saved in a creds.jsonfile. By making sure this file´s name was in the gitignore file, it was not pushed to the repository on Github. By deploying the programme to Heroku, the information from the creds.json file was stored securely in the config Vars. 

## Code to Connect to Google Sheet
![Code to Connect to Google Sheet](./assets/images/readme/googlescope.png)

## Google Sheet Hangman Leaderboard
![Code to Connect to Google Sheet](./assets/images/readme/hangman_leaderboard-Google-Sheets.png)


# Technolgies Used

## Language Used

* [Python 3.12](https://www.python.org/).

## Python Packages
* [os] (https://docs.python.org/3/library/os.html): clears the screen at different stages of the programm.
* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): returns a random integer to get a random word
* [Datetime](https://pypi.org/project/DateTime/): returns the full date
* [Gspread](https://pypi.org/project/gspread/): allows communication with Google Sheets
* [Colorama](https://pypi.org/project/colorama/): allows terminal text to be printed in different colours / styles
* [Time](https://pypi.org/project/time/): defined time sleep
* [google.oauth2.service_accoun](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts

## Framewworks - Libraries - Programs Used
* [Git](https://git-scm.com/)
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
    * GitHub is used to store the project's code after being pushed from Git.
* [GitHuv](https://derlin.github.io/bitdowntoc/)
    * This link was used to create the table of content for the README file.
* [Gitpod](https://gitpod.io/)
    * Gitpod was used to write my code.
* [Draw.io:](https://app.diagrams.net/)
    * Draw.io was used to draw the flowchart for the whole structure of the programm.
* [Cloudinary:](https://cloudinary.com/)
    * The images linked in the readme file are stored here.
* [Heroku:](https://heroku.com/)
    * Heroku was used to deploy the project.
* [Google Sheets:](https://heroku.com/)
    * Google sheets was used to store the user´s inputed information, the date and to track the scores of the user.
    You can view the Google sheets file [here](https://docs.google.com/spreadsheets/d/1a4cQ8MmqxNLSOMSEqPsuPDMlvOTl8-AqtlW-sh9tqBc/edit?usp=sharing).


# Testing
## Code Institute Python Linter 
[CI Python Linter](https://pep8ci.herokuapp.com/) 
The CI Python Linter was used to validate every Python file in the project to ensure there were no syntax errors in the project.
<details><summary>run.py - CI Python Linter Check</summary>

![Screenshot of the errors for the run.py file](./assets/images/readme/runpylinter.png)

</details>

<details><summary>hangman_words.py - CI Python Linter Check</summary>

![Screenshot of the errors for the hangman_words.py file](./assets/images/readme/hangmanwordlistlinter.png)

</details>

<details><summary>hangman_art.py - CI Python Linter Check</summary>

![Screenshot of the errors for the hangman_art.py file](./assets/images/readme/hangmanartlinter.png)

</details>

<details><summary>hangman_typing.py - CI Python Linter Check</summary>

![Screenshot of the errors for the hangman_typing.py file](./assets/images/readme/hangmantypewriterlinter.png)

</details>

<details><summary>Google Lighthouse Check</summary>

![Lighthouse Results:](./assets/images/Features%20of%20Hangmann/Lighthouse-Report-Viewer.png)

</details>


## Manual Testing

The game has been manually tested multiple times during the coding phase. Additionally, it was checked after being deployed to Heroku to ensure that all features are displaying as intended. Furthermore, friends and relatives have also tested the game. 
Testing was performed on various aspects such as: 

| Feature | Expected Result | Steps Taken | Actual Result | Screenshot |
| ------- | ----------------| ------------ | ------------ | ----------|
| Start Screen | To show the logo and the welcome message| None | As intended | ![Screenshot with the logo and welcome message](./assets/images/Features%20of%20Hangmann/logo%20and%20intro.png) |
| Display Rules | To display the rules and scoring system of the game| None | As intended | ![Screenshot of the displayed rules](./assets/images/Features%20of%20Hangmann/gamerules.png) |
| Player Name| To get player´s name and use it in the game´s messages | Insert aphanumeric player city | As intented | ![Screenshot with the playername](./assets/images/Features%20of%20Hangmann/playername.png) ![Screenshot with the personalised messages](./assets/images/Features%20of%20Hangmann/nameinmessage.png)|
| Player city| To get player´s city and store it in google worksheet | Insert aphanumeric player city | As intented | ![Screenshot with the city](./assets/images/Features%20of%20Hangmann/playernameandcity.png)
| Guess a letter or a word | Prompts the player to guess a letter or go for the whole word | Input a letter or a word to guess | As intended | ![Screenshot of the prompt to enter a letter or a word](./assets/images/Features%20of%20Hangmann/numberoflettersofchosenword.png) |
| Correct Guess | To display the position of the letter, the hangman with no lost attempts | Guessed a correct letter | As intended | ![Screenshot of a correct guessed letter](./assets/images/Features%20of%20Hangmann/firstletter.png)
| Incorrect Guess | To display incorrect message, the hangman with the remaining attempts and the wrong letter list | Guessed wrong letter | As intended | ![Screenshot with the incorrect guess message](./assets/images/Features%20of%20Hangmann/wrongletterfirsttime.png) |
| Repeated Guess | To display a message saying the input was already guessed, if wrong no penalty applied | Input a letter previously inserted | As intended | ![Screenshot of a message for a second input of a correct letter](./assets/images/Features%20of%20Hangmann/correctletterrepeatinput.png) ![A second screenshot](./assets/images/Features%20of%20Hangmann/letteralreadycorrect.png) |
| Word Guess | To display a message saying if the word is correct or wrong | Input a word | As intended | ![Screenshot of a message for a correct word](./assets/images/Features%20of%20Hangmann/correctword.png) ![A second screenshot](./assets/images/Features%20of%20Hangmann/wordwrongfirsttime.png) ![A third screenshot](./assets/images/Features%20of%20Hangmann/wrongwordrepeat.png) |
| Hangman Stages | To show the updated hangman stages | Input several letters | As intended | ![Screenshots with the ghangman stages updating whilist inserting right or wrong letters](./assets/images/Features%20of%20Hangmann/playagain4thletter.png) ![A second screenshot](./assets/images/Features%20of%20Hangmann/stage60.png) |
| Win The Game | To show congrats message and show the word | Guess the word in less than 6 attempts| As intended | ![Screenshot with the win message](./assets/images/Features%20of%20Hangmann/correctwordwin.png) ![Screenshot with the win message after guessing letter by letter](./assets/images/Features%20of%20Hangmann/winletterbyletter.png) |
| Lose The Game | To show a message confirming the loss | Fail to guess in 6 attempts| As intended | ![Screenshot with the losing game message](./assets/images/Features%20of%20Hangmann/youlose.png) |
| Play Again | To display the play again choice message | Choose between a, b or c | As intended | ![Screenshot with the play again message](./assets/images/Features%20of%20Hangmann/optiona.png) |
| Play Game Again | Game starts again | Choice A| As intended | ![Screenshot with the play again](./assets/images/Features%20of%20Hangmann/playagain.png) |
| Leaderboard | To display the leaderboard | Choice B | As intended | ![Screenshot with the Lederboard](./assets/images/Features%20of%20Hangmann/leaderboard.png) |
| Exit Game | Exit Game | Choice C | As intended | ![Screenshot with the exit message](./assets/images/Features%20of%20Hangmann/exit.png) |

## Input validation testing
* Enter playername
    * Playername cannot be empty

![Screenshot for Playername input validation](./assets/images/Features%20of%20Hangmann/invalidnameinput.png)

* Enter playercity
    * Playercity cannot be empty

![Screenshot for Playercity input validation](./assets/images/Features%20of%20Hangmann/invalidcityinput.png)

* Enter letter or word

    * Can only contain letters
    * Can not contain numbers

![Screenshot for guess input validation](./assets/images/Features%20of%20Hangmann/invalidinput.png)

* Play Again Input
    * Can only contain letters "a" , "b" or "c"

![Screenshot with the play again input validation](./assets/images/Features%20of%20Hangmann/invalidchoicefeedback.png)
![Screenshot with the play again input validation](./assets/images/Features%20of%20Hangmann/invalidchoiceletter.png)

## Fixed Bugs 

* In the initial setup of the creds.json file, by mistenkly ommiting the "s" in creds.json while writing it in the gitignore file, it was sent to the repository on Github and remained there in the history. I got alerts from Gitpod, github and an email from Google informing me of this error. Through research i was [here]( https://www.git-tower.com/learn/git/commands/git-rm), i was able to use the rm command on git to delete the creds.json file in the repository history as well as from the filesystem. I then created a new Google sheet API and Drive with a new creds.json file that i made sure to save correctly on the gitignore file. 
*  At the initial stages of the project the complete data of players were repeatedly stored in seperate rows every time a player played a game more than once. The scores were not being added up after every game. I had to research and learn how to get the whole records of the sheet and search for the player´s name and then update  the score cell. I then had to amend this and add the city as a second search criteria incase ther were two players with the same name. 
* It took much trail and error to use the sorted function in python to sort through all the scores and get the top five scores and display this in a table format to the user.

## Functionality



# Bugs
* 



# Unfixed Bugs

# Deployment
This project was developed using GitPod, committed and pushed to GitHub using a GitPod terminal.

## Deploying on Heroku 
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create a new app in Heroku.
2. Select "New" and "Create new app".
3. Name the new app and click "Create new app".
4. Click on the "Settings" tab at the top of the page
5. Open the "Reveal Config Vars" section and input the following information - KEY: PORT, VALUE: 8000.
6. Under the Config Vars section in "Settings" select "BuildPack" and select Python and Nodejs, Make sure they are in this order.
7. Now go to the "Deploy" tab at the top of the page and select your deploy method and repository.
8. In "Deployment Method" click on "GitHub" to connect them.
9. Once they are connected search for the repository you want and hit "connect".
10. Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section. Note, if you click on Automatic Deploys, you will still need to hit deploy branch to build the site
11. Heroku will now deploy the site.
12. Deployed site [Hangman](https://hangmann-game-051c0aa67667.herokuapp.com/).

## Forking the GitHub Repository 

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate GitHub Repository [Hangman](https://github.com/angelaanjorin/Hangman). 
2. At the top of the Repository (under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.


## Local Clone

To make a local clone in github, please follow the steps beow:

1. Log in to GitHub and locate GitHub Repository [Hangman](https://github.com/angelaanjorin/Hangman).
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

# Credits

## Information Sources/Resources

* [Git tower:](https://www.git-tower.com/learn/git/commands/git-rm).
* [Python:](https://www.python.org/).
* [gspread:](https://www.gspread.org/).
* [Code Institute:](https://learn.codeinstitute.net/).
* [Stack Overflow](https://stackoverflow.com/).
  

## Content

* All the text content is original. I got inspiration from the following :

    1. [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode)
    2. [100 days of Code by Dr. Angela Yu ](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)
    3. [Portfolio Project 3 by Pedro Cristo](https://github.com/PedroCristo/portfolio_project_3)
    4. [CodeWithdar](https://github.com/CodeWithdar/python-tutorials-/blob/main/main.py)

### Images

* [Logo and Hangman Images:](https://ascii.co.uk/art/hangman)
    * The logo and Hangmanimages were gotten from the above ASCII webpage.
* [Game rules:](https://github.com/PedroCristo/portfolio_project_3)
    * The code for the game rules display was taken from Pedro Cristo, an alumni of Code Institute.
  
# Acknowledgements
 * Thanks to my Mentor Gareth McGirr for his assistance throughout the project.
 * Special thanks to my partner and alumni of Code Institute Eric Jones for his assistance throughout this project.