vboxmanage startvm "ubuntu" --type headless
vboxmanage startvm "ubuntu2" --type headless

vboxmanage showvminfo "ubuntu" | grep -c "running (since"
vboxmanage showvminfo "ubuntu2" | grep -c "running (since"

vboxmanage guestproperty get "ubuntu" "/VirtualBox/GuestInfo/Net/0/V4/IP"
vboxmanage guestproperty get "ubuntu2" "/VirtualBox/GuestInfo/Net/0/V4/IP"