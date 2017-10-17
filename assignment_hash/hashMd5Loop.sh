HASH_VAL="ecsc"
LAST_IS_NEXT="running"

for i in {1..2000}
do
    # "cut -c10-" instead of sed
    HASH_VAL=`echo -n $HASH_VAL | openssl md5 | sed -e "s/(stdin)= //"`
    echo "$i = $HASH_VAL"

    if [[ $LAST_IS_NEXT == *"done"* ]]; then
        exit 1
    fi
    if [[ $HASH_VAL == *"c89aa2ffb9"* ]]; then
  		LAST_IS_NEXT="done"
	fi
    
done