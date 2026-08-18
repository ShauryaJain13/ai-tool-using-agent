from agent.agent import Agent
from agent.memory import Memory
from chat.llm import LLMClient
from chat.prompts import Prompt_Builder
from tools.registry import ToolRegistry, Tool
from controller import Controller
from tools.calculator import Calculator
from tools.read_file import ReadFile


memory = Memory()

prompt_builder = Prompt_Builder(
    system_prompt="""You are a helpful AI assistant.
    Use tools when necessary to answer the user's questions.
    If you are using a tool, mention the tool you are using explicitly""")

llm_client = LLMClient()
tools = ToolRegistry()

calculator = Calculator()
calculator_tool = Tool(
    name="calculator",
    description="Evaluate a mathematical expression.",
    function=calculator.execute,
    arguments={"type": "object",
               "properties": {
                   "expression": {
                       "type": "string",
                       "description": ("The mathematical"
                                       "expression to evaluate.")}},
                "required": ["expression"]})

read_file = ReadFile()
read_file_tool = Tool(name="file_reader",
                      description="Reads a file that has been entered.",
                      function=read_file.execute,
                      arguments={"type": "object",
                                 "properties": {
                                    "expression": {
                                        "type": "string",
                                        "description": ("The link of the file"
                                                        "to be read")}},
                                 "required": ["expression"]})

tools.register(calculator_tool)
tools.register(read_file_tool)
agent = Agent(llm=llm_client, tools=tools, memory=memory,
              prompt_builder=prompt_builder)

controller = Controller(agent)
controller.loop()
