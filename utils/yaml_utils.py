import yaml


class Yaml_Utils:
    @staticmethod
    def read_yaml_file(yaml_path, node_name):
        with open(yaml_path, 'r', encoding='utf-8') as fb:
            data = yaml.safe_load(fb)  # 获取yaml文件内容
            return list(data[node_name].values())  # 获取data[node_name]的值并转换为list格式


read_yaml = Yaml_Utils()

if __name__ == "__main__":
    pass
    # print(Yaml_Utils.read_yaml('../testdata/yaml/login.yml', 'test_login'))
