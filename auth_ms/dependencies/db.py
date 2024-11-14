import contextlib

from loguru import logger
from pymongo.errors import DuplicateKeyError, OperationFailure


def create_indexes():
    pass
    # collection = get_collection(UserDAO.collection_name())

    # with contextlib.suppress(DuplicateKeyError, OperationFailure):
    #     collection.create_indexes(UserDAO.indexes())

    # logger.info("Indexes created")


def init_app() -> None:
    create_indexes()
    logger.info("DB initialized")
