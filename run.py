from environs import env
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig


def acquisition(agent: PhoneAgent):
    while True:
        try:
            print("正在进入搜索结果界面……")
            result = agent.run(
                "打开快手搜索“评论区找对象”，然后点漏斗图标把搜索条件设置为7日内、未看过。若成功完成任务，仅输出“成功”，其他什么都不要输出，严格按照这个格式来。"
            )
            if result != "成功":
                raise Exception(result)
        except Exception as e:
            print("进入搜索结果界面失败：", e)
            continue

        while True:
            try:
                print("正在进入作品界面……")
                result = agent.run(
                    "点进搜索结果中的第一个作品。若成功完成任务，仅输出“成功”，其他什么都不要输出，严格按照这个格式来。"
                )
                if result != "成功":
                    raise Exception(result)
            except Exception as e:
                print("进入作品界面失败：", e)
                continue

            try:
                print("正在判断评论条数……")
                result = agent.run(
                    "判断评论数量有没有达到一百（显示抢首评说明一个评论都没有），若达到则仅输出“y”，若没有达到则仅输出“n”，其他什么都不要输出，严格按照这个格式来。"
                )
                if result == "y":
                    print("正在进入评论区界面……")
                    try:
                        result = agent.run(
                            "点视频右侧气泡图标打开评论区。若成功完成任务，仅输出“成功”，其他什么都不要输出，严格按照这个格式来。"
                        )
                        if result != "成功":
                            raise Exception(result)
                    except Exception as e:
                        print("进入评论区界面失败")
                        
                    print("哈哈哈，我成了")
                    return

                    try:
                        print("正在刷新搜索结果界面……")
                        result = agent.run(
                            "返回到上一页的搜索结果界面（而不是作品界面），并下拉刷新搜索结果（从屏幕中间较小的y值start，到屏幕底部较大的y值end）。若成功完成任务，仅输出“成功”，其他什么都不要输出，严格按照这个格式来。"
                        )
                    except Exception as e:
                        print("刷新搜索界面失败：", e)
                elif result == "n":
                    try:
                        print("正在刷新搜索结果界面……")
                        result = agent.run(
                            "返回到上一页的搜索结果界面（而不是作品界面），并下拉刷新搜索结果（从屏幕中间较小的y值start，到屏幕底部较大的y值end）。若成功完成任务，仅输出“成功”，其他什么都不要输出，严格按照这个格式来。"
                        )
                    except Exception as e:
                        print("刷新搜索界面失败：", e)
                else:
                    raise Exception(result)
            except Exception as e:
                print("判断评论条数失败：", e)
                continue


def run():
    # Read .env into os.environ
    env.read_env()

    # Configure model
    model_config = ModelConfig(
        base_url=env("BASE_URL"),
        api_key=env("API_KEY"),
        model_name=env("MODEL_NAME"),
    )

    # 创建 Agent
    agent = PhoneAgent(model_config=model_config)

    # 用户获取
    acquisition(agent)


if __name__ == "__main__":
    run()
