import asyncio
import time
from time import sleep

def test_get():
    print('hello')
    sleep(1)
    print('world')

async def async_test_get():
    print('hello')
    await asyncio.sleep(1)
    print('world')

#if awaiting a request that takes same amount of time as preceding awaits, code in between would have to
#wait as if blocking
async def async_test_long():
    print('hello')
    await asyncio.sleep(1.5)
    print('long')
async def main():
   print('running fetches sync')
   start_time = time.perf_counter()
   test_get()
   test_get()
   test_get()
   test_get()
   end_time = time.perf_counter()
   print(f'elapsed time: {end_time - start_time}')
   
   #await waits for line to finish before continuing
   print('\nrunning async using only await')
   start_time = time.perf_counter()
   await async_test_get()
   await async_test_get()
   await async_test_get()
   await async_test_get()
   await async_test_get()
   end_time = time.perf_counter()
   print(f'elapsed time: {end_time - start_time}')
   
   print('\nrunning async using create_tasks')
   start_time = time.perf_counter()
   task1 = asyncio.create_task(async_test_get())
   task2 = asyncio.create_task(async_test_get())
   task3 = asyncio.create_task(async_test_long())
   task4 = asyncio.create_task(async_test_long())
   task5 = asyncio.create_task(async_test_long())
   print('print between create_task and await')
   await task1
   await task2
   print('print after get')
   await task3
   await task4
   await task5
   print('print after long')
   end_time = time.perf_counter()
   print(f'elapsed time: {end_time - start_time}') 
   
   print('\nrunning async tasks with TaskGroup')
   start_time = time.perf_counter()
   async with asyncio.TaskGroup() as tg:
       task1 = tg.create_task(async_test_get())
       task2 = tg.create_task(async_test_get())
       task3 = tg.create_task(async_test_get())
       task4 = tg.create_task(async_test_get())
       task5 = tg.create_task(async_test_get())
   end_time = time.perf_counter()
   print(f'elapsed time: {end_time - start_time}') 
   
   print('\nrunning async tasks with asyncio.gather')
   start_time = time.perf_counter()
   results = asyncio.gather(*[async_test_get() for _ in range(5)])
   sleep(1.5)
   print('can exucute still')
   print('wont block until await')
   await results    
   end_time = time.perf_counter()
   print(f'elapsed time: {end_time - start_time}') 
   print('fetched all sites')

asyncio.run(main())





   
