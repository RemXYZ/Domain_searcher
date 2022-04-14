import os
import json

from lib.my_algorythm import binary_search

class File_base():
    def __init__(self):
        self.domains_dir = "domains"
        self.existing_domain = self.domains_dir+"/"+"exists"
        self.free_domains = self.domains_dir+"/"+"free"
        self.favorite_domains = self.domains_dir+"/"+"favorite"
        self.exs_dm_f = "exists_1.txt"
        self.fr_dm_f = "free_1.txt"
        self.fv_dm_f = "favorite_1.txt"
        # domain configuration
        self.dm_conf = "conf.txt"

        self.settings = "setting.txt"

        # existing_domain_column
        self.exs_dm_col = [
            'id',
            'domain_name',
            'time',
            'registrar',
            'expiration_date',
            'creation_date'
            ]
        # free_domains_col
        self.fr_dm_col = ['id', 'domain_name', 'date']
        # favorite_domains_col
        self.fv_dm_col = self.exs_dm_col

    def check_domain_architecture(self):
        pass

    def get_existing_path(self):
        return {
            "storage": [self.existing_domain, self.exs_dm_f],
            "conf": [self.existing_domain, self.dm_conf]
        }

    def get_free_path(self):
        return {
            "storage": [self.free_domains, self.fr_dm_f],
            "conf": [self.free_domains, self.dm_conf]
        }

    def get_favorite_path(self):
        return {
            "storage": [self.favorite_domains, self.fv_dm_f],
            "conf": [self.favorite_domains, self.dm_conf]
        }

    def get_exising_col(self):
        return self.exs_dm_col

    def get_free_col(self):
        return self.fr_dm_col

    def get_favorite_col(self):
        return self.fv_dm_col



class File_manager(File_base):
    def __init__(self):
        super().__init__()

        self.create_dirs()
        self.create_settings()

    def create_dirs(self):
        b = os.path.isdir(self.domains_dir)
        if b == False:
            os.makedirs(self.domains_dir)
            os.makedirs(self.existing_domain)
            os.makedirs(self.free_domains)
            os.makedirs(self.favorite_domains)

            self.create_domain_architecture()
            b = True
        return b

    def create_settings(self):
        b = os.path.exists(self.settings)
        if b == False:
            with open(self.settings, "w") as f:
                json.dump({"first_running": 1}, f)
            b = True
        return b

    def create_domains_type(self, storage, conf, columns):
        with open(storage, "w") as f:
            f.write("\"" + "\",\"".join(columns) + "\"\n")

        with open(conf, "w") as f:
            out_data = {
                "auto_increment": 0,
                "domain_name_dict": {}
            }

            for v in columns:
                out_data[v+"_max"] = 0

            dict_start = ord("a")
            for i in range(10+26):
                if i < 10:
                    out_data["domain_name_dict"][i] = []
                    continue
                out_data["domain_name_dict"][chr(dict_start)] = []
                dict_start += 1

            json.dump(out_data, f)

    def create_domain_architecture(self):
        self.create_domains_type(
            self.existing_domain + "/" + self.exs_dm_f,
            self.existing_domain + "/" + self.dm_conf,
            self.exs_dm_col
        )
        self.create_domains_type(
            self.free_domains + "/" + self.fr_dm_f,
            self.free_domains + "/" + self.dm_conf,
            self.fr_dm_col
        )
        self.create_domains_type(
            self.favorite_domains + "/" + self.fv_dm_f,
            self.favorite_domains + "/" + self.dm_conf,
            self.fv_dm_col
        )

        return ["all", 1]


class Favorite_manager(File_base):
    def __init__(self):
        super().__init__()

    def select(self, col_arg):
        path = self.get_favorite_path()
        storage, conf = path["storage"], path["conf"]
        col = self.get_favorite_col()
        domains = []

        # configuration settings
        conf_s = []

        with open('/'.join(conf), "r") as f:
            conf_s = json.load(f)

        with open('/'.join(storage), "r") as f:
            lines = f.readlines()
            for i in range(1, len(lines)):
                print(lines[i])











