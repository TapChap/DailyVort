from typing import List, Union

class Role:
    USER = 'user'
    CHATGPT = 'assistant'
    SYSTEM = 'system'

class Config():
    def __init__(self, model="gpt-4o-mini", max_tokens=750):
        self.model = model
        self.max_tokens = max_tokens

config = Config()

class CompositePrompt:
    """Interface for any object that can behave like a prompt message"""
    def toJson(self) -> List[dict]:
        raise NotImplementedError("Must implement getMessages")

class Prompt(CompositePrompt):
    def __init__(self, content: str, role: str = Role.USER):
        self.content = content
        self.role = role

    def toJson(self) -> List[dict]:
        return [{"role": self.role, "content": self.content}]

class Conversation(CompositePrompt):
    def __init__(self, *prompts: Union[Prompt, CompositePrompt]):
        self.prompts: List[CompositePrompt] = list(prompts)

    def toJson(self) -> List[dict]:
        conversation = []
        for prompt in self.prompts:
            conversation.extend(prompt.toJson())
        return conversation

    def __add__(self, other):
        return Conversation(self, other)

if __name__ == '__main__':
    m1 = Prompt("try to insert the word 'shall' in every answer", Role.SYSTEM)
    m2 = Prompt("how are you doing today?")
    convo = Conversation(m1, m2)

    print(convo.toJson())