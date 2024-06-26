# Active Directory & Windows Server *Powershell cheat sheet*

Mostly AZ-800-adjacent things, with others thrown in. This sheet is not organized in any meaningful way.

| Command | Description
| --- | --- |
| `repadmin /replsummary` | Replication summary. Identifies domain controllers that are failing inbound replication or outbound replication, and summarizes the results in a report. |
| `repadmin /showrepl` | Displays the replication status when the specified domain controller last attempted to perform inbound replication of Active Directory partitions. |
| `netdom query fsmo` | List FSMO roles |
| `get-aduser -identity myUsername -properties *` | List all properties of AD user ex. get-aduser -identity bob |
| `get-adcomputer -filter * -properties ipv4address, ipv6address \| format-list name, ipv4*, ipv6*` | List computers in domain, with IPv4 + IPv6 addresses. |
| `az vm open-port --port 443 --resource-group myResourceGroup --name myVM` | Open a port on an Azure VM |
| `netdom renamecomputer localhost /NewName:myNewName` | Rename computer using netdom. |
| `Rename-Computer -NewName "Server044" -DomainCredential Domain01\Admin01 -Restart` | Rename computer, using specified credential, and restart. Will prompt for password. |
| `Rename-Computer -ComputerName "Srv01" -NewName "Server001" -DomainCredential Domain01\Admin01 -Force` | Rename remote computer, skip confirmation. See [Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.2) |
| `netsh interface ipv4 show interfaces` | List IPv4 network interfaces |
| `netsh interface ipv4 set address name=$Idx source=static address=10.0.1.10 mask=255.255.255.0 gateway=10.0.0.1` | Set IPv4 address for a network interface. Can use Index or full interface name. Idx of adapter can be found in previous command. If DHCP then `source=DHCP` |
| `netsh interface ipv4 add dnsserver name=$Idx address=10.0.0.30 index=1` | Set DNS resolvers for an interface. Repeat with index=2 etc. to use multiple resolvers. |
| `Get-WindowsFeature \| Where-Object {$_. installstate -eq "installed"} \| Format-List Name,Installstate` | List all installed Roles & Features. Might want to pipe output to `more` or a text file if server has lots of Roles & Features installed because it can be a long list. |
| `Get-WindowsFeature -ComputerName dc01 \| Where-Object {$_. installstate -eq "installed"} \| Format-List Name,Installstate \| more` | Same as above, but for remote host. |
| `Restart-Computer -ComputerName Server01, Server02 -Credential Domain01\User01` | Restart remote machine. Will prompt for password of specified user. See [Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/restart-computer?view=powershell-7.2) |
| `Enter-PSSession -ComputerName Server01 -Credential Domain01\User1` | Start Powershell session with remote machine. End session with `Exit-PSSession`. [Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.2) |
| `Install-WindowsFeature FS-FileServer, FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools` | Install **DFS Namespaces** and **DFS Replication** roles |
| `hostname` or `echo %COMPUTERNAME%` | Display hostname |
| `netsh advfirewall show allprofiles` | Show firewall profiles. Also see [Use netsh advfirewall firewall context](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/netsh-advfirewall-firewall-control-firewall-behavior) |
| `Enable-PSremoting -force` | Enable Powershell remoting. Will generate an error if using Public network profile; use `-force` to bypass. See also [Use Windows PowerShell to remotely administer a server](https://docs.microsoft.com/en-us/learn/modules/describe-windows-server-administration-tools/6-use-windows-powershell-to-remotely-administer-server) |
| `Invoke-Command -ComputerName SEA-DC1, SEA-SVR1 –FilePath C:\Test\Sample.ps1` | Run a local script on remote machines |
| `Get-DhcpServerv4ScopeStatistics` | Gets the IPv4 scope statistics (incl. # of free and in-use addresses) corresponding to the IPv4 scope identifiers specified for a DHCP server service. |
| `Install-WindowsFeature IPAM -IncludeManagementTools` | Install IPAM server feature. You still must provision the IPAM servers and create GPOs for IPAM access. GPOs can be created with the following command. |
| `Invoke-IpamGpoProvisioning -domain domain1.com -GpoPrefixName IPAM -IpamServerFqdn server1.domain1.com` | Create access GPOs for IPAM. GPO prefix must match the one specified in IPAM provisioning wizard. Generally you want to enter Y at the prompts. |
| `disable-windowsoptionalfeature -online -featurename smb1protocol` | Disable SMB 1.0 if it has been enabled. |
| `Add-DnsServerQueryResolutionPolicy -Name "BlackholePolicy" -Action IGNORE -FQDN "EQ,*.contoso.com" -PassThru` | Ignore DNS queries for a domain. See [Docs](https://learn.microsoft.com/en-us/powershell/module/dnsserver/add-dnsserverqueryresolutionpolicy?view=windowsserver2022-ps) and [DNS Policies Overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/deploy/dns-policies-overview). Also see [DnsServer](https://learn.microsoft.com/en-us/powershell/module/dnsserver/?view=windowsserver2022-ps) |
| **Windows Update cmdlets** | 
| `Install-Module -Name PSWindowsUpdate` | Install Windows Update module from PSGallery |
| `Get-WindowsUpdate` or `Get-WUList` | List available updates |
| `Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot` | Download & install all available updates and reboot if needed |
| `Get-WindowsUpdate -KBArticleID KB2267602, KB4533002 -Install` | Install specific updates by KB # |
| `Install-WindowsUpdate -NotCategory "Drivers" -NotTitle OneDrive -NotKBArticleID KB4011670 -AcceptAll -IgnoreReboot` | Exclude certain updates |
| `Get-WUJob -ComputerName $ServerNames` | Check status of update jobs |
| `"server1","server2" \| Get-WUHistory \| Where-Object {$_.Title -match "KB4011634"} \| Select-Object * \| ft` | Check for a specific update's installation status |
|  **Miscellaneous** |
| `cipher /E` | Encrypt each file+dir within current working dir. [Docs](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cipher) |
| `netsh wlan show profile "wifi1" key=clear` | Show wlan profile incl. cleartext passphrase |
|  `net start <ServiceName>` and `net stop <ServiceName>` |  Start/stop a service |
| `Add-MpPreference -ControlledFolderAccessAllowedApplications "c:\apps\test.exe"` | Allow an application to access folders. [Docs](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps&viewFallbackFrom=win10-ps) |
| `fsutil fsinfo drives` | List mounted drives |
| `get-psdrive -psprovider filesystem` | List drives, incl. used + free space |
| `wmic logicaldisk get name,volumename,filesystem,size,description` | List drives incl. network mounts, along with some info |

Note: Powershell output are objects, not strings like other shells
