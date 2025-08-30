import asyncio
import pytest

from configs.db.mongo import db_client


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


async def usar_mongo():
    client = await db_client.get_client()
