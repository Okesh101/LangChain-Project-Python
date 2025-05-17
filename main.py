from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm1 = ChatOpenAI(model="meta-llama/llama-4-scout:free", temperature=0.6)
llm2 = ChatOpenAI(
    model="meta-llama/llama-3.3-70b-instruct:free", temperature=0.6)
llm3 = ChatOpenAI(model="meta-llama/llama-4-maverick:free", temperature=0.6)

print("\n---------You are welcome to the AI debate platform-----------.")
print("We are going to debate on the topic: C++ is better than Python for backend development.")


def AI1():
    messages = [
        (SystemMessage(content="You are a professional humorous programmer that answers questions briefly and is good at debating.")),
        (HumanMessage(
            content="Debate on the topic: C++ is better than Python. Do this while supporting the stated motion. Debate like there's a 1 million dollar prize attached to it so you can win.")),
    ]
    aiAnswer = llm1.invoke(messages)
    result = aiAnswer.content
    return result


def AI2():
    messages = [
        (SystemMessage(content="You are a professional humorous programmer that answers questions briefly and is good at debating.")),
        (HumanMessage(
            content="Debate on the topic: C++ is better than Python. Do this while supporting the stated motion. Debate like there's a 1 million dollar prize attached to it so you can win.")),
        (AIMessage(content=AI1())),
        (HumanMessage(content="Now, please give me a counter-argument to the above argument, while opposing the motion. Debate like there's a 1 million dollar prize attached to it so you can win.")),
    ]
    aiAnswer = llm2.invoke(messages)
    result = aiAnswer.content
    return result


def AI3():
    messages = [
        (SystemMessage(content="You are a professional humorous programmer that answers questions briefly and is good at debating.")),
        (HumanMessage(
            content="Debate on the topic: C++ is better than Python. Do this while supporting the stated motion. Debate like there's a 1 million dollar prize attached to it so you can win.")),
        (AIMessage(content=AI1())),
        (HumanMessage(content="Now, please give me a counter-argument to the above argument, while opposing the motion. Debate like there's a 1 million dollar prize attached to it so you can win.")),
        (AIMessage(content=AI2())),
        (HumanMessage(content="You are a professional programmer that has over 20 years experience in Python and C++ each. Now, please give me the winner of the debate. There must not be a tie. You must choose one of the two debators as the winner. You must also give a reason for your choice.")),
    ]
    aiAnswer = llm3.invoke(messages)
    result = aiAnswer.content
    return result


ai1 = AI1()
print(f"\n\n---------AI Debator 1--------- \n{ai1}")
ai2 = AI2()
print(f"\n\n---------AI Debator 2--------- \n{ai2}")
ai3 = AI3()
print(f"\n\n---------AI Judge--------- \n{ai3}")
