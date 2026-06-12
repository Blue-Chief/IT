import json

string = '{"database": {"connection": {"port": 5432}}}'

config = json.loads(string)

target = None

input = {
    "database": {
        "replica": {
            "timeout": 0
        }
    }
}



# def config_inspector(config:dict, input:dict):

#     for key, values in input.items():
#         if key in config.keys():
#             value = key[values]    

#             if isinstance (value, dict):
#                 result = config_inspector(value)

#         else:
#             return f"Timeout Setting: {target}"
        

if "database" in config:
    level_one = config["database"]
    
    if "replica" in level_one:
        level_two = level_one["replica"]

        if "timeout" in level_two:
            level_three = level_two["timeout"]
        else:
            print(f"Timeout Setting {target}")
    else:
        print(f"Timeout Setting {target}")
else:
    print(f"Timeout Setting {target}")


# print(final = config_inspector(config, input))
