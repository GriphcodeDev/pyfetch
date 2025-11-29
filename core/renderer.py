def render(logos, data, config):
    print(logos)

    print("-" * 40)

    for key in config.get("modules", data.keys()):
        if key in data:
            print(f"{key}: {data[key]}")
