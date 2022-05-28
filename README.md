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
Here is where the actual work starts.

- Program uses a list of dictionaries with all the information about psychologists.
  - Here program contains psychologists' name, id, description and image directory
- Program contains psychologists' names in a `psychologistsNames` list. This list is used when the program sends the user a menu to choose the psychologist.
- Program uses `chosenSpecialist` to remember which psychologist is working with the user. If any of them - the variable has a value of `0`. If the psychologist is chosen, it contains the psychologist's name.
- When the user writes `/start`, the bot greets him and sends instructions with a menu. Now this menu contains only one option.
- When the user writes `/end`, bot ends the session. As well, the program assigns the global variable `chosenPsycologist` to `0` (default value).
- `send_list_of_psychologists` function sends all the information about every psychologist (its image; description, which contains the name, age and a little valuable information)
- When the user presses `Available psychologists`, bot sends him the list of psychologists (their photos, description) and a menu, where the user can choose the psychologist he likes. There are psychologists' names in the menu. When the user presses the button with the psychologist's name, the program assigns this name as value to the global variable `chosenSpecialist`.
- If the user has not chosen a psychologists yet and now he presses the button with the psychologist's name, the program assigns this name as value to the global variable `chosenSpecialist` and removes the menu. Saved information will help when the program will be deciding whose sound to send (in response to the user's message).
- If the user enters other text:
  - If the user has not chosen a psychologist, bot will remind the user about it. It will do it until the user chooses a psychologist or enter `/start` or `/end` command.
  - If the user has already chosen a psychologist, bot will respond with psychologists sound. Sound will be 'said' random times (from 1 to 3 inclusively).
- In the bottom of the program there is a block that helps the bot to work constantly, even if the program gets some troubles while running.


