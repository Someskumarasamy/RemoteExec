from source.src.utils.CommonUtils import CommonUtils
from source.src.wrapper.LinuxParamikoWrapper import LinuxParamikoUtils


class MultiLinuxUtils:
    def __init__(self):
        pass

    def execCommand(self, path_sysdetails=None, path_passUrl=None, password=None):
        if path_sysdetails is None:
            raise Exception("The SystemDetails File Name is Empty")
        if path_passUrl is None and password is None:
            raise Exception("Both password and url to get password is empty. Atleast one input is needed")
        systemDetails = CommonUtils.getJSONFromPath(path_sysdetails)
        for systemData in systemDetails:
            self.port = 22
            if systemData["port"] is not None:
                self.port = systemData["port"]
            if systemData["accountName"] is not None and systemData["networkAddress"] is not None:
                if(systemData["password"] is not None and password is not None):
                    wrapperObject=LinuxParamikoUtils(accountName = systemData["accountName"], hostName = systemData["networkAddress"], accountPassword = systemData["password"], port = self.port)
                    wrapperObject.getSSHNewConnection()
                    wrapperObject.executeCommand("uname -a")
