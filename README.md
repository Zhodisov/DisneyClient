# 🌟 DisneyClient Setup 🚀

Welcome to DisneyClient! This README will guide you through setting up the DisneyClient. If you encounter any issues or need assistance, feel free to contact us on Discord or via email. 📧

# Since 2021, DisneyClient has been available for your use. While we won't continue the project, users with the paid private version will receive support to help set up everything.

### Contributors
- Monkus
- Jodis
- DailyEm
- ラ・ムカテ
- BlancSnz
- BialySnz
- Jawad


## Requirements

Before getting started, ensure you have the following prerequisites:
- 🌐 Mysql Database (Online or Local) | [DigitalOcean](https://digitalocean.com)
- 🌐 Heroku / VPS (Hosting) | [Heroku](https://www.heroku.com/)
- 📊 Google Sheets API (Sheet Reader) | [Google Sheets API](https://developers.google.com/sheets/api)
- 🤖 Discord Bot Token (For Logs and Commands) | [Discord Developer Portal](https://discord.com/developers/applications)
- 🐍 Python 3.11 (Not required if using Heroku) | [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- 🌐 Github Account | [Github](https://github.com/)
- 💼 Disney Client Parser Endpoint
- 🔑 Disney Client Parser Token

## 🌐 Environment Variables (ENV) Example

For your convenience, here's an example of the required environment variables:

- 🏦 MARIADB_ENDPOINT | `mysql://doadmin:AVNS_xxxxxxxxxxxxxxxxxx@db-mysql-frax-xxxxx-do-user-xxxxxxxx-x.b.db.ondigitalocean.com:25060/defaultdb`
- 🤖 DISCORD_API_TOKEN | `MTE1NxxxxxxxxxxxxxxxxxxxYwNg.GgTTV2.ZxxxxxxxxxxxxxxxxYN5LAC6xxxx8-3xxxI`
- 🌐 PORT | `80`
- 🔑 TFM_PARSER_API_TOKEN | `5b5012c589c4cfc51a2b44cbba148908667fe5eee70`
- 💼 TFM_PARSER_ENDPOINT | `https://disneyclient-parser-xxxxxxxxxxxxxxxxxx.herokuapp.com`

## 📥 Where to Download

You can download DisneyClient from [safemarket.xyz/discord](https://safemarket.xyz/discord) or here.

1. **Setting Up Your Github Repository**

   - Create a Github account [here](https://github.com/signup?source=login).
   - After creating your account, create a NEW private repository on Github.
   - Extract the contents of the zip file from [safemarket.xyz/discord](https://safemarket.xyz/discord).
   - Upload all the extracted files to your Github repository.


   - Navigate to the `DisneyClient` folder and edit the `config.json` file.
   - Modify the following parameters:
     - `discord_admins` | ID of the admins
     - `discord_log_channel` | ID of log channel 1
     - `discord_log_channel2` | ID of log channel 2
     - `discord_priv_channel` | ID of private channel 1
     - `discord_priv_channel2` | ID of private channel 2
     - `discord_major_role_id` | ID of the role for Discord commands


   - In a new private repository, upload the contents of the `DisneyParser` folder and replace `Tokens.json` with the desired value for `TFM_PARSER_API_TOKEN`.

2. **Creating Google Sheets API**

   - Follow [these instructions](https://cloud.google.com/docs/authentication#service-accounts) to create a Google Sheets API account.
   - Save the credentials as a file named `service_account_credentials.json` in the root directory.

3. **Creating a MySQL Database with DigitalOcean**

   - Create a MySQL Database with DigitalOcean, either by purchasing it or using the $200 gift [here](https://try.digitalocean.com/freetrialoffer/).
   - Configure the database as shown in this [screenshot](https://prnt.sc/i2ae87WLLyNv).
   - Use `createmariadb.py` to automatically create your database (replace the ID).
   - Tables:
     - Maps | [Screenshot](https://prnt.sc/EbCdzZ_Cy5ls)
     - Soft | [Screenshot](https://prnt.sc/DB_DPSiapxUI)
     - Users | [Screenshot](https://prnt.sc/5O6VhaW3OG1e)
     - Config | No need to modify.

4. **Creating a Heroku Account**

   - Sign up for a Heroku account [here](https://signup.heroku.com/).
   - Use real information and add a valid card to avoid any bans.
   - Create an app with a lowercase name, such as "disneyparse" or "disney-parse."
   - Go to Settings and click on "Reveal Config Vars."
   - Enter all the environment variables like `MARIADB_ENDPOINT`, `DISCORD_API_TOKEN`, `PORT`, `TFM_PARSER_API_TOKEN`, and `TFM_PARSER_ENDPOINT`.
   - Scroll down and add a buildpack (if not already added); you need `heroku/python`.
   - In the Deploy section, connect your Github account.
   - Open a new tab for `DisneyParse` and `DisneyClient` on Heroku.
   - Click Deploy on both tabs and connect your Github repository.
   - Enable automatic deploy, and deploy your app.
   - Check the logs for debugging information and startup.
   - In the Overview section, configure dynos and activate web for both Heroku apps.
   - Once everything is okay, you can access the website by opening the DisneyClient tab on Heroku and clicking "Open App."

5. **Changing the SWF**

   If you need to change the SWF file, you can use [this tool](https://github.com/Jodis974/DisneyClient-Builder).

If you encounter any issues or need assistance, feel free to contact us on Discord or via email:

- 🌐 Website: [safemarket.xyz](https://safemarket.xyz)
- 💬 Discord: [safemarket.xyz/discord](https://safemarket.xyz/discord)
- 📧 Email: support-checkout@safemarket.xyz
