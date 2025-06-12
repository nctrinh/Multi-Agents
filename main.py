# cli_chat.py
from multi_agent.graph import workflow

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    inputs = {"messages": [{"role": "user", "content": user_input}]}
    result = workflow.invoke(inputs)
    print("Bot:", result.get("messages")[-1].content)
