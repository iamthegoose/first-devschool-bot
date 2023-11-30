from app.messages.env import environment
FILENAME_MSG = environment.from_string("""
<i><b>{{name}}</b>, enter the name of the file you want to upload!</i>
""")

FILEUPLOAD_MSG = environment.from_string("""
Upload the file you want!
""")

FILEACCEPTED_MSG = environment.from_string("""
Your file was successfully uploaded!
""")
