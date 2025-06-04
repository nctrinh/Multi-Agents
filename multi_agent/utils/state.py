from typing import Dict, List, TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

class MessagesState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    # Bổ sung trường lưu kết quả tích lũy
    accumulated_results: Annotated[Dict[str, str], operator.add]    