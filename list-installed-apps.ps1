# list all installed applications
echo 'Getting installed applications, please wait...'
Get-WmiObject -Class Win32_Product | Select-Object -Property Name