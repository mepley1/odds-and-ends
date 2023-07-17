# Windows equivalent of ssh-copy-id
# Copying from Windows system to Linux system
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh {IP-ADDRESS-OR-FQDN} "cat >> .ssh/authorized_keys"
