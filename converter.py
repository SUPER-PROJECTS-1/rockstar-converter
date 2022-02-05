## After you have changed rockstars instead of displayed like before > changed they will just display changed

## BEFORE;
## shdjasgdjhasd@gmail.com:fakepassword > 213213123@superspoofer.com:SUPERSPOOFER2022

## AFTER CONVERTED;
## 213213123@superspoofer.com:SUPERSPOOFER2022

with open('changed.txt', 'w') as f:
    with open("accounts.txt") as file:
     for line in file:
      f.write(line.partition("> ")[2])
print("Changed accounts to changed.txt")
input("Press enter to exit ;)")