from database.models import Category, Game, async_session
from sqlalchemy import select, delete, update


async def get_category():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result


async def get_game():
    async with async_session() as session:
        result = await session.scalars(select(Game))
        return result


async def get_games(category_id):
    async with async_session() as session:
        result = await session.scalars(select(Game).where(Game.category_id == category_id))
        return result

async def get_gc(game_id):
    async with async_session() as session:
        result = await session.scalar(select(Game).where(Game.id == game_id))
    return result
 

async def add_category2(category):
    async with async_session() as session:
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category

async def add_game2(game):
    async with async_session() as session:
        
        session.add(game)
        await session.commit()
        await session.refresh(game)
        return game

async def delete_game(game_id):
    async with async_session() as session:
        await session.execute(
            delete(Game).where(Game.id == game_id)
        )
        await session.commit()


async def get_games_cat(category_id, offset, limit):
    async with async_session() as session:
        result_cat_id = await session.scalars(
            select(Game).where(Game.category_id == category_id).offset(offset).limit(limit)
        )
        return result_cat_id.all()


