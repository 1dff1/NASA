# NASAbot RU

#### Описание программы

Данный код представляет собой Telegram-бот, который предоставляет пользователю возможность получить фотографии с Марса, сделанные марсоходами Curiosity, Spirit и Opportunity. Бот также предоставляет список команд для управления и информацию о марсоходах.

#### Использование

Для использования бота необходимо установить библиотеку aiogram. Затем можно запустить программу, указав API-токен Telegram-бота в переменной `API_TOKEN`.

#### Список команд

- `/start` - начать использование бота.
- `/help` - получить список доступных команд.
- `/image` - получить фотографию с Марса.
- `/donat` - поддержать создателя и бобров.

#### Получение фотографии с Марса

Для получения фотографии с Марса необходимо использовать команду `/image`, после чего бот предложит выбрать марсоход: Curiosity, Spirit или Opportunity. После выбора марсохода, бот отправит случайную фотографию с Марса, сделанную выбранным марсоходом.

#### Поддержка создателя и бобров

Если вы хотите поддержать создателя бота и бобров, вы можете воспользоваться командой `/donat`, где будут указаны реквизиты для перевода денег.

#### Информация о марсоходах

Вы также можете получить информацию о марсоходах, используя команду `/info`. Бот предоставит описание марсоходов Curiosity и Spirit, а также информацию о миссии и целях их исследования на Марсе.

#### Пример использования

```
/start - начать использование бота
/help - получить список команд
/image - получить фото с Марса
/donat - поддержать создателя и бобров
```

#### Завершение

Для запуска бота необходимо вызвать функцию `dp.run_polling(bot)`. Бот будет готов к использованию после запуска.
# NASAbot

#### Description of the Program

This code is a Telegram bot that allows users to get photos from Mars taken by the Curiosity, Spirit, and Opportunity rovers. The bot also provides a list of commands for controlling the bot and information about the rovers.

#### Usage

To use the bot, you need to install the aiogram library. Then you can run the program by specifying the Telegram bot's API token in the `API_TOKEN` variable.

#### List of Commands

- `/start` - start using the bot.
- `/help` - get a list of available commands.
- `/image` - get a photo from Mars.
- `/donate` - support the creator and beavers.

#### Getting a Photo from Mars

To get a photo from Mars, use the `/image` command. The bot will then prompt you to choose a rover: Curiosity, Spirit, or Opportunity. After selecting a rover, the bot will send a random photo from Mars taken by the chosen rover.

#### Supporting the Creator and Beavers

If you want to support the bot's creator and beavers, you can use the `/donate` command, which will provide the details for making a donation.

#### Information about the Rovers

You can also get information about the rovers by using the `/info` command. The bot will provide descriptions of the Curiosity and Spirit rovers, as well as information about their missions and research goals on Mars.

#### Example Usage

```
/start - start using the bot
/help - get a list of commands
/image - get a photo from Mars
/donate - support the creator and beavers
```

#### Conclusion

To run the bot, you need to call the `dp.run_polling(bot)` function. The bot will be ready to use after it starts running.
