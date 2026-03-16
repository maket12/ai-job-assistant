from aiogram.fsm.state import State, StatesGroup


class UploadCV(StatesGroup):
    get_cv = State()


class GetVoiceMessage(StatesGroup):
    get_voice = State()


class GetYoutubeVideo(StatesGroup):
    get_video = State()
