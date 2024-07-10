# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .cn22_form_cn22_content import Cn22FormCn22Content


@JsonMap(
    {
        "label_size": "LabelSize",
        "prints_per_page": "PrintsPerPage",
        "label_print_type": "LabelPrintType",
        "cn22_type": "CN22Type",
        "cn22_other_description": "CN22OtherDescription",
        "fold_here_text": "FoldHereText",
        "cn22_content": "CN22Content",
    }
)
class InternationalFormsCn22Form(BaseModel):
    """Container for the CN22 form.  Required if the customer wants to use the UPS generated CN22.

    :param label_size: Provide the valid values:  6 = 4X6 1 = 8.5X11   Required if the CN22 form container is present.
    :type label_size: str
    :param prints_per_page: Number of label per page. Currently 1 per page is supported.  Required if the CN22 form container is present.
    :type prints_per_page: str
    :param label_print_type: Valid Values are pdf, png, gif, zpl, star, epl2 and spl.   Required if the CN22 form container is present.
    :type label_print_type: str
    :param cn22_type: Valid values:  1 = GIFT 2 = DOCUMENTS 3 = COMMERCIAL SAMPLE 4 = OTHER  Required if the CN22 form container is present.
    :type cn22_type: str
    :param cn22_other_description: Required if CN22Type is OTHER.  Required if the CN22 form container is present., defaults to None
    :type cn22_other_description: str, optional
    :param fold_here_text: String will replace default "Fold Here" text displayed on the label., defaults to None
    :type fold_here_text: str, optional
    :param cn22_content: cn22_content
    :type cn22_content: List[Cn22FormCn22Content]
    """

    def __init__(
        self,
        label_size: str,
        prints_per_page: str,
        label_print_type: str,
        cn22_type: str,
        cn22_content: List[Cn22FormCn22Content],
        cn22_other_description: str = None,
        fold_here_text: str = None,
    ):
        self.label_size = label_size
        self.prints_per_page = prints_per_page
        self.label_print_type = label_print_type
        self.cn22_type = cn22_type
        if cn22_other_description is not None:
            self.cn22_other_description = cn22_other_description
        if fold_here_text is not None:
            self.fold_here_text = fold_here_text
        self.cn22_content = self._define_list(cn22_content, Cn22FormCn22Content)