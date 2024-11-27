import asyncio

async def start_strongman(name, power):
    bools_count = 5
    print (f"Силач {name} начал соревнования")
    for i in range(bools_count):
        upper_time = 1/power
        await asyncio.sleep(upper_time)
        print (f"Силач {name} поднял {i+1} шар")
    print(f"Силач {name} закончил соревнование")

async def start_tournament():
    strongman_1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman_2 = asyncio.create_task(start_strongman('Vova', 2))
    strongman_3 = asyncio.create_task(start_strongman('Sasha', 5))
    await strongman_1
    await strongman_2
    await strongman_3

asyncio.run(start_tournament())