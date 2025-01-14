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

