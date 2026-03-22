from aiogram.fsm.state import State, StatesGroup


class UploadCVState(StatesGroup):
    get_cv = State()


class SearchSettingsState(StatesGroup):
    waiting_for_skills = State()
    waiting_for_grade = State()
    waiting_for_job_type = State()
    waiting_for_location = State()
