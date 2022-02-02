# Active Directory Powershell cheat sheet

| Command | Description
| --- | --- |
| `repadmin /replsummary` | Replication summary. Identifies domain controllers that are failing inbound replication or outbound replication, and summarizes the results in a report. |
| `repadmin /showrepl` | Displays the replication status when the specified domain controller last attempted to perform inbound replication of Active Directory partitions. |
| `netdom query fsmo` | List FSMO roles |
| `get-aduser -identity $USERNAME -properties *` | List all properties of AD user ex. get-aduser -identity bob |
