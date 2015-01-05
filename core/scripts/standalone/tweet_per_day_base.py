from abc import abstractmethod
from random import randint

from core import settings
from core.scripts.standalone.base import BaseStandaloneScript


class TweetPerDayBase(BaseStandaloneScript):
    expected_tweet_per_day = 10

    @abstractmethod
    def update(self):
        """
        Called by on_called, approximately @expected_tweet_per_day times each day
        """
        pass

    def on_called(self):
        seconds_per_day = 24 * 60 * 60
        num_of_calls = seconds_per_day / (settings.STAND_ALONE_REPEAT_TIME_CHUNKS * self.repeat_time)

        if randint(0, num_of_calls) < self.expected_tweet_per_day:
            self.update()
        pass