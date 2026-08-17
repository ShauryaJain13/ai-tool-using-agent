import json


class Agent:
    """
    This class decide which tool should be used, and whether the query has
    satisfactorily been handled
    """
    def __init__(self, llm, tools, memory, max_iterations=10):
        self.llm = llm
        self.tools = tools
        self.memory = memory
        self.max_iterations = max_iterations

    def run(self, input):
        """
        Run the code until satisfactory conditions are met
        accept the input, generate output, and keep the loop of ReAct until
        all conditions are met
        """
        self.memory.add({
            "role": "user",
            "content": input
        })

        for k in range(self.max_iterations):
            message = self._build_context()
            response = self.llm.generate(message, self.tools.schemas())

            tool_call = self._is_tool_call(response)
            if tool_call is None:
                return response.content

            result = self._handle_tool_call(tool_call)
            self._add_tool_call_result(response, tool_call, result)

        return "Maximum iterations reached, agent has stopped"

    def _is_tool_call(self, response):
        """
        This function determines whether the LLM response is to do a tool call
        or is the final output
        """
        if response is None:
            return None

        if not response.tool_calls[0]:
            return None

        return response.tool_calls[0]

    def _handle_tool_call(self, call):
        """
        Processes one tool call from the LLM
        """
        tool_name = call.function.name
        arguments = self._parse_arguments(call.function.arguments)
        # tool = self.tools.get(tool_name)
        # if tool is None:
        #     raise ValueError(f"Unknown tool requested: {tool_name}")
        # result = tool.execute(parameters)
        # return result
        return self._execute_tool_call(tool_name, arguments)

    def _parse_arguments(self, arguments):
        """
        Parses the expression that will be entered in the argument
        """
        if isinstance(arguments, str):
            try:
                return json.loads(arguments)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid tool arguments: {arguments}") from e

        if isinstance(arguments, dict):
            return arguments

        raise TypeError(f"Unknown argument type: {type(arguments)}")

    def _execute_tool_call(self, tool_name, arguments):
        """
        The actual execution of the tool call itself-processing it from the llm
        """
        tool = self.tools.get(tool_name)
        if tool is None:
            raise ValueError(f"Tool {tool_name} is not registered")

        try:
            return tool.execute(arguments)
        except Exception as e:
            return {"status": "error",
                    "error": e}

    def _add_tool_call_result(self, response, result):
        """
        Adding the tool call result to the response, so that the LLM can
        evaluate it
        """
        self.memory.add({"role": "assistant",
                         "tool_call": response.tool_calls})
        self.memory.add({"role": "tool",
                         "tool_call_id": "call.id",
                         "content": str(result)})

    def _build_context(self, input):
        """
        Create context for the LLM if necessary
        """
        return self.memory.get_messages()
