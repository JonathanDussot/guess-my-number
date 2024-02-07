# Guess My Number

*Guess My Number* is a python terminal game which runs on a mock terminal in Heroku

[here is the deployed version of it](https://guess-my-number-jpd-5867ef6aed06.herokuapp.com/)

![screenshot of terminal when running program](assets/images/screenshot-game.png)

## How To Play

*Guess My Number* is a fun one-player game vs the computer where the computer randomly selects a number and the user attempts to guess it correctly.  The random number is given parameters from which to choose the random number from depending on the difficulty selected by the user. The amount of attempts can also vary and also depends on the difficulty chosen.  between attempts, the user is given feedback to notify if they're getting closer to or further from the target number.  in addition to this, there are also a set of clues given once user only finds they have 3 attempts left (as seen in the [features section below](#features)). It is run on a loop for user to choose to play again if they wish, otherwise selecting 'no' would break the loop and end the game.

### My GitHub Repository

You can visit the GitHub Repository [here](https://github.com/JonathanDussot/guess-my-number)

## CONTENTS

- [Star Wars Quiz](#star-wars-quiz)
  - [Project Overview](#project-overview)
    - [Live Website](#live-website)
    - [My GitHub Repository](#my-github-repository)
  - [CONTENTS](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Common Usage](#common-usage)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [colour scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
      - [Home Page](#home-page)
      - [Quiz Questions](#quiz-questions)
      - [Results Page](#results-page)
    - [Intelligent Diagramming chart](#intelligent-diagramming-chart)
  - [Features](#features)
    - [General Features on each page](#general-features-on-each-page)
    - [Future Implementations](#future-implementations)
    - [Accessibility](#accessibility)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Libraries and Programs Used](#libraries-and-programs-used)
  - [Deployment And Local Development](#deployment-and-local-development)
    - [Deployment to GitHub pages](#deployment-to-github-pages)
    - [Local Deployment](#local-deployment)
      - [How to Fork](#how-to-fork)
      - [How to Clone](#how-to-clone)
  - [Testing](#testing)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)

### Intelligent Diagramming chart

I created this Intelligent Diagram using Lucid Chart

![diagram of gameflow on Lucidchart](assets/images/diagram-img.png)

## Features

### Existing Features

- Name requested from user
- Instructions to the game given before then requesting game difficulty

![screenshot of inputs and instructions](assets/images/features-1.png)

- Errors generated upon entering invalid characters/information.

![screenshot of errors](assets/images/features-2.png)

- Keeps a record of previous guesses and calculates difference between the last two to indicate if user is getting closer or further.
- Approximity function informs user when they are quite close to the target number.


![screenshot of approximity messages](assets/images/features-3.png)

- Clues are given upon determining the user has only 3 attempts left.  These clues are generated from an *if* statement that calculated if the target number is divisible by 3 or 4.

![screenshot of clues](assets/images/features-4.png)

- A message is displayed at the end to state that user got the number correct.
- An alternative to this is the game over message should the user run out of attempts.
- In both cases, the user is then given the option to restart the game and re-select the difficulty.

![screenshot of end message and restart quiz option](assets/images/features-5.png)



### Future Implementations

ideas for future implementations I would like to include are:

1. A feature to request usernames and provide users with a list of highest scores for the users to compete with.
2. A multi-player feature for participants to compete remotely head-to-head on different devices along with the possibility for them to challenge participants to these head-to-head games.
3. Another multi-player feature mode that will allow players to compete locally in teams to provide users with a fun party game.

### Accessibility

In order to ensure that this website is as accessible friendly as possible, the following measures have been taken:

- Using semantic HTML elements.
- Providing descriptive alt attributes for all images for users with visual impairments.
- Providing information for screen readers for some features on the page.
- Ensuring there is a sufficient colour contrast throughout the site.
- I used Lighthouse and wAVE to ensure good measures were taken for accessibility.
- instructions guide the user through the game's dynamics.
  
## Technologies Used

### Languages Used

The languages used for the website include HTML, CSS and JavaScript.

### Libraries and Programs Used

[icons8.com](https://icons8.com/icons) to create favicon.

[Tiny PNG](https://tinypng.com/) to compress images.

[GitHub](https://github.com/) to save and store my website.

[Codeanywhere](https://app.codeanywhere.com/) IDE I used for this project.

[Google Fonts](https://fonts.google.com/) to import fonts used on the site.

Google Dev tools - to test and fix issues detected.

[freepik](www.freepik.com) to download and use my background-url image.

[Am I Responsive?](https://ui.dev/amiresponsive) to show site on all different screen sizes.

[Colormind.io](http://colormind.io/)  to generate color palette used.

[Balsamiq](https://balsamiq.com/) to create wireframes.

[Lucidchart](https://www.lucidchart.com/pages/) to create intelligent diagramming chart.

## Deployment And Local Development

### Deployment to GitHub pages

The site is deployed using GitHub Pages. To deploy using GitHub pages:

1. Open the project repository.
2. Click on "Settings" on the navigation bar under the repository title.
3. Click on "Pages" in the left-hand navigation panel.
4. Under "Source", choose which branch to deploy. This should be Main for newer repositories.
5. Choose which folder to deploy from, usually "/root".
6. Click "Save", then wait for it to be deployed. It can take some time for the page to be fully deployed.
7. Your URL will be displayed above "Source".

You can visit the website [here](https://github.com/JonathanDussot/star-wars-quiz)

### Local Deployment

#### How to Fork

1. Copy the link to this repository.
2. Log in or sign up to your GitHub account and click on the **Fork** button on the top-right corner.
3. You should now have a copy included in your account.

#### How to Clone

1. Copy the link to this repository.
2. Log in or sign up to your GitHub account and click on the **Code** button.
3. You are given to option to clone using HTTPS or GitHub CLI and copy the link.

## Testing

click [here](TESTING.md) to see the all the details in regard to the testing done on the site.

## Credits

### Content

- The information I got for my questions mostly came from [buzzfeed](https://www.buzzfeed.com/laurafrustaci/star-wars-trivia)

- Some concepts and parts of code were taken from a [tutorial by 'Web Dev Simplified'](https://www.youtube.com/watch?v=riDzcEQbX6k) as detailed in my [script.js](script.js).

- [Stackoverflow](https://stackoverflow.com/questions/9419263/how-to-play-audio) and their ideas of how to implement audios and counters

### Media

- The [3d-space-image.jpg](assets/images/3d-space-image.jpg), was taken from [freepik.com](www.freepik.com) from an author named [@kjpargeter](https://www.freepik.com/author/kjpargeter) to give that outerspace, sci-fi feeling theme to my quiz.

[3d-space-image.jpg from freepik](https://www.freepik.com/free-photo/3d-hyperspace-background-with-warp-tunnel-effect_8879794.htm#query=star%20wars&position=0&from_view=search&track=ais&uuid=2743de4c-8bee-445b-a1a5-01771d3ccbf6)

- The [star-wars-logo.jpg](assets/images/star-wars-logo.jpg) was taken from the [infonegociosmiami](https://infonegocios.miami/) website, which gave me the perfect looking logo for the quiz offering a great colour contrast due to its font-colour and width of the lettering.

[star-wars-logo.jpg from infonegociosmiami](https://infonegocios.miami/impact-mkt/conocida-en-todas-las-estrellas-explorando-el-legado-del-logo-de-star-wars-una-odisea-de-diseno-y-marca-parte-i)

- The [yoda.png](assets/images/yoda.png), [darth-maul-img.png](assets/images/darth-maul-img.png), [darth-sidious-img.png](assets/images/darth-sidious-img.png) and [darth-vader-img.png](assets/images/darth-vader-img.png) were all transparent png images used within my game to give it a nostalgic and dynamic feeling to all users going through the experience provided by the quiz. The images of Yoda and Darth-Vader were taken from [pngimg.com](https://pngimg.com). Darth Maul's image was taken from [iconarchive](https://www.iconarchive.com/) and Darth Sidious's was taken from [pngkey.com](https://www.pngkey.com/).

[yoda.png](https://pngimg.com/image/109430)

[darth-maul-img.png](https://www.iconarchive.com/show/star-wars-characters-icons-by-jonathan-rey/Darth-Maul-02-icon.html) created by Jonathan Rey.

[darth-sidious-img.png](https://www.pngkey.com/maxpic/u2e6w7i1a9a9a9a9/) created by The HD Colin Powell Anthrax.

[darth-vader-img.png](https://pngimg.com/image/28358)

- The sound media files [gamestart-sound.mp3](sounds/gamestart-sound.mp3), [correct-sound.mp3](sounds/correct-sound.mp3) and [incorrect-sound.mp3](sounds/incorrect-sound.mp3) were all taken from [soundfxcenter](https://soundfxcenter.com/).

[All sound files](https://soundfxcenter.com/sound-effects/star-wars/210)

## Acknowledgements

I would like to acknowledge the following people who have been a huge help for this project:

- [Lauren-Nicole](https://github.com/CluelessBiker) - My Code Institute Mentor for her advice and expertise.

- The Slack community of Code Institute for their help and support.

- Tutor Support from Code Institute for their help and support.