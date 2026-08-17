class Memory:
    """
    This class is used to store the memory of the agent,
    what messages have been given and what actions have been taken
    """

    def __init__(self, user):
        self.user = user
        self.messages = []

    # def add_user_history(self, message: str | None = None) -> None:
    #     """
    #     This method adds the new input to the history of inputs entered
    #     by the user
    #     """
    #     self.messages.append({
    #         "role": "user",
    #         "content": message
    #     })

    # def add_assistant_history(self, message: str | None = None) -> None:
    #     """
    #     This method adds the new output to the history of outputs given
    #     by the assistant
    #     """
    #     self.messages.append({
    #         "role": "assistant",
    #         "content": message
    #     })

    def add(self, message):
        """
        Adding the message to the history of the chat
        """
        self.messages.append(message)

    def get_messages(self):
        """
        Returns the message history of the user and the model
        """
        return self.messages

    def clear_history(self):
        """
        This function clears the history of the chat
        """
        self.messages.clear()
