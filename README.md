# Bright Money hiring task

Hi there, i have created a basic automation application for data analysis using django. It analyses your csv file on certain parameters and sends you a periodic mail after every 5 mins.

## Steps to run the project:
-   Create a virtual environment & activate it.
-   `pip install -r requirements.txt`
-   Create a .env file (refer .env.example)
-   `python manage.py runserver`
-   Start your celery in a separate terminal
-   `celery -A task worker -l info -B`


## Note
- Setup rabbitmq in your system (for macos users)
  `brew install rabbitmq`
- If using gmail account to send mails, allow less secure apps settings in your google account.