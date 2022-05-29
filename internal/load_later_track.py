from typing import Optional

from lavalink import LoadResult, Client


class LoadLaterTrack:
    """ This class is used to load tracks when they are played.
    It will lessen the burden on Lavalink server and save a
    lot of time while queuing playlists or albums. """
    def __init__(self, query, lavalink) -> None:
        self.title = query
        self.query = query
        self.lavalink: Client = lavalink

    async def load_track(self) -> Optional[LoadResult]:
        """ Loads the track. """
        results = await self.lavalink.get_tracks(f"ytsearch:{self.query}")

        if not results or not results['tracks']:
            return None

        return results['tracks'][0]
