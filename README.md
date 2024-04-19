# Cross-Game Cloud Variables
## Made for Scratch.

### Example games
Game 1: https://scratch.mit.edu/projects/1002254974/
Game 2: https://scratch.mit.edu/projects/1004691810/

### How does it work?
Any changes made to a cloud variable in either game is detected. Once the change is detected, we set the other variable to make the two match. We also update a server status variable to tell the client if the server is online.

### How are cloud variables read and changed?
We used scratchattach! This is a Python library that allows Python to access Scratch's cloud variables.
https://github.com/TimMcCool/scratchattach

### How can I set it up?
Replace COOKIE with your scratch session cookie. More details can be found at scratchattach's Github. Then, create a copy of Game 1 and Game 2.

## Special thanks to scratchattach!
