# os-alerts
Simple Web Scraping App for get information from website of Operating Systems professor in Uniroma2

# Usage
Hi, if you want to use my code you will need to specify some information in a file called ```.env```, which will contain the following information:

```shell
# MongoDB
export USERNAME=""
export PASSWORD=""
export CLUSTER=""
export SESSION=""

# Scraper
export URL_2023=""
export HOUR=""

# Telegram Bot
export TOKEN=""
export CHAT_ID=""
```

or you can configure the ```config.json``` file as follows:

```shell
{
    "USERNAME": "",
    "PASSWORD": "",
    "CLUSTER": "",
    "SESSION": "",
    "URL_2023": "",
    "HOUR": "",
    "TOKEN": "",
    "CHAT_ID": ""
}
```

>**NOTE:** You need to have an active **mongo** database.

>**NOTE:** Remember to change the value of the ```config_mode``` variable according to the type of mode you choose to use!

# Links
Telegram Bot Link: https://t.me/CleverCodeBot