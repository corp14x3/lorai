from pypresence import Presence
import time , sqlite3

con = sqlite3.connect("lorai.db", check_same_thread=False)
RPC = Presence('1121904567244820500')
RPC.connect()

class LoraiDRPC():
    def __init__(self):
        pass
    def presence(self,status:bool):
        if status == True:
            while True:
                liste = con.execute("SELECT * FROM drpc")
                main = liste.fetchall()
                RPC.update(
                    details=f"{main[0][0]}", 
                    state=f"{main[0][1]}",
                    large_text=f"{main[0][2]}",
                    large_image=f"{main[0][3]}",
                    small_image= "./static/media/lorai.gif",
                    small_text="Lor(A)I",
                    buttons = [{"label": f"{main[0][4]}", "url": f"{main[0][5]}"},{"label": f"{main[0][6]}", "url": f"{main[0][7]}"}]
                    ) 
                time.sleep(3)
        else:
            pass
ll = LoraiDRPC()
ll.presence(status=True)