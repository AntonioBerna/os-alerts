# os-alerts

Simple Telegram Web Scraping App for get information from any website.

> [!NOTE]
> Initially this application was created with the aim of monitoring the website of Professor Francesco Quaglia, university professor of the operating systems (and advanced operating systems) course at the University of Rome Tor Vergata. Today this project has grown into a larger application that can monitor multiple websites at the same time.

## Simple docs
Clone the repository using the following command:

```bash
git clone https://github.com/AntonioBerna/os-alerts.git
```

Once the operation is complete, move to the newly cloned `os-alerts/` folder with the `cd` command. You will need to create (using the `touch` command) and configure the `.env` file having the following structure:

```bash
# MongoDB (in development...)
# export USERNAME=""
# export PASSWORD=""
# export CLUSTER=""
# export SESSION=""

# Telegram Bot
export TOKEN=""
export CHAT_ID=""
```

> [!WARNING]
> The implementation of mongodb has not yet been completed. Do not configure the `.env` file.

> [!NOTE]
> If you don't know how to get Telegram `TOKEN` and `CHAT_ID` don't hesitate to contact me.

Once you have finished configuring the `.env` file you must create a file (I recommend `.csv` but it is not mandatory) with the following structure:

```bash
database,url,hours
...
```

where `database` indicates the name of the database for each single URL that is monitored, `url` is the very URL you want to monitor and finally `hours` are the hours that must pass between one monitoring and the next.

> [!WARNING]
> There must be no spaces or blank lines within the `.csv` file.

Now you will have to create a virtual environment using the `virtualenv venv` command and then you will have to activate it with the `source venv/bin/activate` command. Now you will need to install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

Finally, in the `os-alerts/` folder you will find a file called `run.sh`. If you have configured everything correctly, using the command:

```
./run.sh
```

you should get a result similar to this:

```bash
+ python src/main.py --env .env --urls urls.csv
Bot running.
```

> [!NOTE]
> You can modify the `run.sh` file by adding for example the possibility of saving the database structure in a `.json` file. You should find this option commented out by default.

> [!WARNING]
> If you do not have the necessary permissions to run the `run.sh` file you can use the `chmod +x run.sh` command and the `./run.sh` command again.

## Links
Telegram Bot Link: https://t.me/CleverCodeBot