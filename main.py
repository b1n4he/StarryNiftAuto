import asyncio
import sys
from questionary import Choice
import questionary
from modules.config import PRIVATE_KEYS, PROXIES
from modules.executor import Executor


def get_module(executor: Executor):
    choices = [
        Choice(f"{i}) {key}", value)
        for i, (key, value) in enumerate(
            {
                # "Generate wallets": executor.generate_wallets,
                # "Withdraw BNB from Binance": executor.withdraw_from_binance,
                "签到StarryNift任务": executor.run_starrynift,
                "获取账号状态": executor.get_accounts_stats,
                "退出": "exit",
            }.items(),
            start=1,
        )
    ]
    result = questionary.select(
        "选择并回车执行：",
        choices=choices,
        qmark="🛠 ",
        pointer="✅ ",
    ).ask()
    if result == "exit":
        sys.exit()
    return result


async def main(module):
    await module()


if __name__ == "__main__":
    executor = Executor(PRIVATE_KEYS, PROXIES)
    module = get_module(executor)
    asyncio.run(main(module))
