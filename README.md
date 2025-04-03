# Scaloneta Bot

**Scaloneta Bot** is an automated Twitter bot designed to keep fans of the Argentina national fútbol team informed about upcoming matches. By tweeting countdowns and match details, it ensures supporters are always aware of when the next game is scheduled.

## Features

- **Automated Countdown Tweets**: Regular updates on the time remaining until Argentina's next match.
- **Match Details**: Information about the opponent, date, and time of upcoming fixtures.

## Twitter Account

The bot operates under the Twitter handle [@nextscaloneta](https://x.com/nextscaloneta). An example of its functionality can be seen in this tweet:

> [https://x.com/nextscaloneta/status/1638239195906068480](https://x.com/nextscaloneta/status/1638239195906068480)

## Technologies Used

- **Python**: The core programming language for scripting the bot's functionalities.
- **Twitter API**: For posting tweets and retrieving relevant data.
- **football.api-sports.io**: for fútbol relevant data.
- **AWS Lambda**: To host and run the bot's operations in a serverless environment.
- **AWS CloudWatch**: For scheduling the bot's execution and monitoring its performance.

## Setup and Deployment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/alexing/scaloneta.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd scaloneta
   ```
3. **Install Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure AWS Credentials**: Ensure that your AWS credentials are set up properly to allow the bot to interact with AWS Lambda and CloudWatch.
5. **Deploy to AWS Lambda**: Use the provided `buildpackage.sh` and `createlambdalayer.sh` scripts to package and deploy the bot to AWS Lambda.
6. **Set Up CloudWatch Events**: Schedule the bot's execution using AWS CloudWatch to ensure it runs at specified intervals to check for upcoming matches and tweet updates accordingly.

## Contributing

Contributions to enhance the Scaloneta Bot are welcome. If you have ideas for new features or improvements, please fork the repository and submit a pull request.

