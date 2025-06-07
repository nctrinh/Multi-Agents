from typing import List, TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

class MessagesState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
