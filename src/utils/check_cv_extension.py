allowed_extensions = ('.pdf', '.docx', '.doc', '.txt')
allowed_mimes = (
    'application/pdf',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document', # .docx
    'application/msword', # .doc
    'text/plain' # .txt
)


def cv_is_correct(filename: str, mimetype: str) -> bool:
    return filename.endswith(allowed_extensions) or mimetype in allowed_mimes
