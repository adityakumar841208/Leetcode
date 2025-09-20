import heapq
from typing import List, Tuple, Dict

class TaskManager:
    def __init__(self, tasks: List[Tuple[int, int, int]]):
        # Heap stores (-priority, -taskId, userId)
        self.heap: List[Tuple[int, int, int]] = [(-p, -t, u) for u, t, p in tasks]
        heapq.heapify(self.heap)

        # Map: taskId -> (priority, userId)
        self.task_map: Dict[int, Tuple[int, int]] = {t: (p, u) for u, t, p in tasks}

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        self.task_map[task_id] = (priority, user_id)
        heapq.heappush(self.heap, (-priority, -task_id, user_id))

    def edit(self, task_id: int, new_priority: int) -> None:
        if task_id in self.task_map:
            _, user_id = self.task_map[task_id]
            self.task_map[task_id] = (new_priority, user_id)
            heapq.heappush(self.heap, (-new_priority, -task_id, user_id))

    def rmv(self, task_id: int) -> None:
        self.task_map.pop(task_id, None)

    def execTop(self) -> int:
        
        while self.heap:
            neg_priority, neg_task_id, user_id = heapq.heappop(self.heap)
            task_id = -neg_task_id
            if task_id in self.task_map:
                p_map, u_map = self.task_map[task_id]
                if p_map == -neg_priority and u_map == user_id:
                    del self.task_map[task_id]
                    return user_id
        return -1
