class JsonProcessor:
    def __init__(self):
        self.data = {}

    def flatten(self, json, prefix=""):
        if not isinstance(json, dict):
            self.data[prefix] = json
            return
        for k, v in json.items():
            # need validate k contain "."
            self.flatten(v, prefix + "." + k)

    def contains(self, key):
        return key in self.data

    def replace(self, init_key, map_key):
        self.data[map_key] = self.data[init_key]
        del self.data[init_key]

    def get_json(self):
        json = {}
        for k, v in self.data.items():
            keys = k.split(".")
            cur = json
            for i in range(1, len(keys) - 1):
                cur[keys[i]] = {}
                cur = cur[keys[i]]
            cur[keys[-1]] = v
        return json
