class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """This is a checking if the TV has a mute and channel Volume"""
        self.__status = False
        self.__mute = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self)-> None:
        """ the power function"""
        self.__status = not self.__status
    def mute(self) -> None:
        """ the mute function when the tv is on"""
        self.__status
        self.__mute = not self.__mute

    def channel_up(self)-> None:
        """d 1 to the channel function """
        if self.__status:
            self.__channel += 1

        if self.__channel > Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
    def channel_down(self)-> None:
        """sebtract one to teh channel function"""
        if self.__status:
            self.__channel -= 1

        if self.__channel < Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
    def volume_up(self)-> None:
        """ increase the volume if muted unmuted first"""
        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self)-> None:
        """decreased the volume if muted unmuted first"""
        if self.__status:
            if self.__mute:
                self.__mute = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self)-> str:

        return (f"Power = {self.__status}, Channel = {self.__channel}, "
                f"Volume = {self.__volume}")
