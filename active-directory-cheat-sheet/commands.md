# Active Directory Powershell cheat sheet

| Command | Description
| --- | --- |
| `repadmin /replsummary` | Replication summary. Identifies domain controllers that are failing inbound replication or outbound replication, and summarizes the results in a report. |
| `repadmin /showrepl` | Displays the replication status when the specified domain controller last attempted to perform inbound replication of Active Directory partitions. |
| `netdom query fsmo` | List FSMO roles |
| `get-aduser -identity myUsername -properties *` | List all properties of AD user ex. get-aduser -identity bob |
| `az vm open-port --port 443 --resource-group myResourceGroup --name myVM` | Open a port on an Azure VM |
| `netdom renamecomputer localhost /NewName:myNewName` | Rename computer |
| `Rename-Computer -NewName "Server044" -DomainCredential Domain01\Admin01 -Restart` | Rename computer. Will prompt for Admin01 password. |
| `Rename-Computer -ComputerName "Srv01" -NewName "Server001" -DomainCredential Domain01\Admin01 -Force` | Rename remote computer. See [Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-computer?view=powershell-7.2) |
| `netsh interface ipv4 show interfaces` | List IPv4 network interfaces |
| `netsh interface ipv4 set address name=$Idx source=static address=10.0.1.10 mask=255.255.255.0 gateway=10.0.0.1` | Set IPv4 address for network interface. Can use Index or full interface name. Idx of adapter can be found in previous command. If DHCP then source=DHCP |
| `netsh interface ipv4 add dnsserver name=$Idx address=10.0.0.30 index=1` | Set DNS servers. Repeat with index=2 etc. for multiple servers |
|   `Get-WindowsFeature | Where-Object {$_. installstate -eq "installed"} | Format-List Name,Installstate` | List all installed Roles & Features. Might want to pipe output to `more` or a file because it can be a long list. |
| `Get-WindowsFeature -ComputerName dc01 | Where-Object {$_. installstate -eq "installed"} | Format-List Name,Installstate | more` | Same as above, but for remote host. |
