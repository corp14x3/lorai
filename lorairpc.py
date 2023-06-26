from pypresence import Presence
import time , sqlite3

RPC = Presence('1121904567244820500')
RPC.connect()

while True:
    RPC.update(
        details="as", 
        state="sa",
        large_image="./static/media/lorai.gif",
        large_text="lorai",
        small_image="./static/media/lorai.gif",
        small_text="Lor(A)I",
        buttons = [{"label": f"My Website", "url": f"https://qtqt.cf"},{"label": f"My Website", "url": f"https://qtqt.cf"}]
        ) 
    time.sleep(60)