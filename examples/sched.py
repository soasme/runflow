import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

sched = AsyncIOScheduler()

def main():
    sched.add_job(
        func='runflow:runflow',
        kwargs={
            'module': 'examples.hello:flow',
            'vars': {}
        },
        trigger='interval',
        seconds=10,
    )

    sched.start()
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == '__main__':
    main()
