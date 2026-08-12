from chat.controller import Controller
from chat.history import History
from chat.prompts import Prompt_Builder
from chat.llm import LLMClient
from chat.settings import SYSTEM_PROMPT


def main():
    """
    Point of creation of new object, and used to run the application
    """

    history = History(user="New User")
    prompt_builder = Prompt_Builder(system_prompt=SYSTEM_PROMPT)
    llm_client = LLMClient()
    controller = Controller(hist=history, system_prompt=SYSTEM_PROMPT,
                            prompt_builder=prompt_builder,
                            llm_client=llm_client)
    print("Forecasting agent v0.0.1")
    print("Type 'exit' to quit\n")

    while True:
        message = input("You: ")
        if message.lower() == "exit":
            print("Goodbye!")
            break

        response = controller.handle_message(message)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
