$name = $args[0]
$surname = $args[1]
$alias = $args[2]
$group = $args[3]

$pat = $PSScriptRoot + "\data\path.txt"
$patdata = Get-Content -Path $pat -TotalCount 1

$dispName = $name + " " + $surname + " (" + $group + ")"

$group += $patdata

New-ADUser -Name $dispName -Surname $surname -SamAccountName $alias -DisplayName $dispName -AccountPassword(Read-Host -AsSecureString "Input Password") -Enabled $true