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
  - [How To Play](#how-to-play)
    - [My GitHub Repository](#my-github-repository)
  - [CONTENTS](#contents)
  - [Intelligent Diagramming chart](#intelligent-diagramming-chart)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Implementations](#future-implementations)
    [Technologies Used](#technologies-used)
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

## Intelligent Diagramming chart

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

1. A Multi-player option where users take turns to see who finds the number first.
2. A variety of other clues given especially at higher difficulties so users can put their math skills to the test.
  
## Technologies Used

### Libraries and Programs Used

[GitHub](https://github.com/) to save and store my website.

[Gitpod](https://www.gitpod.io/) IDE I used for this project.

[Lucidchart](https://www.lucidchart.com/pages/) to create intelligent diagramming chart.

Colorama - library I used to apply different colours and styles to my text.

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