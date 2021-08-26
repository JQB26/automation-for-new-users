$name = $args[0]
$surname = $args[1]
$alias = $args[2]
$group = $args[3]

$pat = $PSScriptRoot + "\data\path.txt"
$patdata = Get-Content -Path $pat -TotalCount 1

$dispName = $name + " " + $surname + " (" + $group + ")"

$group += $patdata

New-ADUser -Name $dispName -Surname $surname -SamAccountName $alias -DisplayName $dispName -AccountPassword(Read-Host -AsSecureString "Input Password") -Enabled $true




New-ADUser -SamAccountName $user.sammaccountname -Name $user.name `
 -DisplayName $user.name -GivenName $user.givenname -Surname $user.surname`
  -UserPrincipalName $user.userprincipialname -Path $user.distinguished -Company $user.Company`
  -EmailAddress $user.emailaddress -Office $user.department -Title $user.title`
  -AccountPassword (ConvertTo-SecureString -AsPlainText $user.password -Force) -Enabled $true -ChangePasswordAtLogon $true

 Add-ADGroupMember biuro -Members $user.sammaccountname
Add-ADGroupMember zarzady -Members $user.sammaccountname