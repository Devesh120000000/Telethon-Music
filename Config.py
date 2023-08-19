import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25315984"))
    API_HASH = os.environ.get("API_HASH", "a6ba4319518ec253443f4fee1f4b0810")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6353682770:AAGfJbKYqBwP9Cq_qVVt6gV81inCQUdxhoE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOIEBuyWUqk7WtYY2VHFhQP-xi2c-jamNdF8I5HQZSs-GE-33J6bn9GOYl99QAZyxSSYmDwr_kLMElu_t0fJjR7sCKfK6spre_NJCDY1zUPtVELeKhD6Wmjku6UbZkyIhO1g0A_79LdYHdrktSysqIy3f8V63gU-GpddSEuZXs0F824GPNesLPHsCr3UhLOVFf53sKvEPoQLex_XjDlDOK2JEFFcE8MdHvZYYwynW_flVpfYxaGmhQ8PVTyQvYfNirjc0VIwRr-ziPsKK0gbCKg5EwLnVp5MpINF3lpy6RnV4kIUJlbwgpaYiBKQsZzTY6sJFsg7K_zH8Vr2m4uE6pblH3ok=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Music_Shanu_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1125321520")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
