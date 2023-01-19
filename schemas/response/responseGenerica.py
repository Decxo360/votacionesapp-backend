from dataclasses import dataclass

@dataclass
class ResponseGenerica():
    ok:bool
    msg: str

    def __init__(self,ok,msg):
        self.ok = ok
        self.msg = msg