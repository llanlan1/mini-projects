Intro to my mini projects:

----------------------------------------------------------------------

dice_roll.py
## Roll the dice and guess the dice number!

The Dice Roll game is a simple Python program where the user guesses the outcome of a dice roll. The program generates two random dice rolls, sums them up, and checks if the user's guess matches the total.

### Features
- Generates two random dice rolls.
- Allows the user to guess the total value of the dice rolls.
- Validates the user's input.
- Displays the results with a slight delay for an engaging experience.
- Declares the user as a winner if their guess matches the total or encourages them to try again if they lose.

### Use Case
The Dice Roll game is a fun and interactive way to:
- Practice basic Python programming skills, especially with random number generation and user input handling.
- Understand control flow with conditions and loops in Python.
- Introduce beginners to concepts like probability and randomness in a simple, engaging manner.
- Provide a quick, entertaining program for casual play or educational demonstrations.

###How It Works

- The user is prompted to enter a guess.
- The program rolls two dice with 6 sides (default).
- It calculates the maximum possible value of the dice rolls and checks if the guess is valid.
- The dice rolls are revealed one at a time, followed by the total.
- If the user's guess matches the total, they win. Otherwise, they lose.

### Prequisites

Python 2.x (Uses raw_input and print statements with % formatting specific to Python 2).

###Installation

- Clone or download the repository containing this program.
- Ensure you have Python 2.x installed on your system.

###Usage

- Run the program in a Python 2.x interpreter:
python dice_roll.py
- Follow the prompts:
- Enter your guess when prompted.
- Wait for the results as the program rolls the dice and displays the outcome.

### Example in Python

python dice_roll.py

Output:

Guess a number: 7
Maximum possible value is 12.
Rolling...
The first roll is 3
The second roll is 4
7
Result...
You have won!

###Customization

- You can customize the number of sides on the dice by modifying the roll_dice function. For example:
first_roll, second_roll, max_val = roll_dice(10)

- This will use a 10-sided die instead of the default 6-sided die.

----------------------------------------------------------------------

ic_checker.py
## ID Checker for validity of NRIC/FIN (Singapore ID)

The IC Checker module validates Singapore NRIC (National Registration Identity Card) and FIN (Foreign Identification Number) using an official checksum algorithm. This script ensures IDs are accurate and conform to the required format.

### Features
- Validates NRIC and FIN numbers using prefix and checksum rules.
- Supports both NRIC (e.g., S1234567D) and FIN (e.g., G1234567Q) formats.
- Provides clear error messages for invalid or improperly formatted IDs.

### Use Case
Ideal for scenarios where quick and reliable validation of Singapore IDs is required, such as in personal projects, applications requiring user ID verification, or for learning purposes.

### Example in Python

from ic_checker import validate_id

id_number = "S1234567D"
if validate_id(id_number):
    print("Valid NRIC/FIN!")
else:
    print("Invalid NRIC/FIN.")


------------------------------------------------------------------------


largest_product.py
## LargestProductSeries

The `LargestProductSeries` module is designed to compute the largest product of `n` consecutive digits in a numeric series. This functionality can be applied to solve sequence-based problems efficiently.

### Features
- Calculates the product of any specified number of consecutive elements (`n`).
- Handles both numeric strings and arrays of integers.
- Validates input to ensure the series contains only digits or numbers.

### Use Case
Ideal for scenarios requiring maximum product calculations within a sliding window, such as solving Project Euler challenges or analyzing financial data trends.

### Example in Python

from largest_product_series import calculate_largest_product

series = "73167176531330624919225119674426574742355349194934"
n = 6
result = calculate_largest_product(series, n)
print(f"The largest product of {n} consecutive digits is: {result}")

----------------------------------------------------------------------

rock_paper_scissors.py
## A Rock, Paper, Scissors Game

The Rock, Paper, Scissors game is a simple Python program that lets you play the classic game against a computer opponent. The program randomly selects an option for the computer and determines the winner based on the rules of the game.

### Features
- Allows the user to select one of the three options: Rock, Paper, or Scissors.
- Randomly generates the computer's choice.
- Compares the user's choice with the computer's choice and determines the winner.
- Displays results with corresponding messages for ties, wins, or losses.

### Use Case
The Rock, Paper, Scissors game is ideal for:
- Practicing Python programming basics, such as user input, conditional statements, and random number generation.
- Providing a quick and entertaining game for casual play or demonstrations.
- Introducing beginners to programming through a simple yet engaging project.

###How It Works

- The user is prompted to input their choice (Rock, Paper, or Scissors).
- The computer randomly selects one of the three options.
- The program compares the user's choice with the computer's choice based on the following rules:

Rock beats Scissors.
Scissors beats Paper.
Paper beats Rock.

- A message is displayed indicating whether the user won, lost, or tied.

### Prequisites

Python 2.x (Uses raw_input and print statements with % formatting specific to Python 2).

###Installation

- Clone or download the repository containing this program.
- Ensure you have Python 2.x installed on your system.

###Usage

- Run the program in a Python 2.x interpreter:

python rock_paper_scissors.py

- Follow the prompts:
- Enter your choice (Rock, Paper, or Scissors) when prompted.
- Wait for the program to display the computer's choice and the result.

### Example in Python

python rock_paper_scissors.py

Output:

Enter Rock, Paper, or Scissors: Rock
You selected ROCK
Computer selected SCISSORS
Yay you won!

###Customization

- You can customize the game by modifying the options list or adding more detailed messages in the message dictionary. For example:

options = ["ROCK", "PAPER", "SCISSORS", "LIZARD", "SPOCK"]

- This would extend the game to include the additional options from the expanded version of the game.

----------------------------------------------------------------------

# Server Timestamp and Nmap HTML Viewer

## Overview
This PHP script displays the current server timestamp and includes the content of an `nmap.html` file. It can be used to check the server's time and display information from an existing HTML file.

---

## Features
- Displays the server's current timestamp in the format `hh:mm:ss am/pm`.
- Embeds the content of `nmap.html` for viewing within the browser.
- Provides a simple structure for combining dynamic PHP output and static HTML content.

---

## File Description
- **PHP Script**: 
  - Displays the server timestamp using PHP's `date()` function.
  - Includes and renders the `nmap.html` file within a `<pre>` block for formatted display.
  
- **nmap.html**: 
  - A static HTML file whose content will be included and displayed by the PHP script.

---

## Usage
1. Place the PHP file and `nmap.html` in the same directory on your web server.
2. Ensure your server is configured to handle PHP files.
3. Access the PHP script via your browser by navigating to:

http://localhost/path-to-script/network.php
or
http://your-server-address/path-to-script/network.php

---

## Prerequisites
1. A web server with PHP support (e.g., Apache, Nginx).
2. The `nmap.html` file must exist in the same directory as the PHP script.

---

## Output Example
When the script runs, the browser will display:

Example:

Server Timestamp: 11:22:14am

# Nmap 7.80 scan initiated Wed Nov 27 11:23:01 2024 as: nmap -oN /var/www/html/nmap.html 192.168.1.0/24
Nmap scan report for 192.168.1.0
Host is up (0.00044s latency).
All 1000 scanned ports on 192.168.1.0 are filtered


---

## Notes
- The `date()` function formats the timestamp based on the server's timezone settings. Ensure your server's timezone is correctly configured.
- If `nmap.html` is missing or cannot be found, the script may produce an error.

---

## Troubleshooting
1. **No Output in Browser**:
   - Ensure PHP is installed and configured correctly on your server.
   - Check file permissions to ensure the script and `nmap.html` can be read.

2. **Timezone Issues**:
   - Modify the PHP `date_default_timezone_set()` function in the script to set the correct timezone:
     ```php
     date_default_timezone_set('Asia/Singapore');
     ```

---


## Tutorial (Follow along if you want to make this yourself)

1. Log in as superuser
su -

2. Install the following
apt install apache2
apt install php
apt install nmap

3a. Create cron job
crontab -e
Note: type ’1’ and <ENTER> to use nano
or type ‘2’ and <ENTER>, then ‘i’ to use vim

3b. Append the following to the cron
*/10 * * * * nmap 192.168.1.0/24 -oN /var/www/html/nmap.html
Note: if you have used nano, CTRL-X to exit, then press ‘y’, then press <ENTER>
If you have used vim, <ESC> once to stop editing, then type ‘:wq’ and press <ENTER>

4a. Create a network.php file in /var/www/html/ 
nano /var/www/html/network.php

4b. Use the following code in the PHP file
<?php
echo "Server Timestamp: ";
echo date("h:i:sa");
echo "<pre>";
include("nmap.html");
echo "</pre>";
?>
Note: CTRL-X to exit, then press ‘y’, then press <ENTER>

5. Set the permissions to prevent editing by unauthorised users
chmod 751 /var/www/html

6. Give yourself ownership so you can see the output of the cron job
chown vboxuser /var/www/html
Note: replace ‘vboxuser’ with your own username

7. Log out of superuser
exit


---

## License
Feel free to use and modify this script as needed.

---

## Author
Created by Lan.

---



