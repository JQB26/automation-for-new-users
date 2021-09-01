'''

New-ADUser -SamAccountName $user.sammaccountname -Name $user.name `
 -DisplayName $user.name -GivenName $user.givenname -Surname $user.surname`
  -UserPrincipalName $user.userprincipialname -Path $user.distinguished -Company $user.Company`
  -EmailAddress $user.emailaddress -Office $user.department -Title $user.title`
  -AccountPassword (ConvertTo-SecureString -AsPlainText $user.password -Force) -Enabled $true -ChangePasswordAtLogon $true

 Add-ADGroupMember biuro -Members $user.sammaccountname
Add-ADGroupMember zarzady -Members $user.sammaccountname
'''