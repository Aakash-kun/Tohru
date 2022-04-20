from typing import Union, Optional, Dict
from random import randrange

from lavalink import DefaultPlayer, AudioTrack

from internal.load_later_track import LoadLaterTrack


class CustomPlayer(DefaultPlayer):
    """ Custom Player class to add the `LoadLaterTrack` and the song loop functionality. """
    def __init__(self, guild_id, node):
        self._loop = False
        
        super().__init__(guild_id, node)
            
    async def play(self, track: Union[AudioTrack, LoadLaterTrack, Dict] = None,
                   start_time: int = 0, end_time: int = 0, no_replace: bool = False,
                   volume: Optional[int] = None, pause: bool = False):

        if not track:
            if not self.queue:
                track = None

            pop_at = randrange(len(self.queue)) if self.shuffle else 0
            track = self.queue.pop(pop_at)

        if isinstance(track, LoadLaterTrack):
            track = await track.load_track()

        return await super().play(track, start_time, end_time, no_replace, volume, pause)

    def add(self, track: Union[AudioTrack, LoadLaterTrack, Dict], requester: int = 0, index: int = None):
        return super().add(track, requester, index)
    
    @property
    def song_loop(self):
        """ Returns the current loop status. 
        Lavalink by default loops the queue, this add the song loop functionality. """
        return self._loop
