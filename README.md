# Your best psychologist
## **Description**:

## The main idea
This bot is made for Telegram users. It gives you an opportunity to choose your desired psychologist.
As you chose the psychologist, you can write anything you want and you will get a professional response.

## Folder `static`
This folder contains photos of psychologists.

## File `config.py`
In this file you have to enter your Telegram bot's token to make it work as needed.

## File `bot.py`
Here is actual work starts.

- Program uses a list of dictionaries with all the information about psychologists.
  - Here program contains psychologists' name, id, description and image directory
- Program contains psychologists' names in a `psychologistsNames` list. This list is used when program sends user a menu to choose the psychologist.
- Program uses `chosenSpecialist` to remember, which psychologist is working with user. If any of them - the variable has value of `0`. If the psychologist is chosen, it contains psychologist's name.
- When user writes `/start`, bot greets him and sends instructions with a menu. Now this menu contains only one option.
- When user writes `/end`, bot ends the session. As well, program assign global variable `chosenPsycologist` to `0` (default value).
- `send_list_of_psychologists` function sends all the information about every psychologist (its image; description, which contains the name, age and a little valuable information)
- When user presses `Available psychologists`, bot sends him the list of psychologists (their photos, description) and a menu, where user can choose the psychologist he likes. There are psychologists' names in the menu. When user presses the button with psychologist's name, program assigns this name as value to the global variable `chosenSpecialist`.
- If user have not chosen a psychologists yet and now he presses the button with psychologist's name, program assigns this name as value to the global variable `chosenSpecialist` and removes the menu. Saved information will help when program will be deciding whose sound to send (in response to user's message).
- If user enters other text:
  - If user have not chosen a psychologist, bot will remind the user about it. It will do it until user chooses a psychologist or enter `/start` or `/end` command.
  - If user have already chosen a psychologist, bot will response with psycologists sound. Sound will be 'said' random times (from 1 to 3 inclusively).
- In the bottom of the program there is a block, that helps bot to work constantly, even if program gets some troubles while running.
