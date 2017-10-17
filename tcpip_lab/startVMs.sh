ubuntus=( "ubuntu" "ubuntu2" "ubuntu3" )
for ubuntuId in "${ubuntus[@]}"
do
   : 
   # do whatever on $i
   vboxmanage startvm $ubuntuId --type headless
   vboxmanage showvminfo $ubuntuId | grep -c "running (since"
   UBUNTU=$(vboxmanage guestproperty get $ubuntuId "/VirtualBox/GuestInfo/Net/0/V4/IP")
   echo "$ubuntuId ip is => $UBUNTU"
done

#vboxmanage startvm "ubuntu2" --type headless
#vboxmanage showvminfo "ubuntu2" | grep -c "running (since"
#UBUNTU2=$(vboxmanage guestproperty get "ubuntu2" "/VirtualBox/GuestInfo/Net/0/V4/IP")
#echo "ubuntu  ip is => $UBUNTU"
#echo "ubuntu2 ip is => $UBUNTU2"