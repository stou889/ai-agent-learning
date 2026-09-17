tools = [
    {   
        "type": "function",
        "name": "multiply",
        "description": "计算两个数字的乘法",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number"},
                "b": {"type": "number"}
            },
            "required": ["a", "b"]
        }
    },
    {   
        "type": "function",
        "name": "weather",
        "description":  "查询一个城市当前的天气温度",  
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                "type": "string"
            }
        },
            "required": ["city"]
        }
    },


{
    "type": "function",
    "name": "github_user",
    "description": "查询GitHub用户的公开信息",
    "parameters": {
        "type": "object",
        "properties": {
            "username": {
                "type": "string"
            }
        },
        "required": ["username"]
    }
}
]