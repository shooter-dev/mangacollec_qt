class ItemCollection:
    def __init__(self, name, nb_tome, nb_tome_total, status):
        self.name = name
        self.nb_tome = nb_tome
        self.nb_tome_total = nb_tome_total
        self.status = status
        self.list_url_volume = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def nb_tome(self):
        return self.nb_tome

    @nb_tome.setter
    def nb_tome(self, value):
        self.nb_tome = value

    @property
    def nb_tome_total(self):
        return self.nb_tome_total

    @nb_tome_total.setter
    def nb_tome_total(self, value):
        self.nb_tome_total = value

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value):
        self.status = value

    @property
    def list_url_volume(self):
        return self.list_url_volume

    @list_url_volume.setter
    def list_url_volume(self, value):
        self.list_url_volume = value
