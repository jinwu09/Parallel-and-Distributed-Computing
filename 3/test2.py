from time import sleep
import concurrent.futures

def tasks(taskId:int, sleepCount):
    print(f'Task {taskId}: Starting.')
    sleep(sleepCount)
    return f"Task {taskId}: done"


def tasks1(taskId: int):
    print(f'Task {taskId}: Starting.')
    sleep(taskId)
    return f"Task {taskId}: done"




# with concurrent.futures.ThreadPoolExecutor()as executor:
    # results = executor.map(tasks1,[3,2,5,4])
    # for result in results:
        # print(result)


# with concurrent.futures.ThreadPoolExecutor()as executor:
    # future_a = executor.submit(tasks,1,2)
    # future_b = executor.submit(tasks,2,4)
    # print(future_a.result())
    # print(future_b.result())

task_list = [
    {"taskId": 1, "duration": 2},
    {"taskId": 2, "duration": 3},
]
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for t in task_list:
        future =executor.submit(tasks, t['taskId'], t['duration'])
        futures.append(future)
    for future in futures:
        print(future.result())