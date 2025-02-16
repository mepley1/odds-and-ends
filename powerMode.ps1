# Simple Powershell GUI to change between Windows power plans

# Colors

$bg1 = "#202020"
$fg1 = [System.Drawing.Color]::White

# Positioning

$pos_x = 32

$pos_y1 = 32
$pos_y2 = $pos_y1 + 64
$pos_y3 = $pos_y2 + 64
$pos_y4 = $pos_y3 + 64
$pos_y5 = $pos_y4 + 64
$pos_y6 = $pos_y5 + 64

$btn_size = 96, 48

# Aliases for button click actions

$setPwrBalanced = {powercfg -setactive SCHEME_BALANCED}
$setPwrHigh = {powercfg -s 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c}
$setPwrUltimate = {powercfg -s e9a42b02-d5df-448d-aa00-03f14749eb61}
$setPwrLow = {powercfg -s a1841308-3541-4fab-bc81-f71556f20b4a}

# Create base form

$form = New-Object Windows.Forms.Form
$form.Text = "PowerMode"
$form.Size = New-Object Drawing.Size 160, 352
$form.StartPosition = "CenterScreen"
$form.BackColor = $bg1
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedToolWindow
$form.MaximizeBox = 0

# Buttons

# Ultimate performance
$button1 = New-Object Windows.Forms.Button
$button1.Location = New-Object Drawing.Point $pos_x, $pos_y1
$button1.Size = New-Object Drawing.Size $btn_size
$button1.Text = "Ultimate Performance"
$button1.BackColor = $bg1
$button1.ForeColor = $fg1
$button1.FlatStyle = 0

$button1.Add_Click($setPwrUltimate)
$form.Controls.Add($button1)

# High performance
$button2 = New-Object Windows.Forms.Button
$button2.Location = New-Object Drawing.Point $pos_x, $pos_y2
$button2.Size = New-Object Drawing.Size $btn_size
$button2.Text = "High Performance"
$button2.BackColor = $bg1
$button2.ForeColor = $fg1
$button2.FlatStyle = 0

$button2.Add_Click($setPwrHigh)
$form.Controls.Add($button2)

## Balanced
$button3 = New-Object Windows.Forms.Button
$button3.Location = New-Object Drawing.Point $pos_x, $pos_y3
$button3.Size = New-Object Drawing.Size $btn_size
$button3.Text = "Balanced"
$button3.BackColor = $bg1
$button3.ForeColor = $fg1
$button3.FlatStyle = 0

$button3.Add_Click($setPwrBalanced)
$form.Controls.Add($button3)

## Power saver
$button4 = New-Object Windows.Forms.Button
$button4.Location = New-Object Drawing.Point $pos_x, $pos_y4
$button4.Size = New-Object Drawing.Size $btn_size
$button4.Text = "Power saver"
$button4.BackColor = $bg1
$button4.ForeColor = $fg1
$button4.FlatStyle = 0

$button4.Add_Click($setPwrLow)
$form.Controls.Add($button4)

# Display the form

$form.Topmost = $true
$form.ShowDialog()
