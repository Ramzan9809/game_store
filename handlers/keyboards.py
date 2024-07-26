from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from database.requests import *

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Категории')],
    [KeyboardButton(text='Игры')]
], resize_keyboard=True, input_field_placeholder='Выберете кнопку', one_time_keyboard=True)

# kb1 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='CS:GO',callback_data='cs')],
#     [InlineKeyboardButton(text='Dota2',callback_data='dota')],
#     [InlineKeyboardButton(text='Fortnite', callback_data='fortnite')]
# ])

# kb2 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Одиночные',callback_data='odinochnue')],
#     [InlineKeyboardButton(text='Песочница',callback_data='pesochnuca')],
#     [InlineKeyboardButton(text='Онлайн', callback_data='onlain')]
# ])

# async def builder_kb():
#     num = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         num.add(KeyboardButton(text=str(i)))
#     return num.adjust(4).as_markup()


async def categories():
    category_kb = InlineKeyboardBuilder()
    categories = await get_category()
    for category in categories:
        category_kb.add(InlineKeyboardButton(
            text=category.category_name,
            callback_data=f'category_{category.id}'))
    return category_kb.adjust(2).as_markup()


async def game():
    game_kb = InlineKeyboardBuilder()
    game = await get_game()
    for game in game:
        game_kb.add(InlineKeyboardButton(
            text=game.game_name,
            callback_data=f'game_{game.id}'))
    return game_kb.adjust(2).as_markup()


async def games(category_id):
    games_kb = InlineKeyboardBuilder()
    games = await get_games(category_id)
    for game in games:
        games_kb.add(InlineKeyboardButton(
            text=game.game_name,
            callback_data=f'games_{game.id}'))
    return games_kb.adjust(2).as_markup()

async def back_delete(game_id):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data=f'back_to_categories')],
        [InlineKeyboardButton(text='Удалить', callback_data=f'delete_{game_id}')]
    ])
    return kb

async def back():
    back_kb = InlineKeyboardBuilder()
    back_kb.add(InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_categories'))
    return back_kb.as_markup()


async def categories2():
    category_kb = InlineKeyboardBuilder()
    categories = await get_category()
    for category in categories:
        category_kb.add(InlineKeyboardButton(
            text=category.category_name,
            callback_data=f'category2_{category.id}'))
    return category_kb.adjust(2).as_markup()

async def delete_game(game_id):
    delete_kb = InlineKeyboardBuilder()
    delete_kb.add(InlineKeyboardButton(
        text='Удалить игру',
        callback_data=f'delete_{game_id}'))
    return delete_kb.as_markup() 


PAGE_SIZE = 2
async def games(category_id, page):
    offset = (page - 1) * PAGE_SIZE
    games_kb = InlineKeyboardBuilder()
    all_games = await get_games_cat(category_id=category_id, offset=offset, limit=PAGE_SIZE)
    
    for game in all_games:
        games_kb.add(InlineKeyboardButton(
            text=game.game_name,
            callback_data=f'game_{game.id}'
        ))

    # Add navigation buttons
    if page > 1:
        games_kb.add(InlineKeyboardButton(
            text='Previous',
            callback_data=f'page_{category_id}_{page-1}'
        ))
    if len(all_games) == PAGE_SIZE:
        games_kb.add(InlineKeyboardButton(
            text='Next',
            callback_data=f'page_{category_id}_{page+1}'
        ))
    
    return games_kb.adjust(2).as_markup()
