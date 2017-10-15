vboxmanage controlvm "ubuntu" poweroff
vboxmanage controlvm "ubuntu2" poweroff

vboxmanage showvminfo "ubuntu" | grep -c "running (since"
vboxmanage showvminfo "ubuntu2" | grep -c "running (since"

