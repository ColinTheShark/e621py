import logging

from .ext import EsixClient
from .methods import Methods

log = logging.getLogger(__name__)


class Esix(Methods, EsixClient):
    """e621py Client.

    Parameters
    ----------
    `username` (``str``):
        Your Username.

    `password_hash` (``str``):
        Your API key.

    `safe` (``bool``):
        Whether or not to display NSFW content.
        Defaults to False (show NSFW)
    """
    def __init__(
        self,
        username: str = None,
        password_hash: str = None,
        safe: bool = False
    ):
        super().__init__()
        self.username = username
        self.password_hash = password_hash
        self.url = "https://e926.net" if safe is True else "https://e621.net"
