#This ust  be run in 192.168.0,111
# se conecta para enviar mensajes manualmente
#nc 192.168.0.100 55555
# Envia line a linea un archivo
#while read x; do echo "$x" | nc 192.168.0.100 55555; sleep 5; done < messages.txt

while true; do d=$(date +"%m/%d/%Y %H:%M:%S"); echo "$d-carlos_para_110" | nc 192.168.0.100 55555; sleep 5; done 