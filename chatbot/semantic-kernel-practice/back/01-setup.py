import semantic_kernel as sk

kernel = sk.Kernel()

from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

api_key, org_id = sk.openai_settings_from_dot_env()

kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))


skill = kernel.import_semantic_skill_from_directory("skills", "FunSkill")
joke_function = skill["Joke"]

print(joke_function("time travel to dinosaur age"))