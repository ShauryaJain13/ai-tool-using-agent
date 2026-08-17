class Controller:
    """
    This class serves as the 'brain' or the controller of the entire operation.
    It coordinates with the other classes to work and control the flow of the
    entire chatbot
    """

    def __init__(self, hist, system_prompt, prompt_builder, llm_client):
        self.hist = hist
        self.system_prompt = system_prompt
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client

    def handle_message(self, message: str):
        """
        This function accepts an input from the user. It's default value is
        None (i.e., no input)
        """
        self.hist.add_user_history(message)
        prompt = self.prompt_builder.build_prompt(self.hist)
        response = self.generate_reply(prompt)
        self.hist.add_assistant_history(response)
        return response

    def generate_reply(self, prompt):
        """
        This function allows the assistant to generate a reply for the
        user's prompt
        """
        response = self.llm_client.generate(prompt)
        return response

    def handle_exit():
        """
        This function is to handle closing the connection between user and LLM,
        ensuring protection of memory and functions (I'm guessing for now) from
        end of current conversation
        """

    def run_loop():
        """
        Looping through the different stages of conversation for as many cycles
        as needed: the process input, build prompt, generate response loop
        """
