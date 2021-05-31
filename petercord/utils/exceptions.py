# petercord

class StopConversation(Exception):
    """raise if conversation has terminated"""


class ProcessCanceled(Exception):
    """raise if thread has terminated"""


class PetercordBotNotFound(Exception):
    """raise if userge bot not found"""
