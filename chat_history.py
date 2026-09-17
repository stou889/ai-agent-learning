# from openai import OpenAI
# import json
# client = OpenAI()
# def multiply(a, b):
#     return a * b
# tools = [
#     {
#         "type": "function",
#         "name": "multiply",
#         "description": "计算两个数字的乘法",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number"},
#                 "b": {"type": "number"}
#             },
#             "required": ["a", "b"]
#         }
#     }
# ]
# #messages保存，通过messages_append往里面塞内容
# messages = []
# while True:
#     user_message = input("你：")
#     if user_message == "退出":
#         break
#     messages.append({
#         "role": "user",
#         "content": user_message
#     })
#     #喊gpt开工，responses.create发请求，再将以下东西塞过去，让gpt读取
#     response = client.responses.create(
#     model="gpt-5.6-luna",
#     input=messages,
#     tools=tools
#     )
#     #判断需要工具
#     tool_called = False
#     for item in response.output:
#         print("输出类型:", item.type)
#         if item.type == "function_call":
#             tool_called = True
#     #function_call，判断需要工具
#         if item.type == "function_call":
#             print("AI选择的工具:", item.name)
#             print("AI给的参数:", item.arguments)
#             #数据转换
#             arguments = json.loads(item.arguments)
#             a = arguments["a"]
#             b = arguments["b"]
#             #Python函数执行
#             result = multiply(a, b)
#             print("Python计算结果:", result)
#             second_response = client.responses.create(
#                 model="gpt-5.6-luna",
#                 previous_response_id=response.id,
#                 input=[
#                     {
#                         "type": "function_call_output",
#                         "call_id": item.call_id,
#                         "output": str(result)
#                     }
#                 ]
#             )
#             ai_message = second_response.output_text

#             messages.append({
#                 "role": "assistant",
#                 "content": ai_message
#             })

#             print("AI最终回答:", ai_message)
#             print("AI最终回答:", second_response.output_text)

    #function_call_output
    # ai_message = response.output_text
    # messages.append({
    #     "role": "assistant",
    #     "content": ai_message
    # })
   #GPT生成最终答案
    # print("AI:", ai_message)
    # print("\n当前聊天记录:")

    # for message in messages:
    #     print(
    #         message["role"],
    #         ":",
    #         message["content"]
    #     )

    # print("----------------")
from openai import OpenAI
import json
from tools import multiply, weather,github_user
from tool_schemas import tools
tool_functions = {
    "multiply": multiply,
    "weather": weather,
    "github_user": github_user
}

client = OpenAI()
def execute_tool(tool_name, arguments):
    try:
        if tool_name in tool_functions:
            function = tool_functions[tool_name]
            result = function(**arguments)
            return result
        else:
            return "未知工具"

    except Exception as e:
        print("工具执行出错:", e)
        return "工具执行失败"

# 1. Python真正执行的乘法函数
# def multiply(a, b):
#     return a * b

# def weather(city):
#     geo_url = "https://geocoding-api.open-meteo.com/v1/search"

#     geo_params = {
#         "name": city,
#         "count": 1,
#         "language": "zh"
#     }

#     geo_response = requests.get(
#         geo_url,params=geo_params)

#     geo_data = geo_response.json()

#     if "results" not in geo_data:
#         return "没有找到这个城市"

#     latitude = geo_data["results"][0]["latitude"]
#     longitude = geo_data["results"][0]["longitude"]

#     weather_url = "https://api.open-meteo.com/v1/forecast"

#     weather_params = {
#         "latitude": latitude,
#         "longitude": longitude,
#         "current": "temperature_2m"
#     }

#     weather_response = requests.get(
#         weather_url,
#         params=weather_params
#     )

#     weather_data = weather_response.json()

#     temperature = weather_data["current"]["temperature_2m"]

#     return city + "当前温度：" + str(temperature) + "°C"    


# 2. 告诉AI：你有一个multiply工具
# tools = [
#     {   
#         "type": "function",
#         "name": "multiply",
#         "description": "计算两个数字的乘法",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number"},
#                 "b": {"type": "number"}
#             },
#             "required": ["a", "b"]
#         }
#     },
#     {   
#         "type": "function",
#         "name": "weather",
#         "description":  "查询一个城市当前的天气温度",  
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "city": {
#                 "type": "string"
#             }
#         },
#             "required": ["city"]
#         }
#     }
# ]



# 3. 保存聊天记录
messages = []


# 4. 开始持续聊天
while True:

    user_message = input("你：")

    if user_message == "退出":
        break


    # 保存用户说的话
    messages.append({
        "role": "user",
        "content": user_message
    })


    # 5. 把聊天记录和工具交给AI
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=messages,
        tools=tools
    )


    # 6. 先假设AI没有调用工具
    tool_called = False


    # 7. 检查AI返回的所有内容
    for item in response.output:

        print("输出类型:", item.type)

        # 8. 如果发现AI要调用工具
        if item.type == "function_call":

            tool_called = True

            print("AI选择的工具:", item.name)
            print("AI给的参数:", item.arguments)


            # 9. 把AI给的JSON参数转换成Python字典
            arguments = json.loads(item.arguments)

            result = execute_tool(item.name, arguments)

            print("Python执行结果:", result)

            # 11. 把Python计算结果交回AI
            second_response = client.responses.create(
                model="gpt-5.6-luna",
                previous_response_id=response.id,
                input=[
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": str(result)
                    }
                ]
            )


            # 12. 得到AI最终回答
            ai_message = second_response.output_text


            # 13. 把AI回答保存进messages
            messages.append({
                "role": "assistant",
                "content": ai_message
            })


            print("AI:", ai_message)


    # 14. 如果整个for检查完，都没有调用工具
    if not tool_called:

        ai_message = response.output_text


        # 普通聊天也保存进messages
        messages.append({
            "role": "assistant",
            "content": ai_message
        })


        print("AI:", ai_message)