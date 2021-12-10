# foodgram

Дипломный проект курса Python-разработчик на Яндекс.Практикум.

![foodgram workflow](https://github.com/bayborodin/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

## Описание проекта

С помощью сервиса **foodgram** (продуктовый помощник) пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Стек технологий

- Python 3
- Django
- Django REST Framework
- Djoser and Simple JWT
- React

## Как запустить

Загрузка ингредиентов:

```shell
./manage.py load_ingredients --file='~/Projects/foodgram-project-react/data/ingredients.csv'
```

## Автор

Николай Байбородин ([Twitter](https://twitter.com/bayborodin) | [GitHub](https://github.com/bayborodin) | [Telegram](https://t.me/nbayborodin))

## Лицензия

Данный проект распространяется под лицензией [MIT](http://opensource.org/licenses/MIT).
