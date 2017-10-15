vboxmanage startvm "ubuntu" --type headless
vboxmanage startvm "ubuntu2" --type headless

vboxmanage showvminfo "ubuntu" | grep -c "running (since"
vboxmanage showvminfo "ubuntu2" | grep -c "running (since"

UBUNTU=$(vboxmanage guestproperty get "ubuntu" "/VirtualBox/GuestInfo/Net/0/V4/IP")
UBUNTU2=$(vboxmanage guestproperty get "ubuntu2" "/VirtualBox/GuestInfo/Net/0/V4/IP")

echo "ubuntu  ip is => $UBUNTU"
echo "ubuntu2 ip is => $UBUNTU2"