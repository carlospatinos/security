# The purpose of this is to verify the length of md5 and sha1, 
#also understand if they change when data changes or filename changes
openssl md5 file.txt >> output_md5_sha1.txt
openssl sha1 file.txt >> output_md5_sha1.txt

openssl md5 file2.txt >> output2_md5_sha1.txt
openssl sha1 file2.txt >> output2_md5_sha1.txt

sleep 2

echo " " >> file.txt

openssl md5 file.txt >> output_updated_md5_sha1.txt
openssl sha1 file.txt >> output_updated_md5_sha1.txt

cat file2.txt > file.txt