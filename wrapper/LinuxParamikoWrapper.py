import ftplib
import paramiko


class LinuxParamikoUtils:

    def __init__(self, hostName=None, port=22, accountName=None, accountPassword=None):
            if hostName is not None and accountName is not None and accountPassword is not None:
                self.__setattr__(hostName, accountName, accountPassword, port)
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __setattr__(self,  hostName, accountName, accountPassword, port=22):
        self.hostName=hostName
        self.port=port
        self.accountName=accountName
        self.accountPassword=accountPassword

    # def getSshNewConnection(self, hostName, accountName, accountPassword, port=22):
    #     return self.client.connect(hostName,username=accountName,password=accountPassword,port=port)

    def getSSHNewConnection(self):
        return self.client.connect(self.hostName,username=self.accountName,password=self.accountPassword,port=self.port)

    def openSFTPConnection(self, client=None):
        if client is not None:
            return client.open_sftp()
        else :
            return self.client.open_sftp()

    def executeCommand(self, client=None, command=None):
        if command is None:
            raise Exception(" The command field is empty")
        if client is not None:
            stdin, stdout, stderr = client.exec_command(command)
        else :
            stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().splitlines()
        
    def excuteSudoCommand(self, client=None, command=None, password=None):
        if(self.password is None and password is None):
            raise Exception("Password is Empty");
        return self.executeCommand(client, "sudo -S <<< "+password+" gedit"+command)