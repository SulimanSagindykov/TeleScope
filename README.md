# TeleScope

TeleScope is a powerful Telegram bot for analyzing subscriber interactions, tracking user activity in Telegram channels and groups, and managing invite links. This project is designed to help administrators monitor their community’s engagement and subscriber status efficiently.

## Features

- **Track Subscriber Status**: Track when users subscribe, unsubscribe, or join through invite links.
- **Invite Link Management**: Manage invite links and retrieve detailed statistics on user engagement through various invite links.
- **Real-Time Updates**: Receive real-time updates on subscriber changes directly from Telegram channels and groups.
- **Asynchronous Processing**: Optimized for high performance with asynchronous task handling.
- **Admin Notifications**: Send subscriber status updates directly to admins.
  
## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Bot Commands](#bot-commands)
4. [Database Migrations](#database-migrations)
5. [Running the Tests](#running-the-tests)

## Installation

### Prerequisites

Before running TeleScope, ensure that you have the following installed:

- Python 3.9+
- Poetry (for dependency management)
- A PostgreSQL database (if using a different database, ensure it's properly configured in `settings.py`)
- Telegram Bot API token (from [BotFather](https://core.telegram.org/bots#botfather))

### 1. Clone the Repository

```bash
git clone https://github.com/SulimanSagindykov/TeleScope.git
cd TeleScope
```

### 2. Setup with Poetry
First, ensure you have Poetry installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Install project dependencies:

```bash
poetry install
```

### 3. Setup Environment Variables
Create a .env file at the root of the project and add the necessary environment variables. You can also use export in your terminal.

Example .env file:

```bash
TOKEN_BOT=your_telegram_bot_token
ADMIN_ID=your_admin_chat_id
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```
### 4. Apply Database Migrations
Before starting the bot, ensure the database is set up correctly.

```bash
poetry run python manage.py migrate
```

### 5. Run the Bot
To start the bot:

```bash
poetry run python manage.py run_bot
```

### Running the Django Server
You can also run the Django server for the web interface (if needed):

```bash
poetry run python manage.py runserver
```

### Usage
Once the bot is running, you can manage subscribers and invite links for your Telegram channels or groups. The bot handles:

 - Notifications when a user joins or leaves a channel.
 - Monitoring invite links to check which ones were used to join.
 - Sending detailed user data (username, ID, join method) to the admin.
###  Bot Commands
- ```/start```: Start the bot and receive a welcome message.
- ```/help```: Get help with the bot's functionality.
- The bot sends real-time updates to the admin based on user activity in the monitored channels.


### Database Migrations
If you make changes to the models or database schema, you will need to create and apply migrations:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
### Running the Tests
To run the tests and ensure everything is functioning correctly:

```bash
poetry run python manage.py test
```

