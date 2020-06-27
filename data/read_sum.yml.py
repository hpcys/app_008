import yaml

sum_list = []
with open("./sum.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("data:", data)
    print("values:", data.values())
    for i in data.values():
        # print("tup:", (i.get("a"),i.get("b"),i.get("c")))
        sum_list.append((i.get("a"), i.get("b"), i.get("c")))
print("sum_list", sum_list)
