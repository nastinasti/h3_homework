'''У вас есть список(list) IP адрессов. Вам необходимо создать
класс который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)'''


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""
    def __init__(self, ipList):
        self.__ipList = ipList

    @property
    def ipList(self):
        return self.__ipList

    @ipList.setter
    def ipList(self, newList):
        for item in newList:
            if not type(item) == str:
                return 0
            self.__ipList = newList

    def __str__(self):
        return f"Ip is {self.__ipList}\n"


    def reverse_IP(self):
        """Return it's IPs reversed"""
        reversed_iplist = list()
        for ip_item in self.__ipList:
            reversed_iplist.append('.'.join((str(ip_item).split('.'))[::-1]))
        return f"Reversed Ip list is {reversed_iplist}"

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        get_iplist = list()
        for ip_item in self.__ipList:
            get_iplist.append('.' + '.'.join((str(ip_item).split('.'))[1::]))
        return f"Ip list without first octets {get_iplist}"

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        get_iplist = list()
        for ip_item in self.__ipList:
            get_iplist.append('.' + '.'.join((str(ip_item).split('.'))[-1::]))
        return f"Ip list of last octets {get_iplist}"

inits = ["10.11.12.13", "192.168.1.254", "10.10.1.1"]
test = IpHandler(inits)

'''Создайте класс который будет хранить параметры для
подключения к физическому юниту (например сервер). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров (@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.'''


class ConnHandler:
    __slots__ = ['_unit_name', '_mac_address', '_ip_address', '_login', '_password']

    def __init__(self, unit_name='', mac_address='', ip_address='', login='', password=''):
        self._unit_name = unit_name
        self._mac_address = mac_address
        self._ip_address = ip_address
        self._login = login
        self._password = password

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        self._unit_name = unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        self._mac_address = mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        self._ip_address = ip_address

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f"Name: {self._unit_name}, MAC: {self._mac_address}, IP: {self._ip_address}, \
login: {self._login}, password: {self._password}"

test_handler = ConnHandler("Linux CO.", "10.10.20.10", "192.168.1.2", "guido_user", "tell_me")
