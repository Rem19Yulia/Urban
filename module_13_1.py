import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    
    for i in range(1, 6):  # 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональная силе
        print(f'Силач {name} поднял {i} шар.')
    
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    # Создаём задачи для 3 силачей
    strongman1 = asyncio.create_task(start_strongman('Иван', 2))
    strongman2 = asyncio.create_task(start_strongman('Алексей', 3))
    strongman3 = asyncio.create_task(start_strongman('Станислав', 1.5))

    # Ожидаем завершения всех задач
    await strongman1
    await strongman2
    await strongman3

# Запускаем асинхронную функцию
asyncio.run(start_tournament())