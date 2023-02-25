# Modern replacement for net send

$computername = "COMPUTERNAME" # replace with the name of the target computer
$message = "Hello, this is a custom message!" # replace with your custom message

Invoke-Command -ComputerName $computername -ScriptBlock { msg.exe * "$using:message" }
