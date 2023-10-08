from uuid import UUID

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.tables import Lot
from app.models.lot import LotModel


class AuctionDAO:
    def __init__(self, session: async_sessionmaker):
        self.session = session

    async def find_all(self):
        async with self.session() as transaction:
            return (
                await transaction.scalars(
                    select(Lot).where(
                        Lot.deleted.is_(False),
                    )
                )
            ).all()

    async def find_one(self, action_id: UUID):
        async with self.session() as transaction:
            return (
                await transaction.scalars(
                    select(Lot).where(
                        Lot.id == action_id,
                        Lot.deleted.is_(False),
                    )
                )
            ).one_or_none()

    async def create_one(self, auction_data: LotModel.POST):
        async with self.session.begin() as transaction:
            return (
                await transaction.scalars(
                    insert(Lot).values(**auction_data.dict()).returning(Lot)
                )
            ).one()
