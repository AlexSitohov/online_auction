from app.daos.lot_dao import AuctionDAO
from app.repositories.auction_repository import AuctionRepository


def provide_auction_repository_stub():
    raise NotImplementedError


def provide_auction_repository(auction_dao: AuctionDAO) -> AuctionRepository:
    return AuctionRepository(auction_dao)
