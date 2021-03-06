from typing import Union
import os

import requests

from e621py.esix.ext import EsixClient


class Create(EsixClient):
    def create(
        self,
        file: str,
        tags: Union[str, list],
        rating: str,
        source: Union[str, list],
        description: str = None,
        is_rating_locked: bool = None,
        is_note_locked: bool = None,
        parent_id: int = None
    ) -> object:
        """Create a new post. There are only four mandatory fields: you need
        to supply the tags, and you need to supply the file, either through a
        multipart form or through a source URL. A source, even if blank, and
        a rating are also required.

        Parameters
        ----------
        `file` (`str`):
            URL to the source file. e621 will download it, if it is a
            whitelisted URL.

        `tags` (`str` | `list`):
            Either a space-delimited list as a string or a list of strings for
            the tags.

        `rating` (`str`):
            The rating. Can be `s`, `q` or `e` for safe, questionable and
            explicit, respectively.

        `source` (`str` | `list`):
            The source of the post. Either supply a string with HTML-encoded
            newlines (`%0A`) or a list of strings. Maximum of 5 allowed.

        `description` (`str`):
            The Description for the post.

        `is_rating_locked` (`bool`):
            Whether or not to prevent others from changing the rating.

        `is_note_locked` (`bool`):
            Whether or not to prevent others from changing the notes.

        `parent_id` (`int`):
            The ID of the parent post.

        Returns
        -------
        JSON `object`
        """
        data = {
            'post[upload_url]': file,
            'post[rating]': rating,
            'post[description]': description,
            'post[is_rating_locked]': is_rating_locked,
            'post[is_note_locked]': is_note_locked,
            'post[parent_id]': parent_id
        }

        if type(tags) is list:
            tags = " ".join(tags)
        data['post[tags]'] = tags

        if type(source) is list:
            source = "%0A".join(source)
        data['post[source]'] = source

        data['login'] = self.username
        data['password_hash'] = self.password_hash

        data['post[upload_url]'] = file
        r = requests.post(
            url=self.url + '/post/create.json',
            params=data,
            headers=self.HEADER
        )
        return r.json()
