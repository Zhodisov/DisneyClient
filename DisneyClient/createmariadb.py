



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



import pymysql

def create_tables():
    DATABASE_URL = {
        "host": "",
        "user": "",
        "password": "",
        "database": "",
        "port": 25060,
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
        "ssl": {
            'ca': 'ca-certificate.crt'
        }
    }

    try:
        connection = pymysql.connect(**DATABASE_URL)
        print("Connexion à la base de données réussie !")

        with connection.cursor() as cursor:
            try:
                create_users_table = """
                    CREATE TABLE IF NOT EXISTS `users` (
                        `key` VARCHAR(16) PRIMARY KEY,
                        `level` VARCHAR(10) DEFAULT 'GOLD_II',
                        `last_login` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        `browser_access` BOOLEAN DEFAULT TRUE,
                        `browser_access_token` VARCHAR(40),
                        `flash_token` VARCHAR(32),
                        `key_hidden` BOOLEAN DEFAULT FALSE,
                        `connection_limit` INT DEFAULT 2,
                        `unknown_device_block` BOOLEAN DEFAULT TRUE
                    );
                """
                create_config_table = """
                CREATE TABLE IF NOT EXISTS `config` (
                    `key` VARCHAR(16) PRIMARY KEY,
                    `tfm_menu` JSON
                );
            """
                create_soft_table = """
                CREATE TABLE IF NOT EXISTS `soft` (
                    `key` VARCHAR(16) PRIMARY KEY,
                    `data` LONGBLOB
                );
            """
                create_map_table = """
                CREATE TABLE IF NOT EXISTS `map` (
                    `key` VARCHAR(16) PRIMARY KEY,
                    `data` LONGBLOB,
                    `modified` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                );
            """
                cursor.execute(create_users_table)
                cursor.execute(create_soft_table)
                cursor.execute(create_map_table)
                cursor.execute(create_config_table)


                connection.commit()
                print("Tables créées avec succès !")

            except Exception as e:
                print(f"Erreur lors de la création des tables : {e}")

    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")

    finally:
        if 'connection' in locals() and connection:
            connection.close()

if __name__ == "__main__":
    create_tables()



#                https://safemarket.xyz | https://safemarket.xyz/discord
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#  | | ____     _     _____  _____      __  __     _     ____   _  __ _____  _____ | |  
#  | |/ ___|   / \   |  ___|| ____|    |  \/  |   / \   |  _ \ | |/ /| ____||_   _|| |  
#  | |\___ \  / _ \  | |_   |  _|      | |\/| |  / _ \  | |_) || ' / |  _|    | |  | |  
#  | | ___) |/ ___ \ |  _|  | |___     | |  | | / ___ \ |  _ < | . \ | |___   | |  | |  
#  | ||____//_/   \_\|_|    |_____|    |_|  |_|/_/   \_\|_| \_\|_|\_\|_____|  |_|  | |  
#__| |_____________________________________________________________________________| |__
#__   _____________________________________________________________________________   __
#  | |                                                                             | |  
#                               https://github.com/Jodis974                           



