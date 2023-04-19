
class MSHR:
    def __init__(self) -> None:
        self.id             = 0
        self.debug_id       = 0
        self.status         = False
        self.addr           = 0
        self.set_idx        = 0
        self.replace_way    = 0
        self.replace_dirty  = False
        self.trace          = {}
        self.is_prefetch    = False

    def allocate(self, time, id, debug_id, addr, set_idx,  replace_way, replace_dirty, is_prefetch):
        self.id             = id
        self.debug_id       = debug_id
        self.status         = True
        self.addr           = addr
        self.set_idx        = set_idx
        self.replace_way    = replace_way
        self.replace_dirty  = replace_dirty
        self.is_prefetch    = is_prefetch
        self.trace.update({time:["allocate", id, debug_id, addr, replace_way, is_prefetch]})

    def merge(self, )
