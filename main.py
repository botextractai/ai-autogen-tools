import autogen
import os
from langchain_community.tools import ReadFileTool
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper

os.environ['OPENAI_API_KEY'] = "REPLACE_THIS_WITH_YOUR_OPENAI_API_KEY"
os.environ["SERPAPI_API_KEY"] = "REPLACE_THIS_WITH_YOUR_SERPAPI_API_KEY"

# LLM config
def generate_llm_config(tool):
	function_schema = {
		"name": tool.name.lower().replace(" ", "_"),
		"description": tool.description,
		"parameters": {
			"type": "object",
			"properties": {},
			"required": [],
		},
	}

	if tool.args is not None:
		function_schema["parameters"]["properties"] = tool.args

	return function_schema

# Instantiate the tools
read_file_tool = ReadFileTool()
google_trends_tool = GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())

# Construct the LLM_config
llm_config = {"functions": [
		generate_llm_config(read_file_tool),
		generate_llm_config(google_trends_tool)
	],
	"model": "gpt-4-turbo",
	"timeout": 120,
}

# Create user agent
user = autogen.UserProxyAgent(
	name="user",
	is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
	human_input_mode="NEVER",
	max_consecutive_auto_reply=10,
	code_execution_config={
		"work_dir": "coding",
		"use_docker": False,
	},
)

# Register tools
user.register_function(
	function_map={
		read_file_tool.name: read_file_tool._run,
		google_trends_tool.name: google_trends_tool._run,
	}
)

# Create Google Trends agent
GoogleTrendsAgent = autogen.AssistantAgent(
	name="Google Trends Agent",
	system_message="For coding tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done.",
	llm_config=llm_config,
)

# Task definition
task = '''
    Read the file {"file_path":"google_trends.txt"}.
    Search Google Trends with the content of the file as the search term.
    Analyse and explain the data.
    '''

# Initiate chat (and use the tools)
res = user.initiate_chat(
	recipient=GoogleTrendsAgent,
	message=task,
	llm_config=llm_config,
	max_turns=3,
)

# Show the final answer
print(res.summary)
