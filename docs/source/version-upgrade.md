# Version upgrade

This page documents version upgrade

## Upgrade to 4.1.4
To upgrade to 4.1.4, you need to change the configuration file (sostrades-webapi configuration.json) database sections.
To connect to your previous mysql database, the changes needed are :

### Old format (pre 4.1.4)
```json
...
  "SQL_ALCHEMY_DATABASE": {
    "HOST" : "127.0.0.1",
    "PORT" : 3306,
    "USER_ENV_VAR": "SQL_ACCOUNT",
    "PASSWORD_ENV_VAR": "SQL_PASSWORD",
    "DATABASE_NAME": "sostrades-data",
    "SSL": false
  },
  "SQLALCHEMY_TRACK_MODIFICATIONS": false,
  "LOGGING_DATABASE": {
    "HOST" : "127.0.0.1",
    "PORT" : 3306,
    "USER_ENV_VAR": "LOG_USER",
    "PASSWORD_ENV_VAR": "LOG_PASSWORD",
    "DATABASE_NAME": "sostrades-log",
    "SSL": false
  },
...
```

### New format (post 4.1.4)
```json
...
  "SQL_ALCHEMY_DATABASE": {
      "CONNECT_ARGS": {
          "ssl": false,
          "charset": "utf8mb4"
      },
      "URI":"mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/sostrades-data",
      "URI_ENV_VARS": {
          "USER": "SQL_ACCOUNT",
          "PASSWORD": "SQL_PASSWORD"
      }
  },
  "SQLALCHEMY_TRACK_MODIFICATIONS": false,
  "LOGGING_DATABASE": {
      "CONNECT_ARGS": {
          "ssl": false,
          "charset": "utf8mb4"
      },
      "URI":"mysql+mysqldb://{USER}:{PASSWORD}@127.0.0.1:3306/sostrades-log",
      "URI_ENV_VARS": {
          "USER": "LOG_USER",
          "PASSWORD": "LOG_PASSWORD"
      }
  },
...
```
