from sqlalchemy.ext.asyncio import async_sessionmaker

from app.daos.lot_dao import AuctionDAO


def provide_auction_dao(session: async_sessionmaker) -> AuctionDAO:
    return AuctionDAO(session)
