# Miller Time

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Current Statistics](#statistics)

## About <a name = "about"></a>

Every year Miller Lite tends to put on a giveaway for gear. However, all of these giveaways are "time based" to where a random time is picked and whoever submits an application at that time should win. This program is putting that to the test.

This script will enter in random information for each entry to test if you will win any. This SHOULD NOT be used to try to win anything. It's used to test the statistics of winning an item. Rules are already in place to remove applicants from receiving any item who spam the system.

This program will download the CAPTCHA images used for submission and save the correct answer as the name as the file. This can be used for anything you would like.

Finally, do not use this to spam anyone with mailing list subscriptions. Either use a domain for the generated emails that does not exist or use your own email and add (+any random number EX. fakeemail+923842@fakedomain.com) before your domain. You should be using your own mailing address as well along with your own phone number or create a number through Google. No one likes getting spammed with things especially things they don't sign up for.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You can get the modules for this program by running:

```
pip3 install -r requirements.txt
```
You will need Chrome Driver which can be downloaded at:
```
https://chromedriver.chromium.org/
```
You will also need to get an API key for AZCAPTCHA which can be done here:
```
https://azcaptcha.com/account/signin
```


### Installing

```
git clone https://github.com/ZachJBurns/ItsMillerTime
```

After installing, you will have to fill out the global variables at the top of MillerTime.py
## Usage <a name = "usage"></a>

You can run the script with the following:
```
python3 MillerTime.py
```

## Current Statistics <a name = "statistics"></a>
```
Total Wins: 0
Total Submission: 4133 (This would be a total of 12,399 submissions since you get 3 submissions per account creation)
Total Captcha Failures: 776
```
