from typing import List


class TempmailException(Exception):
    pass


class ResponseException(TempmailException):
    def __init__(self, error_message: str):
        super().__init__(f'Response error: {error_message}')


class InvalidDomain(TempmailException):
    def __init__(self, domain: str, domains: List[str]):
        super().__init__(f'Invalid domain: {domain}. Select one from following: {", ".join(domains)}.')


class MessageNotFound(TempmailException):
    def __init__(self, message_id: str):
        super().__init__(f'Message with id \'{message_id}\' not found.')


class ConditionsEmpty(TempmailException):
    def __init__(self, *conditions: str):
        super().__init__(f'Specify at least one condition from following: {", ".join(conditions)}.')


class TimeoutException(TempmailException):
    pass
