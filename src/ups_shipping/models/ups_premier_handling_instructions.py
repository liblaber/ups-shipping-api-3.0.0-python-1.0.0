# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"instruction": "Instruction"})
class UpsPremierHandlingInstructions(BaseModel):
    """Handling Instruction Container.

    :param instruction: Handling Instruction for UPS Premier package.  Please refer Apendix UPS Premier Handling Instructions.
    :type instruction: str
    """

    def __init__(self, instruction: str):
        self.instruction = instruction