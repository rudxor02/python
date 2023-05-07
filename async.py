import asyncio
import time
import threading


# def blocking_io():
#     print(f"start blocking_io at {time.strftime('%X')}")
#     # Note that time.sleep() can be replaced with any blocking
#     # IO-bound operation, such as file operations.
#     time.sleep(1)
#     print(f"blocking_io complete at {time.strftime('%X')}")

# async def main():
#     print(f"started main at {time.strftime('%X')}")

#     await asyncio.gather(
#         asyncio.to_thread(blocking_io),
#         asyncio.sleep(1))

#     print(f"finished main at {time.strftime('%X')}")


# asyncio.run(main())


class A:
    a = 3032894

    def m(self, k):
        print(k)
        print(self.a)
        for i in range(100):
            print(i)
            time.sleep(1)

    def k(self):
        for i in range(100):
            print(i)
            time.sleep(1)


smaple = A()

t1 = threading.Thread(target=smaple.m, args=["asdkjn"])
t2 = threading.Thread(target=smaple.k)

t1.start()
t2.start()

# t1.join()
# t2.join()

print("sad")

# class A:
#     a = 3

#     async def kk(self):
#         print(self.a)
#         print("Coroutine started")
#         await asyncio.sleep(2)
#         print("Coroutine finished")

#     def mm(self):
#         print("Main function started")
#         task = asyncio.create_task(self.kk())  # 비동기 함수 실행
#         print("Other code")  # 비동기 함수 실행 중에 다른 코드 실행
#         # asyncio.sleep(3)  # 3초간 대기
#         asyncio.gather(task)
#         print("Main function finished")

#     def kkkkkkkk(self):
#         self.mm()
#         print("------------------")
#         for i in range(1000000000000000000):
#             pass

#     async def kkkk(self):
#         self.kkkkkkkk()
#         print(1232443)


# asyncio.run(A().kkkk())
# async def my_coroutine():
#     print("Coroutine started")
#     await asyncio.sleep(2)
#     print("Coroutine finished")


# async def main():
#     print("Main function started")
#     asyncio.create_task(my_coroutine())  # 비동기 함수 실행
#     print("Other code")  # 비동기 함수 실행 중에 다른 코드 실행
#     await asyncio.sleep(3)  # 3초간 대기
#     print("Main function finished")


# asyncio.run(main())
# async def main ():
#     await asyncio.gather(
#         asyncio.to_thread(k),
#         asyncio.sleep(1))


# async def m2():
#     for i in range(100):
#         print(i)
#         await asyncio.sleep(1)


# async def main():
#     await asyncio.gather(m(), m2())


# asyncio.run(main())
# def main():
#     for i in range(100):
#         print(i, end="")
#         time.sleep(1)
#     print()


# main()
# async def main1():
#     await asyncio.gather(main(), main())


# asyncio.run(main1())

# asyncio.run(main())
# asyncio.run(main())
