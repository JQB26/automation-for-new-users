$filePath = (get-item $PSScriptRoot).parent.FullName + '\data\new_users.csv'
$usersfromfile = Import-Csv $filePath -Delimiter ';'

foreach ($user in $usersfromfile) {
New-ADUser -Name $user.name -DisplayName $user.name -GivenName $user.givenname -Surname $user.surname`
  -SamAccountName $user.sammaccountname -UserPrincipalName $user.userprincipialname -Path $user.ou -Company $user.Company`
  -EmailAddress $user.emailaddress -Department $user.department -Title $user.title`
  -AccountPassword (ConvertTo-SecureString $user.password -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $true
  
Add-ADGroupMember biuro -Members $user.sammaccountname
Add-ADGroupMember zarzady -Members $user.sammaccountname
Add-ADGroupMember pracownicybiuro -Members $user.sammaccountname
}
