ubuntus=( "ubuntu" "ubuntu2" "ubuntu3" )
for ubuntuId in "${ubuntus[@]}"
do
   : 
   # do whatever on $i
   #vboxmanage controlvm $ubuntuId poweroff
   vboxmanage controlvm $ubuntuId acpipowerbutton
   vboxmanage showvminfo $ubuntuId | grep -c "running (since"
done