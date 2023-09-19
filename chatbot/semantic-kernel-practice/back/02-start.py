import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatCompletion

kernel = sk.Kernel()

useAzureOpenAI = False

# Configure AI service used by the kernel
if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    kernel.add_chat_service("chat_completion", AzureChatCompletion("gpt-35-turbo", endpoint, api_key))
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))
    
    
# note: using skills from the samples folder
skills_directory = "skills"

funFunctions = kernel.import_semantic_skill_from_directory(skills_directory, "FunSkill")

jokeFunction = funFunctions["Joke"]


result = jokeFunction("today is wednesday. I'm so happy.")

print(result)

# You can also invoke functions asynchronously
# result = await jokeFunction.invoke_async("time travel to dinosaur age")
# print(result)