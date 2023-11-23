from app.messages.env import environment
FILENAME_MSG = environment.from_string(
"""
{{name}}, enter the name of the file you want to upload!
{%for file in files
{{file}}
""")