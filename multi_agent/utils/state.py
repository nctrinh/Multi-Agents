import operator
from typing import Annotated, List, TypedDict

from langchain_core.messages import BaseMessage


class MessagesState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
